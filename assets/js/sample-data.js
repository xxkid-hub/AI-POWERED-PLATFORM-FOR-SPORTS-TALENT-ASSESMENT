/**
 * ApexScout AI - Expanded PRD Dataset
 * Includes multi-sport combines, 3-tier 24-48h medical records, weekly progression trajectories,
 * kinetic deficiency catalog, certified scouts, and helpline directory.
 */

const SAMPLE_DATA = {
  drills: [
    {
      id: 'drill-soccer-penalty',
      sport: 'Football / Soccer',
      skillName: 'Penalty Kick',
      category: 'Shooting & Striking',
      title: 'Precision Penalty Kick & Power Analysis',
      duration: '8s',
      targetMetrics: ['Shot Speed', 'Placement Accuracy', 'Plant Foot Stability', 'Ball Curve'],
      drillType: 'penalty_kick',
      componentAnalysis: {
        skill: 'Penalty Kick',
        shotResult: 'Goal',
        shotSpeed: '91 km/h',
        accuracy: '92%',
        ballPlacement: 'Bottom Left Corner',
        reactionTime: '0.82 sec',
        runUpSpeed: '18.4 km/h',
        plantFoot: 'Good (35° ankle angle, 12cm lateral spacing)',
        balance: 'Excellent (Center of mass stabilized over support leg)',
        followThrough: 'Good (Hips squared to target)',
        contactQuality: 'Clean (Instep sweet-spot strike)',
        ballCurve: 'Slight Inside Curve (14 rad/s spin)',
        overallRating: 94,
        deepfakeConfidence: 99.4,
        tamperingDetected: false
      }
    },
    {
      id: 'drill-cricket-bowling',
      sport: 'Cricket',
      skillName: 'Fast Bowling Release & Seam Action',
      category: 'Pace Bowling & Seam',
      title: 'Fast Bowling Velocity & Action Biomechanics',
      duration: '10s',
      targetMetrics: ['Release Speed', 'Front Foot Brace', 'Seam Position', 'Lateral Outswing'],
      drillType: 'cricket_bowling',
      componentAnalysis: {
        skill: 'Outswinger Fast Bowling',
        shotResult: 'Hit Top of Off-Stump (Wicket)',
        shotSpeed: '138.6 km/h',
        accuracy: '94%',
        ballPlacement: 'Good Length (Outside Off)',
        reactionTime: '0.64 sec',
        runUpSpeed: '24.8 km/h',
        plantFoot: 'Front foot braced (178° lockout)',
        balance: 'Optimal (Trunk hyperextension controlled)',
        followThrough: 'Complete hip rotation across left hip',
        contactQuality: 'Clean (Snap release at 2.15m height)',
        ballCurve: 'Late Outswing (2.4° lateral deviation)',
        overallRating: 96,
        deepfakeConfidence: 99.7,
        tamperingDetected: false
      }
    },
    {
      id: 'drill-kabaddi-raid',
      sport: 'Kabaddi',
      skillName: 'Toe Touch & Dubki Evasion Raid',
      category: 'Raiding & Quick Agility',
      title: 'Grassroots Kabaddi Raid & Agility Combine',
      duration: '14s',
      targetMetrics: ['Foot Extension Reach', 'Evasion Velocity', 'Turn Latency', 'Balance Recovery'],
      drillType: 'kabaddi_raid',
      componentAnalysis: {
        skill: 'Toe Touch & Dubki Raid',
        shotResult: 'Successful Touch (2 Touch Points)',
        shotSpeed: '22.4 km/h (Burst Velocity)',
        accuracy: '96%',
        ballPlacement: 'Bonus Line / Right Corner Ankle',
        reactionTime: '0.38 sec',
        runUpSpeed: '16.2 km/h',
        plantFoot: 'Low center of gravity (45° ankle flex)',
        balance: 'Superior (Rapid ground recovery from squat)',
        followThrough: 'Rapid midline return to baulk line',
        contactQuality: 'Precise (40ms contact window)',
        ballCurve: 'Rapid zig-zag evasion arc',
        overallRating: 95,
        deepfakeConfidence: 99.5,
        tamperingDetected: false
      }
    },
    {
      id: 'drill-vertical-jump',
      sport: 'Athletics / Track & Field',
      skillName: 'Max Vertical Combine Leap',
      category: 'Explosiveness & High Jump',
      title: 'Max Vertical Leap & Takeoff Elevation',
      duration: '10s',
      targetMetrics: ['Apex Height', 'Hang Time', 'Takeoff Impulse', 'Landing Absorption'],
      drillType: 'vertical_jump',
      componentAnalysis: {
        skill: 'Max Vertical Leap',
        shotResult: 'Apex Reached (36.8 inches / 93.5 cm)',
        shotSpeed: '4.35 m/s (Takeoff Velocity)',
        accuracy: '97%',
        ballPlacement: 'Vertical Apex Clearance',
        reactionTime: '0.29 sec',
        runUpSpeed: '12.6 km/h',
        plantFoot: 'Penultimate foot plant with 118° knee preload',
        balance: 'Superior (Vertical alignment through cervical spine)',
        followThrough: 'Triple extension (ankle, knee, hip)',
        contactQuality: 'High Elastic Energy Transfer',
        ballCurve: 'Pure Parabolic Gravitational Curve',
        overallRating: 96,
        deepfakeConfidence: 98.9,
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
      specialties: ['Vertical Leap Optimization', 'Point Guard Dribble Mechanics', 'Grassroots Scouting'],
      avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80',
      status: 'Accepting New Athletes',
      fee: 'Free Initial Assessment Review',
      badge: 'Verified NBA/NCAA Scout',
      bio: 'Over 14 years evaluating grassroots and collegiate prospects. Active scouting programs for rural and small-town talent.'
    },
    {
      id: 'coach-2',
      name: 'Elena Rostova',
      title: 'UEFA Pro License Scout & Technical Coach',
      affiliation: 'Global Football Scouting Network',
      sport: 'Football / Soccer',
      rating: 4.92,
      reviewsCount: 94,
      location: 'London, UK / São Paulo, Brazil',
      specialties: ['Penalty Kick Placement', 'Winger Agility & Cadence', 'Rural Scouting Programs'],
      avatar: 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=150&auto=format&fit=crop&q=80',
      status: 'Accepting Video Submissions',
      fee: 'Free Scout Evaluation',
      badge: 'UEFA Pro Certified',
      bio: 'Former youth academy director passionate about discovering raw soccer talent in remote and underserved regions.'
    },
    {
      id: 'coach-3',
      name: 'Rajeshwar Tyagi',
      title: 'Senior Cricket & Kabaddi High-Performance Coach',
      affiliation: 'National Rural Sports Federation & State Academy',
      sport: 'Cricket / Kabaddi',
      rating: 4.96,
      reviewsCount: 175,
      location: 'Haryana / Punjab / Maharashtra, India',
      specialties: ['Fast Bowling Biomechanics', 'Kabaddi Raid Tactics', 'Village Talent Identification'],
      avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&auto=format&fit=crop&q=80',
      status: 'Reviewing State Talent',
      fee: '100% Free Rural Talent Grants',
      badge: 'Govt Sports Authority Scout',
      bio: 'Discovered over 30 professional athletes from rural villages. Specializes in analyzing raw smartphone videos from clay courts and local grounds.'
    }
  ],

  // Scout Leaderboard with PRD 3-Tier Status Enforcement
  leaderboard: [
    {
      id: 'ath-1',
      name: 'Ravi Kumar',
      sport: 'Kabaddi',
      originType: 'Rural Grassroots Academy (Sonipat, India)',
      age: 18,
      height: '5 ft 11 in (180 cm)',
      location: 'Haryana, India',
      skillTested: 'Dubki Raid & Toe Touch',
      shotSpeed: '22.4 km/h',
      accuracy: '96%',
      reactionTime: '0.38 sec',
      overallScore: 96,
      deepfakeStatus: 'PASSED (99.8% Authentic)',
      medicalStatus: 'VERIFIED',
      medicalSlaBadge: 'badge-med-verified',
      medicalTimestamp: '2026-08-29 08:30 AM',
      videoTimestamp: '2026-08-29 02:15 PM',
      scoutInterest: 24,
      avatar: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=150&auto=format&fit=crop&q=80'
    },
    {
      id: 'ath-2',
      name: 'Mateo Silva',
      sport: 'Football / Soccer',
      originType: 'Grassroots Youth Club (Minas Gerais, Brazil)',
      age: 17,
      height: '5 ft 10 in (178 cm)',
      location: 'Minas Gerais, Brazil',
      skillTested: 'Penalty Kick (Bottom Left)',
      shotSpeed: '91 km/h',
      accuracy: '92%',
      reactionTime: '0.82 sec',
      overallScore: 94,
      deepfakeStatus: 'PASSED (99.4% Authentic)',
      medicalStatus: 'VERIFIED',
      medicalSlaBadge: 'badge-med-verified',
      medicalTimestamp: '2026-08-29 07:00 AM',
      videoTimestamp: '2026-08-29 11:30 AM',
      scoutInterest: 31,
      avatar: 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=150&auto=format&fit=crop&q=80'
    },
    {
      id: 'ath-3',
      name: 'Simran Preet Kaur',
      sport: 'Cricket',
      originType: 'Rural Sports Center (Moga, Punjab)',
      age: 19,
      height: '5 ft 8 in (173 cm)',
      location: 'Punjab, India',
      skillTested: 'Pace Bowling (Outswinger)',
      shotSpeed: '138.6 km/h',
      accuracy: '95%',
      reactionTime: '0.62 sec',
      overallScore: 95,
      deepfakeStatus: 'PASSED (99.9% Authentic)',
      medicalStatus: 'PENDING_REVIEW',
      medicalSlaBadge: 'badge-med-pending',
      medicalTimestamp: '2026-08-28 09:15 AM',
      videoTimestamp: '2026-08-29 01:30 PM',
      scoutInterest: 18,
      avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80'
    }
  ],

  // 24/7 Helplines
  helplines: [
    {
      category: 'Rural Sports & Grassroots Talent Hotline',
      number: '1800-11-SPORTS (Toll-Free 24/7)',
      altNumber: '+1 (800) 555-RURAL',
      available: '24/7 Multi-Lingual Support',
      description: 'Dedicated support for athletes from rural districts and small towns. Assistance with smartphone video combines, scout connections, and free medical clearance camps.'
    },
    {
      category: 'Sports Injury & Emergency First Aid Hotline',
      number: '+1 (800) 555-SPORTS (US/Global)',
      altNumber: '+91 1800 200 4545 (Asia/India)',
      available: '24 Hours / 7 Days a Week',
      description: 'Immediate tele-triage for acute sprains, knee trauma, ligament tears, and first aid guidance for coaches and players.'
    },
    {
      category: 'WADA Anti-Doping & CleanSport Advisory',
      number: '+1 (800) 223-0393 (CleanSport Hotline)',
      altNumber: 'support@wada-ama.org',
      available: '24/7 Advisory Hotline',
      description: 'Check if any local prescription medicine, fever medication, or supplement is WADA compliant before scout combine testing.'
    }
  ]
};

if (typeof window !== 'undefined') {
  window.SAMPLE_DATA = SAMPLE_DATA;
}
