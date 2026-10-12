/**
 * ApexScout AI - 24/7 Helpline & Athlete Wellness Hub Module
 * Emergency hotlines, interactive AI Sports Physiotherapist & Anti-Doping bot, and SOS ticketing.
 */

class HelplineManager {
  constructor() {
    this.helplines = SAMPLE_DATA.helplines;
    this.emergencyHotline = "1800-11-SPORTS";
    this.emergencyAlt = "+91 1800 200 4545";
    this.ambulanceNum = "112 / 108";

    this.seriousKeywords = [
      'fracture', 'broken', 'bone', 'snap', 'snapped', 'crack', 'cracked',
      'deformity', 'deformed', 'crooked', 'bone sticking', 'protruding',
      'pop', 'popped', 'loud pop', 'tear', 'torn', 'rupture', 'ruptured',
      'acl', 'pcl', 'mcl', 'achilles pop', 'unstable knee', 'knee gave way',
      'dislocat', 'dislocation', 'out of socket',
      'concussion', 'hit head', 'head injury', 'unconscious', 'passed out',
      'blacked out', 'loss of consciousness', 'vomit', 'vomiting',
      'spine', 'spinal', 'neck severe', 'cannot move', 'paralysis',
      'cannot walk', 'cannot bear weight'
    ];

    this.sportInjuryResponses = {
      football: {
        ankle: `**Football Inversion Ankle Sprain (Rolled Ankle)**:
1. **P.R.I.C.E. Protocol**: Protect joint, immediate Rest (avoid bearing weight for 24-48h), Ice (15-20 min every 2-3h with towel buffer), Compress (firm elastic wrap from toes upward), and Elevate above heart level.
2. **Rehab**: After 48h resting pain subsides, perform ankle alphabet circles and single-leg balance drills (30s).
3. **Return-to-Play**: 1-3 weeks. Pass full single-leg hop test before competitive play.
4. *Escalation*: If unable to take 4 steps immediately or severe bony tenderness, call 24/7 toll-free emergency hotline at **1800-11-SPORTS**.`,
        hamstring: `**Football Hamstring Strain (Sprint Deceleration)**:
1. **Immediate Stop**: Discontinue sprinting immediately to prevent muscle retraction.
2. **Ice & Compression**: Ice posterior thigh for 15 min, apply thigh compression sleeve. Avoid aggressive toe-touch stretching in the first 48 hours.
3. **Rehab**: Day 3+ submaximal glute bridges; week 2+ eccentric Nordic curls.
4. **Return-to-Play**: 1-2 weeks for mild strain. 100% sprint pain-free clearance required.`,
        groin: `**Football Groin / Adductor Strain**:
1. **Rest & Ice**: Stop cutting and kicking drills. Ice inner thigh 15-20 min 3x daily.
2. **Compression**: Wear supportive compression shorts for pelvic stability.
3. **Rehab**: Isometric ball squeeze between knees (5-second holds, 10 reps).`,
        shin: `**Football Shin Splints (Medial Tibial Stress)**:
1. **Ice Massage**: Rub ice along inner shin border 8-10 min.
2. **Footwear & Load**: Switch to grass pitches or insert cushioned orthotics. Reduce running mileage by 50%.
3. **Rehab**: Towel scrunches with toes and calf wall stretching.`
      },
      volleyball: {
        knee: `**Volleyball Jumper's Knee (Patellar Tendinopathy)**:
1. **Immediate Relief**: Cease repetitive jumping and deep squats. Ice inferior pole of patella 15 min post-practice.
2. **Patellar Strap**: Use a sub-patellar tendon strap during training to disperse tensile patellar load.
3. **Rehab**: Isometric Spanish squats or wall-sits (45s holds, 4 sets) to trigger tendon pain relief and collagen remodeling.
4. **Return-to-Play**: 1-3 weeks progressive re-introduction to court movement.`,
        finger: `**Volleyball Jammed Finger (Collateral Ligament Sprain)**:
1. **Ice & Buddy-Tape**: Ice finger in cold water cup for 10 min. Buddy-tape injured finger to adjacent finger for joint splinting.
2. **Rest**: Avoid direct overhead setting or blocking until swelling abates (3-7 days).`,
        shoulder: `**Volleyball Shoulder Impingement / Rotator Cuff Strain**:
1. **Protocol**: Limit overhead spiking drills. Ice anterior shoulder 15 min.
2. **Rehab**: Resistance band external rotations and Y-T-W scapular retractions (3 sets of 12 reps).`
      },
      basketball: {
        ankle: `**Basketball Lateral Inversion Ankle Sprain**:
1. **P.R.I.C.E. Protocol**: Remove shoe carefully. Apply ice pack 15-20 min. Wrap snugly with ankle compression brace. Keep elevated on chair or bed.
2. **Rehab**: Resistance band ankle eversion, calf raises, and dynamic wobble board balance.
3. **Return-to-Play**: 1-3 weeks. Lace-up ankle brace recommended upon return to court.`,
        finger: `**Basketball Jammed Finger (Ball Impact)**:
1. **Immediate Care**: Check that finger is not deformed (if crooked, see emergency below). Apply ice 10-15 min.
2. **Splint**: Buddy-tape to neighboring finger. Avoid catching drills for 5-7 days.`,
        achilles: `**Basketball Achilles Tightness / Tendonitis**:
1. **Relief**: Ice distal tendon 15 min. Avoid explosive drive steps.
2. **Rehab**: Eccentric heel drops off stair edge (3 sets of 15 reps, slow lowering).`
      },
      kabaddi: {
        ankle: `**Kabaddi Ankle Twist (Ankle Hold / Raid Takedown)**:
1. **Immediate Care**: Withdraw from raid/defense immediately. Apply ice pack 15-20 min with compression crepe bandage.
2. **Joint Protection**: Do not walk on twisted ankle during the initial match session.
3. **Rehab**: Ankle alphabet exercises and calf wall stretches once acute pain drops.
4. *Emergency Escalation*: If ankle bone popped or bearing weight is impossible, call toll-free emergency hotline **1800-11-SPORTS**.`,
        shoulder: `**Kabaddi Shoulder Strain / Tackle Contusion**:
1. **Immediate**: Rest arm in sling or supported position. Ice deltoid/clavicle 15 min.
2. **Rehab**: Gentle pendulum arm swings and band pull-aparts.`,
        burn: `**Kabaddi Mat Friction Burn (Synthetic Mat Abrasions)**:
1. **Clean**: Flush thoroughly with sterile saline or clean lukewarm water.
2. **Antiseptic**: Apply chlorhexidine or bacitracin ointment and non-stick hydrogel dressing to prevent mat infection.`
      },
      cricket: {
        side: `**Cricket Bowling Side Strain (Internal Oblique Tear)**:
1. **Immediate Stop**: Cease fast bowling delivery stride immediately. Fast bowling forces can severely tear abdominal wall.
2. **Ice & Rest**: Ice contralateral rib border 15 min. Avoid trunk twisting and heavy lifting for 7-10 days.
3. **Rehab**: Progressive side-planks (isometric 20-30s holds) and rotational core stabilization.
4. **Return-to-Play**: 2-4 weeks; gradual bowling progression (off 3 paces -> 5 paces -> full run-up).`,
        shoulder: `**Cricket Throwing / Rotator Cuff Tendonitis**:
1. **Protocol**: Rest throwing arm from outfield boundaries. Ice posterior shoulder 15 min.
2. **Rehab**: Sleeper stretch for internal rotation deficit; band external rotations (3x15).`,
        finger: `**Cricket Fielding Finger Impact / Bruise**:
1. **Check**: Verify finger is straight and distal joint can bend. Ice 10-15 min.
2. **Protection**: Buddy-tape finger during light fielding drills.`
      }
    };

    this.botResponses = {
      doping: {
        keywords: ['doping', 'medicine', 'wada', 'supplement', 'creatine', 'protein', 'pre-workout', 'steroid', 'drug', 'banned', 'pill'],
        response: `**CleanSport & Anti-Doping Compliance**:
1. All combine assessments require 24h synchronized medical clearance.
2. **Prohibited Substances**: WADA prohibits anabolic agents, peptide hormones (EPO, hGH), beta-2 agonists, hormone modulators, and central stimulants.
3. **Supplements**: Only use supplements with third-party certification (*Informed-Sport* or *NSF Certified for Sport*).
4. For prescription medications (e.g. asthma inhalers, insulin), submit a **Therapeutic Use Exemption (TUE)** with your medical report. CleanSport Hotline: **+1 (800) 223-0393**.`
      },
      mental: {
        keywords: ['anxiety', 'stress', 'pressure', 'scout', 'nervous', 'burnout', 'fear', 'mental', 'confidence'],
        response: `**Mental Resilience & Focus Protocol**:
1. **Pre-Trial Reset Routine**: Practice 4-7-8 box breathing (4s inhale, 7s hold, 8s exhale) to lower sympathetic heart rate before recording drills.
2. **Focus on Process**: Focus on biomechanical execution (foot plant, hip drive) rather than external scout ratings.
3. Confidential 24/7 mental wellness counselors are on standby: **+1 (800) 273-TALK (Option 4)**.`
      }
    };
  }

  init() {
    this.renderHelplineCards();
    this.bindEvents();
  }

  renderHelplineCards() {
    const container = document.getElementById('helplineCardsContainer');
    if (!container) return;

    container.innerHTML = this.helplines.map(line => `
      <div class="helpline-card glass-card">
        <div class="helpline-header">
          <span class="helpline-icon" style="color: var(--accent-cyan); display: flex; align-items: center;">
            <svg class="btn-icon-svg" style="width: 22px; height: 22px;" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          </span>
          <div>
            <h4 class="helpline-cat">${line.category}</h4>
            <span class="helpline-avail">${line.available}</span>
          </div>
        </div>
        <p class="helpline-desc">${line.description}</p>
        <div class="helpline-action-row">
          <a href="tel:${line.number.replace(/[^0-9+]/g, '')}" class="btn btn-primary btn-sm">
            <svg class="btn-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            Call ${line.number}
          </a>
          <button class="btn btn-outline btn-sm" onclick="window.helplineManager.copyNumber('${line.number}')">
            <svg class="btn-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            Copy Number
          </button>
        </div>
      </div>
    `).join('');
  }

  bindEvents() {
    const sendBtn = document.getElementById('aiPhysioSendBtn');
    const input = document.getElementById('aiPhysioInput');
    const ticketForm = document.getElementById('emergencyTicketForm');

    if (sendBtn && input) {
      const handleSend = () => {
        const text = input.value.trim();
        if (text) {
          this.sendPhysioMessage(text);
          input.value = '';
        }
      };

      sendBtn.addEventListener('click', handleSend);
      input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleSend();
      });
    }

    if (ticketForm) {
      ticketForm.addEventListener('submit', (e) => {
        e.preventDefault();
        this.submitEmergencyTicket();
      });
    }
  }

  sendPhysioMessage(text) {
    const chatContainer = document.getElementById('aiPhysioChatContainer');
    if (!chatContainer) return;

    // Add user message
    const userMsg = document.createElement('div');
    userMsg.className = 'chat-message message-outgoing';
    userMsg.innerHTML = `
      <div class="message-bubble">
        <p>${this.escapeHtml(text)}</p>
        <span class="message-time">Just now</span>
      </div>
    `;
    chatContainer.appendChild(userMsg);
    chatContainer.scrollTop = chatContainer.scrollHeight;

    // Check for SERIOUS / EMERGENCY injuries first
    const lower = text.toLowerCase();
    let bestResponse = null;

    const matchedSerious = this.seriousKeywords.find(kw => lower.includes(kw));
    if (matchedSerious) {
      bestResponse = `🚨 **CRITICAL EMERGENCY MEDICAL ALERT: IMMEDIATE ACTION REQUIRED**

The reported symptom (**'${matchedSerious.toUpperCase()}'**) indicates a **serious acute sports emergency** (suspected bone fracture, complete ligament rupture, joint dislocation, severe concussion, or spinal trauma).

⚠️ **IMMEDIATE FIRST-RESPONDER PROTOCOL:**
1. **DO NOT MOVE THE ATHLETE OR INJURED LIMB**: Strict immobilization. Do NOT attempt to straighten joints.
2. **DO NOT BEAR WEIGHT OR MASSAGE**.
3. **IF HEAD / NECK INJURY**: Keep neck immobilized.
4. **IF ARTERIAL BLEEDING**: Apply firm continuous direct pressure.

📞 **CONTACT OUR 24/7 TOLL-FREE EMERGENCY HOTLINE NOW:**
- 🆘 **Toll-Free Sports Emergency Hotline**: **${this.emergencyHotline}** *(Toll-Free 24/7 Multi-Lingual)*
- 🚑 **National Ambulance Dispatch**: **${this.ambulanceNum}** *(Immediate 24/7)*
- 🏥 **Sports Trauma Line**: **${this.emergencyAlt}**

*Stay on the line with the dispatcher until medical personnel arrive.*`;
    } else {
      // Check sport context
      let detectedSport = null;
      if (lower.includes('football') || lower.includes('soccer')) detectedSport = 'football';
      else if (lower.includes('volleyball')) detectedSport = 'volleyball';
      else if (lower.includes('basketball')) detectedSport = 'basketball';
      else if (lower.includes('kabaddi')) detectedSport = 'kabaddi';
      else if (lower.includes('cricket')) detectedSport = 'cricket';

      // Check injury keywords
      let injuryKey = null;
      if (lower.includes('ankle') || lower.includes('sprain') || lower.includes('twist')) injuryKey = 'ankle';
      else if (lower.includes('knee') || lower.includes('patellar') || lower.includes('jumper')) injuryKey = 'knee';
      else if (lower.includes('hamstring') || lower.includes('thigh')) injuryKey = 'hamstring';
      else if (lower.includes('finger') || lower.includes('thumb')) injuryKey = 'finger';
      else if (lower.includes('groin') || lower.includes('adductor')) injuryKey = 'groin';
      else if (lower.includes('shin')) injuryKey = 'shin';
      else if (lower.includes('side') || lower.includes('oblique') || lower.includes('rib')) injuryKey = 'side';
      else if (lower.includes('shoulder') || lower.includes('rotator')) injuryKey = 'shoulder';
      else if (lower.includes('burn') || lower.includes('mat')) injuryKey = 'burn';
      else if (lower.includes('achilles') || lower.includes('heel')) injuryKey = 'achilles';

      if (detectedSport && this.sportInjuryResponses[detectedSport]) {
        const sportObj = this.sportInjuryResponses[detectedSport];
        if (injuryKey && sportObj[injuryKey]) {
          bestResponse = sportObj[injuryKey];
        } else {
          // first available for that sport
          bestResponse = Object.values(sportObj)[0];
        }
      } else if (injuryKey) {
        // Find in any sport
        for (const s in this.sportInjuryResponses) {
          if (this.sportInjuryResponses[s][injuryKey]) {
            bestResponse = this.sportInjuryResponses[s][injuryKey];
            break;
          }
        }
      }

      // Check other categories (doping, mental)
      if (!bestResponse) {
        for (const key in this.botResponses) {
          const cat = this.botResponses[key];
          if (cat.keywords.some(k => lower.includes(k))) {
            bestResponse = cat.response;
            break;
          }
        }
      }

      if (!bestResponse) {
        bestResponse = `**General Sports Clinical First-Aid (P.R.I.C.E. Protocol)**:
1. **Protect & Rest**: Remove athlete from active play. Avoid bearing weight on affected joints.
2. **Ice**: Apply cold pack wrapped in damp towel for 15-20 min every 2-3 hours.
3. **Compress & Elevate**: Wrap joint firmly with elastic bandage; elevate limb above heart level.
4. ℹ️ **Emergency Escalation**: If acute severe pain, deformity, inability to walk, or numbness occurs, **contact our 24/7 Toll-Free Emergency Hotline immediately at ${this.emergencyHotline}** or dispatch ambulance **${this.ambulanceNum}**.`;
      }
    }

    // Bot reply with typing delay
    setTimeout(() => {
      const botMsg = document.createElement('div');
      botMsg.className = 'chat-message message-incoming';
      botMsg.innerHTML = `
        <div class="message-bubble physio-bubble">
          <div class="physio-badge">Apex AI Sports Physio & Emergency Tele-Triage Bot</div>
          <div class="physio-text">${this.formatMarkdown(bestResponse)}</div>
          <span class="message-time">Just now</span>
        </div>
      `;
      chatContainer.appendChild(botMsg);
      chatContainer.scrollTop = chatContainer.scrollHeight;
    }, 700);
  }

  sendPresetPhysioPrompt(promptText) {
    const input = document.getElementById('aiPhysioInput');
    if (input) input.value = promptText;
    this.sendPhysioMessage(promptText);
  }

  submitEmergencyTicket() {
    const name = document.getElementById('ticketName')?.value || 'Athlete';
    const sport = document.getElementById('ticketSport')?.value || 'General';
    const urgency = document.getElementById('ticketUrgency')?.value || 'Normal';
    const desc = document.getElementById('ticketDesc')?.value || '';

    const ticketId = 'TICK-' + Math.floor(100000 + Math.random() * 900000);

    const ticketModal = document.getElementById('ticketSuccessModal');
    if (ticketModal) {
      document.getElementById('successTicketId').textContent = ticketId;
      document.getElementById('successTicketUrgency').textContent = urgency.toUpperCase();
      ticketModal.classList.add('active');
    }

    window.app.showNotification(`Support Ticket #${ticketId} dispatched to regional sports federation duty officer.`);
    document.getElementById('emergencyTicketForm')?.reset();
  }

  copyNumber(number) {
    navigator.clipboard.writeText(number);
    window.app.showNotification(`Copied ${number} to clipboard!`);
  }

  formatMarkdown(text) {
    return text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/\n/g, '<br/>');
  }

  escapeHtml(str) {
    return str.replace(/[&<>"']/g, m => ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#39;'
    }[m]));
  }
}

// Expose globally
if (typeof window !== 'undefined') {
  window.helplineManager = new HelplineManager();
}
