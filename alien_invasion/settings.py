'''
每次给游戏添加新功能时，通常将引入一些新设置，将所有设置存储在一个地方，让函数调用更简单
'''
class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width=800
        self.screen_height=400
        self.bg_color=(230,230,230)