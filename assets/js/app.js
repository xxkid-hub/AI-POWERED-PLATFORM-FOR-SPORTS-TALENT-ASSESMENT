/**
 * ApexScout AI - Main Application Controller
 * Tab routing, session state management, analysis pipeline orchestration, and UI interactions.
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
      sport: 'Basketball',
      age: 18,
      height: "6'2\" (188 cm)",
      weight: '82 kg (181 lbs)',
      location: 'Dallas, TX, USA'
    };
  }

  init() {
    this.bindNavigation();
    this.bindModals();
    this.bindAssessmentControls();
    this.bindMedicalControls();

    // Initialize submodules
    const videoEl = document.getElementById('assessmentVideo');
    const canvasEl = document.getElementById('assessmentCanvas');
    this.aiEngine.init(videoEl, canvasEl);

    if (window.coachesManager) window.coachesManager.init();
    if (window.leaderboardManager) window.leaderboardManager.init();
    if (window.helplineManager) window.helplineManager.init();

    // Select default preset drill
    this.selectDrill('drill-bball-dribble');

    // Load default sample medical report
    this.loadDefaultMedicalReport();

    // Setup AI engine callbacks
    this.aiEngine.onMetricsUpdate = (metrics) => this.handleMetricsUpdate(metrics);
    this.aiEngine.onAnalysisComplete = (report) => this.handleAnalysisComplete(report);
  }

  bindNavigation() {
    const navButtons = document.querySelectorAll('[data-tab-target]');
    navButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        const target = btn.getAttribute('data-tab-target');
        this.switchTab(target);
      });
    });
  }

  switchTab(tabId) {
    this.currentTab = tabId;

    // Update nav buttons
    document.querySelectorAll('[data-tab-target]').forEach(btn => {
      if (btn.getAttribute('data-tab-target') === tabId) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });

    // Update tab sections
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
    // Close modal on close button or backdrop click
    document.querySelectorAll('.modal-close, .modal-backdrop').forEach(el => {
      el.addEventListener('click', (e) => {
        const modal = el.closest('.modal-container');
        if (modal) modal.classList.remove('active');
      });
    });
  }

  bindAssessmentControls() {
    // Drill selection cards
    document.querySelectorAll('.drill-select-card').forEach(card => {
      card.addEventListener('click', (e) => {
        const drillId = card.getAttribute('data-drill-id');
        this.selectDrill(drillId);
      });
    });

    // Start Analysis button
    const startBtn = document.getElementById('startAnalysisBtn');
    if (startBtn) {
      startBtn.addEventListener('click', () => {
        this.startDrillAnalysis();
      });
    }

    // Video File Upload Input
    const fileInput = document.getElementById('videoFileInput');
    if (fileInput) {
      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          this.handleCustomVideoUpload(e.target.files[0]);
        }
      });
    }

    // Webcam Toggle
    const webcamBtn = document.getElementById('webcamToggleBtn');
    if (webcamBtn) {
      webcamBtn.addEventListener('click', async () => {
        const res = await this.aiEngine.startWebcam();
        if (res.success) {
          this.showNotification('Live combine webcam active. Stand in full frame view.');
          document.getElementById('videoSourceLabel').textContent = 'LIVE WEBCAM STREAM (60 FPS)';
        } else {
          this.showNotification('Webcam inaccessible; loaded simulated combine feed.', 'warning');
        }
      });
    }

    // Tamper Simulation Toggle for Testing
    const tamperCheckbox = document.getElementById('simulateTamperToggle');
    if (tamperCheckbox) {
      tamperCheckbox.addEventListener('change', (e) => {
        this.showNotification(
          e.target.checked 
            ? 'Test Mode: AI Video Speed Tampering enabled (1.40x fake speedup simulation)' 
            : 'Test Mode: Organic Authentic Video enabled'
        );
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

    document.getElementById('videoSourceLabel').textContent = `${drill.sport.toUpperCase()} • ${drill.title.toUpperCase()}`;
    document.getElementById('activeDrillTitle').textContent = drill.title;
    document.getElementById('activeDrillSport').textContent = drill.sport;
    document.getElementById('activeDrillDuration').textContent = drill.duration;

    // Reset metrics on UI
    document.getElementById('liveJumpHeight').textContent = '0.0"';
    document.getElementById('liveDribbleSpeed').textContent = '0.0 Hz';
    document.getElementById('liveSprintSpeed').textContent = '0.0 km/h';
    document.getElementById('liveKneeAngle').textContent = '160°';
    document.getElementById('analysisStatusText').textContent = 'READY TO ANALYZE';
    document.getElementById('deepfakeStatusBadge').className = 'status-pill';
    document.getElementById('deepfakeStatusBadge').textContent = 'PENDING INSPECTION';
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
    startBtn.textContent = '⚡ Analyzing Biomechanics & Deepfake Checks...';
    document.getElementById('analysisStatusText').textContent = 'ANALYSIS IN PROGRESS...';

    const simulateTamper = document.getElementById('simulateTamperToggle')?.checked || false;

    this.aiEngine.startAnalysis({ simulateTamper });
  }

  handleMetricsUpdate(state) {
    document.getElementById('liveJumpHeight').textContent = `${state.currentJumpHeightInches}"`;
    document.getElementById('liveDribbleSpeed').textContent = `${state.dribbleFrequencyHz} Hz`;
    document.getElementById('liveSprintSpeed').textContent = `${state.currentSpeedKmh} km/h`;
    document.getElementById('liveKneeAngle').textContent = `${state.kneeAngleDeg}°`;
    document.getElementById('analysisStatusText').textContent = `TRACKING: ${state.phase}`;
  }

  handleAnalysisComplete(report) {
    this.latestVideoReport = report;

    const startBtn = document.getElementById('startAnalysisBtn');
    startBtn.disabled = false;
    startBtn.textContent = '▶ Run AI Video Analysis';
    document.getElementById('analysisStatusText').textContent = 'ANALYSIS COMPLETE';

    // Update Deepfake Badge on Assessment page
    const badge = document.getElementById('deepfakeStatusBadge');
    if (report.deepfakeForensics.isAuthentic) {
      badge.className = 'status-pill pill-success';
      badge.textContent = `✓ AUTHENTIC (${report.deepfakeForensics.authenticityScore}%)`;
    } else {
      badge.className = 'status-pill pill-danger';
      badge.textContent = `⚠ TAMPERING FLAGGED (${report.deepfakeForensics.authenticityScore}%)`;
    }

    // Populate Report Card Modal
    this.displayAssessmentReportModal(report);
    this.updateAthleteScorecard();
    this.showNotification('AI Biomechanical Analysis & Deepfake Inspection completed!');
  }

  displayAssessmentReportModal(report) {
    const modal = document.getElementById('assessmentReportModal');
    if (!modal) return;

    document.getElementById('reportDrillTitle').textContent = report.drillTitle;
    document.getElementById('reportSport').textContent = report.sport;
    document.getElementById('reportTimestamp').textContent = new Date(report.timestamp).toLocaleString();
    document.getElementById('reportOverallScore').textContent = report.metrics.overallRating;

    document.getElementById('repJumpHeight').textContent = `${report.metrics.jumpHeightInches}" (${report.metrics.jumpHeightCm} cm)`;
    document.getElementById('repHangTime').textContent = `${report.metrics.hangTimeMs} ms`;
    document.getElementById('repDribbleSpeed').textContent = `${report.metrics.dribbleSpeedHz} Hz (${report.metrics.totalDribbles} hits)`;
    document.getElementById('repSprintSpeed').textContent = `${report.metrics.sprintTime40yd}s (${report.metrics.topSpeedKmh} km/h)`;

    // Deepfake Section
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

        // Format to datetime-local format YYYY-MM-DDTHH:mm
        const formatted = targetDate.toISOString().slice(0, 16);
        const medInput = document.getElementById('medicalReportTimestampInput');
        if (medInput) medInput.value = formatted;
      });
    }

    // File input for medical report
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
    const sample = SAMPLE_DATA.sampleMedicalReports[0];
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

    // Render result card on Medical Tab
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

      // Render substance table
      const listContainer = document.getElementById('medSubstanceChecklist');
      if (listContainer) {
        listContainer.innerHTML = verified.substancesTested.map(s => `
          <div class="substance-row">
            <span class="sub-name">${s.name || s.category}</span>
            <span class="sub-code">${s.code || 'WADA-S'}</span>
            <span class="sub-result result-negative">NEGATIVE (CLEAN)</span>
          </div>
        `).join('');
      }
    }

    this.updateAthleteScorecard();
    this.showNotification(verified.isFullyCleared ? '24h Medical & Anti-Doping Verification Passed!' : 'Medical Verification Alert: Check timestamp compliance.', verified.isFullyCleared ? 'success' : 'warning');
  }

  updateAthleteScorecard() {
    const cardEl = document.getElementById('athleteUnifiedScorecard');
    if (!cardEl) return;

    const jumpVal = this.latestVideoReport ? `${this.latestVideoReport.metrics.jumpHeightInches}"` : `36.4"`;
    const dribbleVal = this.latestVideoReport ? `${this.latestVideoReport.metrics.dribbleSpeedHz} Hz` : `4.8 Hz`;
    const sprintVal = this.latestVideoReport ? `${this.latestVideoReport.metrics.sprintTime40yd}s` : `4.42s`;
    const overallVal = this.latestVideoReport ? this.latestVideoReport.metrics.overallRating : 94;

    document.getElementById('cardJumpVal').textContent = jumpVal;
    document.getElementById('cardDribbleVal').textContent = dribbleVal;
    document.getElementById('cardSprintVal').textContent = sprintVal;
    document.getElementById('cardOverallScore').textContent = overallVal;

    // Badges update
    const dfBadge = document.getElementById('cardDeepfakeBadge');
    if (dfBadge) {
      if (this.latestVideoReport && this.latestVideoReport.deepfakeForensics.isAuthentic) {
        dfBadge.className = 'badge-tag badge-green';
        dfBadge.textContent = '✓ AI Deepfake Free';
      } else if (this.latestVideoReport && !this.latestVideoReport.deepfakeForensics.isAuthentic) {
        dfBadge.className = 'badge-tag badge-danger';
        dfBadge.textContent = '⚠ Tampered Video Flag';
      }
    }

    const medBadge = document.getElementById('cardMedBadge');
    if (medBadge) {
      if (this.latestMedicalReport && this.latestMedicalReport.isFullyCleared) {
        medBadge.className = 'badge-tag badge-cyan';
        medBadge.textContent = '🛡 24h Medical Cleared';
      } else if (this.latestMedicalReport && !this.latestMedicalReport.isFullyCleared) {
        medBadge.className = 'badge-tag badge-danger';
        medBadge.textContent = '⚠ Medical Expired/Flagged';
      }
    }
  }

  printOrDownloadScorecard() {
    window.print();
  }

  showNotification(message, type = 'info') {
    const container = document.getElementById('toastContainer');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast-pill toast-${type}`;
    toast.innerHTML = `
      <span class="toast-dot"></span>
      <span class="toast-text">${message}</span>
    `;

    container.appendChild(toast);

    setTimeout(() => {
      toast.classList.add('show');
    }, 50);

    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => toast.remove(), 300);
    }, 4000);
  }
}

// Instantiate and initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  window.app = new App();
  window.app.init();
});
