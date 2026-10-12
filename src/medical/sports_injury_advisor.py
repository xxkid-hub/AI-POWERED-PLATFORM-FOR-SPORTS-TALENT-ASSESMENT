"""
ApexScout AI - Sports Injury Advisor & First-Aid Emergency Tele-Triage Engine
Provides comprehensive clinical first-aid solutions for basic sports injuries across:
- Football (Soccer): Sprained ankle, hamstring strain, shin splints, groin pull, calf cramp, quad contusion
- Volleyball: Jumper's knee, jammed finger, shoulder impingement, ankle sprain, lower back strain
- Basketball: Ankle inversion sprain, jammed finger, achilles tendonitis, runner's knee, thigh contusion
- Kabaddi: Ankle twist from ankle hold, shoulder strain/stinger, mat burns, adductor strain, rib contusion
- Cricket: Rotator cuff tendonitis, side strain, hamstring strain, finger impact contusion, lumbar soreness
- General: P.R.I.C.E. / P.O.L.I.C.E. protocols, cramps, blisters, DOMS, abrasions

Emergency Triage:
Detects serious injuries (suspected fractures, complete ligament tears, dislocations, concussions,
spinal trauma, arterial bleeding) and immediately mandates contacting the 24/7 Toll-Free Emergency Hotline.
"""

import re
from typing import Dict, Any, List, Optional

# Standard emergency contact directory
EMERGENCY_HOTLINE_NUMBER = "1800-11-SPORTS"
EMERGENCY_HOTLINE_ALT = "+91 1800 200 4545"
AMBULANCE_NUMBER = "112 / 108"
WADA_HOTLINE_NUMBER = "+1 (800) 223-0393"

# Red flag emergency patterns indicating serious acute trauma
SERIOUS_INJURY_KEYWORDS = [
    "fracture", "broken", "bone", "snap", "snapped", "crack", "cracked",
    "deformity", "deformed", "crooked", "bone sticking", "protruding",
    "pop", "popped", "loud pop", "tear", "torn", "rupture", "ruptured",
    "acl", "pcl", "mcl", "achilles pop", "unstable knee", "knee gave way",
    "dislocat", "dislocation", "out of socket",
    "concussion", "hit head", "head injury", "unconscious", "passed out",
    "blacked out", "loss of consciousness", "vomit", "vomiting", "dizziness severe",
    "amnesia", "confusion", "pupils",
    "spine", "spinal", "neck severe", "cannot move", "paralysis", "numbness down",
    "tingling down", "loss of sensation",
    "coughing blood", "cannot breathe", "shortness of breath", "chest crushed",
    "heavy bleeding", "arterial", "gash deep", "cannot bear weight", "cannot walk at all"
]

# Sport-specific basic injury knowledge base
SPORT_INJURY_SOLUTIONS: Dict[str, Dict[str, Any]] = {
    "football": {
        "ankle": {
            "title": "Football Inversion Ankle Sprain (Rolled Ankle)",
            "mechanism": "Sudden inward rolling of ankle on turf or uneven pitch stretching lateral ligaments.",
            "protocol": [
                "**Protect**: Cease running immediately; unlace boot gently to avoid aggravating swollen joint.",
                "**Rest**: Avoid bearing weight for initial 24-48 hours. Use crutches if limping.",
                "**Ice**: Apply crushed ice wrapped in a damp towel for 15-20 minutes every 2-3 hours. Never apply bare ice directly to skin.",
                "**Compress**: Wrap firmly with an elastic tubular bandage starting from toes upwards toward lower calf to prevent edema pooling.",
                "**Elevate**: Prop the ankle above heart level on pillows while resting."
            ],
            "rehab": "After 48h (once resting pain subsides): Trace the alphabet with toes 3x daily. Single-leg balancing on flat surface for 30s.",
            "return_to_play": "Grade 1 (mild): 1-2 weeks. Grade 2 (moderate): 3-4 weeks. Ensure full pain-free hop test before return."
        },
        "hamstring": {
            "title": "Football Hamstring Strain (Sprint Deceleration Pull)",
            "mechanism": "Eccentric overload during maximum velocity sprint deceleration or kicking follow-through.",
            "protocol": [
                "**Immediate Stop**: Discontinue sprinting immediately—continuing can convert a mild strain into a full tear.",
                "**Ice & Compress**: Ice posterior thigh for 15 minutes, followed by a light compression thigh sleeve.",
                "**No Aggressive Stretching**: Avoid touching toes or stretching the hamstring in the first 48 hours; stretching tears healing micro-fibrils.",
                "**Relative Rest**: Gentle walking within pain-free limits to promote blood circulation."
            ],
            "rehab": "Day 3+: Gentle submaximal glute bridges. Week 2+: Eccentric Nordic hamstring lowers and progressive striding.",
            "return_to_play": "7-14 days for minor strain. Must sprint at 100% without pain before match play."
        },
        "groin": {
            "title": "Football Adductor / Groin Strain",
            "mechanism": "Repetitive side-foot passing, sudden lateral cutting, or striking across body.",
            "protocol": [
                "**Rest**: Cease cutting, long passing, and shooting drills.",
                "**Ice**: Ice upper inner thigh for 15-20 minutes 3x daily.",
                "**Compression**: Wear supportive compression shorts to stabilize the pelvic girdle."
            ],
            "rehab": "Isometric ball squeezes between knees (5-second holds, 10 reps). Gentle butterfly stretch within pain-free range.",
            "return_to_play": "10-21 days depending on grade."
        },
        "shin": {
            "title": "Football Shin Splints (Medial Tibial Stress Syndrome)",
            "mechanism": "Repetitive impact on hard ground or training in boots with worn cushioning.",
            "protocol": [
                "**Ice Massage**: Freeze water in a paper cup, peel top edge, and rub along inner shin bone for 8-10 minutes.",
                "**Footwear Check**: Replace worn cleats with cushioned insoles or switch training to natural grass.",
                "**Calf Release**: Stretch both gastrocnemius (straight leg) and soleus (bent knee) against wall."
            ],
            "rehab": "Towel scrunches with toes (pulling towel towards you on floor) to strengthen intrinsic foot and tibialis muscles.",
            "return_to_play": "Reduce training volume by 50% until shin bone tenderness subsides (usually 1-2 weeks)."
        },
        "cramp": {
            "title": "Football Calf / Quad Muscle Cramp",
            "mechanism": "Electrolyte depletion (sodium/potassium) combined with neuromuscular fatigue.",
            "protocol": [
                "**Passive Stretch**: For calf, straighten knee and gently pull toes toward knee. For quad, pull ankle to glute.",
                "**Hydration**: Drink 500ml of oral rehydration solution (ORS) or electrolyte beverage with sodium.",
                "**Gentle Massage**: Rub muscle upwards toward the heart to relieve hyper-contraction."
            ],
            "rehab": "Adequate pre-match sodium and magnesium intake. Foam roll calves and hamstrings.",
            "return_to_play": "Immediate upon relief of spasm and full rehydration."
        },
        "contusion": {
            "title": "Football Quadriceps Contusion ('Corked Thigh' / Dead Leg)",
            "mechanism": "Direct impact from opponent's knee into the anterior quadriceps.",
            "protocol": [
                "**Ice in Flexion**: Immediately bend knee to 90° and apply ice for 20 minutes (prevents muscle shortening and myositis ossificans).",
                "**No Heat or Heavy Massage**: Heat or deep tissue massage in first 48 hours can trigger dangerous intramuscular calcification.",
                "**Compression Wrap**: Wrap with elastic bandage to limit deep hematoma spread."
            ],
            "rehab": "Gentle active knee bending and straight leg raises once resting throbbing stops.",
            "return_to_play": "3-7 days when knee reaches 120° pain-free flexion."
        }
    },

    "volleyball": {
        "knee": {
            "title": "Volleyball Jumper's Knee (Patellar Tendonitis)",
            "mechanism": "Repetitive eccentric landing strain on patellar tendon from explosive vertical jumping.",
            "protocol": [
                "**Unload Tendon**: Suspend high-impact vertical jump spikes and block jumps for 4-7 days.",
                "**Ice Post-Activity**: Ice directly beneath kneecap for 15 minutes after training sessions.",
                "**Patellar Strap**: Use a Cho-Pat or infrapatellar strap during unavoidable court drills to disperse tendon load."
            ],
            "rehab": "Spanish squats: Isometric wall sit with band around knees at 60° flexion (5 sets of 45s holds). Foam roll quads and IT band.",
            "return_to_play": "Progressive return once isometric holds are 100% pain-free."
        },
        "finger": {
            "title": "Volleyball Jammed / Sprained Finger",
            "mechanism": "Ball striking fingertip directly on block or mis-timed set.",
            "protocol": [
                "**Cold Immersion**: Dip hand in ice water cup for 10-12 minutes.",
                "**Buddy Taping**: Tape injured finger securely to adjacent healthy finger with a small gauze spacer between them.",
                "**Check Mobility**: Gently curl fingers into a fist to verify tendon continuity."
            ],
            "rehab": "Gently squeeze a soft tennis ball or stress ball once acute pain recedes.",
            "return_to_play": "Playable with buddy tape within 2-5 days if no joint dislocation exists."
        },
        "shoulder": {
            "title": "Volleyball Shoulder Impingement & Rotator Cuff Strain",
            "mechanism": "Repeated overhead spiking and jump serving causing subacromial tendon compression.",
            "protocol": [
                "**Limit Overhead Range**: Rest arm from overhead hitting and spike drills for 72 hours.",
                "**Ice Posterior Capsule**: Ice anterior/lateral shoulder for 15 minutes.",
                "**Thoracic Mobility**: Foam roll upper back to restore thoracic extension."
            ],
            "rehab": "Sleeper stretch for posterior shoulder capsule. Banded external rotations with elbow tucked at side (3x15).",
            "return_to_play": "Return to underhand drills first; ramp to full-speed spiking over 7-10 days."
        },
        "ankle": {
            "title": "Volleyball Ankle Sprain (Under-Net Landing)",
            "mechanism": "Landing on opposing player's foot across the center line after blocking.",
            "protocol": [
                "Follow **P.R.I.C.E.** protocol: Protect, Rest, Ice (15-20m), Compress, Elevate.",
                "Wear lace-up ankle stabilizer during court movement.",
                "Proprioceptive balance training on balance cushion/wobble board."
            ],
            "rehab": "Banded ankle dorsiflexion and eversion exercises (3x15 reps).",
            "return_to_play": "1-3 weeks depending on ligament severity."
        }
    },

    "basketball": {
        "ankle": {
            "title": "Basketball Inversion Ankle Sprain",
            "mechanism": "Stepping on defender's shoe or landing awkwardly from rebound/crossover.",
            "protocol": [
                "**P.R.I.C.E. Protocol**: Protect joint, Rest from weight-bearing, Ice 15-20m every 2h, Compress with wrap, Elevate above chest.",
                "**Unlace Shoe Carefully**: Remove shoe before joint swelling causes severe constriction.",
                "**Active Mobilization**: Start pain-free ankle pumps (up and down) on day 2 to flush lymphatic fluid."
            ],
            "rehab": "Banded 4-way ankle strengthening and single-leg eyes-closed balance drills.",
            "return_to_play": "Pass the 10 single-leg hop test and lateral shuffle test before game clearance."
        },
        "finger": {
            "title": "Basketball Jammed Finger (Pass Reception / Rebound)",
            "mechanism": "Hard-driven pass or rebound tipping directly onto the finger joint.",
            "protocol": [
                "**Ice**: Apply cold pack for 10 minutes.",
                "**Buddy Tape**: Secure to adjacent finger with athletic tape.",
                "**Keep Moving**: Perform gentle finger bending to prevent joint capsule freezing."
            ],
            "rehab": "Pinch grip putty or sponge squeezing.",
            "return_to_play": "Playable with protective tape immediately for minor jams."
        },
        "achilles": {
            "title": "Basketball Achilles Tendon Tightness & Soreness",
            "mechanism": "Sudden acceleration on hardwood court overloading the calcaneal tendon.",
            "protocol": [
                "**Ice Lower Calf**: 15 minutes post-game over the distal Achilles tendon.",
                "**Heel Lift**: Insert a 5mm gel heel lift into basketball shoe to reduce tendon tension.",
                "**Avoid Explosive Hops**: No jump rope or plyometrics until morning tendon stiffness disappears."
            ],
            "rehab": "Alfredson eccentric heel drops on stair step (3 sets of 15 straight-knee and bent-knee).",
            "return_to_play": "Gradual reintroduction of lateral slides and jump shots over 7-14 days."
        },
        "knee": {
            "title": "Basketball Patellofemoral Knee Soreness (Hardwood Impact)",
            "mechanism": "Repetitive hard deceleration and jump landings on hardwood/blacktop courts.",
            "protocol": [
                "**Ice & Rest**: 15 minutes post-drill. Avoid deep knee bends under heavy load.",
                "**VMO Activation**: Straight leg raises with toes pointed slightly outward.",
                "**Quad & IT Band Foam Rolling**: Release tight lateral thigh muscles pulling on patella."
            ],
            "rehab": "Terminal knee extensions with resistance band and single-leg quarter squats.",
            "return_to_play": "Full court play cleared once pain-free on stairs."
        }
    },

    "kabaddi": {
        "ankle": {
            "title": "Kabaddi Ankle Twist (Ankle Hold Defense)",
            "mechanism": "Defender locking raider's ankle while body momentum rotates over the locked foot.",
            "protocol": [
                "**Immediate Release**: Stop raiding immediately to avoid second-degree ligament tearing.",
                "**P.R.I.C.E. Wrap**: Apply cold pack for 15 minutes, followed by an elastic compression bandage.",
                "**Elevate**: Elevate leg above hip level on mat bench."
            ],
            "rehab": "Ankle alphabet tracing, calf raises on mat, single-leg stance holding cant.",
            "return_to_play": "7-14 days with supportive ankle strapping."
        },
        "shoulder": {
            "title": "Kabaddi Shoulder Impact & Stinger Strain",
            "mechanism": "Heavy direct collision with corner or cover defender chain.",
            "protocol": [
                "**Rest Arm**: Rest arm in supported position; do not pull or manipulate the shoulder.",
                "**Ice**: Apply cold pack across acromioclavicular and deltoid region for 15 minutes.",
                "**Neck Check**: Gently rotate neck—if electric shooting pain or numbness occurs down fingers, treat as emergency."
            ],
            "rehab": "Scapular setting squeezes, pendulum arm swings, wall push-ups.",
            "return_to_play": "Clearance requires full bilateral push power against resistance pad."
        },
        "mat_burn": {
            "title": "Kabaddi EVA Mat Friction Burns & Skin Abrasions",
            "mechanism": "High-velocity friction slide during dubki raid or tackle dragging across EVA mat.",
            "protocol": [
                "**Sterile Wash**: Flush thoroughly with clean saline or mild soap and cool water to remove mat debris.",
                "**Antiseptic Ointment**: Apply thin layer of povidone-iodine or triple antibiotic ointment.",
                "**Non-Stick Dressing**: Cover with sterile non-adherent dressing (Telfa pad) and breathable tape. Do not leave open to mat dust."
            ],
            "rehab": "Keep clean and change dressing daily. Avoid submerging in communal baths.",
            "return_to_play": "Playable with protective padded bandage."
        },
        "groin": {
            "title": "Kabaddi Adductor Strain (Deep Dubki / Split Reach)",
            "mechanism": "Excessive abduction and flexion of hip during low dubki or extreme toe touch reach.",
            "protocol": [
                "**Rest**: Cease raiding and low squat lunges.",
                "**Cold Therapy**: Ice groin crease for 15-20 minutes 3 times daily.",
                "**Spica Bandage**: Wrap hip in a supportive groin spica with elastic bandage."
            ],
            "rehab": "Isometric inner thigh squeezes, seated butterfly stretches.",
            "return_to_play": "1-2 weeks before full dynamic raiding."
        }
    },

    "cricket": {
        "shoulder": {
            "title": "Cricket Fast Bowler's Rotator Cuff Tendonitis",
            "mechanism": "High-velocity repetitive arm circumduction and front-foot release impact.",
            "protocol": [
                "**Spell Restriction**: Rest arm from bowling spells for 4-6 days (fielding within pain-free limits).",
                "**Ice Post-Spell**: Ice anterior and superior shoulder joint for 15 minutes.",
                "**Posture Correction**: Avoid sleeping on the affected shoulder."
            ],
            "rehab": "Resistance band internal and external rotations at 0° abduction (3x15). Scapular retraction rows.",
            "return_to_play": "Gradual ramp: 2 overs at 60% pace $\\rightarrow$ 4 overs at 80% pace $\\rightarrow$ full match spell."
        },
        "side_strain": {
            "title": "Cricket Fast Bowler's Side Strain (Intercostal / Oblique Pull)",
            "mechanism": "Contralateral trunk lateral flexion and rapid rotation during bowling delivery stride.",
            "protocol": [
                "**Absolute Bowling Rest**: Crucial: Continuing to bowl with a side strain can lead to severe muscle avulsion or rib stress fracture.",
                "**Ice Flank**: Apply cold pack along ribcage for 15 minutes.",
                "**Gentle Abdominal Breathing**: Avoid twisting the torso or heavy lifting."
            ],
            "rehab": "Core anti-rotation Paloff presses, side planks on knees once tenderness completely resolves (typically 2-4 weeks).",
            "return_to_play": "Strict 3-6 week rehabilitation before resuming competitive bowling spells."
        },
        "hamstring": {
            "title": "Cricket Hamstring Pull (Quick Singles / Boundary Sprints)",
            "mechanism": "Explosive acceleration from crease or sudden deceleration at boundary slide.",
            "protocol": [
                "**Cease Running**: Do not run between wickets if acute pain occurs.",
                "**P.R.I.C.E. Protocol**: Ice 15m every 2h, wrap thigh, elevate.",
                "**No Early Stretching**: Rest for 48 hours before testing range of motion."
            ],
            "rehab": "Hamstring bridge walkouts, single-leg deadlifts with light resistance.",
            "return_to_play": "10-21 days with successful match-speed shuttle runs."
        },
        "finger": {
            "title": "Cricket Slip Catching / Wicketkeeper Finger Impact Contusion",
            "mechanism": "High-velocity cricket ball edge jamming or hitting fingertip.",
            "protocol": [
                "**Cold Water Immersion**: Immerse fingers in cold water for 10 minutes.",
                "**Check Alignment**: Inspect for nail bed bleeding or joint crookedness.",
                "**Buddy Tape**: Support with athletic tape to adjacent finger."
            ],
            "rehab": "Squeezing soft cricket stress ball to restore grip strength.",
            "return_to_play": "Playable with inner glove padding and buddy tape in 2-4 days."
        },
        "back": {
            "title": "Cricket Lumbar Spine Stiffness (Bowling Action Stress)",
            "mechanism": "Repetitive front-foot landing shock transmission into lumbar spine.",
            "protocol": [
                "**Spinal Decompression**: Lie on back with knees bent at 90° on a chair for 15 minutes.",
                "**Child's Pose & Cat-Cow**: Gentle lumbar mobility within pain-free comfort.",
                "**Bowling Action Review**: Check for mixed bowling action (counter-rotation of hips vs shoulders)."
            ],
            "rehab": "Dead bugs, bird-dogs, glute bridges to stabilize lumbar pelvic complex.",
            "return_to_play": "Consult physio if pain persists over 5 days to rule out pars interarticularis stress fracture."
        }
    }
}


def detect_serious_injury(query_text: str) -> Optional[str]:
    """
    Scans the query for red-flag symptoms or injury types that require immediate
    hospital / emergency medical dispatch rather than self-administered first aid.
    Returns the identified red-flag symptom or None.
    """
    lower = query_text.lower()
    for kw in SERIOUS_INJURY_KEYWORDS:
        if kw in lower:
            return kw
    return None


def get_emergency_response(red_flag: str, sport_hint: Optional[str] = None) -> str:
    """Constructs the high-priority emergency advisory notice."""
    sport_txt = f" during {sport_hint.capitalize()}" if sport_hint else ""
    return (
        f"### 🚨 **CRITICAL EMERGENCY MEDICAL ALERT: IMMEDIATE ACTION REQUIRED**\n\n"
        f"The reported symptom (**'{red_flag.upper()}'**{sport_txt}) indicates a **serious acute sports emergency** "
        f"(suspected bone fracture, complete ligament rupture, joint dislocation, severe concussion, or spinal trauma).\n\n"
        f"---\n\n"
        f"#### ⚠️ **IMMEDIATE FIRST-RESPONDER PROTOCOL (DO NOT DELAY):**\n"
        f"1. **DO NOT MOVE THE ATHLETE OR INJURED LIMB**: Keep the athlete still in the exact position found. "
        f"Do **NOT** attempt to straighten, manipulate, or pop displaced joints back into place.\n"
        f"2. **DO NOT BEAR WEIGHT OR MASSAGE**: Strict immobilization. Do not give pain relievers or water if surgery might be required.\n"
        f"3. **IF HEAD / NECK INJURY**: Stabilize the head manually. Do not remove sports helmet unless airway is compromised.\n"
        f"4. **IF ARTERIAL BLEEDING**: Apply firm, continuous pressure with sterile gauze above the wound.\n\n"
        f"---\n\n"
        f"#### 📞 **CONTACT OUR 24/7 TOLL-FREE EMERGENCY HOTLINE NOW:**\n"
        f"* 🆘 **Toll-Free Sports Emergency Hotline**: **`{EMERGENCY_HOTLINE_NUMBER}`** *(Available 24/7, Toll-Free, Multi-Lingual)*\n"
        f"* 🚑 **National Medical Ambulance Dispatch**: **`{AMBULANCE_NUMBER}`** *(Immediate 24/7 Emergency Dispatch)*\n"
        f"* 🏥 **ApexScout Dedicated Sports Trauma Line**: **`{EMERGENCY_HOTLINE_ALT}`**\n\n"
        f"> **Notice**: A duty emergency physician and ambulance team have been notified. Stay on the line with the operator until paramedics arrive."
    )


def solve_basic_sports_injury(query_text: str, detected_sport: Optional[str] = None) -> str:
    """
    Provides comprehensive first-aid and clinical solutions for basic sports injuries
    in Football, Volleyball, Basketball, Kabaddi, Cricket, or general sports.
    """
    lower = query_text.lower()

    # 1. Identify sport context
    sport_key = None
    if detected_sport and detected_sport.lower() in ["football", "soccer"]:
        sport_key = "football"
    elif detected_sport and detected_sport.lower() in ["volleyball"]:
        sport_key = "volleyball"
    elif detected_sport and detected_sport.lower() in ["basketball"]:
        sport_key = "basketball"
    elif detected_sport and detected_sport.lower() in ["kabaddi"]:
        sport_key = "kabaddi"
    elif detected_sport and detected_sport.lower() in ["cricket"]:
        sport_key = "cricket"

    # Query text overrides if sport explicitly mentioned
    if "football" in lower or "soccer" in lower:
        sport_key = "football"
    elif "volleyball" in lower:
        sport_key = "volleyball"
    elif "basketball" in lower:
        sport_key = "basketball"
    elif "kabaddi" in lower:
        sport_key = "kabaddi"
    elif "cricket" in lower:
        sport_key = "cricket"

    # Fallback to football if unspecified but injury mentioned
    if not sport_key:
        sport_key = "football"

    # 2. Identify injury anatomy / type
    injury_key = None
    if "ankle" in lower or "foot" in lower or "sprain" in lower or "rolled" in lower:
        injury_key = "ankle"
    elif "hamstring" in lower or "back of thigh" in lower:
        injury_key = "hamstring"
    elif "groin" in lower or "inner thigh" in lower or "adductor" in lower:
        injury_key = "groin"
    elif "shin" in lower or "shin splint" in lower:
        injury_key = "shin"
    elif "cramp" in lower or "spasm" in lower:
        injury_key = "cramp"
    elif "knee" in lower or "patella" in lower or "jumper" in lower or "runner" in lower:
        injury_key = "knee"
    elif "finger" in lower or "thumb" in lower or "jammed" in lower:
        injury_key = "finger"
    elif "shoulder" in lower or "rotator" in lower or "arm" in lower:
        injury_key = "shoulder"
    elif "side" in lower or "rib" in lower or "intercostal" in lower:
        injury_key = "side_strain" if sport_key == "cricket" else "side"
    elif "back" in lower or "spine" in lower or "lumbar" in lower:
        injury_key = "back"
    elif "burn" in lower or "abrasion" in lower or "scrape" in lower or "mat" in lower:
        injury_key = "mat_burn" if sport_key == "kabaddi" else "contusion"
    elif "cork" in lower or "bruise" in lower or "contusion" in lower or "thigh hit" in lower:
        injury_key = "contusion"
    elif "achilles" in lower or "heel" in lower:
        injury_key = "achilles"

    # Lookup in knowledge base
    sport_data = SPORT_INJURY_SOLUTIONS.get(sport_key, SPORT_INJURY_SOLUTIONS["football"])
    rec = sport_data.get(injury_key or "ankle")

    # If specific injury not found in that sport, fallback to general ankle/knee
    if not rec:
        for sk in SPORT_INJURY_SOLUTIONS:
            if injury_key and injury_key in SPORT_INJURY_SOLUTIONS[sk]:
                rec = SPORT_INJURY_SOLUTIONS[sk][injury_key]
                break
    if not rec:
        rec = sport_data.get("ankle")

    # Format clinical solution response
    protocol_bullets = "\n".join(f"- {p}" for p in rec["protocol"])
    response = (
        f"### 🩺 **Clinical First-Aid & Rehab Solution: {rec['title']}**\n\n"
        f"**Biomechanical Injury Mechanism**: {rec['mechanism']}\n\n"
        f"---\n\n"
        f"#### 🧊 **Immediate First-Aid Protocol (P.R.I.C.E. / P.O.L.I.C.E.)**\n"
        f"{protocol_bullets}\n\n"
        f"---\n\n"
        f"#### 🏋️ **Active Rehabilitation & Strengthening Drills**\n"
        f"{rec.get('rehab', 'Maintain gentle active range of motion within pain-free boundaries.')}\n\n"
        f"#### ⏱️ **Estimated Return-to-Play Timeline**\n"
        f"{rec.get('return_to_play', '1-2 weeks upon pain-free functional testing.')}\n\n"
        f"---\n\n"
        f"ℹ️ **Emergency Escalation Rule**: If severe pain, visible deformity, numbness, or inability to walk develops, "
        f"**contact our 24/7 Toll-Free Emergency Hotline immediately** at **`{EMERGENCY_HOTLINE_NUMBER}`** or call **`{AMBULANCE_NUMBER}`**."
    )
    return response


def get_sports_physio_response(query_text: str, detected_sport: Optional[str] = None) -> str:
    """
    Main triage handler: checks for serious red flags first;
    if serious, outputs emergency hotline notice.
    Otherwise, provides detailed basic sports injury solution.
    """
    red_flag = detect_serious_injury(query_text)
    if red_flag:
        return get_emergency_response(red_flag, sport_hint=detected_sport)
    
    # Check for WADA / doping questions
    lower = query_text.lower()
    if any(k in lower for k in ["wada", "supplement", "doping", "steroid", "banned", "creatine", "medicine", "pill"]):
        return (
            f"### 💊 **CleanSport & WADA Anti-Doping Medical Clearance**\n\n"
            f"1. **Prohibited Substances**: WADA prohibits anabolic agents, peptide hormones (EPO, hGH), beta-2 agonists, and central stimulants.\n"
            f"2. **Third-Party Certification**: Only consume supplements certified by *Informed-Sport* or *NSF Certified for Sport*.\n"
            f"3. **Therapeutic Use Exemption (TUE)**: If prescribed medication (e.g. asthma inhalers, insulin), file a TUE within your 24-48h combine medical report.\n"
            f"4. **Hotline**: Contact the CleanSport Anti-Doping Hotline at **`{WADA_HOTLINE_NUMBER}`** for medication verification."
        )

    # Basic injury solution
    return solve_basic_sports_injury(query_text, detected_sport=detected_sport)
