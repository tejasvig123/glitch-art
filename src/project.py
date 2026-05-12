import pygame
from PIL import Image
import sys
import random
import os

class GlitchSynthesizer:
    def __init__(self, image_path):
        pygame.init()
        
        # Navigate up one directory since project.py is in /src/
        # but test.jpg is in the root directory.
        root_dir = os.path.dirname(os.path.dirname(__file__))
        full_image_path = os.path.join(root_dir, image_path)

        try:
            self.master_image = Image.open(full_image_path).convert("RGB")
        except FileNotFoundError:
            print(f"CRITICAL ERROR: Could not find '{image_path}' in the root folder.")
            sys.exit()

        # scale down if image is too large
        width, height = self.master_image.size
        if width > 1200 or height > 800:
            self.master_image.thumbnail((1200, 800))
            width, height = self.master_image.size

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Algorithmic Glitch Synthesizer")
        self.font = pygame.font.SysFont("Courier", 24, bold=True)

    def apply_rgb_shift(self, image, offset_x):
        """Class Method 1: Shifts the red color channel."""
        if offset_x == 0:
            return image.copy()
            
        r, g, b = image.split()
        r_shifted = Image.new("L", r.size)
        r_shifted.paste(r, (offset_x, 0))
        
        return Image.merge("RGB", (r_shifted, g, b))

    def apply_datamosh(self, image, intensity):
        """Class Method 2: Creates block displacements."""
        if intensity <= 0:
            return image.copy()
            
        glitched = image.copy()
        for _ in range(intensity):
            box_w = random.randint(10, max(20, self.width // 10))
            box_h = random.randint(10, max(20, self.height // 10))
            x1 = random.randint(0, self.width - box_w)
            y1 = random.randint(0, self.height - box_h)
            
            region = glitched.crop((x1, y1, x1 + box_w, y1 + box_h))
            
            offset_x = random.randint(-20, 20)
            offset_y = random.randint(-20, 20)
            
            glitched.paste(region, (x1 + offset_x, y1 + offset_y))
            
        return glitched

    