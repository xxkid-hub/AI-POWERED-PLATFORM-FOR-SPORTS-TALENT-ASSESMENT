# ⚡ ApexScout AI — Next-Gen AI Vision Sports Ecosystem

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI Vision Engine](https://img.shields.io/badge/AI%20Vision-Biomechanical%20HUD-00F2FE.svg)](#)
[![Integrity Guard](https://img.shields.io/badge/Integrity%20Guard-FFT%20%26%20Bio--Plausibility-39FF14.svg)](#)
[![Medical SLA](https://img.shields.io/badge/Medical%20SLA-24--48h%20WADA%20OCR-FF6B00.svg)](#)
[![Progression Arena](https://img.shields.io/badge/Progression%20Arena-Weekly%20AI%20%26%20Duels-9B51E0.svg)](#)

> **ApexScout AI** is an autonomous, vision-first sports talent scouting and progression ecosystem. The platform ingests raw sports video footage with zero manual preset selection, automatically infers the sport and specific action skill, extracts real-time kinematic telemetry, evaluates the athlete's personal score and performance tier, and enforces rigorous anti-deepfake (2D FFT) and anti-doping (24–48h SLA) compliance.

---

## 🏗 System Architecture & Autonomous Video Pipeline

```
+─────────────────────────────────────────────────────────────────────────+
│                    Raw Video Ingestion Layer (Zero-Preset)              │
│  - Raw Video File Upload (.mp4, .mov, .avi, .webm)                      │
│  - Live Athlete Camera Stream Ingestion                                 │
│  - 6-Sport Benchmark Action Dataset Testing                             │
+─────────────────────────────────────────────────────────────────────────+
                                     │
                                     ▼
+─────────────────────────────────────────────────────────────────────────+
│                   Temporal Kinematics & Motion Engine                   │
│  - Optical Flow Displacement & Velocity Telemetry (km/h)                │
│  - Active Frame Density (%) & Reaction Onset Latency (sec)              │
│  - Peak Kinetic Energy Keyframe Extraction                              │
│  - Stationary / Non-Sports Motion Rejection Guard                       │
+─────────────────────────────────────────────────────────────────────────+
                                     │
                                     ▼
+─────────────────────────────────────────────────────────────────────────+
│              Multi-Modal Neural Vision & Domain Fusion Engine           │
│  - 5-Class VotingClassifier Ensemble (RandomForest + ExtraTrees)        │
│  - Domain Signature Fusion:                                             │
│    * Cricket: Longitudinal tan pitch strip flanked by green grass       │
│    * Soccer: Uniform full-field green natural turf                      │
│    * Basketball: Hardwood amber parquet court                           │
│    * Kabaddi: Interlocking dual-zone EVA foam mat                       │
│    * Volleyball: Indoor court with high net boundary                    │
+─────────────────────────────────────────────────────────────────────────+
                                     │
                                     ▼
+─────────────────────────────────────────────────────────────────────────+
│                 Athlete Personal Scorecard & Biomechanics               │
│  - Overall Talent Composite Rating (0-100)                              │
│  - Performance Classification Tiers (Tier 1 Elite, Tier 2, Tier 3)      │
│  - 4 Dimensional Sub-Scores: Power, Accuracy, Reaction, Joint Safety    │
│  - 8-Component Skill-by-Skill Kinematic Breakdown Table                 │
│  - Scout Talent Evaluation & AI Coach Action Prescription               │
+─────────────────────────────────────────────────────────────────────────+
```

---

## 🛡 1. Integrity, Anti-Deepfake & Medical Verification

### Deepfake & Video Tampering Detection
* **Temporal & Frequency Artifact Analysis:** Runs spatial-frequency 2D FFT residue checks across frames to detect face swaps, diffusion-generated artifacts (Sora/Runway), and frame-rate splicing.
* **Biomechanical Plausibility Filter:** Compares physical acceleration against physiological human limits (maximum angular velocity of knee flexion $\le 1000^\circ/\text{sec}$, acceleration $\le 12.5\text{ m/s}^2$, valgus inward collapse $< 18^\circ$).
* **Liveness & Dynamic Prompting:** Prompts the athlete with randomized AR cues during recording (e.g. *"Touch Left Ear with Right Hand before sprint"*) to block pre-recorded playback attacks.

### Medical & Anti-Doping Compliance Engine
* **24–48 Hour Verification SLA:** Athletes competing in verified trials or leaderboard rankings must upload an accredited medical/anti-doping certificate within a strict $24\text{ to }48\text{ hour}$ window.
* **Automated Document OCR & Validation:** Scans lab accreditation stamps, digital signatures, NADA/WADA registration numbers, and timestamp metadata.
* **3-Tier Status Enforcement:**
  * 🟢 **Verified (Green Badge):** Validated by OCR + tested within 24–48h window + clean anti-doping panel.
  * 🟡 **Pending Verification (Yellow Badge):** Grace period active ($< 48\text{ hrs}$). Provisional scores recorded.
  * 🔴 **Flagged / Delisted (Red Badge):** Window expired ($> 48\text{ hrs}$) or test non-compliant; delisted from public leaderboards.

---

## 📈 2. Weekly AI Training & Improvement Progression

### Dynamic Weekly Training Loops
* **Automated Kinetic Breakdown:** Translates video assessments into specific biomechanical deficiencies:
  * *Asymmetric Takeoff Force (12% Right Bias)*
  * *Dynamic Knee Valgus during Landing Phase (14° Inward Collapse)*
  * *Sub-Optimal Arm Swing Kinetic Latency (95ms Delay)*
* **AI Training Recommendations:** Generates a 7-day, drill-by-drill regimen with real-time video feedback to correct flagged movement patterns.

### Peer Comparison & Internal Competition
* **Peer Progression Curves:** Interactive multi-athlete trajectory graphs displaying velocity, jump airtime, stamina decay, and symmetry indices over weeks (Weeks 1 to 8).
* **Head-to-Head Drill Duels:** Athletes challenge peers to drill duels (e.g. *"Vertical Jump Weekly Showdown"*, *"40-Yard Sprint Duel"*), overlaying skeletal runs side-by-side with live kinematic comparisons.

---

## 👥 3. Coach Connectivity & Scouting Portal

* **Scout Discovery Engine:** Coaches and regional scouts filter verified profiles using biometric thresholds, sport categories, and performance trajectory curves.
* **Direct Talent Pipeline:** Integrated messaging, trial invitations, and **Verifiable Digital Athlete Passports** (containing verified motion telemetry, anti-doping records, and match logs).

---

## 🌾 4. Grassroots & Rural Accessibility Suite

* **📶 2G/3G Low-Data Mode:** Compresses video telemetry ($<120\text{ KB}$) for smooth submission over basic village cellular networks.
* **🔊 AI Voiceover Coach:** Reads biomechanical telemetry aloud in **English, Hindi (हिन्दी), or Spanish**.
* **📲 1-Click WhatsApp Scout Dossier:** Instantly dispatch verified dossiers to coaches and academy directors via WhatsApp.
* **📞 24/7 Toll-Free Hotline:** Direct support for grassroots combines and state federations (`1800-11-SPORTS`).

---

## 🎯 Multi-Sport Biomechanical Skill Matrices & Dimensions

ApexScout AI classifies and analyzes specialized kinematics tailored to 5 core sports:

| Sport | Primary Action Skill | Domain Category | Key Kinematic Dimensions Analyzed |
| :--- | :--- | :--- | :--- |
| **Cricket** | Outswinger Fast Bowling Action | Pace Bowling & Seam | Run-up momentum, front-knee lockout (178°), release apex (2.15m), outswing deviation (2.4°), upright seam backspin |
| **Basketball** | Crossover to 3-Point Jump Shot | Elevation & Shooting Arc | 4.8 Hz dribble separation, square 1-2 foot plant, 24.5" vertical rise, 48° entry launch angle, gooseneck wrist snap |
| **Football / Soccer** | Precision Penalty Strike & Placement | Striking & Kinematics | 45° angled approach, 35° ankle plant foot angle, 42° hip torque, instep sweet-spot strike, 14 rad/s Magnus spin |
| **Kabaddi** | Toe Touch & Low-Squat Dubki Raid | Agility & Evasion | 16.2 km/h baulk approach, 142cm leg reach extension, 45° low-squat dubki flex, 22.4 km/h burst recovery |
| **Volleyball** | Power Cross-Court Aerial Spike | Aerial Attack | 4-step approach, heel-to-toe block step, 31.2" net clearance, 55° thoracic coil, -28° downward topspin penetration |

---

## 🤖 Machine Learning Pipeline & Architecture

```
sports-talent-ai/
├── config/
│   ├── settings.py             # Centralized paths, seeds, schema & constants
│   └── config.yaml             # External YAML config for hyperparameter tuning
├── dataset/                    # 500 multi-sport sample frames (100 per sport)
│   └── dataset_index.json      # Dataset manifest & distribution metadata
├── src/
│   ├── biomechanics/           # Kinematics, angular velocity, and 12-component telemetry
│   │   ├── kinematics.py       # Joint angles, valgus collapse, and bio-plausibility checks
│   │   └── telemetry.py        # BiomechanicsTelemetry dataclass & score computation
│   ├── security/               # 2D FFT spectral anti-deepfake & AR liveness guard
│   │   ├── fft_detector.py     # Frequency residue energy ratio & tamper probability
│   │   └── liveness.py         # Dynamic randomized AR action challenges
│   ├── medical/                # Medical & Anti-Doping compliance engine
│   │   └── sla_verifier.py     # 24–48h SLA verifier, WADA OCR scanner & 3-tier badges
│   ├── server/                 # REST API & static web serving package
│   │   └── handlers.py         # Request dispatcher for health, predict, and medical endpoints
│   ├── ui/                     # Modular Streamlit UI presentation system
│   │   ├── styles.py           # Athletic dark carbon theme & custom design tokens
│   │   ├── mock_data.py        # Centralized catalogs, peer curves, and drill registers
│   │   ├── audio.py            # Synthetic audio chime generator & multilingual voice scripts
│   │   └── tabs/               # Specialized presentation tab modules
│   ├── motion_detector.py      # Optical flow & video motion energy filter
│   ├── preprocessor.py         # SportsImagePreprocessor (BGR, PIL, 62-dim features)
│   ├── trainer.py              # SportsModelTrainer with seed_everything()
│   ├── evaluate.py             # Standalone evaluator & confusion matrix plotter
│   ├── benchmark.py            # Latency benchmark (p50, p95, p99 ms)
│   └── eda.py                  # Exploratory Data Analysis & balance verification
├── tests/                      # 40 passing unit and integration tests
│   ├── test_biomechanics.py    # Joint kinematics and telemetry scoring tests
│   ├── test_security.py        # 2D FFT spectral and dynamic AR liveness tests
│   ├── test_medical.py         # 24-48h SLA verifier and WADA OCR tests
│   ├── test_server.py          # Server and REST endpoint unit tests
│   ├── test_ui_modules.py      # UI data structures and audio chime tests
│   ├── test_preprocessor.py    # Image feature extraction & BGR/PIL tests
│   ├── test_model.py           # Model loading, domain signature fusion & prediction tests
│   └── test_pipeline.py        # End-to-end integration & inference tests
├── results/
│   ├── confusion_matrix.png    # High-resolution evaluated confusion matrix plot
│   ├── evaluation_summary.json # Standalone test set metrics
│   ├── benchmark_report.json   # Latency SLA report (p95: 42.7ms < 100ms)
│   └── eda_summary.json        # Dataset balance and variance report
└── trained_model/              # Saved model checkpoints & scalers
    ├── sports_talent_model.joblib
    └── feature_scaler.joblib
```

---

## 🛠 Reproducible Commands

### 1. Run Automated Unit & Integration Tests (40/40 Passing)
```bash
python -m pytest tests/ -v
```

### 2. Retrain Model with Deterministic Random Seed
```bash
python train_model.py --seed 42 --test-split 0.20 --n-estimators 100
```

### 3. Run Standalone Evaluation & Generate Confusion Matrix
```bash
python evaluate.py
```

### 4. Run Latency Benchmark
```bash
python benchmark.py --iterations 100
```

### 5. Run Live Inference on a Sports Image
```bash
python infer.py --image dataset/Cricket/CR_aug_001.png
```

---

## Quick Start — Streamlit Platform Server (Port 8501)

ApexScout AI runs exclusively on the **Streamlit Port** ([http://localhost:8501](http://localhost:8501)):

```bash
# Launch the Streamlit Platform (Serves on http://localhost:8501)
python server.py
```
*Alternatively, run `python app.py` or `streamlit run streamlit_app.py`.*

### Platform Tabs on [http://localhost:8501](http://localhost:8501):
1. **Autonomous Video & AR Combine Analysis:** Ingests raw video, classifies sport and skill, computes personal score, and renders the 8-component kinematic analysis table.
2. **Custom ML Model & Dataset Hub:** Live image inference, multi-class probability charts, and model evaluation metrics.
3. **24–48h Medical SLA Engine:** WADA document OCR scanner & compliance timer.
4. **Progression Arena:** Weekly AI improvement trajectories and head-to-head peer duels.
5. **Verified Scout Leaderboard & Passports:** Verifiable athlete passports and coaches marketplace.
6. **24/7 Helpline & Grassroots Suite:** Low-data mode, multilingual voiceover coach, and WhatsApp dossier dispatch.

---

## License
This project is open-source under the [MIT License](LICENSE).
