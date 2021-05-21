import sys
import pygame
from bullet import Bullet


def check_keydown_event(event, ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:  # 检测到是向右的键
        ship.moving_right = True
    if event.key == pygame.K_LEFT:  # 检测到是向左的键
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹并将其加入到编组bullets
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:  # 检测到是向右的键
        ship.moving_right = False
    if event.key == pygame.K_LEFT:  # 检测到是向左的键
        ship.moving_left = False


def check_events(ai_setting, screen, ship, bullets):
    # 监视键盘和鼠标状态
    for event in pygame.event.get():
        # 如果单击关闭按钮，退出游戏
        if event.type == pygame.QUIT:
            # 退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 响应按键
            check_keydown_event(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:  # 响应松开
            check_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship, back_ground_image, bullets):
    """更新屏幕上的图像，并切换到新图像"""
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 缓冲区中绘制图像
    screen.blit(back_ground_image, (0, 0))
    # 在飞船和外星人后面重新绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
