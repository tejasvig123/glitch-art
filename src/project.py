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

    