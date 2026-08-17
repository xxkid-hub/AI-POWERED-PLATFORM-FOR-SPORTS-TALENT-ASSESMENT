/**
 * ApexScout AI - Talent Leaderboard & Athlete Profiles Module
 * Verified athlete rankings, performance telemetry badges, and scout recruitment cards.
 */

class LeaderboardManager {
  constructor() {
    this.athletes = SAMPLE_DATA.leaderboard;
    this.activeSport = 'All';
    this.sortBy = 'overallScore';
    this.selectedAthlete = null;
  }

  init() {
    this.renderLeaderboard();
    this.bindEvents();
  }

  bindEvents() {
    const sportSelect = document.getElementById('leaderboardSportFilter');
    if (sportSelect) {
      sportSelect.addEventListener('change', (e) => {
        this.activeSport = e.target.value;
        this.renderLeaderboard();
      });
    }

    const sortSelect = document.getElementById('leaderboardSortSelect');
    if (sortSelect) {
      sortSelect.addEventListener('change', (e) => {
        this.sortBy = e.target.value;
        this.renderLeaderboard();
      });
    }
  }

  getSortedAthletes() {
    return this.athletes
      .filter(ath => this.activeSport === 'All' || ath.sport.toLowerCase().includes(this.activeSport.toLowerCase()))
      .sort((a, b) => {
        if (this.sortBy === 'overallScore') return b.overallScore - a.overallScore;
        if (this.sortBy === 'jumpHeightInches') return b.jumpHeightInches - a.jumpHeightInches;
        if (this.sortBy === 'dribbleSpeedHz') return b.dribbleSpeedHz - a.dribbleSpeedHz;
        if (this.sortBy === 'sprint40yd') return a.sprint40yd - b.sprint40yd; // lower is better for sprint
        return 0;
      });
  }

  renderLeaderboard() {
    const tableBody = document.getElementById('leaderboardTableBody');
    if (!tableBody) return;

    const list = this.getSortedAthletes();

    tableBody.innerHTML = list.map((ath, idx) => `
      <tr class="leaderboard-row" onclick="window.leaderboardManager.openAthleteProfile('${ath.id}')">
        <td class="rank-cell">
          <span class="rank-badge rank-${idx + 1}">#${idx + 1}</span>
        </td>
        <td class="athlete-cell">
          <div class="athlete-info-group">
            <img src="${ath.avatar}" alt="${ath.name}" class="athlete-table-avatar" />
            <div>
              <div class="athlete-name-text">${ath.name}</div>
              <div class="athlete-sub-text">${ath.sport} • ${ath.location} • Age ${ath.age}</div>
            </div>
          </div>
        </td>
        <td class="metric-cell">
          <span class="metric-highlight">${ath.jumpHeightInches}"</span>
          <span class="metric-sub">(${(ath.jumpHeightInches * 2.54).toFixed(1)} cm)</span>
        </td>
        <td class="metric-cell">
          <span class="metric-highlight">${ath.dribbleSpeedHz} Hz</span>
          <span class="metric-sub">cadence</span>
        </td>
        <td class="metric-cell">
          <span class="metric-highlight">${ath.sprint40yd}s</span>
          <span class="metric-sub">40-yard</span>
        </td>
        <td class="badge-cell">
          <div class="badges-stack">
            <span class="badge-mini badge-green" title="${ath.deepfakeStatus}">✓ AI Authenticated</span>
            <span class="badge-mini badge-cyan" title="${ath.medicalStatus}">🛡 24h Med Cleared</span>
          </div>
        </td>
        <td class="score-cell">
          <div class="overall-pill">${ath.overallScore}</div>
        </td>
        <td class="action-cell">
          <button class="btn btn-icon btn-sm" title="View Full AI Dossier">
            ➔
          </button>
        </td>
      </tr>
    `).join('');
  }

  openAthleteProfile(athleteId) {
    const athlete = this.athletes.find(a => a.id === athleteId);
    if (!athlete) return;

    this.selectedAthlete = athlete;
    const modal = document.getElementById('athleteProfileModal');
    if (!modal) return;

    // Fill profile fields
    document.getElementById('modalAthName').textContent = athlete.name;
    document.getElementById('modalAthSport').textContent = athlete.sport;
    document.getElementById('modalAthLocation').textContent = athlete.location;
    document.getElementById('modalAthAge').textContent = `${athlete.age} yrs • ${athlete.height}`;
    document.getElementById('modalAthAvatar').src = athlete.avatar;
    document.getElementById('modalAthOverallScore').textContent = athlete.overallScore;

    document.getElementById('modalAthJump').textContent = `${athlete.jumpHeightInches}" (${(athlete.jumpHeightInches * 2.54).toFixed(1)} cm)`;
    document.getElementById('modalAthDribble').textContent = `${athlete.dribbleSpeedHz} Hz`;
    document.getElementById('modalAthSprint').textContent = `${athlete.sprint40yd}s`;

    document.getElementById('modalAthDeepfake').textContent = athlete.deepfakeStatus;
    document.getElementById('modalAthMedical').textContent = athlete.medicalStatus;
    document.getElementById('modalAthMedTime').textContent = `Med Test: ${athlete.medicalTimestamp} | Video: ${athlete.videoTimestamp}`;

    modal.classList.add('active');
  }

  bookmarkAthlete() {
    if (!this.selectedAthlete) return;
    window.app.showNotification(`Bookmarked ${this.selectedAthlete.name} to Scout Watchlist!`);
    const modal = document.getElementById('athleteProfileModal');
    if (modal) modal.classList.remove('active');
  }

  inviteToCombine() {
    if (!this.selectedAthlete) return;
    window.app.showNotification(`Combine Invitation & Scout Contract sent to ${this.selectedAthlete.name}!`);
    const modal = document.getElementById('athleteProfileModal');
    if (modal) modal.classList.remove('active');
  }
}

// Expose globally
if (typeof window !== 'undefined') {
  window.leaderboardManager = new LeaderboardManager();
}
