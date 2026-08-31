/**
 * ApexScout AI - Weekly AI Training & Peer Progression Arena Module
 * - Automated Kinetic Deficiency Breakdown (pelvic tilt, asymmetric takeoff, knee valgus)
 * - 7-Day AI Corrective Training Regimen with drill feedback
 * - Interactive Multi-Athlete Peer Progression Curves (Weeks 1 to 8)
 * - Head-to-Head Side-by-Side Dual Skeletal Challenge Arena
 */

class TrainingProgressionManager {
  constructor() {
    this.currentWeek = 4;
    this.selectedDeficiency = null;
    this.activeDuelPeer = 'ath-2'; // Mateo Silva default
    this.isDuelPlaying = false;
    this.duelAnimationFrame = null;

    // 8-Week Multi-Athlete Historical Progression Dataset
    this.progressionHistory = {
      weeks: ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8'],
      metrics: {
        jumpHeightInches: {
          label: 'Vertical Jump (inches)',
          athlete: [31.2, 32.5, 34.0, 36.4, 37.1, 37.8, 38.4, 39.0],
          peerAverage: [28.5, 29.2, 30.0, 31.0, 31.8, 32.4, 33.0, 33.6],
          eliteBenchmark: [36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5]
        },
        dribbleSpeedHz: {
          label: 'Dribble Cadence (Hz)',
          athlete: [3.6, 3.9, 4.2, 4.8, 5.0, 5.2, 5.3, 5.5],
          peerAverage: [3.2, 3.4, 3.6, 3.8, 4.0, 4.1, 4.2, 4.3],
          eliteBenchmark: [4.5, 4.7, 4.8, 5.0, 5.2, 5.3, 5.5, 5.6]
        },
        sprint40ydSec: {
          label: '40-Yard Sprint Time (sec - lower is better)',
          athlete: [4.82, 4.71, 4.58, 4.42, 4.38, 4.34, 4.30, 4.28],
          peerAverage: [5.10, 5.02, 4.95, 4.88, 4.80, 4.75, 4.70, 4.65],
          eliteBenchmark: [4.45, 4.40, 4.36, 4.32, 4.28, 4.25, 4.22, 4.20]
        },
        symmetryIndex: {
          label: 'Kinetic Symmetry Index (%)',
          athlete: [78, 82, 88, 94, 95, 97, 98, 99],
          peerAverage: [72, 74, 76, 80, 82, 84, 85, 87],
          eliteBenchmark: [92, 94, 95, 96, 97, 98, 99, 100]
        }
      }
    };

    // Automated Kinetic Deficiency Catalog
    this.kineticDeficiencies = [
      {
        id: 'def-1',
        title: 'Asymmetric Takeoff Ground Reaction Force',
        severity: 'Moderate (12% Right Bias)',
        impact: 'Reduces peak vertical leap by ~2.4 inches; uneven knee loading',
        kineticTrace: 'Left Ankle Ground Contact 115ms vs Right 98ms',
        correctionFocus: 'Unilateral plyometric bounding and single-leg force plate balance',
        prescribedDrill: 'Single-Leg Bulgarian Split Squats & Depth Drops'
      },
      {
        id: 'def-2',
        title: 'Dynamic Knee Valgus during Landing Phase',
        severity: 'Mild (14° Inward Collapse)',
        impact: 'Increases ACL strain upon deceleration and slows transition speed',
        kineticTrace: 'Knee Flexion Angle collapses inward at 0.62s timestamp',
        correctionFocus: 'Gluteus medius activation and banded landing mechanics',
        prescribedDrill: 'Banded Broad Jumps with Stick Landing'
      },
      {
        id: 'def-3',
        title: 'Sub-Optimal Arm Swing Kinetic Latency',
        severity: 'Low (95ms Arm Delay)',
        impact: 'Misses 8-10% potential momentum boost during penultimate step',
        kineticTrace: 'Shoulder extension peaks after hip lockout',
        correctionFocus: 'Synchronized arm drive initiation during knee flexion',
        prescribedDrill: 'Seated Arm Drive Sprint Cycles'
      }
    ];

    // 7-Day AI Corrective Training Regimen
    this.weeklySchedule = [
      { day: 'Day 1 (Mon)', focus: 'Unilateral Power & Takeoff Symmetry', drills: ['Single-Leg Box Step-Ups (4x8)', 'Depth Rebound Jumps (3x6)'], duration: '45 mins' },
      { day: 'Day 2 (Tue)', focus: 'Speed Cadence & Reaction Latency', drills: ['Tennis Ball Drop Reaction Sprints (5x)', 'Crossover Agility Ladders (4x)'], duration: '40 mins' },
      { day: 'Day 3 (Wed)', focus: 'Rest & Biomechanical Recovery', drills: ['Hip Mobility Foam Rolling', 'Hamstring Eccentric Lengthening'], duration: '25 mins' },
      { day: 'Day 4 (Thu)', focus: 'Triple Extension & Apex Force', drills: ['Trap Bar Jumps (4x5 @ 30% 1RM)', 'Knee Drive Hurdles (4x6)'], duration: '50 mins' },
      { day: 'Day 5 (Fri)', focus: 'Rotational Core & Pelvic Alignment', drills: ['Med Ball Rotational Wall Slams (3x10)', 'Side Plank Hip Abductions'], duration: '40 mins' },
      { day: 'Day 6 (Sat)', focus: 'Head-to-Head Combine Test Run', drills: ['Official AI Combine Video Recording', 'Peer Showdown Duel Submission'], duration: '30 mins' },
      { day: 'Day 7 (Sun)', focus: 'Weekly Progress Review & Rest', drills: ['AI Progress Trajectory Audit', '24h Medical Check Update'], duration: '20 mins' }
    ];
  }

  init() {
    this.renderDeficiencies();
    this.renderWeeklySchedule();
    this.renderProgressionGraph('jumpHeightInches');
    this.bindEvents();
  }

  bindEvents() {
    // Metric tab switcher for progression graph
    const metricButtons = document.querySelectorAll('.progression-metric-btn');
    metricButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        metricButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const metricKey = btn.getAttribute('data-metric');
        this.renderProgressionGraph(metricKey);
      });
    });

    // Head-to-head peer selector
    const peerSelect = document.getElementById('duelPeerSelect');
    if (peerSelect) {
      peerSelect.addEventListener('change', (e) => {
        this.activeDuelPeer = e.target.value;
        this.updateDuelPeerCard();
      });
    }

    // Play duel button
    const playDuelBtn = document.getElementById('playDuelBtn');
    if (playDuelBtn) {
      playDuelBtn.addEventListener('click', () => {
        this.startHeadToHeadDuel();
      });
    }
  }

  renderDeficiencies() {
    const container = document.getElementById('kineticDeficienciesList');
    if (!container) return;

    container.innerHTML = this.kineticDeficiencies.map((def, idx) => `
      <div class="deficiency-card ${idx === 0 ? 'active' : ''}" onclick="window.trainingManager.selectDeficiency(${idx})">
        <div class="def-header">
          <span class="def-severity">${def.severity}</span>
          <h4 class="def-title">${def.title}</h4>
        </div>
        <p class="def-impact"><strong>Biomechanical Impact:</strong> ${def.impact}</p>
        <div class="def-trace"><code>Telemetry Trace: ${def.kineticTrace}</code></div>
        <div class="def-prescribed">
          <strong>AI Prescribed Drill:</strong> ${def.prescribedDrill}
        </div>
      </div>
    `).join('');
  }

  selectDeficiency(index) {
    document.querySelectorAll('.deficiency-card').forEach((c, idx) => {
      if (idx === index) c.classList.add('active');
      else c.classList.remove('active');
    });
    this.selectedDeficiency = this.kineticDeficiencies[index];
  }

  renderWeeklySchedule() {
    const container = document.getElementById('weeklyScheduleContainer');
    if (!container) return;

    container.innerHTML = this.weeklySchedule.map(item => `
      <div class="schedule-day-row">
        <div class="day-badge">${item.day}</div>
        <div style="flex: 1; padding: 0 1rem;">
          <div class="day-focus">${item.focus}</div>
          <div class="day-drills">${item.drills.map(d => `<span class="drill-chip">${d}</span>`).join('')}</div>
        </div>
        <div class="day-duration">${item.duration}</div>
      </div>
    `).join('');
  }

  /**
   * Render Interactive Multi-Athlete Progression SVG Chart
   */
  renderProgressionGraph(metricKey) {
    const chartContainer = document.getElementById('progressionChartCanvas');
    if (!chartContainer) return;

    const data = this.progressionHistory.metrics[metricKey] || this.progressionHistory.metrics.jumpHeightInches;
    const weeks = this.progressionHistory.weeks;

    const minVal = Math.min(...data.athlete, ...data.peerAverage, ...data.eliteBenchmark) * 0.92;
    const maxVal = Math.max(...data.athlete, ...data.peerAverage, ...data.eliteBenchmark) * 1.08;

    const width = 640;
    const height = 240;
    const padX = 50;
    const padY = 30;

    const scaleX = (idx) => padX + (idx / (weeks.length - 1)) * (width - 2 * padX);
    const scaleY = (val) => height - padY - ((val - minVal) / (maxVal - minVal)) * (height - 2 * padY);

    const makePath = (arr) => arr.map((v, i) => `${i === 0 ? 'M' : 'L'} ${scaleX(i)} ${scaleY(v)}`).join(' ');

    const athletePath = makePath(data.athlete);
    const peerPath = makePath(data.peerAverage);
    const elitePath = makePath(data.eliteBenchmark);

    chartContainer.innerHTML = `
      <svg viewBox="0 0 ${width} ${height}" class="progression-svg" style="width: 100%; height: 100%;">
        <!-- Grid lines -->
        ${[0, 0.25, 0.5, 0.75, 1].map(pct => {
          const y = padY + pct * (height - 2 * padY);
          const val = (maxVal - pct * (maxVal - minVal)).toFixed(1);
          return `
            <line x1="${padX}" y1="${y}" x2="${width - padX}" y2="${y}" stroke="rgba(255,255,255,0.06)" stroke-dasharray="4 4" />
            <text x="${padX - 8}" y="${y + 4}" fill="#64748B" font-size="10" text-anchor="end">${val}</text>
          `;
        }).join('')}

        <!-- X Axis labels -->
        ${weeks.map((w, idx) => `
          <text x="${scaleX(idx)}" y="${height - 8}" fill="#94A3B8" font-size="11" font-weight="600" text-anchor="middle">${w}</text>
        `).join('')}

        <!-- Peer Average Line -->
        <path d="${peerPath}" fill="none" stroke="#64748B" stroke-width="2" stroke-dasharray="3 3" opacity="0.8" />

        <!-- Elite Benchmark Line -->
        <path d="${elitePath}" fill="none" stroke="#FFB800" stroke-width="2.5" opacity="0.85" />

        <!-- Athlete Line (Neon Cyan Glow) -->
        <path d="${athletePath}" fill="none" stroke="#00F2FE" stroke-width="3.5" filter="drop-shadow(0 0 8px rgba(0,242,254,0.6))" />

        <!-- Athlete Data Points -->
        ${data.athlete.map((v, i) => `
          <circle cx="${scaleX(i)}" cy="${scaleY(v)}" r="4.5" fill="#00F2FE" stroke="#080B11" stroke-width="2" />
        `).join('')}
      </svg>
    `;

    document.getElementById('progressionMetricTitle').textContent = data.label;
    document.getElementById('currentAthleteProgVal').textContent = `${data.athlete[data.athlete.length - 1]}`;
    document.getElementById('progGrowthPct').textContent = `+${(((data.athlete[7] - data.athlete[0]) / data.athlete[0]) * 100).toFixed(1)}% since W1`;
  }

  /**
   * Head-to-Head Side-by-Side Dual Skeletal Duel Animation
   */
  startHeadToHeadDuel() {
    const canvas = document.getElementById('duelCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const playBtn = document.getElementById('playDuelBtn');
    if (playBtn) playBtn.disabled = true;

    this.isDuelPlaying = true;
    const startTime = performance.now();
    const durationMs = 6000; // 6 seconds duel

    const duelLoop = (timestamp) => {
      if (!this.isDuelPlaying) return;
      const elapsed = timestamp - startTime;
      const progress = Math.min(1.0, elapsed / durationMs);

      this.renderDuelSkeletons(ctx, canvas, progress);

      if (progress < 1.0) {
        this.duelAnimationFrame = requestAnimationFrame(duelLoop);
      } else {
        this.isDuelPlaying = false;
        if (playBtn) playBtn.disabled = false;
        if (window.app) window.app.showNotification('Duel Completed! You won by +1.4" apex elevation!');
      }
    };

    this.duelAnimationFrame = requestAnimationFrame(duelLoop);
  }

  renderDuelSkeletons(ctx, canvas, progress) {
    const width = canvas.width = canvas.offsetWidth || 700;
    const height = canvas.height = canvas.offsetHeight || 320;
    ctx.clearRect(0, 0, width, height);

    // Split line
    ctx.strokeStyle = 'rgba(255,255,255,0.1)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(width / 2, 20);
    ctx.lineTo(width / 2, height - 20);
    ctx.stroke();

    // Athlete 1 (You - Cyan)
    this.drawDuelFighter(ctx, width * 0.25, height, progress, '#00F2FE', 'You (Alex Rivera)', '36.4" Apex');

    // Athlete 2 (Peer - Orange)
    this.drawDuelFighter(ctx, width * 0.75, height, progress * 0.96, '#FF6B00', 'Mateo Silva (Peer)', '31.5" Apex');
  }

  drawDuelFighter(ctx, posX, height, progress, color, name, stat) {
    const groundY = height * 0.82;
    const cycle = (progress * 2) % 1;
    const jump = cycle > 0.3 && cycle < 0.7 ? Math.sin((cycle - 0.3) / 0.4 * Math.PI) * 75 : 0;
    const athleteY = groundY - jump;

    // Head, torso, limbs
    ctx.strokeStyle = color;
    ctx.lineWidth = 3;
    ctx.shadowColor = color;
    ctx.shadowBlur = 8;

    // Draw stick skeleton
    ctx.beginPath();
    // Spine
    ctx.moveTo(posX, athleteY - 70); ctx.lineTo(posX, athleteY - 30);
    // Legs
    ctx.lineTo(posX - 18, athleteY);
    ctx.moveTo(posX, athleteY - 30); ctx.lineTo(posX + 18, athleteY);
    // Arms
    ctx.moveTo(posX - 22, athleteY - 50); ctx.lineTo(posX, athleteY - 60); ctx.lineTo(posX + 22, athleteY - 50);
    ctx.stroke();

    // Head
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.arc(posX, athleteY - 80, 10, 0, Math.PI * 2);
    ctx.fill();

    // Names & Tags
    ctx.shadowBlur = 0;
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(name, posX, height - 32);
    ctx.fillStyle = color;
    ctx.fillText(stat, posX, height - 16);
  }
}

if (typeof window !== 'undefined') {
  window.trainingManager = new TrainingProgressionManager();
}
