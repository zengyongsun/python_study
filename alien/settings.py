class Settings():
    """
    存储《外星人入侵》的所有配置信息
    """

    def __init__(self):
        """
        初始化游戏设置
        """
        # 屏幕尺寸
        self.screen_width = 1024
        self.screen_height = 780
        self.bg_color = (230, 230, 230)

        # 飞船的速度
        self.ship_speed_factor = 1

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_with = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3

