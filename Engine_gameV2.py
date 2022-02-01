import signal
import threading
from UIClassesV3 import Text, Button, Image, Entry
import pygame
import PiecesV10
from PiecesV10 import Piece
import os
import time
import datetime
import json
from fractions import Fraction
import sys
from ctypes import windll



class APP:
    def timer():
        """make a timer for both players. This timer has te value inputted in the main menu"""
        global black_score
        global white_score
        PiecesV10.draw = False
        PiecesV10.stale_mate = False
        PiecesV10.fifty_move_draw = False
        PiecesV10.white_checkmate = False
        PiecesV10.black_checkmate = False
        PiecesV10.instant_draw = False
        # load the times from json files
        with open('time.json', 'r') as seconds:
            seconds = json.load(seconds)
        with open('time2.json', 'r') as minutes:
            minutes = json.load(minutes)
        with open('time3.json', 'r') as hours_int:
            hours_int = json.load(hours_int)
        with open('time4.json', 'r') as increment:
            increment = json.load(increment)

        global secs
        global secs2
        global mins
        global mins2
        global hours
        global hours2
        global mili_secs
        global mili_secs2
        mili_secs = 98
        mili_secs2 = 98
        secs = int(seconds)
        secs2 = int(seconds)
        mins = int(minutes)
        mins2 = int(minutes)
        hours =  int(hours_int)
        hours2 = int(hours_int)
        timer_seconds = int(seconds) + int(60*int(minutes)) + int(3600*int(hours))
        timer_seconds =  timer_seconds*100
        timer_seconds2 = int(seconds) + int(60*int(minutes)) + int(3600*int(hours2))
        timer_seconds2 = timer_seconds2*100
        clock2 = pygame.time.Clock()
        clock3 = pygame.time.Clock()
        global white_turn
        global black_turn
        if int(PiecesV10.turn) % 2 == 0:
            white_turn = True
        elif int(PiecesV10.turn) % 2 == 1:
            white_turn = False

        global timer_run
        global run
        global timer_run_always
        timer_run_always = True
        global close_game
        global black_time_out
        global white_time_out
        black_time_out = False
        white_time_out = False
        global resign_white_win
        global resign_black_win
        resign_white_win = False
        resign_black_win = False
        timer_run = True
        close_game = False

        while timer_run_always:
            while timer_run:
                while not white_turn:
                    clock3.tick(100)
                    timer_seconds2 -= 1
                    if 101 > mili_secs2 > -1:
                        mili_secs2 -= 1
                    elif mili_secs2 == -1:
                        mili_secs2 = 98
                        secs2 -= 1
                        if secs2 == -1:
                            secs2 = 59
                            mins2 -= 1
                            if mins2 == -1:
                                hours2 -=1
                                mins2 = 59
                    if timer_seconds2 == 0:
                        black_time_out = True
                        if not PiecesV10.white_draw_TO:
                            white_score += 1
                        if PiecesV10.white_draw_TO:
                            white_score += 0.5
                            black_score += 0.5
                        timer_run = False
                        break
                    if int(PiecesV10.turn) % 2 == 0:
                        timer_seconds2 += (int(increment)*100)
                        secs2 += int(increment)
                        if secs2 > 59:
                            mins2 += 1
                            secs2 = int(secs2) - 60
                            if mins2 > 59:
                                hours2 += 1
                                mins2 = int(mins2) - 60
                        white_turn = True
                    if PiecesV10.draw \
                            or PiecesV10.stale_mate \
                            or PiecesV10.fifty_move_draw \
                            or PiecesV10.instant_draw:
                        black_score += 0.5
                        white_score += 0.5
                        white_turn = False
                        timer_run = False
                        break
                    if PiecesV10.black_checkmate \
                            or resign_white_win:
                        resign_white_win = False
                        resign_black_win = False
                        white_score += 1
                        white_turn = False
                        timer_run = False
                        break
                    if PiecesV10.white_checkmate \
                            or resign_black_win:
                        black_score += 1
                        resign_white_win = False
                        resign_black_win = False
                        white_turn = False
                        timer_run = False
                        break
                    break
                while white_turn:
                    clock2.tick(100)
                    timer_seconds -= 1
                    if 101 > mili_secs > -1:
                        mili_secs -= 1
                    elif mili_secs == -1:
                        mili_secs = 98
                        secs -= 1
                        if secs == -1:
                            secs = 59
                            mins -= 1
                            if mins == -1:
                                hours -=1
                                mins = 59
                    if timer_seconds == 0:
                        white_time_out = True
                        if not PiecesV10.black_draw_TO:
                            black_score +=1
                        if PiecesV10.black_draw_TO:
                            black_score += 0.5
                            white_score += 0.5
                        timer_run = False
                        break
                    if int(PiecesV10.turn) % 2 == 1:
                        timer_seconds += (int(increment)*100)
                        secs += int(increment)
                        if secs > 59:
                            mins += 1
                            secs = int(secs) - 60
                            if mins > 59:
                                hours += 1
                                mins = int(hours) - 60
                        white_turn = False
                    if PiecesV10.draw \
                            or PiecesV10.stale_mate \
                            or PiecesV10.fifty_move_draw \
                            or PiecesV10.instant_draw:
                        black_score += 0.5
                        white_score += 0.5
                        white_turn = False
                        timer_run = False
                        break
                    if PiecesV10.black_checkmate \
                            or resign_white_win:
                        resign_white_win = False
                        resign_black_win = False
                        white_score += 1
                        white_turn = False
                        timer_run = False
                        break
                    if PiecesV10.white_checkmate \
                            or resign_black_win:
                        resign_white_win = False
                        resign_black_win = False
                        black_score += 1
                        white_turn = False
                        timer_run = False
                        break
                    break
            while not timer_run:
                timer_seconds = timer_seconds
                timer_seconds2 = timer_seconds2
                if close_game:
                    sys.exit()


    def main():
        """draw the board and the pieces and handle the events of the game"""
        x = 80
        y = 30
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
        pygame.init()

        screen = pygame.display.set_mode((1250, 700))
        cwd = os.getcwd()
        path = cwd + "/Images"
        background = pygame.image.load(path + r"\bg_image.jpg")
        screen_rect = pygame.Rect(0, 0, 1000, 700)
        clock = pygame.time.Clock()


        # init score for black and white when starting a new game from main menu
        global white_score
        global black_score
        white_score = 0
        black_score = 0
        global black_time_out
        global white_time_out
        black_time_out = False
        white_time_out = False
        global play_color

        with open ('play_color.json', 'r') as file_object:
            play_color = json.load(file_object)


        check_text = Text("Check!", 1030, 325, font_size=48)
            # make an interface left of the screen with different buttons and text
        main_menu_btn_2 = Button(50, 80, 140, 40, (65, 243, 30), (65, 243, 30), font_size=22, text="Main menu")
        pause_btn = Button(50, 210, 140, 40, (255, 36, 36), (255, 160, 160), font_size=22, text="Pause game")
        pause_btn.button_clicked(status="OFF")
        resign_btn = Button(50, 280, 140, 40, (255, 36, 36), (255, 36, 36), font_size=22, text="Resign")
        draw_btn = Button(50, 350, 140, 40, (255, 36, 36), (255, 36, 36), font_size=22, text="Offer draw")
        score_text = Text("Score:", 50, 460, font_size=32, underline="True")
        white_text = Text("White: ", 50, 540, font_size=26)
        black_text = Text("Black: ", 50, 610, font_size=26)
            # make a pop op with buttons if game ends
                    # if checkmate by either
        white_win_kader = Button(420, 240, 400, 200, (255, 203, 97), (255, 203, 97), border_radius=10, font_size=36, text="White: 1 - Black: 0")
        black_win_kader = Button(420, 240, 400, 200, (255, 203, 97), (255, 203, 97), border_radius=10, font_size=36, text="White: 0 - Black: 1")
        checkmate_text = Text("Checkmate!", 510, 255, font_size=48)
                    # if exit game
        quit_kader = Button(420, 240, 400, 200, (255, 203, 97), (255, 203, 97), border_radius=10)
        yes_btn =  Button(450, 380, 140, 40, (219, 117, 212), (219, 117, 212), font_size=24, text="Yes")
        no_btn =  Button(650, 380, 140, 40, (219, 117, 212), (219, 117, 212), font_size=24, text="No")
        quit_text = Text("Are you sure u want", 460, 255, font_size=40)
        quit_text_2 =  Text("to quit?", 570, 305, font_size=40)
                    # if draw
        draw_kader = Button(420, 240, 400, 200, (255, 203, 97), (255, 203, 97), border_radius=10, font_size=36, text="White " + str(Fraction(1, 2)) + " - Black " + str(Fraction(1, 2)))
        draw_by_rep_text = Text("Draw by repetition", 440, 255, font_size=48)
        stale_mate_text = Text("Draw by stalemate", 440, 255, font_size=48)
        fifty_draw_text = Text("Draw by fifty-move-rule", 430, 255, font_size=38)
        material_draw_text = Text("Draw by insufficient material", 430, 255, font_size=32)
        black_win_time_text = Text("Black wins on time", 460, 255, font_size=42)
        white_win_time_text = Text("White wins on time", 460, 255, font_size=42)
        play_again_btn = Button(650, 380, 140, 40, (219, 117, 212), (219, 117, 212), font_size=22, text="Play again")
        main_menu_btn = Button(450, 380, 140, 40, (219, 117, 212), (219, 117, 212), font_size=22, text="Main menu")
            # make draw by agreement pop op bound to "Offer draw" button
        draw_agree_btn = Button(420, 240, 400, 200, (255, 203, 97), (255, 203, 97), border_radius=10)
        draw_agree_question = Text("Draw?", 565, 280, font_size=48)
        draw_agree_text =  Text("Draw by agreement", 455, 255, font_size=42)
            # resign button binds and text
        resign_win_white = Button(420, 240, 400, 200, (255, 203, 97), (255, 203, 97), border_radius=10, font_size = 36, text="White: 1 - Black: 0")
        resign_win_black = Button(420, 240, 400, 200, (255, 203, 97), (255, 203, 97), border_radius=10, font_size=36, text="White: 0 - Black: 1")
        resign_text = Text("Result by resignation", 460, 255, font_size=38)



        global secs
        global mins
        global secs2
        global mins2
        global hours
        global hours2
        global run
        run = True
        global timer_run
        global quit_pop_up
        quit_pop_up = False
        global draw_pop_up
        draw_pop_up = False
        global draw_by_agreement
        draw_by_agreement = False
        global draw_by_agreement_2
        draw_by_agreement_2 = False
        global resign_pop_up
        resign_pop_up = False
        global resign_white_win
        resign_white_win = False
        global resign_black_win
        resign_black_win = False
        global close_game
        close_game = False

        Piece.init_state_and_reset()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_pop_up = True
                    draw_pop_up = False
                    draw_by_agreement = False
                    draw_by_agreement_2 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    # Draw pop up event handeling
                    if draw_pop_up \
                            and not quit_pop_up \
                            and not resign_pop_up \
                            and yes_btn.rect.collidepoint(pos):
                        draw_pop_up = False
                        draw_by_agreement = True
                        draw_by_agreement_2 = True
                        PiecesV10.draw = True
                    if draw_pop_up \
                            and not quit_pop_up \
                            and not resign_pop_up \
                            and no_btn.rect.collidepoint(pos):
                        draw_pop_up = False
                    # make pieces active for moving
                    for piece in PiecesV10.white_pieces_list:
                        if piece.rect.collidepoint(pos):
                            piece.active = True
                    for piece in PiecesV10.black_pieces_list:
                        if piece.rect.collidepoint(pos):
                            piece.active = True

                    # event handeling for play again and main menu button in pop up if game ends
                    if PiecesV10.draw \
                            or PiecesV10.stale_mate \
                            or PiecesV10.fifty_move_draw \
                            or PiecesV10.black_checkmate \
                            or PiecesV10.white_checkmate \
                            or resign_pop_up \
                            or white_time_out \
                            or black_time_out \
                            or PiecesV10.instant_draw:
                        if not quit_pop_up \
                                and not draw_pop_up \
                                and not draw_by_agreement:
                            if play_again_btn.rect.collidepoint(pos):
                                resign_black_win = False
                                resign_white_win = False
                                resign_pop_up = False
                                draw_by_agreement_2 = False
                                close_game = True
                                Piece.init_state_and_reset()
                                threading.Thread(target=APP.timer).start()
                            else:
                                pass
                    if PiecesV10.draw \
                            or PiecesV10.stale_mate \
                            or PiecesV10.fifty_move_draw \
                            or PiecesV10.black_checkmate \
                            or PiecesV10.white_checkmate \
                            or resign_pop_up \
                            or white_time_out \
                            or black_time_out \
                            or PiecesV10.instant_draw:
                        if not quit_pop_up \
                                and not draw_pop_up \
                                and not draw_by_agreement:
                            if main_menu_btn.rect.collidepoint(pos):
                                close_game = True
                                draw_by_agreement_2 = False
                                pygame.quit()
                                with open("main_menu2.py") as f:
                                    code = f.read()
                                    exec(code)
                                os._exit(0)
                            else:
                                pass

                    # inter face button handeling (left side of board)
                    if main_menu_btn_2.rect.collidepoint(pos) \
                            and not quit_pop_up \
                            and not draw_pop_up \
                            and not PiecesV10.draw \
                            and not PiecesV10.stale_mate \
                            and not PiecesV10.fifty_move_draw \
                            and not PiecesV10.black_checkmate \
                            and not PiecesV10.white_checkmate \
                            and not resign_pop_up \
                            and not white_time_out \
                            and not black_time_out \
                            and not PiecesV10.instant_draw:
                        pygame.quit()
                        with open("main_menu2.py") as f:
                            code = f.read()
                            exec(code)
                        os._exit(0)
                    if pause_btn.rect.collidepoint(pos) \
                            and not quit_pop_up \
                            and not draw_pop_up \
                            and not PiecesV10.draw \
                            and not PiecesV10.stale_mate \
                            and not PiecesV10.fifty_move_draw \
                            and not PiecesV10.black_checkmate \
                            and not PiecesV10.white_checkmate \
                            and not resign_pop_up \
                            and not white_time_out \
                            and not black_time_out \
                            and not PiecesV10.instant_draw:
                        if pause_btn.status == "OFF":
                            pause_btn.button_clicked(status="ON")
                            timer_run = False
                        elif pause_btn.status == "ON":
                            pause_btn.button_clicked(status="OFF")
                            timer_run = True
                    if resign_btn.rect.collidepoint(pos) \
                            and not quit_pop_up \
                            and not draw_pop_up \
                            and not PiecesV10.draw \
                            and not PiecesV10.stale_mate \
                            and not PiecesV10.fifty_move_draw \
                            and not PiecesV10.black_checkmate \
                            and not PiecesV10.white_checkmate \
                            and not resign_pop_up \
                            and not white_time_out \
                            and not black_time_out \
                            and not PiecesV10.instant_draw:
                        resign_pop_up = True
                    if draw_btn.rect.collidepoint(pos) \
                            and not quit_pop_up \
                            and not draw_pop_up \
                            and not PiecesV10.draw \
                            and not PiecesV10.stale_mate \
                            and not PiecesV10.fifty_move_draw \
                            and not PiecesV10.black_checkmate \
                            and not PiecesV10.white_checkmate \
                            and not resign_pop_up \
                            and not white_time_out \
                            and not black_time_out \
                            and not PiecesV10.instant_draw:
                        draw_pop_up = True

                    if quit_pop_up \
                            and yes_btn.rect.collidepoint(pos):
                        close_game = True
                        pygame.quit()
                        os._exit(0)
                    if quit_pop_up \
                            and no_btn.rect.collidepoint(pos):
                        quit_pop_up = False

                # make pieces not active if mouse button is up (not down)
                if event.type == pygame.MOUSEBUTTONUP:
                    for piece in PiecesV10.white_pieces_list:
                        piece.active = False
                    for piece in PiecesV10.black_pieces_list:
                        piece.active = False

            # handles the position and placing of pieces while moving
            for piece in PiecesV10.white_pieces_list:
                piece.image_move()
                piece.place_pieces()
            for piece in PiecesV10.black_pieces_list:
                piece.image_move()
                piece.place_pieces()

            screen.blit(background, screen_rect)
            Piece.draw_bord(screen)

            # prints a text if either king is in check
            if PiecesV10.white_king_check \
                    and not PiecesV10.white_checkmate \
                    and not PiecesV10.black_checkmate \
                    or PiecesV10.black_king_check \
                    and not PiecesV10.white_checkmate \
                    and not PiecesV10.black_checkmate:
                check_text.draw_text(screen)

            # Pieces get drawn over pieces of other color in own turn
            if int(PiecesV10.turn) % 2 == 0:
                PiecesV10.black_pieces_list.draw(screen)
                PiecesV10.white_pieces_list.draw(screen)
            elif int(PiecesV10.turn) % 2 == 1:
                PiecesV10.white_pieces_list.draw(screen)
                PiecesV10.black_pieces_list.draw(screen)

            # handle drawing pawn promotion events
            Piece.pawn_promotion(screen, event)


            # Handle different outcomes of the game
            if PiecesV10.draw:
                timer_run = False
                draw_kader.draw_button(screen)
                if draw_by_agreement_2:
                    draw_agree_text.draw_text(screen)
                else:
                    draw_by_rep_text.draw_text(screen)
                play_again_btn.draw_button(screen)
                main_menu_btn.draw_button(screen)
                draw_by_agreement = False
            if PiecesV10.stale_mate:
                timer_run =  False
                draw_kader.draw_button(screen)
                stale_mate_text.draw_text(screen)
                play_again_btn.draw_button(screen)
                main_menu_btn.draw_button(screen)
            if PiecesV10.fifty_move_draw:
                timer_run =  False
                draw_kader.draw_button(screen)
                fifty_draw_text.draw_text(screen)
                play_again_btn.draw_button(screen)
                main_menu_btn.draw_button(screen)
            if PiecesV10.white_checkmate:
                timer_run = False
                black_win_kader.draw_button(screen)
                checkmate_text.draw_text(screen)
                play_again_btn.draw_button(screen)
                main_menu_btn.draw_button(screen)
            if PiecesV10.black_checkmate:
                timer_run = False
                white_win_kader.draw_button(screen)
                checkmate_text.draw_text(screen)
                play_again_btn.draw_button(screen)
                main_menu_btn.draw_button(screen)
            if white_time_out:
                if PiecesV10.black_draw_TO:
                    draw_kader.draw_button(screen)
                    material_draw_text.draw_text(screen)
                else:
                    black_win_kader.draw_button(screen)
                    black_win_time_text.draw_text(screen)
                play_again_btn.draw_button(screen)
                main_menu_btn.draw_button(screen)
            if black_time_out:
                if PiecesV10.white_draw_TO:
                    draw_kader.draw_button(screen)
                    material_draw_text.draw_text(screen)
                else:
                    white_win_kader.draw_button(screen)
                    white_win_time_text.draw_text(screen)
                play_again_btn.draw_button(screen)
                main_menu_btn.draw_button(screen)
            if PiecesV10.instant_draw:
                timer_run = False
                draw_kader.draw_button(screen)
                material_draw_text.draw_text(screen)
                play_again_btn.draw_button(screen)
                main_menu_btn.draw_button(screen)
            if quit_pop_up:
                quit_kader.draw_button(screen)
                yes_btn.draw_button(screen)
                no_btn.draw_button(screen)
                quit_text.draw_text(screen)
                quit_text_2.draw_text(screen)
            if draw_pop_up:
                draw_agree_btn.draw_button(screen)
                draw_agree_question.draw_text(screen)
                yes_btn.draw_button(screen)
                no_btn.draw_button(screen)
            if resign_pop_up and not quit_pop_up:
                timer_run = False
                if PiecesV10.turn % 2 == 1:
                    resign_win_white.draw_button(screen)
                    resign_white_win = True
                if PiecesV10.turn % 2 == 0:
                    resign_black_win = True
                    resign_win_black.draw_button(screen)
                resign_text.draw_text(screen)
                play_again_btn.draw_button(screen)
                main_menu_btn.draw_button(screen)


                # print the score
            white_score_text = Text(str(white_score), 150, 540, font_size=26)
            black_score_text = Text(str(black_score), 150, 610, font_size=26)

            # make an interface on the left side of the board
            pygame.draw.line(screen, (180, 180, 200), (250, 0), (250, 700), width=4)
            pygame.draw.line(screen, (180, 180, 200), (0, 162), (250, 162), width=4)
            pygame.draw.line(screen, (180, 180, 200), (0, 432), (250, 432), width=4)
            main_menu_btn_2.draw_button(screen)
            pause_btn.draw_button(screen)
            resign_btn.draw_button(screen)
            draw_btn.draw_button(screen)
            score_text.draw_text(screen)
            white_text.draw_text(screen)
            black_text.draw_text(screen)
            white_score_text.draw_text(screen)
            black_score_text.draw_text(screen)

            # Draw timers on screen
            global timer_text
            global timer_text2
            global timer_text3
            global timer_text_black1
            global timer_text_black2
            global timer_text_black3
            global timer_dubbelepunt3
            global timer_dubbelepunt4


            if play_color == "white":
            # Positioning of the white timer
                if int(secs) < 10:
                    timer_text = Text('0' + str(secs), 1145, 550, font_size=48)
                else:
                    timer_text = Text(str(secs), 1145, 550, font_size=48)
                if int(mins) < 10:
                    timer_text2 = Text('0' + str(mins), 1075, 550, font_size=48)
                    timer_dubbelepunt3 = Text(":", 1060, 547, font_size=48)
                else:
                    timer_text2 = Text(str(mins), 1080, 550, font_size=48)
                    timer_dubbelepunt3 = Text(":", 1070, 547, font_size=48)
                if int(hours) < 10 and int(hours)!= 0:
                    timer_text3 = Text('0' + str(hours), 1015, 550, font_size=48)
                else:
                    timer_text3 = Text(str(hours), 1025, 550, font_size=48)


                timer_dubbelepunt = Text(":", 1130, 547, font_size=48)


                # Positioning of the black timer
                if int(secs2) < 10:
                    timer_text_black1 = Text('0' + str(secs2), 1145, 100, font_size=48)
                else:
                    timer_text_black1 = Text(str(secs2), 1145, 100, font_size=48)
                if int(mins2) < 10:
                    timer_text_black2 = Text('0' + str(mins2), 1075, 100, font_size=48)
                    timer_dubbelepunt4 = Text(":", 1060, 97, font_size=48)
                else:
                    timer_text_black2 = Text(str(mins2), 1080, 100, font_size=48)
                    timer_dubbelepunt4 = Text(":", 1070, 97, font_size=48)
                if int(hours2) < 10 and int(hours2) != 0:
                    timer_text_black3 = Text('0' + str(hours2), 1015, 100, font_size=48)
                else:
                    timer_text_black3 = Text(str(hours2), 1025, 100, font_size=48)
                timer_dubbelepunt2 = Text(":", 1130, 97, font_size=48)
                timer_text.draw_text(screen)
                timer_text2.draw_text(screen)
                if int(hours) != 0:
                    timer_text3.draw_text(screen)
                    timer_dubbelepunt3.draw_text(screen)
                timer_dubbelepunt.draw_text(screen)
                timer_text_black1.draw_text(screen)
                timer_text_black2.draw_text(screen)
                if int(hours2) != 0:
                    timer_text_black3.draw_text(screen)
                    timer_dubbelepunt4.draw_text(screen)
                timer_dubbelepunt2.draw_text(screen)

            elif play_color == "black":
                # positioning of white timer
                if int(secs2) < 10:
                    timer_text_black1 = Text('0' + str(secs2), 1145, 550, font_size=48)
                else:
                    timer_text_black1 = Text(str(secs2), 1145, 550, font_size=48)
                if int(mins) < 10:
                    timer_text_black2 = Text('0' + str(mins2), 1075, 550, font_size=48)
                    timer_dubbelepunt3 = Text(":", 1060, 547, font_size=48)
                else:
                    timer_text_black2 = Text(str(mins2), 1085, 550, font_size=48)
                    timer_dubbelepunt3 = Text(":", 1070, 547, font_size=48)
                if int(hours2) < 10 and int(hours2) != 0:
                    timer_text3 = Text('0' + str(hours2), 1015, 550, font_size=48)
                else:
                    timer_text3 = Text(str(hours2), 1025, 550, font_size=48)
                    
                    
                    
                timer_dubbelepunt = Text(":", 1130, 547, font_size=48)

                # Positioning of the black timer
                if int(secs) < 10:
                    timer_text = Text('0' + str(secs), 1145, 100, font_size=48)
                else:
                    timer_text = Text(str(secs), 1145, 100, font_size=48)
                if int(mins2) < 10:
                    timer_text2 = Text('0' + str(mins), 1075, 100, font_size=48)
                    timer_dubbelepunt4 = Text(":", 1060, 97, font_size=48)
                else:
                    timer_text2 = Text(str(mins), 1085, 100, font_size=48)
                    timer_dubbelepunt4 = Text(":", 1070, 97, font_size=48)
                if int(hours) < 10 and int(hours) != 0:
                    timer_text_black3 = Text('0' + str(hours), 1015, 100, font_size=48)
                else:
                    timer_text_black3 = Text(str(hours), 1025, 100, font_size=48)

                    
                timer_dubbelepunt2 = Text(":", 1130, 97, font_size=48)

                timer_text.draw_text(screen)
                timer_text2.draw_text(screen)
                if int(hours) != 0:
                    timer_text3.draw_text(screen)
                    timer_dubbelepunt3.draw_text(screen)
                timer_dubbelepunt.draw_text(screen)
                timer_text_black1.draw_text(screen)
                timer_text_black2.draw_text(screen)
                if int(hours2) != 0:
                    timer_text_black3.draw_text(screen)
                    timer_dubbelepunt4.draw_text(screen)
                timer_dubbelepunt2.draw_text(screen)

            pygame.display.update()

pygame.init()
main_t  = threading.Thread(target=APP.main).start()
timer_t = threading.Thread(target=APP.timer).start()





