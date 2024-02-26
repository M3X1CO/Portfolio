import pygame
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

WINDOW_SIZE = (400, 400)
FONT_SIZE = 24
BORDER_SIZE = 50
FONT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

pygame.init()

font = ImageFont.truetype("arial.ttf", FONT_SIZE)
text = "Hello World"
text_width, text_height = font.getsize(text)

border_radius = math.ceil(max(text_width, text_height) / 2) + BORDER_SIZE

circle_mask = Image.new("L", (border_radius * 2, border_radius * 2), 0)
ImageDraw.Draw(circle_mask).ellipse((0, 0, border_radius * 2, border_radius * 2), fill=255)

circle_mask = np.array(circle_mask)
circle_mask = np.dstack([circle_mask] * 3)

circle_image = Image.new("RGBA", (border_radius * 2, border_radius * 2), 0)
ImageDraw.Draw(circle_image).text((border_radius - text_width // 2, border_radius - text_height // 2), text, font=font, fill=FONT_COLOR)

circle_image = np.array(circle_image)

circle_image[:, :, 3] = circle_mask[:, :, 0]

circle_image = Image.fromarray(circle_image)

circle_mask = circle_image.convert("L")
circle_mask = np.array(circle_mask)
circle_mask = np.dstack([circle_mask] * 3)

circle_image = np.array(circle_image)

window_surface = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Pygame Font Circle")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window_surface.fill(BACKGROUND_COLOR)

    window_surface.set_clip(pygame.draw.circle(window_surface, (255, 255, 255), (border_radius, border_radius), border_radius, 0))

    window_surface.blit(pygame.surfarray.make_surface(circle_image), (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    pygame.display.update()
