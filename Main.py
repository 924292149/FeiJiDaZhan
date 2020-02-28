import pygame # 导入pygame模块
pygame.init() # 初始化pygame模块
screen = pygame.display.set_mode((480,700)) # 设置屏幕尺寸
bg = pygame.image.load("./images/background.png") # 加载背景图像
hero = pygame.image.load("./images/me1.png") # 加载飞机图像
heroRect = pygame.Rect(180,480,102,126) # 飞机矩形的坐标信息初始化
clock = pygame.time.Clock() # 生成刷新时钟对象
while True: # 游戏循环
    clock.tick(30) # 刷新率设置为60
    heroRect.y -=10 # 英雄的移动速度 1
    screen.blit(bg, (0, 0)) # 打印背景
    screen.blit(hero,heroRect) # 打印飞机
    pygame.display.update() # 刷新屏幕
    if heroRect.y +126 <0: # 如果移出屏幕,则从下方出现
        heroRect.y = 700
    eventList = pygame.event.get()
    if len(eventList) > 0 :
        print(eventList)
    for event in pygame.event.get(): # 监听事件
        if event.type == pygame.QUIT: # 用户按下退出键
            print("退出游戏……")
            pygame.quit() # 退出游戏
            exit()
        if event.type == pygame.
