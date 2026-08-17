/**
 * ApexScout AI - Coaches & Scouts Marketplace Module
 * Browse certified coaches, filter by sport, send verified AI talent dossiers, and direct messaging.
 */

class CoachesManager {
  constructor() {
    this.coaches = SAMPLE_DATA.coaches;
    this.activeSportFilter = 'All';
    this.searchQuery = '';
    this.activeChatCoach = null;
    this.chatMessages = JSON.parse(localStorage.getItem('apex_coach_chats') || '{}');
  }

  init() {
    this.renderCoachGrid();
    this.bindEvents();
  }

  bindEvents() {
    const searchInput = document.getElementById('coachSearchInput');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        this.searchQuery = e.target.value.toLowerCase();
        this.renderCoachGrid();
      });
    }

    const sportPills = document.querySelectorAll('.coach-sport-pill');
    sportPills.forEach(pill => {
      pill.addEventListener('click', (e) => {
        sportPills.forEach(p => p.classList.remove('active'));
        e.target.classList.add('active');
        this.activeSportFilter = e.target.getAttribute('data-sport') || 'All';
        this.renderCoachGrid();
      });
    });
  }

  getFilteredCoaches() {
    return this.coaches.filter(coach => {
      const matchSport = this.activeSportFilter === 'All' || coach.sport.toLowerCase().includes(this.activeSportFilter.toLowerCase());
      const matchSearch = !this.searchQuery || 
        coach.name.toLowerCase().includes(this.searchQuery) ||
        coach.affiliation.toLowerCase().includes(this.searchQuery) ||
        coach.location.toLowerCase().includes(this.searchQuery) ||
        coach.specialties.some(s => s.toLowerCase().includes(this.searchQuery));
      return matchSport && matchSearch;
    });
  }

  renderCoachGrid() {
    const container = document.getElementById('coachesGridContainer');
    if (!container) return;

    const filtered = this.getFilteredCoaches();

    if (filtered.length === 0) {
      container.innerHTML = `
        <div class="empty-state">
          <div class="empty-icon">🔍</div>
          <h3>No certified coaches found</h3>
          <p>Try adjusting your sport filter or search terms.</p>
        </div>
      `;
      return;
    }

    container.innerHTML = filtered.map(coach => `
      <div class="coach-card glass-card">
        <div class="coach-card-header">
          <img src="${coach.avatar}" alt="${coach.name}" class="coach-avatar" />
          <div class="coach-title-group">
            <div class="coach-badge">${coach.badge}</div>
            <h3 class="coach-name">${coach.name}</h3>
            <p class="coach-affiliation">${coach.affiliation}</p>
          </div>
        </div>

        <p class="coach-bio">${coach.bio}</p>

        <div class="coach-meta-grid">
          <div class="meta-item">
            <span class="meta-label">Sport</span>
            <span class="meta-value">${coach.sport}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">Location</span>
            <span class="meta-value">${coach.location}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">Rating</span>
            <span class="meta-value rating">★ ${coach.rating} <small>(${coach.reviewsCount})</small></span>
          </div>
          <div class="meta-item">
            <span class="meta-label">Combine Fee</span>
            <span class="meta-value highlight-cyan">${coach.fee}</span>
          </div>
        </div>

        <div class="coach-specialties">
          ${coach.specialties.map(s => `<span class="specialty-tag">${s}</span>`).join('')}
        </div>

        <div class="coach-actions">
          <button class="btn btn-outline btn-sm" onclick="window.coachesManager.openChat('${coach.id}')">
            💬 Direct Message
          </button>
          <button class="btn btn-primary btn-sm" onclick="window.coachesManager.openSendDossierModal('${coach.id}')">
            📤 Send AI Assessment
          </button>
        </div>
      </div>
    `).join('');
  }

  openChat(coachId) {
    const coach = this.coaches.find(c => c.id === coachId);
    if (!coach) return;

    this.activeChatCoach = coach;
    const modal = document.getElementById('coachChatModal');
    const headerTitle = document.getElementById('chatModalCoachName');
    const headerSub = document.getElementById('chatModalCoachSub');
    const avatar = document.getElementById('chatModalCoachAvatar');

    if (headerTitle) headerTitle.textContent = coach.name;
    if (headerSub) headerSub.textContent = `${coach.badge} • ${coach.affiliation}`;
    if (avatar) avatar.src = coach.avatar;

    this.renderChatMessages(coachId);

    if (modal) {
      modal.classList.add('active');
    }
  }

  renderChatMessages(coachId) {
    const chatBody = document.getElementById('coachChatMessagesBody');
    if (!chatBody) return;

    const messages = this.chatMessages[coachId] || [
      {
        sender: 'coach',
        text: `Hello! I'm ${this.activeChatCoach.name}. Send me your AI-verified video report along with your 24h medical clearance, and I'll analyze your mechanics for upcoming scout trials!`,
        time: 'Just now'
      }
    ];

    chatBody.innerHTML = messages.map(m => `
      <div class="chat-message ${m.sender === 'user' ? 'message-outgoing' : 'message-incoming'}">
        <div class="message-bubble">
          <p>${m.text}</p>
          <span class="message-time">${m.time}</span>
        </div>
      </div>
    `).join('');

    chatBody.scrollTop = chatBody.scrollHeight;
  }

  sendChatMessage(coachId, text) {
    if (!text || !text.trim()) return;

    if (!this.chatMessages[coachId]) {
      this.chatMessages[coachId] = [];
    }

    const now = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

    this.chatMessages[coachId].push({
      sender: 'user',
      text: text.trim(),
      time: now
    });

    localStorage.setItem('apex_coach_chats', JSON.stringify(this.chatMessages));
    this.renderChatMessages(coachId);

    // Automated intelligent coach reply
    setTimeout(() => {
      let reply = `Thanks for sharing! I reviewed your profile. Your mechanics look very sharp. Make sure to keep your 24h medical certificate updated on your profile so our scouting department can invite you to the regional combine!`;
      if (text.toLowerCase().includes('jump') || text.toLowerCase().includes('vertical')) {
        reply = `Great vertical leap numbers! Your takeoff knee flexion is in an optimal zone. I recommend working on plyometric landing absorption to prevent patellar strain.`;
      } else if (text.toLowerCase().includes('dribble') || text.toLowerCase().includes('speed')) {
        reply = `Your dribbling cadence and hand symmetry are impressive! We're currently looking for point guards with exactly this level of ball control for our combine trials.`;
      }

      this.chatMessages[coachId].push({
        sender: 'coach',
        text: reply,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      });

      localStorage.setItem('apex_coach_chats', JSON.stringify(this.chatMessages));
      this.renderChatMessages(coachId);
    }, 1200);
  }

  openSendDossierModal(coachId) {
    const coach = this.coaches.find(c => c.id === coachId);
    if (!coach) return;

    const modal = document.getElementById('sendDossierModal');
    const targetName = document.getElementById('dossierTargetCoachName');
    if (targetName) targetName.textContent = coach.name;

    if (modal) {
      modal.setAttribute('data-target-coach-id', coachId);
      modal.classList.add('active');
    }
  }

  confirmSendDossier() {
    const modal = document.getElementById('sendDossierModal');
    const coachId = modal ? modal.getAttribute('data-target-coach-id') : null;
    const coach = this.coaches.find(c => c.id === coachId);

    if (modal) modal.classList.remove('active');

    // Notify user
    window.app.showNotification(`Dossier sent to ${coach ? coach.name : 'Coach'}! AI Telemetry + 24h Medical Badge included.`);

    // Add confirmation message to chat
    if (coachId) {
      if (!this.chatMessages[coachId]) this.chatMessages[coachId] = [];
      this.chatMessages[coachId].push({
        sender: 'user',
        text: `📄 [OFFICIAL DOSSIER SUBMISSION]: Sent verified AI assessment scorecard with 24-hour WADA Anti-Doping Medical Clearance.`,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      });
      localStorage.setItem('apex_coach_chats', JSON.stringify(this.chatMessages));
    }
  }
}

// Expose globally
if (typeof window !== 'undefined') {
  window.coachesManager = new CoachesManager();
}
