'''
创建一个game_functions模块，将存储大量让游戏《外星人入侵》运行的函数。
通过创建模块game_functions,可避免alien_invasion.py太长，并使其逻辑更容易理解。
'''

#将管理事件的代码移到一个名为check_events()的函数中，以简化run_game()并隔离事件管理循环。
#通过隔离事件循环，可将事件管理与游戏的其他方面（如更新屏幕）分离。

import  sys
import  pygame

def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #响应按键
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PRINT:
                #向右移动飞船
                ship.rect.centerx += 1

def update_screen(ai_settings,screen,ship):
    '''更新屏幕上的图像，并切换到新屏幕'''
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    #在指定位置绘制飞船
    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()