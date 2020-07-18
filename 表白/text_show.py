'''文字显示'''
import pygame
def text_show(screen, text, position, font_path, font_size, font_color, is_bold=False):
	font = pygame.font.Font(font_path, font_size)
	font.set_bold(is_bold)
	text_render = font.render(text, True, font_color)
	screen.blit(text_render, position)