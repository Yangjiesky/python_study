'''
表白小程序
'''
import sys
import settings as st
import os
import pygame
from tkinter import Tk, messagebox
import text_show as ts
from button import Button

def main():
	# 初始化屏幕对象
	pygame.init()
	screen = pygame.display.set_mode(st.screen_size, 0, 32)
	#pygame.display.set_icon(pygame.image.load(st.bg_pic_path))
	pygame.display.set_caption('To my dearest one.')
	#pygame.display.set_caption('来自一位小哥哥的')

	# 背景音乐
	pygame.mixer.music.load(st.bgm_path)
	pygame.mixer.music.play(-1, 25.0)

	# 背景图片
	bg_pic = pygame.image.load(st.bg_pic_path)
	# (平滑缩放任意大小)
	# bg_pic = pygame.transform.smoothscale(bg_pic, (680, 453))
	# 实例两个按钮
	button_yes = Button(x=40, y=st.screen_size[1]-80, width=120, height=40, text='好呀',
						fontpath=st.font_path, fontsize=25, fontcolor=st.black, edgecolor=st.skyblue, edgesize=2,
						bgcolors=[st.darkgray, st.gainsboro], is_want_to_select=True, screensize=st.screen_size)
	button_no = Button(x=st.screen_size[0]-160, y=st.screen_size[1] - 80, width=120, height=40, text='算了吧',
						fontpath=st.font_path, fontsize=25, fontcolor=st.black, edgecolor=st.skyblue, edgesize=2,
						bgcolors=[st.darkgray, st.gainsboro], is_want_to_select=False, screensize=st.screen_size)
	# 程序主循环
	while True:
		# 背景图片
		# screen.fill(st.bg_color)
		screen.blit(bg_pic, (0, 0))
		is_agree = False

		# 监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				# 没有点击好呀按钮之前不许退出程序
				if is_agree:
					pygame.quit()
					sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button:
				if button_yes.rect.collidepoint(pygame.mouse.get_pos()):
					button_yes.is_selected = True
					root = Tk()
					root.withdraw()
					messagebox.showinfo('', '❤❤❤么么哒❤❤❤')
					root.destroy()
					is_agree = True

		# 显示文字
		ts.text_show(screen=screen, text='我观察你很久了,做我女朋友好不好？', position=(40, 50),
					font_path=st.font_path, font_size=25, font_color=st.black, is_bold=False)
		#显示按钮
		button_yes.draw(screen, pygame.mouse.get_pos())
		button_no.draw(screen, pygame.mouse.get_pos())
		# 每次循环时都重绘屏幕
		# screen.fill(st.bg_color)
		# # 让最近绘制的屏幕可见
		pygame.display.update()

if __name__ == '__main__':
	main()
