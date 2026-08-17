/**
 * ApexScout AI - 24/7 Helpline & Athlete Wellness Hub Module
 * Emergency hotlines, interactive AI Sports Physiotherapist & Anti-Doping bot, and SOS ticketing.
 */

class HelplineManager {
  constructor() {
    this.helplines = SAMPLE_DATA.helplines;
    this.botResponses = {
      injury: {
        keywords: ['pain', 'injury', 'knee', 'ankle', 'sprain', 'tear', 'patellar', 'shin', 'hamstring', 'sore'],
        response: `⚠️ **Sports Physio Protocol (Immediate First Response)**:
1. **P.R.I.C.E. / P.O.L.I.C.E.**: Protect joint, Optimal Loading, Ice (15-20 min intervals), Compress, and Elevate.
2. If experiencing acute swelling, inability to bear weight, or audible 'pop' in the knee/ankle, stop all drill activity immediately.
3. For acute combine recovery, schedule an immediate ultrasound/MRI through our Emergency Sports Injury Hotline: **+1 (800) 555-SPORTS**.`
      },
      doping: {
        keywords: ['doping', 'medicine', 'wada', 'supplement', 'creatine', 'protein', 'pre-workout', 'steroid', 'drug', 'banned', 'pill', 'increase speed', 'power'],
        response: `🛡️ **CleanSport & Anti-Doping Advisory**:
1. All performance assessment submissions require a **24-hour synchronized medical clearance**.
2. **Prohibited Substances**: WADA prohibits anabolic agents, peptide hormones (EPO, hGH), beta-2 agonists, hormone modulators, and central stimulants.
3. **Supplements**: Only use supplements with third-party certification (*Informed-Sport* or *NSF Certified for Sport*).
4. For prescription medications (e.g., asthma inhalers), submit a **Therapeutic Use Exemption (TUE)** with your 24h medical report. Hotline: **+1 (800) 223-0393**.`
      },
      mental: {
        keywords: ['anxiety', 'stress', 'pressure', 'scout', 'nervous', 'burnout', 'fear', 'mental', 'confidence'],
        response: `🧠 **Athlete Mental Resilience & Combine Preparation**:
1. **Pre-Trial Reset Routine**: Practice 4-7-8 box breathing (4s inhale, 7s hold, 8s exhale) to lower sympathetic heart rate before recording drills.
2. **Focus on Process**: Focus on biomechanical execution (foot plant, hip drive) rather than external scout ratings.
3. Confidential 24/7 mental wellness counselors are on standby: **+1 (800) 273-TALK (Option 4)**.`
      },
      jump: {
        keywords: ['jump', 'vertical', 'hangtime', 'height', 'dunk', 'explosiveness'],
        response: `⚡ **Biomechanical Jump Enhancement**:
1. Maximize triple extension (simultaneous extension of hips, knees, and ankles).
2. Deepen kinetic arm-swing momentum (adds 10-15% to peak takeoff velocity).
3. Land with minimum 30° knee flexion to absorb 3x-5x body weight and protect the ACL.`
      },
      dribble: {
        keywords: ['dribble', 'dribbling', 'crossover', 'ball control', 'hands'],
        response: `🏀 **Ball Control & Cadence Optimization**:
1. Keep center of gravity low and keep eyes up (reduces reaction latency by 120ms).
2. Use fingertips and wrist snap rather than the palm to achieve high frequency (> 4.5 Hz).
3. Practice blindfolded sensory drills to develop subconscious muscle memory.`
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
          <span class="helpline-icon">📞</span>
          <div>
            <h4 class="helpline-cat">${line.category}</h4>
            <span class="helpline-avail">${line.available}</span>
          </div>
        </div>
        <p class="helpline-desc">${line.description}</p>
        <div class="helpline-action-row">
          <a href="tel:${line.number.replace(/[^0-9+]/g, '')}" class="btn btn-primary btn-sm">
            Call ${line.number}
          </a>
          <button class="btn btn-outline btn-sm" onclick="window.helplineManager.copyNumber('${line.number}')">
            📋 Copy Number
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

    // Find best matching response
    const lower = text.toLowerCase();
    let bestResponse = null;

    for (const key in this.botResponses) {
      const cat = this.botResponses[key];
      if (cat.keywords.some(k => lower.includes(k))) {
        bestResponse = cat.response;
        break;
      }
    }

    if (!bestResponse) {
      bestResponse = `Thank you for consulting ApexScout Sports Health & Anti-Doping AI. For medical assessments, injury consultations, or drug clearance checks, please provide details regarding the sport or injury area, or call our 24/7 hotline at **+1 (800) 555-SPORTS**.`;
    }

    // Bot reply with typing delay
    setTimeout(() => {
      const botMsg = document.createElement('div');
      botMsg.className = 'chat-message message-incoming';
      botMsg.innerHTML = `
        <div class="message-bubble physio-bubble">
          <div class="physio-badge">🤖 ApexScout Sports Physio & Anti-Doping AI</div>
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
