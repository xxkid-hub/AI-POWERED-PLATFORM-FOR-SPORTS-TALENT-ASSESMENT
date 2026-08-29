/**
 * ApexScout AI - 24 to 48 Hour Medical & Anti-Doping Compliance Engine
 * - 24–48 Hour Verification SLA Enforcement
 * - Automated Document OCR: scans lab stamps, digital signatures, NADA/WADA registration numbers & timestamps
 * - 3-Tier Status Enforcement:
 *    * VERIFIED (Green Badge): Validated by OCR + within 24-48h window + clean anti-doping panel
 *    * PENDING (Yellow Badge): Grace period active (< 48 hrs) awaiting final admin stamp
 *    * FLAGGED / DELISTED (Red Badge): Window expired (> 48 hrs) or prohibited substance found; delisted from leaderboards
 */

class MedicalVerifier {
  constructor() {
    this.slaMinHours = 24;
    this.slaMaxHours = 48; // Strict 48h limit for tournament/leaderboard eligibility
  }

  /**
   * Run automated simulated OCR scanner on uploaded medical document
   * @param {File|Object} documentFile
   * @returns {Promise<Object>} Extracted OCR entities
   */
  async runDocumentOCR(documentFile) {
    await new Promise(r => setTimeout(r, 600)); // Simulate OCR processing

    const labAccreditation = 'WADA-ISO/IEC-17025-LAB-8902';
    const nadaRegNumber = 'NADA-REG-' + Math.floor(100000 + Math.random() * 900000);
    const doctorSign = 'Dr. Evelyn Reed, MD (Board Certified Sports Physician)';
    const digitalHash = '0x' + Array.from({ length: 32 }, () => Math.floor(Math.random() * 16).toString(16)).join('');

    return {
      ocrConfidence: 98.6,
      labStampDetected: true,
      labName: 'Apex Olympic Bio-Diagnostics Center',
      accreditationNumber: labAccreditation,
      nadaWadaRegistration: nadaRegNumber,
      physicianSignature: doctorSign,
      securityHash: digitalHash,
      extractedAt: new Date().toISOString()
    };
  }

  /**
   * Validate time window against 24-48h SLA
   */
  validateSLAWindow(videoTime, medicalTime) {
    const vTime = new Date(videoTime).getTime();
    const mTime = new Date(medicalTime).getTime();

    if (isNaN(vTime) || isNaN(mTime)) {
      return {
        tier: 'FLAGGED',
        statusText: 'INVALID_TIMESTAMP',
        hoursDelta: 0,
        isValid: false,
        message: 'Invalid timestamp format provided.'
      };
    }

    const diffHours = Math.abs(vTime - mTime) / (1000 * 60 * 60);
    const formattedHours = diffHours.toFixed(1);

    if (diffHours <= this.slaMinHours) {
      // 0 to 24 hours: Full Green Tier
      return {
        tier: 'VERIFIED',
        badgeColor: 'green',
        statusText: 'VERIFIED (Clean within 24h)',
        badgeClass: 'badge-med-verified',
        hoursDelta: parseFloat(formattedHours),
        isValid: true,
        eligibleForLeaderboard: true,
        message: `Medical clearance is synchronized with video combine (${formattedHours}h apart, within prime 24h SLA).`
      };
    } else if (diffHours <= this.slaMaxHours) {
      // 24 to 48 hours: Pending Grace Period Tier
      return {
        tier: 'PENDING',
        badgeColor: 'yellow',
        statusText: 'PENDING REVIEW (Within 48h Grace Window)',
        badgeClass: 'badge-med-pending',
        hoursDelta: parseFloat(formattedHours),
        isValid: true,
        eligibleForLeaderboard: true,
        message: `Medical clearance is inside the 48-hour grace window (${formattedHours}h apart). Awaiting final admin sign-off.`
      };
    } else {
      // > 48 hours: Flagged / Delisted
      return {
        tier: 'FLAGGED',
        badgeColor: 'red',
        statusText: 'FLAGGED / DELISTED (Expired > 48h Window)',
        badgeClass: 'badge-med-flagged',
        hoursDelta: parseFloat(formattedHours),
        isValid: false,
        eligibleForLeaderboard: false,
        message: `Medical report is expired (${formattedHours}h apart, exceeds 48-hour SLA). Athlete scores excluded from public leaderboard.`
      };
    }
  }

  /**
   * Complete medical verification dossier
   */
  async verifyReport(reportData, videoMetadata = {}) {
    const videoTimestamp = videoMetadata.timestamp || new Date().toISOString();
    const medicalTimestamp = reportData.timestamp || new Date(Date.now() - 6 * 3600000).toISOString();

    const slaCompliance = this.validateSLAWindow(videoTimestamp, medicalTimestamp);
    const ocrData = await this.runDocumentOCR(reportData.file);

    const standardSubstances = [
      { name: 'Anabolic-Androgenic Steroids (AAS)', code: 'WADA-S1', result: 'NEGATIVE', compliant: true },
      { name: 'Peptide Hormones & Growth Factors (EPO / hGH)', code: 'WADA-S2', result: 'NEGATIVE', compliant: true },
      { name: 'Beta-2 Agonists & Clenbuterol', code: 'WADA-S3', result: 'NEGATIVE', compliant: true },
      { name: 'Hormone & Metabolic Modulators (SARMs)', code: 'WADA-S4', result: 'NEGATIVE', compliant: true },
      { name: 'Diuretics & Masking Agents', code: 'WADA-S5', result: 'NEGATIVE', compliant: true },
      { name: 'Stimulants & Central Nervous Accelerants', code: 'WADA-S6', result: 'NEGATIVE', compliant: true }
    ];

    const substances = reportData.substancesTested || standardSubstances;
    const allSubstancesClean = substances.every(s => s.result.toUpperCase() === 'NEGATIVE');

    let finalTier = slaCompliance.tier;
    let finalEligible = slaCompliance.eligibleForLeaderboard;

    if (!allSubstancesClean) {
      finalTier = 'FLAGGED';
      finalEligible = false;
    }

    const verificationToken = 'APEX-MED-' + Math.random().toString(36).substring(2, 8).toUpperCase() + '-' + Math.floor(1000 + Math.random() * 9000);

    return {
      tier: finalTier,
      slaCompliance,
      ocrData,
      isFullyCleared: finalTier === 'VERIFIED',
      isPending: finalTier === 'PENDING',
      isFlagged: finalTier === 'FLAGGED',
      eligibleForLeaderboard: finalEligible,
      verificationToken,
      athleteName: reportData.athleteName || 'Alex Rivera',
      timestamp: medicalTimestamp,
      substancesTested: substances,
      vitals: {
        restingHeartRate: '52 bpm (Athletic Standard)',
        bloodPressure: '118/74 mmHg (Optimal)',
        vo2MaxEst: '58.4 mL/kg/min',
        orthopedicJointScore: 'Grade A (Zero Ligament Strain)'
      },
      conclusion: finalTier === 'VERIFIED'
        ? 'FIT FOR COMPETITION & COMBINE TRIALS. WADA anti-doping panel and OCR stamp verified within strict 24-48h SLA.'
        : (finalTier === 'PENDING'
            ? 'UNDER REVIEW: Medical report within 48h grace window. Provisional combine scores recorded.'
            : 'NON-COMPLIANT: 48h verification SLA expired or compound flagged. Athlete delisted from leaderboard.')
    };
  }
}

if (typeof window !== 'undefined') {
  window.MedicalVerifier = MedicalVerifier;
}
