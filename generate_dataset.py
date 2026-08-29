#!/usr/bin/env python3
"""
ApexScout AI - Dataset Expansion & Biomechanical Augmentation Engine
Expands the raw dataset in dataset/ from 90 images to 600+ diverse training samples
with multi-angle camera perspectives, motion blur, lighting variance, and horizontal mirroring.
"""

import os
import glob
import json
import random
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

DATASET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset")
TARGET_SAMPLES_PER_SPORT = 100

SPORTS_CATEGORIES = [
    "Athletics",
    "Basketball",
    "Cricket",
    "Kabaddi",
    "Soccer",
    "Volleyball"
]

def augment_image(image, seed_idx):
    """
    Apply realistic biomechanical and photographic augmentations.
    """
    img = image.copy()
    np.random.seed(seed_idx)
    random.seed(seed_idx)
    
    # 1. Random Horizontal Flip (simulates left/right dominant athletes)
    if random.random() > 0.4:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        
    # 2. Random Subtle Rotation (simulates camera tilt at combine)
    angle = random.uniform(-18.0, 18.0)
    img = img.rotate(angle, resample=Image.BICUBIC, expand=False, fillcolor=(0, 0, 0))
    
    # 3. Random Lighting / Brightness (indoor hall vs outdoor sunlight)
    brightness_factor = random.uniform(0.75, 1.30)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness_factor)
    
    # 4. Random Contrast Adjustment
    contrast_factor = random.uniform(0.80, 1.25)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast_factor)
    
    # 5. Random Color Saturation
    color_factor = random.uniform(0.85, 1.30)
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(color_factor)
    
    # 6. Random Motion Blur or Sharpness
    blur_choice = random.random()
    if blur_choice > 0.65:
        img = img.filter(ImageFilter.GaussianBlur(radius=random.uniform(0.4, 1.0)))
    elif blur_choice < 0.25:
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(random.uniform(1.2, 1.8))
        
    # 7. Random Zoom Crop (distance variations from camera)
    if random.random() > 0.5:
        w, h = img.size
        crop_pct = random.uniform(0.88, 0.98)
        new_w, new_h = int(w * crop_pct), int(h * crop_pct)
        left = random.randint(0, w - new_w)
        top = random.randint(0, h - new_h)
        img = img.crop((left, top, left + new_w, top + new_h))
        img = img.resize((w, h), resample=Image.BICUBIC)
        
    return img

import sys

# Ensure UTF-8 output encoding on Windows stdout
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def expand_all_sports():
    print("=" * 65)
    print(" [ApexScout AI] - Sports Dataset Expansion & Augmentation")
    print("=" * 65)
    
    dataset_summary = {}
    total_images_generated = 0
    
    for sport in SPORTS_CATEGORIES:
        sport_dir = os.path.join(DATASET_DIR, sport)
        os.makedirs(sport_dir, exist_ok=True)
        
        # Find original base images (those without _aug_)
        all_files = glob.glob(os.path.join(sport_dir, "*.png"))
        base_files = [f for f in all_files if "_aug_" not in os.path.basename(f)]
        
        if not base_files:
            print(f"[!] No base files found in {sport}, searching all images...")
            base_files = all_files
            
        print(f"\n>> Processing sport: [{sport}] | Base images: {len(base_files)}")
        
        if not base_files:
            print(f"[X] Skipping {sport} (empty directory)")
            continue
            
        current_count = len(base_files)
        aug_index = 1
        
        # Generate augmented images until TARGET_SAMPLES_PER_SPORT is reached
        while current_count < TARGET_SAMPLES_PER_SPORT:
            # Pick a base image in round-robin fashion
            base_file = base_files[(aug_index - 1) % len(base_files)]
            try:
                with Image.open(base_file) as img:
                    img_rgb = img.convert("RGB")
                    aug_img = augment_image(img_rgb, seed_idx=(hash(sport) + aug_index) % 100000)
                    
                    # Save augmented file
                    out_filename = f"{sport[:2].upper()}_aug_{aug_index:03d}.png"
                    out_path = os.path.join(sport_dir, out_filename)
                    aug_img.save(out_path, "PNG")
                    
                    current_count += 1
                    aug_index += 1
                    total_images_generated += 1
            except Exception as e:
                print(f"  Error augmenting {base_file}: {e}")
                aug_index += 1
                
        final_files = glob.glob(os.path.join(sport_dir, "*.png"))
        dataset_summary[sport] = {
            "base_samples": len(base_files),
            "augmented_samples": len(final_files) - len(base_files),
            "total_samples": len(final_files)
        }
        print(f"  [+] {sport}: Expanded from {len(base_files)} to {len(final_files)} training samples.")
        
    # Write dataset index manifest
    manifest_path = os.path.join(DATASET_DIR, "dataset_index.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump({
            "dataset_name": "ApexScout Augmented Multi-Sport Training Dataset",
            "version": "3.0.0",
            "total_sports": len(SPORTS_CATEGORIES),
            "total_samples": sum(s["total_samples"] for s in dataset_summary.values()),
            "sports_breakdown": dataset_summary
        }, f, indent=2)
        
    print("\n" + "=" * 65)
    print(" [DONE] DATASET EXPANSION COMPLETE!")
    print(f" Total Samples in Dataset: {sum(s['total_samples'] for s in dataset_summary.values())}")
    print(f" Manifest saved to: {manifest_path}")
    print("=" * 65)

if __name__ == "__main__":
    expand_all_sports()
