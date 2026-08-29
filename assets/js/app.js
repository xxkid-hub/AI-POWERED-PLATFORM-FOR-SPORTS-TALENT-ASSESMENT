/**
 * ApexScout AI - Main Application Controller
 * Tab routing, multi-sport skill breakdown rendering, rural accessibility, and session orchestration.
 */

class App {
  constructor() {
    this.currentTab = 'video-assessment';
    this.aiEngine = new AIEngine();
    this.medicalVerifier = new MedicalVerifier();
    this.latestVideoReport = null;
    this.latestMedicalReport = null;
    this.currentAthlete = {
      name: 'Alex Rivera',
      sport: 'Football / Soccer',
      age: 18,
      height: "5'11\" (180 cm)",
      location: 'Grassroots Combine'
    };
  }

  init() {
    this.bindNavigation();
    this.bindModals();
    this.bindAssessmentControls();
    this.bindMedicalControls();

    const videoEl = document.getElementById('assessmentVideo');
    const canvasEl = document.getElementById('assessmentCanvas');
    this.aiEngine.init(videoEl, canvasEl);

    if (window.coachesManager) window.coachesManager.init();
    if (window.leaderboardManager) window.leaderboardManager.init();
    if (window.helplineManager) window.helplineManager.init();
    if (window.ruralAccess) window.ruralAccess.init();

    // Select default preset drill: Soccer Penalty Kick (matches user image)
    this.selectDrill('drill-soccer-penalty');
    this.loadDefaultMedicalReport();

    this.aiEngine.onMetricsUpdate = (metrics) => this.handleMetricsUpdate(metrics);
    this.aiEngine.onAnalysisComplete = (report) => this.handleAnalysisComplete(report);
  }

  bindNavigation() {
    const navButtons = document.querySelectorAll('[data-tab-target]');
    navButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const target = btn.getAttribute('data-tab-target');
        this.switchTab(target);
      });
    });
  }

  switchTab(tabId) {
    this.currentTab = tabId;

    document.querySelectorAll('[data-tab-target]').forEach(btn => {
      if (btn.getAttribute('data-tab-target') === tabId) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });

    document.querySelectorAll('.tab-content-section').forEach(sec => {
      if (sec.id === `section-${tabId}`) {
        sec.classList.add('active');
      } else {
        sec.classList.remove('active');
      }
    });

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  bindModals() {
    document.querySelectorAll('.modal-close, .modal-backdrop').forEach(el => {
      el.addEventListener('click', () => {
        const modal = el.closest('.modal-container');
        if (modal) modal.classList.remove('active');
      });
    });
  }

  bindAssessmentControls() {
    document.querySelectorAll('.drill-select-card').forEach(card => {
      card.addEventListener('click', () => {
        const drillId = card.getAttribute('data-drill-id');
        this.selectDrill(drillId);
      });
    });

    const startBtn = document.getElementById('startAnalysisBtn');
    if (startBtn) {
      startBtn.addEventListener('click', () => {
        this.startDrillAnalysis();
      });
    }

    const fileInput = document.getElementById('videoFileInput');
    if (fileInput) {
      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          this.handleCustomVideoUpload(e.target.files[0]);
        }
      });
    }

    const webcamBtn = document.getElementById('webcamToggleBtn');
    if (webcamBtn) {
      webcamBtn.addEventListener('click', async () => {
        const res = await this.aiEngine.startWebcam();
        if (res.success) {
          this.showNotification('Live combine webcam active. Position athlete in full body view.');
          document.getElementById('videoSourceLabel').textContent = 'LIVE WEBCAM STREAM (60 FPS)';
        } else {
          this.showNotification('Webcam inaccessible; running standard combine simulation.', 'warning');
        }
      });
    }

    const audioCoachBtn = document.getElementById('audioCoachBtn');
    if (audioCoachBtn) {
      audioCoachBtn.addEventListener('click', () => {
        const comp = this.aiEngine.currentDrill?.componentAnalysis || SAMPLE_DATA.drills[0].componentAnalysis;
        if (window.ruralAccess) {
          window.ruralAccess.speakAnalysis(comp);
        }
      });
    }

    const whatsappBtn = document.getElementById('shareWhatsAppBtn');
    if (whatsappBtn) {
      whatsappBtn.addEventListener('click', () => {
        const comp = this.aiEngine.currentDrill?.componentAnalysis || SAMPLE_DATA.drills[0].componentAnalysis;
        if (window.ruralAccess) {
          window.ruralAccess.shareToWhatsApp(this.currentAthlete.name, comp);
        }
      });
    }
  }

  selectDrill(drillId) {
    document.querySelectorAll('.drill-select-card').forEach(c => {
      if (c.getAttribute('data-drill-id') === drillId) {
        c.classList.add('active');
      } else {
        c.classList.remove('active');
      }
    });

    const drill = this.aiEngine.loadDrill(drillId);
    if (!drill) return;

    document.getElementById('videoSourceLabel').textContent = `${drill.sport.toUpperCase()} • ${drill.skillName.toUpperCase()}`;
    document.getElementById('analysisStatusText').textContent = 'READY TO ANALYZE';
    document.getElementById('deepfakeStatusBadge').className = 'status-pill';
    document.getElementById('deepfakeStatusBadge').textContent = 'PENDING INSPECTION';

    // Populate Skill Table immediately with preset baseline
    this.renderSkillAnalysisTable(drill.componentAnalysis, drill.skillName);
  }

  renderSkillAnalysisTable(comp, skillTitle) {
    const titleEl = document.getElementById('skillAnalysisTableTitle');
    if (titleEl) titleEl.textContent = `${(skillTitle || comp.skill || 'PENALTY').toUpperCase()} ANALYSIS`;

    document.getElementById('valSkill').textContent = comp.skill;
    document.getElementById('valShotResult').textContent = comp.shotResult;
    document.getElementById('valShotSpeed').textContent = comp.shotSpeed;
    document.getElementById('valAccuracy').textContent = comp.accuracy;
    document.getElementById('valBallPlacement').textContent = comp.ballPlacement;
    document.getElementById('valReactionTime').textContent = comp.reactionTime;
    document.getElementById('valRunUpSpeed').textContent = comp.runUpSpeed;
    document.getElementById('valPlantFoot').textContent = comp.plantFoot;
    document.getElementById('valBalance').textContent = comp.balance;
    document.getElementById('valFollowThrough').textContent = comp.followThrough;
    document.getElementById('valContactQuality').textContent = comp.contactQuality;
    document.getElementById('valBallCurve').textContent = comp.ballCurve;
  }

  handleCustomVideoUpload(file) {
    const url = URL.createObjectURL(file);
    const videoEl = document.getElementById('assessmentVideo');
    if (videoEl) {
      videoEl.src = url;
      videoEl.play();
    }
    document.getElementById('videoSourceLabel').textContent = `CUSTOM UPLOAD: ${file.name}`;
    this.showNotification(`Loaded video: ${file.name}. Click "Run AI Video Analysis" to begin.`);
  }

  startDrillAnalysis() {
    const startBtn = document.getElementById('startAnalysisBtn');
    startBtn.disabled = true;
    startBtn.textContent = '⚡ Analyzing Biomechanical Skill Components...';
    document.getElementById('analysisStatusText').textContent = 'ANALYZING MOTION...';

    const simulateTamper = document.getElementById('simulateTamperToggle')?.checked || false;
    this.aiEngine.startAnalysis({ simulateTamper });
  }

  handleMetricsUpdate(state) {
    document.getElementById('analysisStatusText').textContent = `TRACKING: ${state.phase}`;
  }

  handleAnalysisComplete(report) {
    this.latestVideoReport = report;

    const startBtn = document.getElementById('startAnalysisBtn');
    startBtn.disabled = false;
    startBtn.textContent = '▶ Run AI Video Analysis';
    document.getElementById('analysisStatusText').textContent = 'ANALYSIS COMPLETE';

    const badge = document.getElementById('deepfakeStatusBadge');
    if (report.deepfakeForensics.isAuthentic) {
      badge.className = 'status-pill pill-success';
      badge.textContent = `✓ AUTHENTIC (${report.deepfakeForensics.authenticityScore}%)`;
    } else {
      badge.className = 'status-pill pill-danger';
      badge.textContent = `⚠ TAMPERING FLAGGED (${report.deepfakeForensics.authenticityScore}%)`;
    }

    this.renderSkillAnalysisTable(report.components, report.skillName);
    this.displayAssessmentReportModal(report);
    this.updateAthleteScorecard();
    this.showNotification('Biomechanical Skill Analysis & Deepfake Inspection completed!');
  }

  displayAssessmentReportModal(report) {
    const modal = document.getElementById('assessmentReportModal');
    if (!modal) return;

    document.getElementById('reportDrillTitle').textContent = report.drillTitle;
    document.getElementById('reportSport').textContent = report.sport;
    document.getElementById('reportTimestamp').textContent = new Date(report.timestamp).toLocaleString();
    document.getElementById('reportOverallScore').textContent = report.components.overallRating || 94;

    const df = report.deepfakeForensics;
    document.getElementById('repDeepfakeScore').textContent = `${df.authenticityScore}%`;
    document.getElementById('repDeepfakeStatus').textContent = df.isAuthentic ? 'PASSED: Zero Synthetic Artifacts' : 'FAILED: Speed/Splicing Tampered';
    document.getElementById('repDeepfakeSpeed').textContent = `${df.speedMultiplier}x Playback Speed`;

    const auditContainer = document.getElementById('repDeepfakeAuditList');
    if (auditContainer) {
      auditContainer.innerHTML = df.auditLog.map(item => `
        <div class="audit-item ${item.status === 'PASSED' ? 'audit-pass' : 'audit-fail'}">
          <div class="audit-header">
            <strong>${item.check}</strong>
            <span class="audit-badge">${item.score}</span>
          </div>
          <p class="audit-detail">${item.detail}</p>
        </div>
      `).join('');
    }

    modal.classList.add('active');
  }

  bindMedicalControls() {
    const verifyBtn = document.getElementById('verifyMedicalBtn');
    if (verifyBtn) {
      verifyBtn.addEventListener('click', () => {
        this.processMedicalVerification();
      });
    }

    const testTimePreset = document.getElementById('medTimePresetSelect');
    if (testTimePreset) {
      testTimePreset.addEventListener('change', (e) => {
        const val = e.target.value;
        const now = new Date();
        let targetDate = new Date();

        if (val === 'fresh-4h') {
          targetDate = new Date(now.getTime() - 4 * 3600000);
        } else if (val === 'valid-18h') {
          targetDate = new Date(now.getTime() - 18 * 3600000);
        } else if (val === 'expired-38h') {
          targetDate = new Date(now.getTime() - 38 * 3600000);
        }

        const formatted = targetDate.toISOString().slice(0, 16);
        const medInput = document.getElementById('medicalReportTimestampInput');
        if (medInput) medInput.value = formatted;
      });
    }

    const medFileInput = document.getElementById('medicalDocFileInput');
    if (medFileInput) {
      medFileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          document.getElementById('uploadedMedicalDocName').textContent = `📄 ${e.target.files[0].name}`;
          this.showNotification(`Uploaded medical certificate: ${e.target.files[0].name}`);
        }
      });
    }
  }

  loadDefaultMedicalReport() {
    const now = new Date();
    const fourHoursAgo = new Date(now.getTime() - 4 * 3600000).toISOString().slice(0, 16);
    const videoTimeNow = now.toISOString().slice(0, 16);

    const medInput = document.getElementById('medicalReportTimestampInput');
    const vidInput = document.getElementById('videoRecordedTimestampInput');
    if (medInput) medInput.value = fourHoursAgo;
    if (vidInput) vidInput.value = videoTimeNow;
  }

  processMedicalVerification() {
    const medTime = document.getElementById('medicalReportTimestampInput')?.value;
    const vidTime = document.getElementById('videoRecordedTimestampInput')?.value;
    const athleteName = document.getElementById('medAthleteNameInput')?.value || 'Alex Rivera';

    const rawReport = {
      athleteName,
      timestamp: medTime ? new Date(medTime).toISOString() : new Date().toISOString(),
      labName: 'Apex Olympic Certified Bio-Diagnostic Lab',
      accreditationId: 'WADA-ISO/IEC-17025-CL492',
      doctorName: 'Dr. Evelyn Reed, MD (Sports Medicine)'
    };

    const verified = this.medicalVerifier.verifyReport(rawReport, {
      timestamp: vidTime ? new Date(vidTime).toISOString() : new Date().toISOString()
    });

    this.latestMedicalReport = verified;

    const resultCard = document.getElementById('medicalVerificationResultCard');
    if (resultCard) {
      resultCard.style.display = 'block';

      document.getElementById('medResultToken').textContent = verified.verificationToken;
      document.getElementById('medResultAthlete').textContent = verified.athleteName;
      document.getElementById('medResultTimeDiff').textContent = `${verified.timeCompliance.timeDifferenceHours} hours apart`;

      const statusBadge = document.getElementById('medResultStatusBadge');
      if (verified.isFullyCleared) {
        statusBadge.className = 'status-pill pill-success';
        statusBadge.textContent = '🛡 VERIFIED WITHIN 24H (CLEARED)';
      } else {
        statusBadge.className = 'status-pill pill-danger';
        statusBadge.textContent = verified.timeCompliance.isValid ? '⚠ DOPING FLAGGED' : '⚠ EXPIRED (>24H WINDOW)';
      }

      document.getElementById('medResultConclusion').textContent = verified.conclusion;
    }

    this.updateAthleteScorecard();
    this.showNotification(
      verified.isFullyCleared ? '24h Medical & Anti-Doping Verification Passed!' : 'Medical Verification Alert: Check timestamp compliance.',
      verified.isFullyCleared ? 'success' : 'warning'
    );
  }

  updateAthleteScorecard() {
    const comp = this.latestVideoReport ? this.latestVideoReport.components : SAMPLE_DATA.drills[0].componentAnalysis;
    const cardEl = document.getElementById('athleteUnifiedScorecard');
    if (!cardEl) return;

    document.getElementById('cardSkillTested').textContent = comp.skill;
    document.getElementById('cardShotSpeedVal').textContent = comp.shotSpeed;
    document.getElementById('cardAccuracyVal').textContent = comp.accuracy;
    document.getElementById('cardReactionVal').textContent = comp.reactionTime;
    document.getElementById('cardOverallScore').textContent = comp.overallRating || 94;
  }

  printOrDownloadScorecard() {
    window.print();
  }

  showNotification(message, type = 'info') {
    const container = document.getElementById('toastContainer');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast-pill toast-${type}`;
    toast.innerHTML = `<span class="toast-text">${message}</span>`;
    container.appendChild(toast);

    setTimeout(() => toast.classList.add('show'), 50);
    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => toast.remove(), 300);
    }, 4000);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.app = new App();
  window.app.init();
});
