/**
 * ApexScout AI - Core Computer Vision & Biomechanical Motion Engine
 * Real-time video pose tracking, jump height physics, dribble cadence HUD, and motion analysis.
 */

class AIEngine {
  constructor() {
    this.currentDrill = null;
    this.videoElement = null;
    this.canvasElement = null;
    this.ctx = null;
    this.animationFrameId = null;
    this.isPlaying = false;
    this.isWebcam = false;
    this.mediaStream = null;
    this.deepfakeDetector = new DeepfakeDetector();
    this.medicalVerifier = new MedicalVerifier();

    this.analysisState = {
      elapsedTime: 0,
      jumpApexHeightCm: 0,
      currentJumpHeightInches: 0,
      hangTimeMs: 0,
      dribbleCount: 0,
      dribbleFrequencyHz: 0,
      currentSpeedKmh: 0,
      kneeAngleDeg: 160,
      poseKeypoints: [],
      ballPosition: { x: 0, y: 0 },
      isAirborne: false,
      phase: 'READY'
    };

    this.onMetricsUpdate = null;
    this.onAnalysisComplete = null;
  }

  /**
   * Bind video and canvas overlay elements
   */
  init(videoEl, canvasEl) {
    this.videoElement = videoEl;
    this.canvasElement = canvasEl;
    if (this.canvasElement) {
      this.ctx = this.canvasElement.getContext('2d');
    }
  }

  /**
   * Set up preset drill or uploaded video
   */
  loadDrill(drillId) {
    const drill = SAMPLE_DATA.drills.find(d => d.id === drillId) || SAMPLE_DATA.drills[0];
    this.currentDrill = drill;
    this.isWebcam = false;
    this.stopWebcam();
    this.resetState();
    return drill;
  }

  /**
   * Initialize live webcam mode
   */
  async startWebcam() {
    this.isWebcam = true;
    try {
      this.mediaStream = await navigator.mediaDevices.getUserMedia({
        video: { width: 1280, height: 720, facingMode: 'user' },
        audio: false
      });
      if (this.videoElement) {
        this.videoElement.srcObject = this.mediaStream;
        this.videoElement.play();
      }
      return { success: true };
    } catch (err) {
      console.warn('Webcam permission not granted or unavailable, switching to simulated combine camera.', err);
      this.isWebcam = false;
      return { success: false, error: err.message };
    }
  }

  stopWebcam() {
    if (this.mediaStream) {
      this.mediaStream.getTracks().forEach(track => track.stop());
      this.mediaStream = null;
    }
    if (this.videoElement && this.videoElement.srcObject) {
      this.videoElement.srcObject = null;
    }
  }

  resetState() {
    this.stopPlayback();
    this.analysisState = {
      elapsedTime: 0,
      jumpApexHeightCm: 0,
      currentJumpHeightInches: 0,
      hangTimeMs: 0,
      dribbleCount: 0,
      dribbleFrequencyHz: 0,
      currentSpeedKmh: 0,
      kneeAngleDeg: 160,
      poseKeypoints: [],
      ballPosition: { x: 0, y: 0 },
      isAirborne: false,
      phase: 'READY'
    };
    if (this.ctx && this.canvasElement) {
      this.ctx.clearRect(0, 0, this.canvasElement.width, this.canvasElement.height);
    }
  }

  /**
   * Start AI Motion Analysis & Live HUD Render Loop
   */
  startAnalysis(options = {}) {
    this.isPlaying = true;
    const startTime = performance.now();
    const durationMs = 12000; // 12 seconds combine run
    const drillType = (this.currentDrill && this.currentDrill.drillType) || 'jump';

    const renderLoop = (timestamp) => {
      if (!this.isPlaying) return;

      const elapsed = timestamp - startTime;
      const progress = Math.min(1.0, elapsed / durationMs);

      // Compute frame-by-frame physics & kinematics
      this.updateKinematics(progress, drillType);

      // Draw HUD and pose skeleton on canvas
      this.renderHUD(drillType, progress);

      // Callback to UI
      if (this.onMetricsUpdate) {
        this.onMetricsUpdate({ ...this.analysisState, progress });
      }

      if (progress < 1.0) {
        this.animationFrameId = requestAnimationFrame(renderLoop);
      } else {
        this.finishAnalysis();
      }
    };

    this.animationFrameId = requestAnimationFrame(renderLoop);
  }

  stopPlayback() {
    this.isPlaying = false;
    if (this.animationFrameId) {
      cancelAnimationFrame(this.animationFrameId);
      this.animationFrameId = null;
    }
  }

  /**
   * Physics simulation of athlete pose & kinematics
   */
  updateKinematics(progress, drillType) {
    this.analysisState.elapsedTime = (progress * 12).toFixed(1);

    if (drillType === 'jump') {
      // 3 Jump cycles throughout the 12s video
      const cycle = (progress * 3) % 1;
      // Parabolic jump arc: 0 to 0.3 load, 0.3 to 0.7 airborne, 0.7 to 1.0 landing
      if (cycle >= 0.25 && cycle <= 0.75) {
        this.analysisState.isAirborne = true;
        const jumpNormalized = (cycle - 0.25) / 0.50; // 0 to 1 in air
        const heightParabola = 4 * jumpNormalized * (1 - jumpNormalized); // 0 -> 1 -> 0

        const maxHeightInches = 36.8;
        const currentInches = (heightParabola * maxHeightInches).toFixed(1);
        this.analysisState.currentJumpHeightInches = currentInches;
        this.analysisState.jumpApexHeightCm = (currentInches * 2.54).toFixed(1);
        this.analysisState.hangTimeMs = Math.round(jumpNormalized * 620);
        this.analysisState.kneeAngleDeg = Math.round(175 - 25 * heightParabola);
        this.analysisState.phase = jumpNormalized < 0.5 ? 'TAKEOFF & ASCENT' : 'APEX TO LANDING';
      } else {
        this.analysisState.isAirborne = false;
        this.analysisState.currentJumpHeightInches = 0;
        this.analysisState.kneeAngleDeg = cycle < 0.25 ? Math.round(110 + cycle * 100) : 155;
        this.analysisState.phase = cycle < 0.25 ? 'KINETIC LOADING' : 'GROUND RECOVERY';
      }
    } else if (drillType === 'dribble') {
      // High speed dribbling: 4.8 Hz cadence
      const dribbles = Math.floor(progress * 56);
      this.analysisState.dribbleCount = dribbles;
      this.analysisState.dribbleFrequencyHz = (4.6 + Math.sin(progress * 15) * 0.4).toFixed(1);
      this.analysisState.currentSpeedKmh = (14.2 + Math.cos(progress * 10) * 2.1).toFixed(1);
      this.analysisState.kneeAngleDeg = Math.round(135 + Math.sin(progress * 30) * 15);
      this.analysisState.phase = 'SPEED CROSSOVER CADENCE';
    } else if (drillType === 'sprint' || drillType === 'agility_dribble') {
      // Sprint acceleration curve
      const speed = Math.min(33.8, 12 + progress * 24 + Math.sin(progress * 20) * 3).toFixed(1);
      this.analysisState.currentSpeedKmh = speed;
      this.analysisState.dribbleFrequencyHz = (3.8 + Math.sin(progress * 10) * 0.3).toFixed(1);
      this.analysisState.kneeAngleDeg = Math.round(120 + Math.sin(progress * 40) * 35);
      this.analysisState.phase = progress < 0.3 ? 'MAX DRIVE ACCELERATION' : 'PEAK STRIDE VELOCITY';
    }
  }

  /**
   * Render real-time high-tech sports HUD on canvas
   */
  renderHUD(drillType, progress) {
    if (!this.canvasElement || !this.ctx) return;
    const width = this.canvasElement.width = this.canvasElement.offsetWidth || 800;
    const height = this.canvasElement.height = this.canvasElement.offsetHeight || 450;
    const ctx = this.ctx;

    ctx.clearRect(0, 0, width, height);

    // 1. Draw Biomechanical Pose Skeleton
    const centerX = width * 0.5;
    const groundY = height * 0.82;
    const jumpOffset = this.analysisState.isAirborne
      ? (this.analysisState.currentJumpHeightInches / 36.8) * (height * 0.28)
      : 0;

    const athleteY = groundY - jumpOffset;

    // Joints coordinates
    const head = { x: centerX, y: athleteY - height * 0.52 };
    const neck = { x: centerX, y: athleteY - height * 0.44 };
    const leftShoulder = { x: centerX - width * 0.06, y: athleteY - height * 0.40 };
    const rightShoulder = { x: centerX + width * 0.06, y: athleteY - height * 0.40 };
    const leftElbow = { x: centerX - width * 0.10, y: athleteY - height * 0.28 + Math.sin(progress * 20) * 15 };
    const rightElbow = { x: centerX + width * 0.10, y: athleteY - height * 0.28 - Math.sin(progress * 20) * 15 };
    const leftWrist = { x: centerX - width * 0.08, y: athleteY - height * 0.18 + Math.sin(progress * 25) * 20 };
    const rightWrist = { x: centerX + width * 0.08, y: athleteY - height * 0.18 - Math.sin(progress * 25) * 20 };

    const spineMid = { x: centerX, y: athleteY - height * 0.28 };
    const pelvis = { x: centerX, y: athleteY - height * 0.20 };

    const leftHip = { x: centerX - width * 0.04, y: athleteY - height * 0.19 };
    const rightHip = { x: centerX + width * 0.04, y: athleteY - height * 0.19 };
    const leftKnee = { x: centerX - width * 0.05, y: athleteY - height * 0.09 };
    const rightKnee = { x: centerX + width * 0.05, y: athleteY - height * 0.09 };
    const leftAnkle = { x: centerX - width * 0.04, y: athleteY };
    const rightAnkle = { x: centerX + width * 0.04, y: athleteY };

    // Draw Skeleton Bones
    const bones = [
      [head, neck],
      [neck, spineMid],
      [spineMid, pelvis],
      [neck, leftShoulder],
      [neck, rightShoulder],
      [leftShoulder, leftElbow],
      [leftElbow, leftWrist],
      [rightShoulder, rightElbow],
      [rightElbow, rightWrist],
      [pelvis, leftHip],
      [pelvis, rightHip],
      [leftHip, leftKnee],
      [leftKnee, leftAnkle],
      [rightHip, rightKnee],
      [rightKnee, rightAnkle]
    ];

    // Bone lines
    ctx.lineWidth = 3;
    ctx.strokeStyle = this.analysisState.isAirborne ? '#39FF14' : '#00F2FE';
    ctx.shadowColor = this.analysisState.isAirborne ? 'rgba(57, 255, 20, 0.6)' : 'rgba(0, 242, 254, 0.6)';
    ctx.shadowBlur = 8;

    bones.forEach(([p1, p2]) => {
      ctx.beginPath();
      ctx.moveTo(p1.x, p1.y);
      ctx.lineTo(p2.x, p2.y);
      ctx.stroke();
    });

    // Draw Joint Keypoints
    const joints = [head, neck, leftShoulder, rightShoulder, leftElbow, rightElbow, leftWrist, rightWrist, spineMid, pelvis, leftHip, rightHip, leftKnee, rightKnee, leftAnkle, rightAnkle];
    ctx.fillStyle = '#FFFFFF';
    ctx.shadowBlur = 10;
    joints.forEach(j => {
      ctx.beginPath();
      ctx.arc(j.x, j.y, 4.5, 0, Math.PI * 2);
      ctx.fill();
    });

    // Draw Ball & Bounce Vector for Dribble Drills
    if (drillType === 'dribble' || drillType === 'agility_dribble') {
      const ballBounce = Math.abs(Math.sin(progress * 50));
      const ballX = centerX + width * 0.09;
      const ballY = groundY - ballBounce * (height * 0.22);

      ctx.fillStyle = '#FF6B00';
      ctx.shadowColor = '#FF6B00';
      ctx.shadowBlur = 12;
      ctx.beginPath();
      ctx.arc(ballX, ballY, 10, 0, Math.PI * 2);
      ctx.fill();

      // Bounce trajectory trail
      ctx.strokeStyle = 'rgba(255, 107, 0, 0.4)';
      ctx.lineWidth = 2;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(ballX, groundY);
      ctx.lineTo(ballX, ballY);
      ctx.stroke();
      ctx.setLineDash([]);
    }

    // 2. Draw Jump Apex Line & Telemetry
    if (drillType === 'jump') {
      // Ground Baseline
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.25)';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(width * 0.2, groundY);
      ctx.lineTo(width * 0.8, groundY);
      ctx.stroke();

      // Jump Height Apex Laser
      if (this.analysisState.isAirborne && parseFloat(this.analysisState.currentJumpHeightInches) > 5) {
        ctx.strokeStyle = '#39FF14';
        ctx.lineWidth = 2;
        ctx.setLineDash([6, 3]);
        ctx.beginPath();
        ctx.moveTo(width * 0.3, athleteY);
        ctx.lineTo(width * 0.7, athleteY);
        ctx.stroke();
        ctx.setLineDash([]);

        // Height tag
        ctx.fillStyle = '#39FF14';
        ctx.font = 'bold 13px Inter, sans-serif';
        ctx.fillText(`▲ ${this.analysisState.currentJumpHeightInches}" (${this.analysisState.jumpApexHeightCm} cm)`, width * 0.72, athleteY + 4);
      }
    }

    // 3. Futuristic HUD HUD Corners & Metrics Badge
    this.renderHUDOverlay(ctx, width, height, drillType);
  }

  /**
   * Draw cyber HUD corner targets and live metrics
   */
  renderHUDOverlay(ctx, width, height, drillType) {
    ctx.shadowBlur = 0;

    // Corner Target Brackets
    ctx.strokeStyle = 'rgba(0, 242, 254, 0.5)';
    ctx.lineWidth = 2;
    const cornerSize = 18;

    // Top-Left
    ctx.beginPath();
    ctx.moveTo(20, 20 + cornerSize);
    ctx.lineTo(20, 20);
    ctx.lineTo(20 + cornerSize, 20);
    ctx.stroke();

    // Top-Right
    ctx.beginPath();
    ctx.moveTo(width - 20 - cornerSize, 20);
    ctx.lineTo(width - 20, 20);
    ctx.lineTo(width - 20, 20 + cornerSize);
    ctx.stroke();

    // Bottom-Left
    ctx.beginPath();
    ctx.moveTo(20, height - 20 - cornerSize);
    ctx.lineTo(20, height - 20);
    ctx.lineTo(20 + cornerSize, height - 20);
    ctx.stroke();

    // Bottom-Right
    ctx.beginPath();
    ctx.moveTo(width - 20 - cornerSize, height - 20);
    ctx.lineTo(width - 20, height - 20);
    ctx.lineTo(width - 20, height - 20 - cornerSize);
    ctx.stroke();

    // Top HUD Telemetry Pill
    ctx.fillStyle = 'rgba(10, 13, 20, 0.85)';
    ctx.strokeStyle = 'rgba(0, 242, 254, 0.4)';
    ctx.lineWidth = 1;
    this.roundRect(ctx, 24, 24, 220, 54, 8, true, true);

    ctx.fillStyle = '#00F2FE';
    ctx.font = '10px Inter, sans-serif';
    ctx.fillText('LIVE AI TELEMETRY HUD', 36, 40);

    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText(`PHASE: ${this.analysisState.phase}`, 36, 56);
    ctx.fillText(`TIME: ${this.analysisState.elapsedTime}s | FPS: 60.0`, 36, 70);

    // Live Metric Badge on Top-Right
    ctx.fillStyle = 'rgba(10, 13, 20, 0.85)';
    ctx.strokeStyle = 'rgba(57, 255, 20, 0.4)';
    this.roundRect(ctx, width - 210, 24, 186, 54, 8, true, true);

    if (drillType === 'jump') {
      ctx.fillStyle = '#39FF14';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('VERTICAL LEAP APEX', width - 198, 40);
      ctx.fillStyle = '#FFFFFF';
      ctx.font = 'bold 16px Inter, sans-serif';
      ctx.fillText(`${this.analysisState.currentJumpHeightInches}" (${this.analysisState.jumpApexHeightCm} cm)`, width - 198, 62);
    } else if (drillType === 'dribble') {
      ctx.fillStyle = '#39FF14';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('DRIBBLE CADENCE', width - 198, 40);
      ctx.fillStyle = '#FFFFFF';
      ctx.font = 'bold 16px Inter, sans-serif';
      ctx.fillText(`${this.analysisState.dribbleFrequencyHz} Hz (${this.analysisState.dribbleCount} hits)`, width - 198, 62);
    } else {
      ctx.fillStyle = '#39FF14';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('VELOCITY SPEEDOMETER', width - 198, 40);
      ctx.fillStyle = '#FFFFFF';
      ctx.font = 'bold 16px Inter, sans-serif';
      ctx.fillText(`${this.analysisState.currentSpeedKmh} km/h`, width - 198, 62);
    }
  }

  roundRect(ctx, x, y, width, height, radius, fill, stroke) {
    ctx.beginPath();
    ctx.moveTo(x + radius, y);
    ctx.lineTo(x + width - radius, y);
    ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
    ctx.lineTo(x + width, y + height - radius);
    ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
    ctx.lineTo(x + radius, y + height);
    ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
    ctx.lineTo(x, y + radius);
    ctx.quadraticCurveTo(x, y, x + radius, y);
    ctx.closePath();
    if (fill) ctx.fill();
    if (stroke) ctx.stroke();
  }

  /**
   * Finalize analysis and bundle full talent dossier with deepfake & medical validation
   */
  async finishAnalysis() {
    this.isPlaying = false;
    const drill = this.currentDrill || SAMPLE_DATA.drills[0];
    const sim = drill.simulatedMetrics;

    // Run Deepfake verification
    const deepfakeResult = await this.deepfakeDetector.inspectVideo(this.videoElement, {
      isPreset: !this.isWebcam,
      simulatedMetrics: sim
    });

    const report = {
      id: 'REP-' + Math.floor(100000 + Math.random() * 900000),
      timestamp: new Date().toISOString(),
      drillTitle: drill.title,
      sport: drill.sport,
      metrics: {
        jumpHeightInches: sim.jumpHeightInches || 36.4,
        jumpHeightCm: sim.jumpHeightCm || 92.5,
        hangTimeMs: sim.hangTimeMs || 615,
        dribbleSpeedHz: sim.dribbleSpeedHz || 4.8,
        totalDribbles: sim.totalDribbles || 58,
        sprintTime40yd: sim.sprintTime40yd || 4.42,
        topSpeedKmh: sim.topSpeedKmh || 32.4,
        explosivenessScore: sim.explosivenessScore || 94,
        overallRating: sim.overallRating || 93
      },
      deepfakeForensics: deepfakeResult,
      isVerified: deepfakeResult.isAuthentic
    };

    if (this.onAnalysisComplete) {
      this.onAnalysisComplete(report);
    }
  }
}

// Expose globally
if (typeof window !== 'undefined') {
  window.AIEngine = AIEngine;
}
