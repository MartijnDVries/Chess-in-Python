import pygame
from UIClassesV3 import Button, Text, Image, Entry
import time
import os
import threading
import json
import ctypes
from ctypes import windll
import sys

def main():

    x = 275
    y = 75
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("ChessPy Main Menu")
    screen.fill((255, 255, 255))
    # create buttons
    btn_1 = Button(100, 100, 200, 75, btn_color=(222, 80, 80), click_btn_color=(233, 82, 162))
    btn_2 = Button(100, 200, 200, 75, btn_color=(222, 80, 80), click_btn_color=(233, 82, 162))
    btn_3 = Button(505, 350, 325, 200, btn_color=(46, 200, 20), click_btn_color=(100, 100, 100), text="Start", font_size=50, border_radius=10)
    btn_4 = Button(477, 100, 94, 47, btn_color=(222, 80, 80), click_btn_color=(233, 82, 162), text="15|10", font_size=24)
    btn_5 = Button(618, 100, 94, 47, btn_color=(222, 80, 80), click_btn_color=(233, 82, 162), text="5|5", font_size=24)
    btn_6 = Button(759, 100, 94, 47, btn_color=(222, 80, 80), click_btn_color=(233, 82, 162), text="3|2", font_size=24)

    # create a button list for easy drawing
    button_list = []
    button_list.append(btn_1)
    button_list.append(btn_2)
    button_list.append(btn_3)
    button_list.append(btn_4)
    button_list.append(btn_5)
    button_list.append(btn_6)

    # set button state for switching buttons
    for button in button_list:
        button.status = "OFF"

    # Set text
    # mode block
    text_mode = Text("Mode", 75, 30, font_size=42, underline="True")
    Player_text = Text("Player", 110, 105, font_size=24)
    vs_text = Text("vs.", 180, 125, font_size=24)
    player_text = Text("player", 225, 145, font_size=24)
    Player2_text = Text("Player", 110, 205, font_size=24)
    vs2_text = Text("vs.", 180, 225, font_size=24)
    computer_text = Text("computer", 205, 245, font_size=24)
    # color block
    text_color = Text("Color", 75, 330, font_size=42, underline="True")
    text_time_control = Text("Time-control", 505, 30, font_size=42, underline="True")
    # time-control block
    hour_text = Text("Hour", 477, 180, font_size=16)
    min_text = Text("Min.", 577, 180, font_size=16)
    sec_text = Text("Sec.", 677, 180, font_size=16)
    incr_text = Text("Increment (sec.)", 777, 180, font_size=16)

    text_list = []
    text_list.append(text_mode)
    text_list.append(Player_text)
    text_list.append(vs_text)
    text_list.append(player_text)
    text_list.append(Player2_text)
    text_list.append(vs2_text)
    text_list.append(computer_text)
    text_list.append(text_color)
    text_list.append(text_time_control)
    text_list.append(hour_text)
    text_list.append(min_text)
    text_list.append(sec_text)
    text_list.append(incr_text)

    # load images
    cwd = os.getcwd()
    path = cwd + "/Images"
    background = pygame.image.load(path+r"\bg_image.jpg")
    white_pawn_image = Image(100, 405, 100, 150, image_file="/white_pawn_button.png",clickimage_file="/white_pawn_button_pressed.jpg")
    black_pawn_image = Image(250, 405, 100, 150, image_file="/black_pawn_raw.png", clickimage_file="/black_pawn_button_pressed.jpg")
    white_pawn_non_active = Image(100, 405, 100, 150, image_file="/white_pawn_button_nonactive.png")
    black_pawn_non_active = Image(250, 405, 100, 150, image_file="/black_pawn_raw_nonactive.png")
    up_button = Image(477, 200, 33, 30, image_file="/arrow_up.png")
    up_button2 = Image(577, 200, 33, 30, image_file="/arrow_up.png")
    up_button3 = Image(677, 200, 33, 30, image_file="/arrow_up.png")
    up_button4 = Image(777, 200, 33, 30, image_file="/arrow_up.png")
    down_button = Image(477, 230, 33, 30, image_file="/down_arrow.png")
    down_button2 = Image(577, 230, 33, 30, image_file="/down_arrow.png")
    down_button3 = Image(677, 230, 33, 30, image_file="/down_arrow.png")
    down_button4 = Image(777, 230, 33, 30, image_file="/down_arrow.png")

    image_list = []
    image_list.append(up_button)
    image_list.append(down_button)
    image_list.append(up_button2)
    image_list.append(up_button3)
    image_list.append(up_button4)
    image_list.append(down_button2)
    image_list.append(down_button3)
    image_list.append(down_button4)

    # set button state for switching images
    for image in image_list:
        image.status = "OFF"

    # create text entries
    hour_entry = Entry(517, 215, 30, 30)
    min_entry = Entry(617, 215, 30, 30)
    sec_entry = Entry(717, 215, 30, 30)
    incr_entry = Entry(817, 215, 30, 30)

    entry_list = list()
    entry_list.append(hour_entry)
    entry_list.append(min_entry)
    entry_list.append(sec_entry)
    entry_list.append(incr_entry)
    global color_pick
    color_pick = True
    global run
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                os._exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # make buttons switching buttons so they can never be selected at the same time in the same block
                if btn_1.rect.collidepoint(pos):
                    if btn_1.status == "OFF" and btn_2.status == "OFF":
                        btn_1.button_clicked(status="ON")
                        color_pick = False
                        white_pawn_image.image_click(status="OFF")
                        black_pawn_image.image_click(status="OFF")
                    elif btn_1.status == "OFF" and btn_2.status == "ON":
                        btn_1.button_clicked(status="ON")
                        btn_2.button_clicked(status="OFF")
                        color_pick = False
                        white_pawn_image.image_click(status="OFF")
                        black_pawn_image.image_click(status="OFF")
                    elif btn_1.status == "ON":
                        btn_1.button_clicked(status="OFF")
                        color_pick = True
                if btn_2.rect.collidepoint(pos):
                    if btn_2.status == "OFF" and btn_1.status == "OFF":
                        btn_2.button_clicked(status="ON")
                        color_pick = True
                    elif btn_2.status == "OFF" and btn_1.status == "ON":
                        btn_2.button_clicked(status="ON")
                        btn_1.button_clicked(status="OFF")
                        color_pick = True
                    elif btn_2.status == "ON":
                        btn_2.button_clicked(status="OFF")
                if btn_4.rect.collidepoint(pos):
                    if btn_4.status == "OFF" and btn_5.status == "OFF" and btn_6.status == "OFF":
                        btn_4.button_clicked(status="ON")
                    elif btn_4.status == "OFF" and btn_5.status == "ON":
                        btn_4.button_clicked(status="ON")
                        btn_5.button_clicked(status="OFF")
                    elif btn_4.status == "OFF" and btn_6.status == "ON":
                        btn_4.button_clicked(status="ON")
                        btn_6.button_clicked(status="OFF")
                    elif btn_4.status == "ON":
                        btn_4.button_clicked(status="OFF")
                if btn_5.rect.collidepoint(pos):
                    if btn_5.status == "OFF" and btn_4.status == "OFF" and btn_6.status == "OFF":
                        btn_5.button_clicked(status="ON")
                    elif btn_5.status == "OFF" and btn_4.status == "ON":
                        btn_5.button_clicked(status="ON")
                        btn_4.button_clicked(status="OFF")
                    elif btn_5.status == "OFF" and btn_6.status == "ON":
                        btn_5.button_clicked(status="ON")
                        btn_6.button_clicked(status="OFF")
                    elif btn_5.status == "ON":
                        btn_5.button_clicked(status="OFF")
                if btn_6.rect.collidepoint(pos):
                    if btn_6.status == "OFF" and btn_4.status == "OFF" and btn_5.status == "OFF":
                        btn_6.button_clicked(status="ON")
                    elif btn_6.status == "OFF" and btn_4.status == "ON":
                        btn_6.button_clicked(status="ON")
                        btn_4.button_clicked(status="OFF")
                    elif btn_6.status == "OFF" and btn_5.status == "ON":
                        btn_6.button_clicked(status="ON")
                        btn_5.button_clicked(status="OFF")
                    elif btn_6.status == "ON":
                        btn_6.button_clicked(status="OFF")

                # now make switching images same principle as the buttons above
                if white_pawn_image.rect.collidepoint(pos) and color_pick:
                    if white_pawn_image.status == "OFF" and black_pawn_image.status == "OFF":
                        white_pawn_image.image_click(status="ON")
                    elif white_pawn_image.status == "OFF" and black_pawn_image.status == "ON":
                        white_pawn_image.image_click(status="ON")
                        black_pawn_image.image_click(status="OFF")
                    elif white_pawn_image.status == "ON":
                        white_pawn_image.image_click(status="OFF")
                if black_pawn_image.rect.collidepoint(pos) and color_pick:
                    if black_pawn_image.status == "OFF" and white_pawn_image.status == "OFF":
                        black_pawn_image.image_click(status="ON")
                    elif black_pawn_image.status == "OFF" and white_pawn_image.status == "ON":
                        black_pawn_image.image_click(status="ON")
                        white_pawn_image.image_click(status="OFF")
                    elif black_pawn_image.status == "ON":
                        black_pawn_image.image_click(status="OFF")

                # Activate entries for text entry
                if hour_entry.rect.collidepoint(pos):
                    hour_entry.active = True
                    min_entry.active = False
                    sec_entry.active = False
                    incr_entry.active = False
                if min_entry.rect.collidepoint(pos):
                    hour_entry.active = False
                    min_entry.active = True
                    sec_entry.active = False
                    incr_entry.active = False
                if sec_entry.rect.collidepoint(pos):
                    hour_entry.active = False
                    min_entry.active = False
                    sec_entry.active = True
                    incr_entry.active = False
                if incr_entry.rect.collidepoint(pos):
                    hour_entry.active = False
                    min_entry.active = False
                    sec_entry.active = False
                    incr_entry.active = True

                # Add functionality to the up and down arrows
                # Hour_entry
                if up_button.rect.collidepoint(pos):
                    if hour_entry.text != '':
                        hour_entry.active = True
                        new_entry_val = int(str(hour_entry.text)) + 1
                        if int(new_entry_val) > 60:
                            ctypes.windll.user32.MessageBoxW(0, "Can't be higher than 60", "Error", 1)
                        else:
                            hour_entry.text_entry(event, str(new_entry_val))
                if down_button.rect.collidepoint(pos):
                    if hour_entry.text != '':
                        hour_entry.active = True
                        new_entry_val = int(str(hour_entry.text)) - 1
                        if int(new_entry_val) < 0:
                            ctypes.windll.user32.MessageBoxW(0, "Can't be lower than 0", "Error", 1)
                        else:
                            hour_entry.text_entry(event, str(new_entry_val))

                        # minute entry
                if up_button2.rect.collidepoint(pos):
                    if min_entry.text != '':
                        min_entry.active = True
                        new_entry_val = int(str(min_entry.text)) + 1
                        if int(new_entry_val) > 60:
                            ctypes.windll.user32.MessageBoxW(0, "Can't be higher than 60", "Error", 1)
                        else:
                            min_entry.text_entry(event, str(new_entry_val))
                if down_button2.rect.collidepoint(pos):
                    if min_entry.text != '':
                        min_entry.active = True
                        new_entry_val = int(str(min_entry.text)) - 1
                        if int(new_entry_val) < 0:
                            ctypes.windll.user32.MessageBoxW(0, "Can't be lower than 0", "Error", 1)
                        else:
                            min_entry.text_entry(event, str(new_entry_val))

                        # seconds entry
                if up_button3.rect.collidepoint(pos):
                    if sec_entry.text != '':
                        sec_entry.active = True
                        new_entry_val = int(str(sec_entry.text)) + 1
                        if int(new_entry_val) > 60:
                            ctypes.windll.user32.MessageBoxW(0, "Can't be higher than 60", "Error", 1)
                        else:
                            sec_entry.text_entry(event, str(new_entry_val))
                if down_button3.rect.collidepoint(pos):
                    if sec_entry.text != '':
                        sec_entry.active = True
                        new_entry_val = int(str(sec_entry.text)) - 1
                        if int(new_entry_val) < 0:
                            ctypes.windll.user32.MessageBoxW(0, "Can't be lower than 0", "Error", 1)
                        else:
                            sec_entry.text_entry(event, str(new_entry_val))

                        # increment entry
                if up_button4.rect.collidepoint(pos):
                    if incr_entry.text != '':
                        incr_entry.active = True
                        new_entry_val = int(str(incr_entry.text)) + 1
                        if int(new_entry_val) > 60:
                            ctypes.windll.user32.MessageBoxW(0, "Can't be higher than 60", "Error", 1)
                        else:
                            incr_entry.text_entry(event, str(new_entry_val))
                if down_button4.rect.collidepoint(pos):
                    if incr_entry.text != '':
                        incr_entry.active = True
                        new_entry_val = int(str(incr_entry.text)) - 1
                        if int(new_entry_val) < 0:
                            ctypes.windll.user32.MessageBoxW(0, "Can't be lower than 0", "Error", 1)
                        else:
                            incr_entry.text_entry(event, str(new_entry_val))

                if btn_3.rect.collidepoint(pos):
                    if btn_1.status == "ON":
                        if btn_4.status == "ON":
                            if hour_entry.text == '' \
                                    or sec_entry.text == '' \
                                    or min_entry.text == '' \
                                    or incr_entry.text == '' \
                                    or hour_entry.text != '' \
                                    or min_entry.text != '' \
                                    or sec_entry.text != '' \
                                    or inr_entry.text != '':
                                turn = 2
                                hour_entry.text = 0
                                min_entry.text = 15
                                sec_entry.text = 0
                                incr_entry.text = 10
                                with open('time.json', 'w') as seconds:
                                    json.dump(sec_entry.text, seconds)
                                with open('time2.json', 'w') as minutes:
                                    json.dump(min_entry.text, minutes)
                                with open('time3.json', 'w') as hours:
                                    json.dump(hour_entry.text, hours)
                                with open('time4.json', 'w') as increment:
                                    json.dump(incr_entry.text, increment)
                                with open('turn.json', 'w') as turnings:
                                    json.dump(turn, turnings)
                                run = False
                                pygame.quit()
                                with open("PvP_gameV2.py") as f:
                                    code = compile(f.read(), "PvP_gameV2.py", 'exec')
                                    exec(code, {})
                                sys.exit()
                        if btn_5.status == "ON":
                            if hour_entry.text == '' \
                                    or sec_entry.text == '' \
                                    or min_entry.text == '' \
                                    or incr_entry.text == '' \
                                    or hour_entry.text != '' \
                                    or min_entry.text != '' \
                                    or sec_entry.text != '' \
                                    or inr_entry.text != '':
                                turn = 2
                                hour_entry.text = 0
                                min_entry.text = 5
                                sec_entry.text = 0
                                incr_entry.text = 5
                                with open('time.json', 'w') as seconds:
                                    json.dump(sec_entry.text, seconds)
                                with open('time2.json', 'w') as minutes:
                                    json.dump(min_entry.text, minutes)
                                with open('time3.json', 'w') as hours:
                                    json.dump(hour_entry.text, hours)
                                with open('time4.json', 'w') as increment:
                                    json.dump(incr_entry.text, increment)
                                with open('turn.json', 'w') as turnings:
                                    json.dump(turn, turnings)
                                run = False
                                pygame.quit()
                                with open("PvP_gameV2.py") as f:
                                    code = compile(f.read(), "PvP_gameV2.py", 'exec')
                                    exec(code, {})
                                sys.exit()
                        if btn_6.status == "ON":
                            if hour_entry.text == '' \
                                    or sec_entry.text == '' \
                                    or min_entry.text == '' \
                                    or incr_entry.text == '' \
                                    or hour_entry.text != '' \
                                    or min_entry.text != '' \
                                    or sec_entry.text != '' \
                                    or inr_entry.text != '':
                                turn = 2
                                hour_entry.text = 0
                                min_entry.text = 3
                                sec_entry.text = 0
                                incr_entry.text = 2
                                with open('time.json', 'w') as seconds:
                                    json.dump(sec_entry.text, seconds)
                                with open('time2.json', 'w') as minutes:
                                    json.dump(min_entry.text, minutes)
                                with open('time3.json', 'w') as hours:
                                    json.dump(hour_entry.text, hours)
                                with open('time4.json', 'w') as increment:
                                    json.dump(incr_entry.text, increment)
                                with open('turn.json', 'w') as turnings:
                                    json.dump(turn, turnings)
                                run = False
                                pygame.quit()
                                with open("PvP_gameV2.py") as f:
                                    code = compile(f.read(), "PvP_gameV2.py", 'exec')
                                    exec(code, {})
                                sys.exit()
                        if btn_4.status == "OFF" \
                                and btn_5.status == "OFF" \
                                and btn_6.status == "OFF":
                            if hour_entry.text != '' \
                            or min_entry.text != '' \
                            or sec_entry.text != '':
                                if sec_entry.text == '':
                                    sec_entry.text = 0
                                if min_entry.text == '':
                                    min_entry.text = 0
                                if hour_entry.text == '':
                                    hour_entry.text = 0
                                if incr_entry.text == '':
                                    incr_entry.text = 0
                                turn = 2
                                with open('time.json', 'w') as seconds:
                                    json.dump(sec_entry.text, seconds)
                                with open('time2.json', 'w') as minutes:
                                    json.dump(min_entry.text, minutes)
                                with open('time3.json', 'w') as hours:
                                    json.dump(hour_entry.text, hours)
                                with open('time4.json', 'w') as increment:
                                    json.dump(incr_entry.text, increment)
                                with open('turn.json', 'w') as turnings:
                                    json.dump(turn, turnings)
                                run = False
                                pygame.quit()
                                with open("PvP_gameV2.py") as f:
                                    code = compile(f.read(), "PvP_gameV2.py", 'exec')
                                exec(code, {})
                                sys.exit()
                        if btn_4.status == "OFF" \
                                and btn_5.status == "OFF" \
                                and btn_6.status == "OFF" \
                                and hour_entry.text == '' \
                                and sec_entry.text == '' \
                                and min_entry.text == '' \
                                and incr_entry.text == '' \
                                or btn_4.status == "OFF" \
                                and btn_5.status == "OFF" \
                                and btn_6.status == "OFF" \
                                and hour_entry.text == '' \
                                and sec_entry.text == '' \
                                and min_entry.text == '' \
                                and incr_entry.text != '':
                            ctypes.windll.user32.MessageBoxW(0, "Please enter a time-control", "Error", 1)
                    if btn_2.status == "ON":
                        if black_pawn_image.status == "ON":
                            if btn_4.status == "ON":
                                if hour_entry.text == '' \
                                        or sec_entry.text == '' \
                                        or min_entry.text == '' \
                                        or incr_entry.text == '' \
                                        or hour_entry.text != '' \
                                        or min_entry.text != '' \
                                        or sec_entry.text != '' \
                                        or inr_entry.text != '':
                                    turn = 2
                                    hour_entry.text = 0
                                    min_entry.text = 15
                                    sec_entry.text = 0
                                    incr_entry.text = 10
                                    with open('time.json', 'w') as seconds:
                                        json.dump(sec_entry.text, seconds)
                                    with open('time2.json', 'w') as minutes:
                                        json.dump(min_entry.text, minutes)
                                    with open('time3.json', 'w') as hours:
                                        json.dump(hour_entry.text, hours)
                                    with open('time4.json', 'w') as increment:
                                        json.dump(incr_entry.text, increment)
                                    with open('play_color.json', 'w') as file_object:
                                        json.dump("black", file_object)
                                    run = False
                                    pygame.quit()
                                    with open("Engine_gameV2.py") as f:
                                        code = compile(f.read(), "Engine_gameV2.py", 'exec')
                                        exec(code, {})
                                    sys.exit()
                            if btn_5.status == "ON":
                                if hour_entry.text == '' \
                                        or sec_entry.text == '' \
                                        or min_entry.text == '' \
                                        or incr_entry.text == '' \
                                        or hour_entry.text != '' \
                                        or min_entry.text != '' \
                                        or sec_entry.text != '' \
                                        or inr_entry.text != '':
                                    turn = 2
                                    hour_entry.text = 0
                                    min_entry.text = 5
                                    sec_entry.text = 0
                                    incr_entry.text = 5
                                    with open('time.json', 'w') as seconds:
                                        json.dump(sec_entry.text, seconds)
                                    with open('time2.json', 'w') as minutes:
                                        json.dump(min_entry.text, minutes)
                                    with open('time3.json', 'w') as hours:
                                        json.dump(hour_entry.text, hours)
                                    with open('time4.json', 'w') as increment:
                                        json.dump(incr_entry.text, increment)
                                    with open('play_color.json', 'w') as file_object:
                                        json.dump("black", file_object)
                                    run = False
                                    pygame.quit()
                                    with open("Engine_gameV2.py") as f:
                                        code = compile(f.read(), "Engine_gameV2.py", 'exec')
                                        exec(code, {})
                                    sys.exit()
                            if btn_6.status == "ON":
                                if hour_entry.text == '' \
                                        or sec_entry.text == '' \
                                        or min_entry.text == '' \
                                        or incr_entry.text == '' \
                                        or hour_entry.text != '' \
                                        or min_entry.text != '' \
                                        or sec_entry.text != '' \
                                        or inr_entry.text != '':
                                    turn = 2
                                    hour_entry.text = 0
                                    min_entry.text = 3
                                    sec_entry.text = 0
                                    incr_entry.text = 2
                                    with open('time.json', 'w') as seconds:
                                        json.dump(sec_entry.text, seconds)
                                    with open('time2.json', 'w') as minutes:
                                        json.dump(min_entry.text, minutes)
                                    with open('time3.json', 'w') as hours:
                                        json.dump(hour_entry.text, hours)
                                    with open('time4.json', 'w') as increment:
                                        json.dump(incr_entry.text, increment)
                                    with open('play_color.json', 'w') as file_object:
                                        json.dump("black", file_object)
                                    run = False
                                    pygame.quit()
                                    with open("Engine_gameV2.py") as f:
                                        code = compile(f.read(), "Engine_gameV2.py", 'exec')
                                        exec(code, {})
                                    sys.exit()
                            if btn_4.status == "OFF" \
                                    and btn_5.status == "OFF" \
                                    and btn_6.status == "OFF":
                                if hour_entry.text != '' \
                                        or min_entry.text != '' \
                                        or sec_entry.text != '':
                                    if sec_entry.text == '':
                                        sec_entry.text = 0
                                    if min_entry.text == '':
                                        min_entry.text = 0
                                    if hour_entry.text == '':
                                        hour_entry.text = 0
                                    if incr_entry.text == '':
                                        incr_entry.text = 0
                                    turn = 2
                                    with open('time.json', 'w') as seconds:
                                        json.dump(sec_entry.text, seconds)
                                    with open('time2.json', 'w') as minutes:
                                        json.dump(min_entry.text, minutes)
                                    with open('time3.json', 'w') as hours:
                                        json.dump(hour_entry.text, hours)
                                    with open('time4.json', 'w') as increment:
                                        json.dump(incr_entry.text, increment)
                                    with open('play_color.json', 'w') as file_object:
                                        json.dump("black", file_object)
                                    run = False
                                    pygame.quit()
                                    with open("Engine_gameV2.py") as f:
                                        code = compile(f.read(), "Engine_gameV2.py", 'exec')
                                    exec(code, {})
                                    sys.exit()
                            if btn_4.status == "OFF" \
                                    and btn_5.status == "OFF" \
                                    and btn_6.status == "OFF" \
                                    and hour_entry.text == '' \
                                    and sec_entry.text == '' \
                                    and min_entry.text == '' \
                                    and incr_entry.text == '' \
                                    or btn_4.status == "OFF" \
                                    and btn_5.status == "OFF" \
                                    and btn_6.status == "OFF" \
                                    and hour_entry.text == '' \
                                    and sec_entry.text == '' \
                                    and min_entry.text == '' \
                                    and incr_entry.text != '':
                                ctypes.windll.user32.MessageBoxW(0, "Please enter a time-control", "Error", 1)
                        if white_pawn_image.status == "ON":
                            if btn_4.status == "ON":
                                if hour_entry.text == '' \
                                        or sec_entry.text == '' \
                                        or min_entry.text == '' \
                                        or incr_entry.text == '' \
                                        or hour_entry.text != '' \
                                        or min_entry.text != '' \
                                        or sec_entry.text != '' \
                                        or inr_entry.text != '':
                                    turn = 2
                                    hour_entry.text = 0
                                    min_entry.text = 15
                                    sec_entry.text = 0
                                    incr_entry.text = 10
                                    with open('time.json', 'w') as seconds:
                                        json.dump(sec_entry.text, seconds)
                                    with open('time2.json', 'w') as minutes:
                                        json.dump(min_entry.text, minutes)
                                    with open('time3.json', 'w') as hours:
                                        json.dump(hour_entry.text, hours)
                                    with open('time4.json', 'w') as increment:
                                        json.dump(incr_entry.text, increment)
                                    with open('play_color.json', 'w') as file_object:
                                        json.dump("white", file_object)
                                    run = False
                                    pygame.quit()
                                    with open("Engine_gameV2.py") as f:
                                        code = compile(f.read(), "Engine_gameV2.py", 'exec')
                                        exec(code, {})
                                    sys.exit()
                            if btn_5.status == "ON":
                                if hour_entry.text == '' \
                                        or sec_entry.text == '' \
                                        or min_entry.text == '' \
                                        or incr_entry.text == '' \
                                        or hour_entry.text != '' \
                                        or min_entry.text != '' \
                                        or sec_entry.text != '' \
                                        or inr_entry.text != '':
                                    turn = 2
                                    hour_entry.text = 0
                                    min_entry.text = 5
                                    sec_entry.text = 0
                                    incr_entry.text = 5
                                    with open('time.json', 'w') as seconds:
                                        json.dump(sec_entry.text, seconds)
                                    with open('time2.json', 'w') as minutes:
                                        json.dump(min_entry.text, minutes)
                                    with open('time3.json', 'w') as hours:
                                        json.dump(hour_entry.text, hours)
                                    with open('time4.json', 'w') as increment:
                                        json.dump(incr_entry.text, increment)
                                    with open('play_color.json', 'w') as file_object:
                                        json.dump("white", file_object)
                                    run = False
                                    pygame.quit()
                                    with open("Engine_gameV2.py") as f:
                                        code = compile(f.read(), "Engine_gameV2.py", 'exec')
                                        exec(code, {})
                                    sys.exit()
                            if btn_6.status == "ON":
                                if hour_entry.text == '' \
                                        or sec_entry.text == '' \
                                        or min_entry.text == '' \
                                        or incr_entry.text == '' \
                                        or hour_entry.text != '' \
                                        or min_entry.text != '' \
                                        or sec_entry.text != '' \
                                        or inr_entry.text != '':
                                    turn = 2
                                    hour_entry.text = 0
                                    min_entry.text = 3
                                    sec_entry.text = 0
                                    incr_entry.text = 2
                                    with open('time.json', 'w') as seconds:
                                        json.dump(sec_entry.text, seconds)
                                    with open('time2.json', 'w') as minutes:
                                        json.dump(min_entry.text, minutes)
                                    with open('time3.json', 'w') as hours:
                                        json.dump(hour_entry.text, hours)
                                    with open('time4.json', 'w') as increment:
                                        json.dump(incr_entry.text, increment)
                                    with open('play_color.json', 'w') as file_object:
                                        json.dump("white", file_object)
                                    run = False
                                    pygame.quit()
                                    with open("Engine_gameV2.py") as f:
                                        code = compile(f.read(), "Engine_gameV2.py", 'exec')
                                        exec(code, {})
                                    sys.exit()
                            if btn_4.status == "OFF" \
                                    and btn_5.status == "OFF" \
                                    and btn_6.status == "OFF":
                                if hour_entry.text != '' \
                                        or min_entry.text != '' \
                                        or sec_entry.text != '':
                                    if sec_entry.text == '':
                                        sec_entry.text = 0
                                    if min_entry.text == '':
                                        min_entry.text = 0
                                    if hour_entry.text == '':
                                        hour_entry.text = 0
                                    if incr_entry.text == '':
                                        incr_entry.text = 0
                                    turn = 2
                                    with open('time.json', 'w') as seconds:
                                        json.dump(sec_entry.text, seconds)
                                    with open('time2.json', 'w') as minutes:
                                        json.dump(min_entry.text, minutes)
                                    with open('time3.json', 'w') as hours:
                                        json.dump(hour_entry.text, hours)
                                    with open('time4.json', 'w') as increment:
                                        json.dump(incr_entry.text, increment)
                                    with open('play_color.json', 'w') as file_object:
                                        json.dump("white", file_object)
                                    run = False
                                    pygame.quit()
                                    with open("Engine_gameV2.py") as f:
                                        code = compile(f.read(), "Engine_gameV2.py", 'exec')
                                    exec(code, {})
                                    sys.exit()
                            if btn_4.status == "OFF" \
                                    and btn_5.status == "OFF" \
                                    and btn_6.status == "OFF" \
                                    and hour_entry.text == '' \
                                    and sec_entry.text == '' \
                                    and min_entry.text == '' \
                                    and incr_entry.text == '' \
                                    or btn_4.status == "OFF" \
                                    and btn_5.status == "OFF" \
                                    and btn_6.status == "OFF" \
                                    and hour_entry.text == '' \
                                    and sec_entry.text == '' \
                                    and min_entry.text == '' \
                                    and incr_entry.text != '':
                                ctypes.windll.user32.MessageBoxW(0, "Please enter a time-control", "Error", 1)
                        if white_pawn_image.status == "OFF" \
                                and black_pawn_image.status == "OFF":
                            ctypes.windll.user32.MessageBoxW(0, "Please pick a color", "Error", 1)
                    if btn_1.status == "OFF" \
                            and btn_2.status == "OFF":
                        ctypes.windll.user32.MessageBoxW(0, "Please pick a mode", "Error", 1)


            hour_entry.text_entry(event, hour_entry.text)
            min_entry.text_entry(event, min_entry.text)
            sec_entry.text_entry(event, sec_entry.text)
            incr_entry.text_entry(event, incr_entry.text)

        # backgound image and lines for seperate sections
        screen.blit(background, (0, 0))
        pygame.draw.line(screen, (180, 180, 200), (430, 0), (430, 600), width=4)
        pygame.draw.line(screen, (180, 180, 200), (0, 300), (900, 300), width=4)
        # draw images on screen
        if not color_pick:
            white_pawn_non_active.draw_image(screen)
            black_pawn_non_active.draw_image(screen)
        else:
            white_pawn_image.draw_image(screen)
            black_pawn_image.draw_image(screen)
        for image in image_list:
            image.draw_image(screen)
        # draw buttons on screen
        for button in button_list:
            button.draw_button(screen)
        # draw text on screen
        for text in text_list:
            text.draw_text(screen)
        # draw text entry on screen
        for entry in entry_list:
            entry.draw_entry(screen)

        pygame.display.update()

main()

if __name__ == "__main__":
    main()
