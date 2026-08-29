# ⚡ ApexScout AI — Next-Gen AI Vision Sports Ecosystem

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI Vision Engine](https://img.shields.io/badge/AI%20Vision-Biomechanical%20HUD-00F2FE.svg)](#)
[![Integrity Guard](https://img.shields.io/badge/Integrity%20Guard-FFT%20%26%20Bio--Plausibility-39FF14.svg)](#)
[![Medical SLA](https://img.shields.io/badge/Medical%20SLA-24--48h%20WADA%20OCR-FF6B00.svg)](#)
[![Progression Arena](https://img.shields.io/badge/Progression%20Arena-Weekly%20AI%20%26%20Duels-9B51E0.svg)](#)

> **ApexScout AI** is a real-time, vision-first sports scouting and development ecosystem. The platform enforces strict video integrity (anti-deepfake, biomechanical plausibility, anti-doping verification) while driving athlete engagement via weekly AI training, coach matching, and an open peer-to-peer progression arena.

---

## 🏗 System Architecture & PRD Functional Matrix

```
+-------------------------------------------------------------------+
|                        Client Layer (Mobile App)                  |
|  - Real-Time Camera Stream   - AR Dynamic Liveness Prompts        |
|  - On-Device Pose Inference  - Medical Document Upload (Camera/PDF|
+-------------------------------------------------------------------+
                                  │
                                  ▼
+-------------------------------------------------------------------+
|                     Security & Ingestion Gateway                  |
|  - Deepfake / Frame Tampering Filter (FFT & Diffusion Detection)  |
|  - Biomechanical Human Movement Plausibility Check                |
|  - Anti-Doping Expiration Timer (24-48h Strict SLA)               |
+-------------------------------------------------------------------+
                                  │
                                  ▼
+─────────────────────────────────+    +────────────────────────────+
|     AI Vision & Analytics Engine|    |     Medical OCR & Admin    |
|  - Frame-by-Frame Kinematics    |    |  - WADA/Lab Signature OCR  |
|  - Weekly Improvement Modeler   |    |  - Tamper & Timestamp Check|
+─────────────────────────────────+    +────────────────────────────+
                                  │
                                  ▼
+-------------------------------------------------------------------+
|                    Community & Scouting Portal                    |
|  - Peer-to-Peer Progress Graphs  - Scout Filters & Direct Inbox   |
+-------------------------------------------------------------------+
```

---

## 🛡 1. Integrity, Anti-Deepfake & Medical Verification

### Deepfake & Video Tampering Detection
* **Temporal & Frequency Artifact Analysis:** Runs spatial-frequency 2D FFT residue checks across frames to detect face swaps, diffusion-generated artifacts (Sora/Runway), and frame-rate splicing.
* **Biomechanical Plausibility Filter:** Compares physical acceleration against physiological human limits (maximum angular velocity of knee flexion $\le 1000^\circ/\text{sec}$, acceleration $\le 12.5\text{ m/s}^2$). Unnatural kinematic spikes trigger automated flags.
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

## 🎯 12-Component Biomechanical Telemetry Matrix

| Component | Football / Soccer (Penalty) | Cricket (Fast Bowling) | Kabaddi (Raid & Evasion) |
| :--- | :--- | :--- | :--- |
| **Skill** | `Penalty Kick` | `Outswinger Fast Bowling` | `Toe Touch & Dubki Raid` |
| **Shot Result** | `Goal` | `Hit Top of Off-Stump` | `2 Touch Points (Successful)` |
| **Shot Speed / Velocity** | `91 km/h` | `138.6 km/h` | `22.4 km/h (Burst)` |
| **Accuracy** | `92%` | `94%` | `96%` |
| **Ball Placement / Target**| `Bottom Left Corner` | `Good Length (Outside Off)` | `Bonus Line / Right Corner` |
| **Reaction Time** | `0.82 sec` | `0.64 sec` | `0.38 sec` |
| **Run-up Speed** | `18.4 km/h` | `24.8 km/h` | `16.2 km/h` |
| **Plant Foot** | `Good (35° ankle angle)` | `Front foot braced (178° lockout)` | `Low center of gravity (45° flex)`|
| **Balance** | `Excellent` | `Optimal trunk stabilization` | `Superior ground recovery` |
| **Follow Through** | `Good (Hips squared)` | `Complete hip rotation` | `Rapid midline return` |
| **Contact Quality** | `Clean (Instep sweet-spot)` | `Clean 2.15m snap release` | `Precise 40ms touch tap` |
| **Ball Curve / Trajectory**| `Slight Inside Curve` | `Late 2.4° lateral outswing`| `Rapid zig-zag evasion arc` |

---

## 🚀 Quick Start & Run Locally

```bash
# Start the local development server
python server.py
```
Open **`http://localhost:8000`** in your browser.

---

## 📄 License
This project is open-source under the [MIT License](LICENSE).
