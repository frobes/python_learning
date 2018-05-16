'''
Ship类负责管理飞船的大部分行为
'''

import  pygame

class Ship():

    def __init__(self,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')  #pygame.image.load()函数返回一个表示飞船的surface
        #处理矩形(rect对象)一样处理游戏元素
        #处理rect对象时，可使用矩形四角和中心的x和y坐标，设置这些值来指定矩形位置
        self.rect = self.image.get_rect()
        #将屏幕的矩形存储在self.screen_rect
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        #要将游戏对象居中，可设置相应rect对象的属性center、centerx或centery
        #要将游戏元素与屏幕边缘对齐，可使用属性top、bottom、left或right
        #调整游戏元素的水平或垂直位置，可使用属性x和y,分别是相应矩形左上角的x和y坐标
        self.rect.centerx = self.screen_rect.centerx #将self.rect.centerx(飞船中心的x坐标)设置为表示屏幕的矩形的属性centerx
        self.rect.bottom = self.screen_rect.bottom  #将self.rect.bottom(飞船下边缘的y坐标)设置为表示屏幕的矩形的属性bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect) #根据self.rect指定的位置将图像绘制到屏幕上

