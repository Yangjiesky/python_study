import pygame
import random

# 创建一个按钮的类
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text, fontpath, fontsize, fontcolor, bgcolors, edgecolor, edgesize=1,
                 is_want_to_select=True, screensize=None, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(fontpath, fontsize)
        self.fontcolor = fontcolor
        self.bgcolors = bgcolors
        self.edgecolor = edgecolor
        self.edgesize = edgesize
        self.is_want_to_select = is_want_to_select
        self.screensize = screensize

    # 根据各种情况将按钮绑定到屏幕
    def draw(self, screen, mouse_pos):
        # 鼠标在按钮范围内
        if self.rect.collidepoint(mouse_pos):
            if not self.is_want_to_select:
                while self.rect.collidepoint(mouse_pos):
                    self.rect.left = random.randint(0, self.screensize[0]-self.rect.width)
                    self.rect.top = random.randint(0, self.screensize[1] - self.rect.height)
            pygame.draw.rect(screen, self.bgcolors[0], self.rect, 0)
            pygame.draw.rect(screen, self.edgecolor, self.rect, self.edgesize)

        else:
            pygame.draw.rect(screen, self.bgcolors[0], self.rect, 0)
            pygame.draw.rect(screen, self.edgecolor, self.rect, self.edgesize)

        text_render = self.font.render(self.text, True, self.fontcolor)
        fontsize = self.font.size(self.text)
        screen.blit(text_render, (self.rect.x+(self.rect.width-fontsize[0])/2,
                                  self.rect.y+(self.rect.height-fontsize[1]/2)))

