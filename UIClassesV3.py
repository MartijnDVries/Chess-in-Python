"\Banda Niera-Medium.ttf"
"\TobagoPoster.ttf"

import pygame
from tkinter import *
from tkinter import messagebox
import os



Tk().wm_withdraw()


class Button:
    path = r"C:\Users\Martijn\AppData\Local\Programs\Python\Python39\Scripts\pygame-1.9.6"

    def __init__(self, x, y, width, height, btn_color, click_btn_color, fin_btn_color=None, border_radius=5,
                 font="Arial", font_size=24, text='', textcolor=(0, 0, 0)):
        """Class to create buttons with different aspects of this button"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont(font, font_size)
        self.text = text
        self.textcolor = textcolor
        self.border_radius = border_radius
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.btn_color = btn_color
        self.click_btn_color = click_btn_color
        self.fin_btn_color = fin_btn_color
        if not fin_btn_color:
            self.fin_btn_color = self.btn_color

    def draw_button(self, surface):
        """when all info is collected in init method draw button on the screen, also blit text in center of button"""
        self.surface = surface
        pygame.draw.rect(self.surface, self.fin_btn_color, self.rect, border_radius=self.border_radius)
        text_surf = self.font.render(self.text, True, self.textcolor)
        self.surface.blit(text_surf, (self.x + (self.width / 2 - text_surf.get_width() / 2), self.y + (self.height / 2 - text_surf.get_height() / 2)))


    def button_clicked(self, status):
        """function call when button is clicked. It changes te color of the button"""
        self.status = status
        if self.status == "ON":
            self.fin_btn_color = self.click_btn_color
            return self.status
        elif self.status == "OFF":
            self.fin_btn_color = self.btn_color
            return self.status


class Text:
    path = r"C:\Users\Martijn\AppData\Local\Programs\Python\Python39\Scripts\pygame-1.9.6"

    def __init__(self, text, x, y, font="Arial", font_size=24, font_color=(0, 0, 0), underline="False"):
        """Create text without placing it in a button"""
        self.text = text
        self.x = x
        self.y = y
        self.font_size = font_size
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
        self.underline = underline
        self.text_surf = self.font.render(text, True, font_color)


    def draw_text(self, surface):
        """draw text on screen"""
        self.surface = surface
        self.surface.blit(self.text_surf, (self.x, self.y))
        if self.underline == "True":
            pygame.draw.line(self.surface, self.font_color, (self.x, self.y+self.text_surf.get_height()), (self.x+self.text_surf.get_width(), self.y+self.text_surf.get_height()), width=4)


class Image:
    def __init__(self, x, y, width, height, image_file, clickimage_file=None, fin_image=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image_file = image_file
        cwd =  os.getcwd()
        path = cwd+"/Images"
        self.image_surf = pygame.Surface((self.width, self.height))
        self.imageload = pygame.image.load(path+self.image_file)
        self.imageload = pygame.transform.scale(self.imageload, (self.width, self.height))
        self.fin_image = fin_image
        self.rect = self.image_surf.get_rect(topleft=(self.x, self.y))
        self.clickimage_file = clickimage_file
        self.active = False
        if not self.clickimage_file:
            self.fin_image = self.imageload
        else:
            self.clickimage = pygame.image.load(path + self.clickimage_file)
            self.clickimage = pygame.transform.scale(self.clickimage, (self.width, self.height))
            self.image_click(status="OFF")


    def draw_image(self, surface):
        self.surface = surface
        self.surface.blit(self.fin_image, self.rect)

    def image_click(self, status):
        """change image (color) when selected"""
        self.status = status
        if self.status == "OFF":
            self.fin_image = self.imageload

        elif self.status == "ON":
            self.fin_image = self.clickimage


class Entry:
    def __init__(self, x, y, width, height, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.active = False
        self.entry_surf = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.SysFont("Arial", 20)
        self.text_surf = self.font.render(self.text, True, (0,0,0))
        self.text_rect = self.text_surf.get_rect(topleft=(self.x, self.y))

    def text_entry(self, event, text):
        self.text = text

        if event.type == pygame.KEYDOWN:
             if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key != pygame.K_1\
                    and event.key != pygame.K_2 \
                    and event.key != pygame.K_3 \
                    and event.key != pygame.K_4 \
                    and event.key != pygame.K_5 \
                    and event.key != pygame.K_6 \
                    and event.key != pygame.K_7 \
                    and event.key != pygame.K_8 \
                    and event.key != pygame.K_9 \
                    and event.key != pygame.K_0:
                    messagebox.showwarning("Error", "Please enter a number")
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                if len(self.text) > 2:
                    self.text = self.text[:-1]
                if self.text != '':
                    if int(str(self.text)) > 60:
                        messagebox.showwarning("Error", "Can't go higher than 60")
                        self.text = ''

        self.text_surf = self.font.render(self.text, True, (0, 0, 0))

    def draw_entry(self, surface):
        self.surface = surface
        self.surface.blit(self.entry_surf, self.rect)
        self.entry_surf.fill((255,255,255))
        self.surface.blit(self.text_surf, (self.x + 5, self.y + 5))







