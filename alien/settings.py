class Settings():
    """
    存储《外星人入侵》的所有配置信息
    """

    def __init__(self):
        """
        初始化游戏设置
        """
        # 屏幕尺寸
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的速度
        self.ship_speed_factor = 1
