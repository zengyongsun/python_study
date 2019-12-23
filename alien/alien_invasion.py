import pygame
from alien.settings import Settings
from alien.ship import Ship
from alien.alien_cl import Alien
import alien.game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((
        settings.screen_width, settings.screen_height
    ))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(settings, screen)

    # 外星人编组
    aliens = Group()

    create_fleet(settings,screen,aliens)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        # 监听键和鼠标事件
        gf.check_events(settings, screen, ship, bullets)

        ship.update()

        gf.update_bullets(bullets)

        gf.update_screen(settings, screen, ship, aliens, bullets)


def create_fleet(settings, screen, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可以容纳多少这样个外星人
    # 外星人的间距为一个外星人的宽度

    alien = Alien(settings, screen)
    alien_width = alien.rect.width

    alien_space_x = settings.screen_width - (2 * alien_width)
    number_alien_x = int(alien_space_x / (2*alien_width))

    # 创建第一行外星人
    for alien_number in range(number_alien_x):
        # 创建一个外星人，并加入当前行
        alien = Alien(settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


run_game()
