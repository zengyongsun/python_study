import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, settings, screen):
        """初始化外星人并设置初始位置"""
        super().__init__()
        self.settings = settings
        self.screen = screen

        # 加载外星人图像，并设置 rect
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # 每个外星人的初始位置都是左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置画外星人"""
        self.screen.blit(self.image, self.rect)
