'''
import sys
import pygame

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    #创建一个名为screen的显示窗口（实参（1200,800）是一个元组，指定游戏窗口尺寸，将尺寸值传给pygame.display.set_mode()）
    #对象screen是一个surface
    screen=pygame.display.set_mode((1200,800))
    #pygame窗口名字
    pygame.display.set_caption("Alien Invasion")

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        #使用方法pygame.event.get()访问pygame检测到的事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #让最近绘制的屏幕可见
        #每次执行while循环都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见。在移动游戏元素时，pygame.display.flip()将不断更新屏幕，
        #以显示元素的新位置，并在原来的位置隐鲹元素，从而营造平滑移动的效果。
        pygame.display.flip()

#初始化游戏并开始主循环
run_game()


##第二种方法
#设置背景色

import sys
import pygame

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    #创建一个名为screen的显示窗口（实参（1200,800）是一个元组，指定游戏窗口尺寸，将尺寸值传给pygame.display.set_mode()）
    #对象screen是一个surface
    screen=pygame.display.set_mode((1200,800))
    #pygame窗口名字
    pygame.display.set_caption("Alien Invasion")

    #设置背景色
    #(255,0,0)表示红色，(0,255,0)表示绿色，(0,0,255)表示蓝色
    bg_color=(230,230,230)

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        #使用方法pygame.event.get()访问pygame检测到的事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #每次循环时都重绘屏幕
        screen.fill(bg_color)

        #让最近绘制的屏幕可见
        #每次执行while循环都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见。在移动游戏元素时，pygame.display.flip()将不断更新屏幕，
        #以显示元素的新位置，并在原来的位置隐鲹元素，从而营造平滑移动的效果。
        pygame.display.flip()

#初始化游戏并开始主循环
run_game()




##第三种方法
#设置背景色

import sys
import pygame
from settings import  Settings

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings=Settings()

    #创建一个名为screen的显示窗口（实参（1200,800）是一个元组，指定游戏窗口尺寸，将尺寸值传给pygame.display.set_mode()）
    #对象screen是一个surface
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #pygame窗口名字
    pygame.display.set_caption("Alien Invasion")

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        #使用方法pygame.event.get()访问pygame检测到的事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)

        #让最近绘制的屏幕可见
        #每次执行while循环都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见。在移动游戏元素时，pygame.display.flip()将不断更新屏幕，
        #以显示元素的新位置，并在原来的位置隐鲹元素，从而营造平滑移动的效果。
        pygame.display.flip()

#初始化游戏并开始主循环
run_game()



##第四种方法
#在屏幕上绘制飞船

import sys
import pygame
from settings import  Settings
from ship import Ship

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings=Settings()

    #创建一个名为screen的显示窗口（实参（1200,800）是一个元组，指定游戏窗口尺寸，将尺寸值传给pygame.display.set_mode()）
    #对象screen是一个surface
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #pygame窗口名字
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    #必须在主while循环前面创建该实例，以免每次循环时都创建一艘飞船
    ship = Ship(screen)

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        #使用方法pygame.event.get()访问pygame检测到的事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)

        #在指定位置绘制飞船
        ship.blitme()

        #让最近绘制的屏幕可见
        #每次执行while循环都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见。在移动游戏元素时，pygame.display.flip()将不断更新屏幕，
        #以显示元素的新位置，并在原来的位置隐鲹元素，从而营造平滑移动的效果。
        pygame.display.flip()

#初始化游戏并开始主循环
run_game()
'''


##第5种方法
#重构：模块game_functions

import sys
import pygame
from settings import  Settings
from ship import Ship
import  game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()

    #创建一个名为screen的显示窗口（实参（1200,800）是一个元组，指定游戏窗口尺寸，将尺寸值传给pygame.display.set_mode()）
    #对象screen是一个surface
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #pygame窗口名字
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    #必须在主while循环前面创建该实例，以免每次循环时都创建一艘飞船
    ship = Ship(screen)

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        #使用方法pygame.event.get()访问pygame检测到的事件
        gf.check_events(ship)

        #每次循环时都重绘屏幕
        #在指定位置绘制飞船
        #让最近绘制的屏幕可见
        #每次执行while循环都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见。在移动游戏元素时，pygame.display.flip()将不断更新屏幕，
        #以显示元素的新位置，并在原来的位置隐鲹元素，从而营造平滑移动的效果。
        gf.update_screen(ai_settings,screen,ship)

#初始化游戏并开始主循环
run_game()