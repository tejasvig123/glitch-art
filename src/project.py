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

    def apply_pixel_sort(self, image, num_strips=15):
        glitched = image.copy()
        for _ in range(num_strips):
            y = random.randint(0, self.height - 1)
            x_start = random.randint(0, self.width // 2)
            length = random.randint(50, self.width // 2)
            x_end = min(x_start + length, self.width)
            
            box = (x_start, y, x_end, y + 1)
            strip = glitched.crop(box)
            pixels = list(strip.getdata())
            
            # Sort by brightness
            pixels.sort(key=lambda p: 0.299*p[0] + 0.587*p[1] + 0.114*p[2])
            
            strip.putdata(pixels)
            glitched.paste(strip, box)
            
        return glitched

    def pil_to_pygame(self, pil_image):
        mode = pil_image.mode
        size = pil_image.size
        data = pil_image.tobytes()
        return pygame.image.frombuffer(data, size, mode)

    def run(self):
        rgb_offset = 0
        mosh_intensity = 0
        needs_update = True
        
        base_image = self.master_image.copy() 
        current_image = base_image.copy()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        rgb_offset += 5
                        needs_update = True
                    elif event.key == pygame.K_LEFT:
                        rgb_offset -= 5
                        needs_update = True
                    elif event.key == pygame.K_UP:
                        mosh_intensity += 5
                        needs_update = True
                    elif event.key == pygame.K_DOWN:
                        mosh_intensity = max(0, mosh_intensity - 5)
                        needs_update = True
                    elif event.key == pygame.K_SPACE:
                        base_image = self.apply_pixel_sort(base_image, num_strips=25)
                        needs_update = True
                    elif event.key == pygame.K_r:
                        rgb_offset = 0
                        mosh_intensity = 0
                        base_image = self.master_image.copy()
                        needs_update = True
                    elif event.key == pygame.K_s:
                        save_name = f"glitch_export_{random.randint(1000,9999)}.png"
                        # Save to root folder
                        root_dir = os.path.dirname(os.path.dirname(__file__))
                        save_path = os.path.join(root_dir, save_name)
                        current_image.save(save_path)
                        print(f"SUCCESS: Saved as '{save_name}' in the root folder!")

            if needs_update:
                current_image = self.apply_rgb_shift(base_image, rgb_offset)
                current_image = self.apply_datamosh(current_image, mosh_intensity)
                
                pg_surface = self.pil_to_pygame(current_image)
                self.screen.blit(pg_surface, (0, 0))
                
                ui_text = f"RGB:{rgb_offset} | MOSH:{mosh_intensity} | SORT(SPACE) | [R]ESET | [S]AVE"
                text_shadow = self.font.render(ui_text, True, (0, 0, 0))
                text_surface = self.font.render(ui_text, True, (0, 255, 150))
                
                overlay = pygame.Surface((self.width, 40))
                overlay.set_alpha(150)
                overlay.fill((0, 0, 0))
                self.screen.blit(overlay, (0, 0))
                
                self.screen.blit(text_shadow, (12, 10))
                self.screen.blit(text_surface, (10, 8))
                
                pygame.display.flip()
                needs_update = False

        pygame.quit()


def main():
    app = GlitchSynthesizer("test.jpg")
    app.run()


if __name__ == "__main__":
    main()
