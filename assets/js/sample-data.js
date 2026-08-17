/**
 * ApexScout AI - Sample & Benchmark Dataset
 * Pre-configured drills, elite coaches, scout leaderboard, medical test profiles & helpline directory.
 */

const SAMPLE_DATA = {
  // Preset Drills for Instant AI Testing
  drills: [
    {
      id: 'drill-bball-dribble',
      sport: 'Basketball',
      title: 'Crossover & Speed Dribble Combine',
      duration: '15s',
      targetMetrics: ['Dribble Speed (Hz)', 'Hand Symmetry', 'Ball Control Height', 'Reaction Time'],
      videoPlaceholderText: 'Basketball Crossover Drill',
      drillType: 'dribble',
      simulatedMetrics: {
        dribbleSpeedHz: 4.8, // 4.8 dribbles per second
        totalDribbles: 58,
        leftHandRatio: 48,
        rightHandRatio: 52,
        controlHeightCm: 68,
        speedConsistency: 94,
        overallRating: 92,
        deepfakeConfidence: 99.4,
        tamperingDetected: false
      }
    },
    {
      id: 'drill-vertical-jump',
      sport: 'Basketball / Athletics',
      title: 'Max Vertical Leap & Apex Combine',
      duration: '10s',
      targetMetrics: ['Vertical Jump Height', 'Hang Time', 'Takeoff Velocity', 'Landing Angle'],
      videoPlaceholderText: 'Max Vertical Jump Combine',
      drillType: 'jump',
      simulatedMetrics: {
        jumpHeightInches: 36.4, // 36.4 inches (92.5 cm)
        jumpHeightCm: 92.5,
        hangTimeMs: 615,
        takeoffVelocityMs: 4.25,
        landingKneeFlexionDeg: 122,
        explosivenessScore: 96,
        overallRating: 95,
        deepfakeConfidence: 98.8,
        tamperingDetected: false
      }
    },
    {
      id: 'drill-soccer-agility',
      sport: 'Football / Soccer',
      title: 'Slalom Cone Dribble & Acceleration',
      duration: '18s',
      targetMetrics: ['Slalom Dribble Cadence', 'Sprint Speed', 'Agility Index', 'Ball Proximity'],
      videoPlaceholderText: 'Soccer Slalom Agility Drill',
      drillType: 'agility_dribble',
      simulatedMetrics: {
        dribbleSpeedHz: 3.9,
        topSpeedKmh: 27.8,
        coneTurnLatencyMs: 210,
        ballTouchAccuracy: 91,
        agilityScore: 89,
        overallRating: 90,
        deepfakeConfidence: 99.1,
        tamperingDetected: false
      }
    },
    {
      id: 'drill-track-sprint',
      sport: 'Athletics / Track',
      title: '40-Yard Sprint & Acceleration Burst',
      duration: '8s',
      targetMetrics: ['40-Yard Time', 'Top Velocity', 'Stride Frequency', 'Ground Contact Time'],
      videoPlaceholderText: '40-Yard Sprint Combine',
      drillType: 'sprint',
      simulatedMetrics: {
        sprintTime40yd: 4.42,
        topSpeedKmh: 33.6,
        strideFrequencyHz: 4.5,
        groundContactMs: 98,
        sprintScore: 97,
        overallRating: 96,
        deepfakeConfidence: 99.6,
        tamperingDetected: false
      }
    }
  ],

  // Certified Coaches & Talent Scouts
  coaches: [
    {
      id: 'coach-1',
      name: 'Marcus Vance',
      title: 'Head Talent Scout & Performance Director',
      affiliation: 'Elite Hoops Academy & NBA G-League Scout Partner',
      sport: 'Basketball',
      rating: 4.95,
      reviewsCount: 128,
      location: 'Chicago, IL, USA',
      specialties: ['Vertical Leap Optimization', 'Point Guard Dribble Mechanics', 'College Recruitment'],
      avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80',
      status: 'Accepting New Athletes',
      fee: 'Free Initial Assessment Review',
      badge: 'Verified NBA/NCAA Scout',
      bio: 'Over 14 years evaluating elite high school and collegiate basketball prospects. Specializes in biomechanical breakdown and athletic combine preparation.'
    },
    {
      id: 'coach-2',
      name: 'Elena Rostova',
      title: 'UEFA Pro License Scout & Technical Coach',
      affiliation: 'Global Football Scouting Network',
      sport: 'Football / Soccer',
      rating: 4.92,
      reviewsCount: 94,
      location: 'London, UK / Barcelona, Spain',
      specialties: ['Winger Agility & Dribble Cadence', 'First-Touch Analytics', 'European Academy Trials'],
      avatar: 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=150&auto=format&fit=crop&q=80',
      status: 'Accepting Video Submissions',
      fee: 'Free Scout Evaluation',
      badge: 'UEFA Pro Certified',
      bio: 'Former youth academy director. Utilizes AI video telemetry to uncover undiscovered talent across South America, Europe, and Asia.'
    },
    {
      id: 'coach-3',
      name: 'David O\'Connor',
      title: 'Olympic Sprint & Biomechanics Specialist',
      affiliation: 'USATF High Performance Center',
      sport: 'Athletics / Track',
      rating: 4.98,
      reviewsCount: 160,
      location: 'Austin, TX, USA',
      specialties: ['Sprint Acceleration Curve', 'Ground Reaction Force', 'Jump Mechanics'],
      avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&auto=format&fit=crop&q=80',
      status: 'Open for Consultations',
      fee: 'Scholarship Sponsorship Track Available',
      badge: 'Olympic Coach',
      bio: 'Coached multiple national champions in 100m, 200m, and long jump. Focuses on stride frequency efficiency and injury-preventative posture.'
    },
    {
      id: 'coach-4',
      name: 'Vikram Sengupta',
      title: 'High-Performance Cricket Analyst & Scout',
      affiliation: 'National Cricket Academy Talent Panel',
      sport: 'Cricket',
      rating: 4.88,
      reviewsCount: 82,
      location: 'Mumbai / Bangalore, India',
      specialties: ['Fast Bowling Release Speed', 'Bat Speed & Footwork Latency', 'Fielding Agility'],
      avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&auto=format&fit=crop&q=80',
      status: 'Reviewing State Talent',
      fee: 'Free Talent Assessment',
      badge: 'BCCI Certified Analyst',
      bio: 'Former first-class cricketer and current franchise scouting consultant. Passionate about grassroots cricket talent identification.'
    },
    {
      id: 'coach-5',
      name: 'Sarah Chen',
      title: 'Strength & Conditioning Specialist (CSCS)',
      affiliation: 'Athletics & Tennis Performance Lab',
      sport: 'Tennis / Multi-Sport',
      rating: 4.96,
      reviewsCount: 110,
      location: 'Melbourne, Australia',
      specialties: ['Rotational Power', 'Lateral Quickness', 'Anti-Doping & Safe Supplementation'],
      avatar: 'https://images.unsplash.com/photo-1580489944761-15a19d654956?w=150&auto=format&fit=crop&q=80',
      status: 'Accepting Video Submissions',
      fee: 'Free Review for Verified Profiles',
      badge: 'NSCA CSCS Master',
      bio: 'Expert in tennis court coverage, serve explosiveness, and youth athletic longevity.'
    }
  ],

  // Scout Leaderboard Athletes
  leaderboard: [
    {
      id: 'ath-1',
      name: 'Kobe Alvarez',
      sport: 'Basketball',
      age: 18,
      height: '6 ft 4 in (193 cm)',
      location: 'Los Angeles, USA',
      jumpHeightInches: 38.2,
      dribbleSpeedHz: 4.9,
      sprint40yd: 4.48,
      overallScore: 96,
      deepfakeStatus: 'PASSED (99.8% Authentic)',
      medicalStatus: 'VERIFIED (Cleared within 24h)',
      medicalTimestamp: '2026-08-17 08:30 AM',
      videoTimestamp: '2026-08-17 02:15 PM',
      scoutInterest: 14,
      avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&auto=format&fit=crop&q=80'
    },
    {
      id: 'ath-2',
      name: 'Mateo Silva',
      sport: 'Football / Soccer',
      age: 17,
      height: '5 ft 10 in (178 cm)',
      location: 'São Paulo, Brazil',
      jumpHeightInches: 31.5,
      dribbleSpeedHz: 5.2,
      sprint40yd: 4.39,
      overallScore: 94,
      deepfakeStatus: 'PASSED (99.4% Authentic)',
      medicalStatus: 'VERIFIED (Cleared within 24h)',
      medicalTimestamp: '2026-08-16 11:00 AM',
      videoTimestamp: '2026-08-16 04:45 PM',
      scoutInterest: 22,
      avatar: 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=150&auto=format&fit=crop&q=80'
    },
    {
      id: 'ath-3',
      name: 'Amina Diallo',
      sport: 'Athletics / Track',
      age: 19,
      height: '5 ft 9 in (175 cm)',
      location: 'Dakar, Senegal',
      jumpHeightInches: 35.8,
      dribbleSpeedHz: 3.4,
      sprint40yd: 4.32,
      overallScore: 95,
      deepfakeStatus: 'PASSED (99.9% Authentic)',
      medicalStatus: 'VERIFIED (Cleared within 24h)',
      medicalTimestamp: '2026-08-17 09:15 AM',
      videoTimestamp: '2026-08-17 11:30 AM',
      scoutInterest: 19,
      avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80'
    },
    {
      id: 'ath-4',
      name: 'Arjun Verma',
      sport: 'Cricket',
      age: 18,
      height: '6 ft 1 in (185 cm)',
      location: 'Delhi, India',
      jumpHeightInches: 32.4,
      dribbleSpeedHz: 4.1,
      sprint40yd: 4.52,
      overallScore: 91,
      deepfakeStatus: 'PASSED (99.2% Authentic)',
      medicalStatus: 'VERIFIED (Cleared within 24h)',
      medicalTimestamp: '2026-08-17 07:00 AM',
      videoTimestamp: '2026-08-17 01:20 PM',
      scoutInterest: 11,
      avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&auto=format&fit=crop&q=80'
    },
    {
      id: 'ath-5',
      name: 'Sophia Lindqvist',
      sport: 'Tennis',
      age: 16,
      height: '5 ft 11 in (180 cm)',
      location: 'Stockholm, Sweden',
      jumpHeightInches: 30.2,
      dribbleSpeedHz: 4.6,
      sprint40yd: 4.46,
      overallScore: 92,
      deepfakeStatus: 'PASSED (99.5% Authentic)',
      medicalStatus: 'VERIFIED (Cleared within 24h)',
      medicalTimestamp: '2026-08-16 02:30 PM',
      videoTimestamp: '2026-08-16 06:10 PM',
      scoutInterest: 16,
      avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=150&auto=format&fit=crop&q=80'
    }
  ],

  // Preset Verified Medical & Anti-Doping Reports
  sampleMedicalReports: [
    {
      id: 'med-rep-101',
      athleteName: 'Kobe Alvarez',
      reportType: 'WADA-Standard Anti-Doping & Physiological Clearance',
      labName: 'Apex Olympic Certified Bio-Diagnostic Lab',
      accreditationId: 'WADA-ISO/IEC-17025-CL492',
      doctorName: 'Dr. Evelyn Reed, MD (Sports Medicine)',
      timestamp: '2026-08-17 08:30:00',
      validityHours: 24,
      substancesTested: [
        { category: 'Anabolic-Androgenic Steroids (AAS)', result: 'NEGATIVE', status: 'CLEARED' },
        { category: 'Peptide Hormones & Growth Factors (EPO/hGH)', result: 'NEGATIVE', status: 'CLEARED' },
        { category: 'Beta-2 Agonists & Bronchodilators', result: 'NEGATIVE', status: 'CLEARED' },
        { category: 'Hormone & Metabolic Modulators', result: 'NEGATIVE', status: 'CLEARED' },
        { category: 'Stimulants & Central Nervous System Agents', result: 'NEGATIVE', status: 'CLEARED' },
        { category: 'Narcotics & Cannabinoids', result: 'NEGATIVE', status: 'CLEARED' },
        { category: 'Glucocorticoids', result: 'NEGATIVE', status: 'CLEARED' }
      ],
      vitals: {
        restingHeartRate: '52 bpm (Athletic Norm)',
        bloodPressure: '118/74 mmHg (Optimal)',
        vo2MaxEst: '58.4 mL/kg/min',
        orthopedicJointScore: 'Grade A (Full Mobility, Zero Ligament Strain)'
      },
      conclusion: 'FIT FOR COMPETITION & SCOUT COMBINE. No prohibited performance enhancers detected. Certificate valid for 24-hour verification window.'
    }
  ],

  // 24/7 Helpline Hotlines & Emergency Directory
  helplines: [
    {
      category: 'Sports Injury & Emergency First Aid',
      number: '+1 (800) 555-SPORTS (US/Global)',
      altNumber: '+44 20 7946 0912 (UK/EU)',
      available: '24 Hours / 7 Days a Week',
      description: 'Immediate tele-triage for acute ligament tears, sprains, muscle ruptures, and sports trauma by certified physiotherapists.'
    },
    {
      category: 'Athlete Mental Wellness & Pressure Helpline',
      number: '+1 (800) 273-TALK (Option 4 Athlete)',
      altNumber: 'Text "PLAY" to 741741',
      available: '24/7 Confidential',
      description: 'Support for performance anxiety, burnout, scout trial stress, and student-athlete mental resilience counseling.'
    },
    {
      category: 'Anti-Doping & Safe Supplement Advisory Hotline',
      number: '+1 (800) 223-0393 (CleanSport Hotline)',
      altNumber: 'support@wada-ama.org',
      available: '24/7 Inquiry Support',
      description: 'Verify if any over-the-counter medication, pre-workout, or prescription drug is on the prohibited list before trials.'
    },
    {
      category: 'Concussion & Head Trauma Emergency Protocol',
      number: '+1 (888) CONCUSS (888-266-2877)',
      altNumber: 'Immediate 911 / 112 for severe trauma',
      available: '24/7 Immediate Protocol',
      description: 'Step-by-step SCAT6 concussion assessment guidance and return-to-play protocol verification.'
    }
  ]
};

// Expose globally
if (typeof window !== 'undefined') {
  window.SAMPLE_DATA = SAMPLE_DATA;
}
