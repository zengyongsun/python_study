import pygame
from alien.settings import Settings
from alien.ship import Ship
import alien.game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((
        settings.screen_width,settings.screen_height
    ))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(settings,screen)

    # 开始游戏的主循环
    while True:
        # 监听键和鼠标事件
        gf.check_events(ship)

        ship.update()

        gf.update_screen(settings,screen,ship)

run_game()
