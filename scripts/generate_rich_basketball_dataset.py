"""
ApexScout AI - Diverse Basketball Dataset Generator
Generates realistic, diverse basketball training imagery encompassing:
- Green / Teal acrylic courts (CBSE National tournament style courts)
- Blue & Red FIBA tournament courts
- Hardwood parquet courts with boundary lines and keys
- Distinctive basketballs (orange #EE6730 with black seams)
- Basketball hoops, backboards, rims (#FF4500), and nets
- Biomechanical athletic silhouettes performing all 8 fundamental basketball skills:
  Dribbling, Passing, Shooting, Lay-up, Rebounding, Defending, Stealing, Footwork.
"""

import os
import math
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

DATASET_BASKETBALL_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dataset", "Basketball")
os.makedirs(DATASET_BASKETBALL_DIR, exist_ok=True)

# Diverse court color palettes
COURT_PALETTES = [
    # 1. CBSE / Indian School Acrylic Green & Teal Courts
    {"name": "cbse_green", "court": (24, 120, 72), "key": (20, 100, 60), "lines": (255, 255, 255), "apron": (15, 80, 50)},
    {"name": "national_teal", "court": (16, 128, 110), "key": (210, 80, 45), "lines": (255, 255, 255), "apron": (10, 90, 80)},
    {"name": "emerald_court", "court": (34, 139, 90), "key": (30, 110, 70), "lines": (245, 245, 245), "apron": (20, 95, 60)},
    {"name": "acrylic_olive", "court": (46, 125, 80), "key": (200, 70, 40), "lines": (255, 255, 255), "apron": (30, 90, 55)},
    # 2. Hardwood Parquet Courts
    {"name": "hardwood_amber", "court": (212, 160, 90), "key": (180, 40, 40), "lines": (255, 255, 255), "apron": (160, 110, 60)},
    {"name": "hardwood_honey", "court": (225, 178, 105), "key": (30, 60, 140), "lines": (255, 255, 255), "apron": (190, 140, 80)},
    {"name": "polished_beech", "court": (235, 195, 125), "key": (160, 30, 30), "lines": (255, 255, 255), "apron": (200, 155, 95)},
    # 3. Modern Two-Tone Tournament Courts
    {"name": "fiba_blue_red", "court": (35, 85, 165), "key": (195, 45, 45), "lines": (255, 255, 255), "apron": (25, 60, 120)},
    {"name": "navy_amber", "court": (25, 65, 130), "key": (215, 145, 55), "lines": (255, 255, 255), "apron": (18, 45, 90)},
]

BASKETBALL_ORANGE = (238, 103, 48)
BASKETBALL_SHADOW = (180, 70, 25)
BASKETBALL_SEAMS = (30, 20, 15)
RIM_ORANGE = (255, 69, 0)
BACKBOARD_WHITE = (245, 248, 250)
NET_WHITE = (230, 235, 240)


def draw_basketball_court(draw, width, height, palette):
    """Draws court surface with realistic perspective lines, 3-pt arc, key, and free throw circle."""
    c_court = palette["court"]
    c_key = palette["key"]
    c_lines = palette["lines"]
    c_apron = palette["apron"]

    # Fill background/apron
    draw.rectangle([0, 0, width, height], fill=c_apron)

    # Infield court boundary
    pad_x = int(width * 0.08)
    pad_y = int(height * 0.12)
    draw.rectangle([pad_x, pad_y, width - pad_x, height - pad_y], fill=c_court, outline=c_lines, width=2)

    # Center court circle or key depending on orientation
    cx, cy = width // 2, height // 2
    r_center = int(width * 0.16)
    draw.ellipse([cx - r_center, cy - r_center, cx + r_center, cy + r_center], outline=c_lines, width=2)
    draw.line([cx, pad_y, cx, height - pad_y], fill=c_lines, width=2)

    # Key / Painted restricted area at one or both ends
    key_w = int(width * 0.22)
    key_h = int(height * 0.35)
    # Left key
    draw.rectangle([pad_x, cy - key_w // 2, pad_x + key_h, cy + key_w // 2], fill=c_key, outline=c_lines, width=2)
    # Free throw circle on left key
    ft_cx = pad_x + key_h
    ft_r = key_w // 2
    draw.arc([ft_cx - ft_r, cy - ft_r, ft_cx + ft_r, cy + ft_r], start=270, end=90, fill=c_lines, width=2)

    # 3-Point Arc
    arc_r = int(width * 0.38)
    draw.arc([pad_x - arc_r // 3, cy - arc_r, pad_x + arc_r, cy + arc_r], start=290, end=70, fill=c_lines, width=2)


def draw_basketball_hoop(draw, width, height, x_pos, y_pos, scale=1.0):
    """Draws a regulation basketball backboard, rim, and net."""
    bb_w = int(48 * scale)
    bb_h = int(32 * scale)
    bb_x = x_pos - bb_w // 2
    bb_y = y_pos

    # Backboard (white rectangle with inner box)
    draw.rectangle([bb_x, bb_y, bb_x + bb_w, bb_y + bb_h], fill=BACKBOARD_WHITE, outline=(50, 50, 50), width=1)
    inner_w = int(bb_w * 0.45)
    inner_h = int(bb_h * 0.45)
    in_x = x_pos - inner_w // 2
    in_y = bb_y + bb_h - inner_h - 2
    draw.rectangle([in_x, in_y, in_x + inner_w, in_y + inner_h], outline=RIM_ORANGE, width=1)

    # Rim (orange circle protruding forward)
    rim_r = int(9 * scale)
    rim_x = x_pos
    rim_y = bb_y + bb_h + int(2 * scale)
    draw.ellipse([rim_x - rim_r, rim_y - int(3 * scale), rim_x + rim_r, rim_y + int(3 * scale)], outline=RIM_ORANGE, width=2)

    # Net (triangular mesh hanging from rim)
    net_h = int(14 * scale)
    draw.line([rim_x - rim_r, rim_y, rim_x - rim_r // 2, rim_y + net_h], fill=NET_WHITE, width=1)
    draw.line([rim_x + rim_r, rim_y, rim_x + rim_r // 2, rim_y + net_h], fill=NET_WHITE, width=1)
    draw.line([rim_x, rim_y + 2, rim_x, rim_y + net_h], fill=NET_WHITE, width=1)
    draw.line([rim_x - rim_r // 2, rim_y + net_h, rim_x + rim_r // 2, rim_y + net_h], fill=NET_WHITE, width=1)


def draw_basketball(draw, cx, cy, radius):
    """Draws an authentic basketball with orange sphere, shading, and black seams."""
    r = int(radius)
    # Shaded ball
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BASKETBALL_ORANGE, outline=BASKETBALL_SHADOW, width=1)
    # Black seam lines
    draw.line([cx - r, cy, cx + r, cy], fill=BASKETBALL_SEAMS, width=1)
    draw.line([cx, cy - r, cx, cy + r], fill=BASKETBALL_SEAMS, width=1)
    # Curved ribs
    draw.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], start=0, end=180, fill=BASKETBALL_SEAMS, width=1)
    draw.arc([cx - r // 2, cy - r, cx + r // 2, cy + r], start=90, end=270, fill=BASKETBALL_SEAMS, width=1)


def draw_basketball_player(draw, cx, cy, skill_type, height_px=55, jersey_color=(200, 30, 30)):
    """Draws an athlete figure performing a specific fundamental basketball skill."""
    skin_color = (195, 135, 95)
    short_color = (20, 30, 80)
    shoe_color = (240, 240, 245)

    head_r = int(height_px * 0.10)
    torso_h = int(height_px * 0.32)
    leg_h = int(height_px * 0.38)
    arm_l = int(height_px * 0.28)

    # 1. SHOOTING / JUMP SHOT (High vertical leap, arms extended overhead with ball)
    if skill_type in ["Shooting", "jump_shot"]:
        # Elevated off ground
        by = cy - int(height_px * 0.18)
        # Head
        draw.ellipse([cx - head_r, by - head_r * 2, cx + head_r, by], fill=skin_color)
        # Torso / Jersey
        draw.rectangle([cx - head_r - 2, by, cx + head_r + 2, by + torso_h], fill=jersey_color)
        # Arms extended high upward holding ball
        draw.line([cx - head_r, by + 4, cx - 2, by - head_r * 3], fill=skin_color, width=3)
        draw.line([cx + head_r, by + 4, cx + 4, by - head_r * 3], fill=skin_color, width=3)
        # Basketball at release apex above head
        draw_basketball(draw, cx + 2, by - head_r * 3 - 6, radius=7)
        # Legs extended down in air
        draw.line([cx - 4, by + torso_h, cx - 6, by + torso_h + leg_h], fill=short_color, width=4)
        draw.line([cx + 4, by + torso_h, cx + 4, by + torso_h + leg_h], fill=short_color, width=4)

    # 2. DRIBBLING / CROSSOVER (Low athletic stance, pounding ball to court)
    elif skill_type in ["Dribbling", "crossover"]:
        by = cy
        # Head
        draw.ellipse([cx - head_r, by - head_r * 2, cx + head_r, by], fill=skin_color)
        # Torso angled forward
        draw.rectangle([cx - head_r - 3, by, cx + head_r + 1, by + torso_h - 4], fill=jersey_color)
        # Low flexed legs (wide squat)
        draw.line([cx - 5, by + torso_h - 4, cx - 14, by + torso_h + leg_h - 8], fill=short_color, width=4)
        draw.line([cx + 3, by + torso_h - 4, cx + 12, by + torso_h + leg_h - 8], fill=short_color, width=4)
        # Left arm protective off-hand
        draw.line([cx - head_r, by + 4, cx - 18, by + 12], fill=skin_color, width=3)
        # Right arm pounding ball downward
        draw.line([cx + head_r, by + 4, cx + 16, by + torso_h], fill=skin_color, width=3)
        # Basketball near ground
        draw_basketball(draw, cx + 20, by + torso_h + 8, radius=7)

    # 3. LAY-UP / RIM FINISH (Driving knee high, one-handed finger roll towards hoop)
    elif skill_type in ["Lay-up", "layup"]:
        by = cy - int(height_px * 0.22)
        # Head
        draw.ellipse([cx - head_r, by - head_r * 2, cx + head_r, by], fill=skin_color)
        # Torso
        draw.rectangle([cx - head_r - 2, by, cx + head_r + 2, by + torso_h], fill=jersey_color)
        # Right arm high reaching for backboard with ball
        draw.line([cx + head_r, by + 4, cx + 12, by - head_r * 3], fill=skin_color, width=3)
        draw_basketball(draw, cx + 14, by - head_r * 3 - 6, radius=7)
        # Left arm for balance
        draw.line([cx - head_r, by + 6, cx - 12, by + 16], fill=skin_color, width=3)
        # Right knee driven high (90° flex)
        draw.line([cx + 3, by + torso_h, cx + 12, by + torso_h + 8], fill=short_color, width=4)
        draw.line([cx + 12, by + torso_h + 8, cx + 10, by + torso_h + 20], fill=skin_color, width=3)
        # Left leg trailing extended downward
        draw.line([cx - 4, by + torso_h, cx - 8, by + torso_h + leg_h], fill=short_color, width=4)

    # 4. REBOUNDING (Two hands high in air snatching ball)
    elif skill_type in ["Rebounding", "rebound"]:
        by = cy - int(height_px * 0.25)
        draw.ellipse([cx - head_r, by - head_r * 2, cx + head_r, by], fill=skin_color)
        draw.rectangle([cx - head_r - 3, by, cx + head_r + 3, by + torso_h], fill=jersey_color)
        # Both arms high overhead grabbing ball
        draw.line([cx - head_r, by + 4, cx - 6, by - head_r * 3], fill=skin_color, width=3)
        draw.line([cx + head_r, by + 4, cx + 6, by - head_r * 3], fill=skin_color, width=3)
        draw_basketball(draw, cx, by - head_r * 3 - 8, radius=8)
        # Legs splayed for balance in air
        draw.line([cx - 5, by + torso_h, cx - 12, by + torso_h + leg_h], fill=short_color, width=4)
        draw.line([cx + 5, by + torso_h, cx + 12, by + torso_h + leg_h], fill=short_color, width=4)

    # 5. DEFENDING (Wide lateral stance, arms outstretched contesting space)
    elif skill_type in ["Defending", "defense"]:
        by = cy
        draw.ellipse([cx - head_r, by - head_r * 2, cx + head_r, by], fill=skin_color)
        draw.rectangle([cx - head_r - 4, by, cx + head_r + 4, by + torso_h - 6], fill=jersey_color)
        # Both arms outstretched wide horizontally
        draw.line([cx - head_r - 4, by + 6, cx - 24, by + 2], fill=skin_color, width=3)
        draw.line([cx + head_r + 4, by + 6, cx + 24, by + 2], fill=skin_color, width=3)
        # Wide deep defensive slide stance
        draw.line([cx - 6, by + torso_h - 6, cx - 18, by + torso_h + leg_h - 10], fill=short_color, width=4)
        draw.line([cx + 6, by + torso_h - 6, cx + 18, by + torso_h + leg_h - 10], fill=short_color, width=4)

    # 6. PASSING (Two-hand chest pass extension forward)
    elif skill_type in ["Passing", "chest_pass"]:
        by = cy
        draw.ellipse([cx - head_r, by - head_r * 2, cx + head_r, by], fill=skin_color)
        draw.rectangle([cx - head_r - 2, by, cx + head_r + 2, by + torso_h], fill=jersey_color)
        # Forward step
        draw.line([cx - 4, by + torso_h, cx - 12, by + torso_h + leg_h], fill=short_color, width=4)
        draw.line([cx + 4, by + torso_h, cx + 14, by + torso_h + leg_h - 2], fill=short_color, width=4)
        # Arms pushed straight forward with ball departing
        draw.line([cx, by + 8, cx + 18, by + 6], fill=skin_color, width=3)
        draw_basketball(draw, cx + 28, by + 6, radius=7)

    # 7. STEALING (Lunging swipe at ball)
    elif skill_type in ["Stealing the ball", "steal"]:
        by = cy
        draw.ellipse([cx - head_r, by - head_r * 2, cx + head_r, by], fill=skin_color)
        draw.rectangle([cx - head_r - 3, by, cx + head_r + 1, by + torso_h - 4], fill=jersey_color)
        # Low lunge forward
        draw.line([cx - 4, by + torso_h - 4, cx - 16, by + torso_h + leg_h - 6], fill=short_color, width=4)
        draw.line([cx + 2, by + torso_h - 4, cx + 18, by + torso_h + leg_h - 8], fill=short_color, width=4)
        # Lunging reaching arm swiping downward
        draw.line([cx + head_r, by + 6, cx + 24, by + torso_h + 2], fill=skin_color, width=3)
        draw_basketball(draw, cx + 28, by + torso_h + 6, radius=6)

    # 8. FOOTWORK (Triple threat athletic base, ball tucked at hip)
    else:
        by = cy
        draw.ellipse([cx - head_r, by - head_r * 2, cx + head_r, by], fill=skin_color)
        draw.rectangle([cx - head_r - 2, by, cx + head_r + 2, by + torso_h], fill=jersey_color)
        # Plant foot + jab step
        draw.line([cx - 4, by + torso_h, cx - 6, by + torso_h + leg_h], fill=short_color, width=4)
        draw.line([cx + 4, by + torso_h, cx + 16, by + torso_h + leg_h - 4], fill=short_color, width=4)
        # Ball tucked tightly at right hip (triple threat)
        draw.line([cx + head_r, by + 6, cx + 12, by + torso_h - 2], fill=skin_color, width=3)
        draw_basketball(draw, cx + 12, by + torso_h - 2, radius=7)


def generate_rich_basketball_dataset(num_base_samples=50):
    """Generates diverse high-quality basketball images across all palettes and skills."""
    print(f">> Generating {num_base_samples} diverse Basketball base images...")

    skills = [
        "Dribbling", "Passing", "Shooting", "Lay-up",
        "Rebounding", "Defending", "Stealing the ball", "Footwork"
    ]

    jersey_colors = [
        (220, 40, 40),   # Red
        (30, 60, 180),   # Navy/Blue
        (240, 200, 20),  # Yellow/Gold
        (255, 255, 255), # White
        (30, 30, 30),    # Black
        (20, 140, 70),   # Green
        (130, 40, 160)   # Purple
    ]

    generated_paths = []
    w, h = 160, 160

    for i in range(1, num_base_samples + 1):
        palette = COURT_PALETTES[(i - 1) % len(COURT_PALETTES)]
        skill = skills[(i - 1) % len(skills)]
        jersey = jersey_colors[(i - 1) % len(jersey_colors)]

        img = Image.new("RGB", (w, h), palette["apron"])
        draw = ImageDraw.Draw(img)

        # 1. Draw Court Flooring and Boundary Lines
        draw_basketball_court(draw, w, h, palette)

        # 2. Add Basketball Hoop at top or side
        if (i % 2) == 1:
            hoop_x = int(w * 0.20) if (i % 4 == 1) else int(w * 0.50)
            hoop_y = int(h * 0.08)
            draw_basketball_hoop(draw, w, h, hoop_x, hoop_y, scale=random.uniform(0.85, 1.15))

        # 3. Draw Player performing the fundamental skill
        player_x = int(w * random.uniform(0.40, 0.65))
        player_y = int(h * random.uniform(0.48, 0.68))
        draw_basketball_player(draw, player_x, player_y, skill, height_px=random.randint(52, 65), jersey_color=jersey)

        # 4. Add subtle photographic noise / blur
        if random.random() > 0.4:
            img = img.filter(ImageFilter.SMOOTH_MORE)

        # Save to dataset/Basketball with clear naming
        filename = f"BA_rich_{i:03d}.png"
        out_path = os.path.join(DATASET_BASKETBALL_DIR, filename)
        img.save(out_path, "PNG")
        generated_paths.append(out_path)

    print(f" [+] Generated {len(generated_paths)} diverse Basketball training images in {DATASET_BASKETBALL_DIR}")
    return generated_paths


if __name__ == "__main__":
    generate_rich_basketball_dataset(50)
