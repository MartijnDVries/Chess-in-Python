import pygame
import math
from UIClassesV3 import Text, Image
import time
import json
global turn
import os
turn = 2

class Piece(pygame.sprite.Sprite):
    def __init__(self, piece_name, piece_color, image_file, file, row):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        cwd = os.getcwd()
        path = cwd+"\Images"
        self.image = pygame.image.load(path + self.image_file)
        self.active = False
        self.placed = True
        self.piece_name = piece_name
        self.piece_color = piece_color
        self.image_rect = self.image.get_rect()
        self.row = row
        self.file = file
        self.square = str(self.file + str(self.row))
        self.x = int(square_list[self.square][0]) - self.image_rect.w // 2
        self.y = int(square_list[self.square][1]) - self.image_rect.h // 2
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        square_list[self.square].append("OCCUPIED")
        square_list[self.square].append(self.piece_color)
        square_list[self.square].append(self.piece_name)
        self.white_king_check = False
        self.black_king_check = False
        self.white_king_castle = False
        self.black_king_castle = False
        self.checkmate_check = False
        global pawn_promotion
        pawn_promotion = False
        global white_king_check
        global black_king_check
        white_king_check = False
        black_king_check = False
        global white_checkmate
        global black_checkmate
        white_checkmate = False
        black_checkmate = False
        global draw
        draw = False
        global stale_mate
        stale_mate = False
        global fifty_move_draw
        fifty_move_draw = False
        global instant_draw
        global white_draw_TO
        global black_draw_TO
        instant_draw = False
        white_draw_TO = False
        black_draw_TO = False

    def init_state_and_reset():
        global square_list
        global square_list_list
        global rep_pos_list
        global fifty_count
        global turn

        turn = 2
        x = 287
        square_list = dict()
        charlist = "abcdefgh"
        for char in charlist:
            x += 74
            y = 17
            for cif in range(8, 0, -1):
                y += 74
                square_int = char + str(cif)
                square_list[square_int] = [str(x), str(y)]

        square_list_list = list()
        rep_pos_list = dict()
        fifty_count = 0

        global white_king_check
        global black_king_check
        global black_pieces_list
        global white_pieces_list
        black_pieces_list = pygame.sprite.Group()
        white_pieces_list = pygame.sprite.Group()
        
        global white_king
        global white_queen
        global white_knight
        global white_knight2
        global white_bishop
        global white_bishop2
        global white_rook
        global white_rook2

        white_king = Piece("king", "white", "/white_kingpiece4.png", 'e', 1)
        white_queen = Piece("queen", "white", "/white_queenpiece.png", 'd', 1)
        white_knight = Piece("knight", "white", "/white_knightpiece2.png", 'b', 1)
        white_knight2 = Piece("knight", "white", "/white_knightpiece2.png", 'g', 1)
        white_bishop = Piece("bishop", "white", "/white_bishoppiece.png", 'c', 1)
        white_bishop2 = Piece("bishop", "white", "/white_bishoppiece.png", 'f', 1)
        white_rook = Piece("rook", "white", "/white_rookpiece.png", 'h', 1)
        white_rook2 = Piece("rook", "white", "/white_rookpiece.png", 'a', 1)

        global white_a_pawn
        global white_b_pawn
        global white_c_pawn
        global white_d_pawn
        global white_e_pawn
        global white_f_pawn
        global white_g_pawn
        global white_h_pawn
        
        white_a_pawn = Piece("pawn", "white", "/white_pawnpiece2.png", 'a', 2)
        white_b_pawn = Piece("pawn", "white", "/white_pawnpiece2.png", 'b', 2)
        white_c_pawn = Piece("pawn", "white", "/white_pawnpiece2.png", 'c', 2)
        white_d_pawn = Piece("pawn", "white", "/white_pawnpiece2.png", 'd', 2)
        white_e_pawn = Piece("pawn", "white", "/white_pawnpiece2.png", 'e', 2)
        white_f_pawn = Piece("pawn", "white", "/white_pawnpiece2.png", 'f', 2)
        white_g_pawn = Piece("pawn", "white", "/white_pawnpiece2.png", 'g', 2)
        white_h_pawn = Piece("pawn", "white", "/white_pawnpiece2.png", 'h', 2)

        white_pieces_list.add(white_king)
        white_pieces_list.add(white_queen)
        white_pieces_list.add(white_knight)
        white_pieces_list.add(white_knight2)
        white_pieces_list.add(white_bishop)
        white_pieces_list.add(white_bishop2)
        white_pieces_list.add(white_rook)
        white_pieces_list.add(white_rook2)

        white_pieces_list.add(white_a_pawn)
        white_pieces_list.add(white_b_pawn)
        white_pieces_list.add(white_c_pawn)
        white_pieces_list.add(white_d_pawn)
        white_pieces_list.add(white_e_pawn)
        white_pieces_list.add(white_f_pawn)
        white_pieces_list.add(white_g_pawn)
        white_pieces_list.add(white_h_pawn)
        
        global black_king
        global black_queen
        global black_knight
        global black_knight2
        global black_bishop
        global black_bishop2
        global black_rook
        global black_rook2

        black_king = Piece("king", "black", "/black_kingpiece.png", 'e', 8)
        black_queen = Piece("queen", "black", "/black_queenpiece.png", 'd', 8)
        black_knight = Piece("knight", "black", "/black_knightpiece.png", 'b', 8)
        black_knight2 = Piece("knight", "black", "/black_knightpiece.png", 'g', 8)
        black_bishop = Piece("bishop", "black", "/black_bishoppiece.png", 'f', 8)
        black_bishop2 = Piece("bishop", "black", "/black_bishoppiece.png", 'c', 8)
        black_rook = Piece("rook", "black", "/black_rookpiece.png", 'a', 8)
        black_rook2 = Piece("rook", "black", "/black_rookpiece.png", 'h', 8)
        
        global black_a_pawn
        global black_b_pawn
        global black_c_pawn
        global black_d_pawn
        global black_e_pawn
        global black_f_pawn
        global black_g_pawn
        global black_h_pawn

        black_a_pawn = Piece("pawn", "black", "/black_pawnpiece.png", 'a', 7)
        black_b_pawn = Piece("pawn", "black", "/black_pawnpiece.png", 'b', 7)
        black_c_pawn = Piece("pawn", "black", "/black_pawnpiece.png", 'c', 7)
        black_d_pawn = Piece("pawn", "black", "/black_pawnpiece.png", 'd', 7)
        black_e_pawn = Piece("pawn", "black", "/black_pawnpiece.png", 'e', 7)
        black_f_pawn = Piece("pawn", "black", "/black_pawnpiece.png", 'f', 7)
        black_g_pawn = Piece("pawn", "black", "/black_pawnpiece.png", 'g', 7)
        black_h_pawn = Piece("pawn", "black", "/black_pawnpiece.png", 'h', 7)

        black_pieces_list.add(black_king)
        black_pieces_list.add(black_queen)
        black_pieces_list.add(black_knight)
        black_pieces_list.add(black_knight2)
        black_pieces_list.add(black_bishop)
        black_pieces_list.add(black_bishop2)
        black_pieces_list.add(black_rook)
        black_pieces_list.add(black_rook2)
        black_pieces_list.add(black_a_pawn)
        black_pieces_list.add(black_b_pawn)
        black_pieces_list.add(black_c_pawn)
        black_pieces_list.add(black_d_pawn)
        black_pieces_list.add(black_e_pawn)
        black_pieces_list.add(black_f_pawn)
        black_pieces_list.add(black_g_pawn)
        black_pieces_list.add(black_h_pawn)

        global pawn_promotion
        pawn_promotion = False
        global white_king_check
        global black_king_check
        white_king_check = False
        black_king_check = False
        global white_checkmate
        global black_checkmate
        white_checkmate = False
        black_checkmate = False
        global draw
        draw = False
        global stale_mate
        stale_mate = False
        global fifty_move_draw
        fifty_move_draw = False
        global instant_draw
        global white_draw_TO
        global black_draw_TO
        instant_draw = False
        white_draw_TO = False
        black_draw_TO = False

        if turn % 2 == 0:
            color_turn = " white "
            castle = " has_no_queen_castle_rights "
            castle_king = " has_no_king_castle_rights "
            square_list_list.append(color_turn +castle+castle_king+ str(square_list))

    def place_pieces_on_board(self, new_square):
        global turn
        if turn % 2 == 0:
            x = 287
            square_list = dict()
            charlist = "abcdefgh"
            for char in charlist:
                x += 74
                y = 17
                for cif in range(8, 0, -1):
                    y += 74
                    square_int = char + str(cif)
                    square_list[square_int] = [str(x), str(y)]
            self.x = int(square_list[new_square][0]) - self.image_rect.w // 2
            self.y = int(square_list[new_square][1]) - self.image_rect.h // 2
            self.rect = self.image.get_rect(topleft=(self.x, self.y))
            for piece in white_pieces_list:
                piece.x = int(square_list[piece.square][0]) - piece.image_rect.w // 2
                piece.y = int(square_list[piece.square][1]) - piece.image_rect.h // 2
                piece.rect = piece.image.get_rect(topleft=(piece.x, piece.y))
            for piece in black_pieces_list:
                piece.x = int(square_list[piece.square][0]) - piece.image_rect.w // 2
                piece.y = int(square_list[piece.square][1]) - piece.image_rect.h // 2
                piece.rect = piece.image.get_rect(topleft=(piece.x, piece.y))
            self.placed = True
            time.sleep(0.15)

        if turn % 2 == 1:
            x = 953
            square_list = dict()
            charlist = "abcdefgh"
            for char in charlist:
                x -= 74
                y = 683
                for cif in range(8, 0, -1):
                    y -= 74
                    square_int = char + str(cif)
                    square_list[square_int] = [str(x), str(y)]
            self.x = int(square_list[new_square][0]) - self.image_rect.w // 2
            self.y = int(square_list[new_square][1]) - self.image_rect.h // 2
            self.rect = self.image.get_rect(topleft=(self.x, self.y))
            for piece in white_pieces_list:
                piece.x = int(square_list[piece.square][0]) - piece.image_rect.w // 2
                piece.y = int(square_list[piece.square][1]) - piece.image_rect.h // 2
                piece.rect = piece.image.get_rect(topleft=(piece.x, piece.y))
            for piece in black_pieces_list:
                piece.x = int(square_list[piece.square][0]) - piece.image_rect.w // 2
                piece.y = int(square_list[piece.square][1]) - piece.image_rect.h // 2
                piece.rect = piece.image.get_rect(topleft=(piece.x, piece.y))
            self.placed = True
            time.sleep(0.15)

    def draw_bord(surface):
        # draw 8x8 board
        global turn
        y = -20
        for row in range(8):
            x = 250
            y += 74
            if row % 2 == 0:
                for column in range(8):
                    x += 74
                    if column % 2 == 0:
                        pygame.draw.rect(surface, (255, 160, 160), pygame.Rect(x, y, 74, 74))
                    if column % 2 == 1:
                        pygame.draw.rect(surface, (7, 92, 156), pygame.Rect(x, y, 74, 74))
            elif row % 2 == 1:
                for column in range(8):
                    x += 74
                    if column % 2 == 1:
                        pygame.draw.rect(surface, (255, 160, 160), pygame.Rect(x, y, 74, 74))
                    if column % 2 == 0:
                        pygame.draw.rect(surface, (7, 92, 156), pygame.Rect(x, y, 74, 74))

        if turn % 2 == 0:
            y = 37
            for number in range(8, 0, -1):
                y += 74
                text = Text(str(number), 327, y, font_size=14, font_color=(103, 42, 125))
                text.draw_text(surface)
            char_list = "abcdefgh"
            x = 315
            for char in char_list:
                x += 74
                text = Text(char, x, 631, font_size=14, font_color=(103, 42, 125))
                text.draw_text(surface)
        if turn % 2 == 1:
            y = 703
            for number in range(8, 0, -1):
                y -= 74
                text = Text(str(number), 327, y, font_size=14, font_color=(103, 42, 125))
                text.draw_text(surface)
            char_list = "abcdefgh"
            x = 981
            for char in char_list:
                x -= 74
                text = Text(char, x, 631, font_size=14, font_color=(103, 42, 125))
                text.draw_text(surface)

    def image_move(self):
        global pawn_promotion
        global draw
        if self.active and not pawn_promotion and not draw and not stale_mate:
            pos = pygame.mouse.get_pos()
            self.rect.x = pos[0] - self.rect.w // 2
            self.rect.y = pos[1] - self.rect.h // 2
            self.placed = False

    def place_pieces(self):
        global white_king_check
        global black_king_check
        if not self.active and not self.placed:
            if self.rect.x < 324 - self.image_rect.w // 2 \
                    or self.rect.x > 916 - self.image_rect.w // 2 \
                    or self.rect.y < 55 - self.image_rect.h // 2 \
                    or self.rect.y > 646 - self.image_rect.h // 2:
                self.square = str(self.file + str(self.row))
                self.place_pieces_on_board(self.square)
                self.placed = True
            else:
                filelist = "abcdefgh"
                file_letter = []
                row_number = []
                for file in filelist:
                    file_letter.append(file)
                for row in range(1, 9):
                    row_number.append(row)
                pos = pygame.mouse.get_pos()
                global turn

                horizontal_move = math.ceil((int(pos[0] - (self.x + math.floor(self.image_rect.w / 2))) // 37) / 2)
                vertical_move = math.ceil((int(pos[1] - (self.y + math.floor(self.image_rect.h / 2))) // 37) / 2)

                if self.piece_name == "king" \
                        and horizontal_move in range(-1, 2) \
                        and vertical_move in range(-1, 2):
                    self.steps_x = horizontal_move
                    self.steps_y = vertical_move
                    self.white_king_castle = False
                    self.black_king_castle = False
                elif self.piece_name == "king" \
                        and self.piece_color == "white" \
                        and "MOVED" not in square_list[self.square] \
                        and "MOVED" not in square_list['a1'] \
                        and "white" in square_list['a1'] \
                        and "rook" in square_list['a1'] \
                        and horizontal_move in range(-4, -1, 1) \
                        and vertical_move == 0 \
                        and "OCCUPIED" not in square_list['b1'] \
                        and "OCCUPIED" not in square_list['c1'] \
                        and "OCCUPIED" not in square_list['d1'] \
                        and turn % 2 == 0:
                    self.white_king_castle = True
                    self.old_square = 'e1'
                    self.old_file = 'e'
                    self.old_row = 1
                    Piece.check_check_white(self, 'e1', 'd', 1)
                    if not self.white_king_check:
                        Piece.check_check_white(self, 'e1', 'c', 1)
                        if not self.white_king_check:
                            self.steps_x = -2
                            self.steps_y = 0
                            square_list[white_rook2.square].remove("OCCUPIED")
                            square_list[white_rook2.square].remove(white_rook2.piece_color)
                            square_list[white_rook2.square].remove("rook")
                            white_rook2.row = 1
                            white_rook2.file = 'd'
                            white_rook2.square = 'd1'
                            square_list[white_rook2.square].append("OCCUPIED")
                            square_list[white_rook2.square].append(white_rook2.piece_color)
                            square_list[white_rook2.square].append(white_rook2.piece_name)
                            square_list[white_rook2.square].append("MOVED")
                            white_rook2.x = int(square_list[white_rook2.square][0]) - white_rook2.image_rect.w // 2
                            white_rook2.y = int(square_list[white_rook2.square][1]) - white_rook2.image_rect.h // 2
                            white_rook2.rect = white_rook.image.get_rect(topleft=(white_rook2.x, white_rook2.y))
                            self.white_king_castle = False
                            self.white_king_check = False
                            white_king_check = False
                        else:
                            self.steps_x = 0
                            self.steps_y = 0
                            self.white_king_castle = False
                            self.white_king_check = False
                            white_king_check = False

                    else:
                        self.steps_x = 0
                        self.steps_y = 0
                        self.white_king_castle = False
                        self.white_king_check = False
                        white_king_check = False

                elif self.piece_name == "king" \
                        and self.piece_color == "white" \
                        and "MOVED" not in square_list[self.square] \
                        and "MOVED" not in square_list['h1'] \
                        and "white" in square_list['h1'] \
                        and "rook" in square_list['h1'] \
                        and horizontal_move in range(2, 4, 1) \
                        and vertical_move == 0 \
                        and "OCCUPIED" not in square_list['f1'] \
                        and "OCCUPIED" not in square_list['g1'] \
                        and turn % 2 == 0:
                    self.white_king_castle = True
                    self.old_square = 'e1'
                    self.old_file = 'e'
                    self.old_row = 1
                    Piece.check_check_white(self, 'e1', 'f', 1)
                    if not self.white_king_check:
                        Piece.check_check_white(self, 'e1', 'g', 1)
                        if not self.white_king_check:
                            self.steps_x = 2
                            self.steps_y = 0
                            del square_list[white_rook.square][2:]
                            white_rook.row = 1
                            white_rook.file = 'f'
                            white_rook.square = 'f1'
                            square_list[white_rook.square].append("OCCUPIED")
                            square_list[white_rook.square].append(white_rook.piece_color)
                            square_list[white_rook.square].append(white_rook.piece_name)
                            square_list[white_rook.square].append("MOVED")
                            white_rook.x = int(square_list[white_rook.square][0]) - white_rook.image_rect.w // 2
                            white_rook.y = int(square_list[white_rook.square][1]) - white_rook.image_rect.h // 2
                            white_rook.rect = white_rook.image.get_rect(topleft=(white_rook.x, white_rook.y))
                            self.white_king_castle = False
                            self.white_king_check = False
                            white_king_check = False
                        else:
                            self.steps_x = 0
                            self.steps_y = 0
                            self.white_king_castle = False
                            self.white_king_check= False
                            white_king_check = False
                    else:
                        self.steps_x = 0
                        self.steps_y = 0
                        self.white_king_castle = False
                        self.white_king_check = False
                        white_king_check = False

                elif self.piece_name == "king" \
                        and self.piece_color == "black" \
                        and "MOVED" not in square_list[self.square] \
                        and "MOVED" not in square_list['a8'] \
                        and "black" in square_list['a8'] \
                        and "rook" in square_list['a8'] \
                        and horizontal_move in range(2, 5) \
                        and vertical_move == 0 \
                        and "OCCUPIED" not in square_list['b8'] \
                        and "OCCUPIED" not in square_list['c8'] \
                        and "OCCUPIED" not in square_list['d8'] \
                        and turn % 2 == 1:
                    self.black_king_castle = True
                    self.old_square = 'e8'
                    self.old_file = 'e'
                    self.old_row = 8
                    Piece.check_check_black(self, 'e1', 'c', 8)
                    if not self.black_king_check:
                        Piece.check_check_black(self, 'e1', 'd', 8)
                        if not self.black_king_check:
                            self.steps_x = - 2
                            self.steps_y = 0
                            del square_list[black_rook.square][2:]
                            black_rook.square = 'd8'
                            black_rook.row = 8
                            black_rook.file = 'd'
                            square_list[black_rook.square].append("OCCUPIED")
                            square_list[black_rook.square].append(black_rook.piece_color)
                            square_list[black_rook.square].append(black_rook.piece_name)
                            square_list[black_rook.square].append("MOVED")
                            black_rook.x = int(square_list[black_rook.square][0]) - black_rook.image_rect.w // 2
                            black_rook.y = int(square_list[black_rook.square][1]) - black_rook.image_rect.h // 2
                            black_rook.rect = black_rook.image.get_rect(topleft=(black_rook.x, black_rook.y))
                            self.black_king_castle = False
                            self.black_king_check = False
                            black_king_check = False
                        else:
                            self.steps_x = 0
                            self.steps_y = 0
                            self.black_king_castle = False
                            self.black_king_check = False
                            black_king_check = False
                    else:
                        self.steps_x = 0
                        self.steps_y = 0
                        self.black_king_castle = False
                        self.black_king_check = False
                        black_king_check = False
                elif self.piece_name == "king" \
                        and self.piece_color == "black" \
                        and "MOVED" not in square_list[self.square] \
                        and "MOVED" not in square_list['h8'] \
                        and "black" in square_list['h8'] \
                        and "rook" in square_list['h8'] \
                        and horizontal_move in range(-3,-1, 1) \
                        and vertical_move == 0 \
                        and "OCCUPIED" not in square_list['f8'] \
                        and "OCCUPIED" not in square_list['g8'] \
                        and turn % 2 == 1:
                    self.black_king_castle = True
                    self.old_square = 'e8'
                    self.old_file = 'e'
                    self.old_row = 8
                    Piece.check_check_black(self, 'e1', 'f', 8)
                    if not self.black_king_check:
                        Piece.check_check_black(self, 'e1', 'g', 8)
                        if not self.black_king_check:
                            self.steps_x = - 2
                            self.steps_y = 0
                            del square_list[black_rook2.square][2:]
                            black_rook2.row = 8
                            black_rook2.file = 'f'
                            black_rook2.square = 'f8'
                            square_list[black_rook2.square].append("OCCUPIED")
                            square_list[black_rook2.square].append(black_rook2.piece_color)
                            square_list[black_rook2.square].append(black_rook2.piece_name)
                            square_list[black_rook2.square].append("MOVED")
                            black_rook2.x = int(square_list[black_rook2.square][0]) - black_rook2.image_rect.w // 2
                            black_rook2.y = int(square_list[black_rook2.square][1]) - black_rook2.image_rect.h // 2
                            black_rook2.rect = black_rook2.image.get_rect(topleft=(black_rook2.x, black_rook2.y))
                            self.black_king_castle = False
                            self.black_king_check = False
                            black_king_check = False
                        else:
                            self.steps_x = 0
                            self.steps_y = 0
                            self.black_king_castle = False
                            self.black_king_check = False
                            black_king_check = False
                    else:
                        self.steps_x = 0
                        self.steps_y = 0
                        self.black_king_castle = False
                        self.black_king_check = False
                        black_king_check = False
                else:
                    self.steps_x = 0
                    self.steps_y = 0


                if self.piece_name == "pawn":
                    if "MOVED" not in square_list[self.square]:
                        if self.piece_color == "white":
                            if horizontal_move == 0 \
                                    and vertical_move in range(-1, -3, -1):
                                self.steps_x = horizontal_move
                                self.steps_y = vertical_move
                            elif horizontal_move in range(-1, 2, 2) \
                                    and vertical_move == -1:
                                self.steps_x = horizontal_move
                                self.steps_y = vertical_move
                            else:
                                self.steps_x = 0
                                self.steps_y = 0
                        if self.piece_color == "black":
                            if horizontal_move == 0 \
                                    and vertical_move in range(-1, -3, -1):
                                self.steps_x = horizontal_move
                                self.steps_y = vertical_move
                            elif horizontal_move in range(-1, 2, 2) \
                                    and vertical_move == - 1:
                                self.steps_x = horizontal_move
                                self.steps_y = vertical_move
                            else:
                                self.steps_x = 0
                                self.steps_y = 0
                    elif "MOVED" in square_list[self.square]:
                        if self.piece_color == "white":
                            if horizontal_move == 0 \
                                    and vertical_move == -1:
                                self.steps_x = horizontal_move
                                self.steps_y = vertical_move
                            elif horizontal_move in range(-1, 2, 2) \
                                    and vertical_move == -1:
                                self.steps_x = horizontal_move
                                self.steps_y = vertical_move
                            else:
                                self.steps_x = 0
                                self.steps_y = 0
                        if self.piece_color == "black":
                            if horizontal_move == 0 \
                                    and vertical_move == - 1:
                                self.steps_x = horizontal_move
                                self.steps_y = vertical_move
                            elif horizontal_move in range(-1, 2, 2) \
                                    and vertical_move == - 1:
                                self.steps_x = horizontal_move
                                self.steps_y = vertical_move
                            else:
                                self.steps_x = 0
                                self.steps_y = 0

                if self.piece_name == "knight":
                    if horizontal_move in range(-1, 2, 2) \
                            and vertical_move in range(-2, 3, 4) \
                            or horizontal_move in range(-2, 3, 4) \
                            and vertical_move in range(-1, 2, 2):
                        self.steps_x = horizontal_move
                        self.steps_y = vertical_move
                    else:
                        self.steps_x = 0
                        self.steps_y = 0

                if self.piece_name == "bishop":
                    if horizontal_move in range(-8, 8) \
                            and vertical_move in range(-8, 8) \
                            and abs(horizontal_move) == abs(vertical_move):
                        self.steps_x = horizontal_move
                        self.steps_y = vertical_move
                    else:
                        self.steps_x = 0
                        self.steps_y = 0

                if self.piece_name == "rook":
                    if horizontal_move in range(-8, 8) \
                            and vertical_move == 0 \
                            or horizontal_move == 0 \
                            and vertical_move in range(-8, 8):
                        self.steps_x = horizontal_move
                        self.steps_y = vertical_move
                    else:
                        self.steps_x = 0
                        self.steps_y = 0

                if self.piece_name == "queen":
                    if horizontal_move in range(-8, 8) \
                            and vertical_move == 0 \
                            or horizontal_move == 0 \
                            and vertical_move in range(-8, 8) \
                            or horizontal_move in range(-8, 8) \
                            and vertical_move in range(-8, 8) \
                            and abs(horizontal_move) == abs(vertical_move):
                        self.steps_x = horizontal_move
                        self.steps_y = vertical_move
                    else:
                        self.steps_x = 0
                        self.steps_y = 0


                if turn % 2 == 0:
                    self.new_row = row_number[(row_number.index(self.row) - self.steps_y)]
                    self.new_file = file_letter[(file_letter.index(self.file) + self.steps_x)]
                if turn % 2 == 1:
                    self.new_row = row_number[(row_number.index(self.row) + self.steps_y)]
                    self.new_file = file_letter[(file_letter.index(self.file) - self.steps_x)]
                self.new_square = (str(self.new_file) + str(self.new_row))

                # make a list of the traveled squares in order to check if they're occupied
                # only the knight can jump over other pieces so we count that one out
                # Since we have 4 directions we need to make 4 IF's to account for that ( if (+x, +y), if (+x - y), if (-x, +y), if (-x, -y)
                between_square_list = []
                if self.piece_name != "knight":
                    between_file_list = []
                    between_row_list = []
                    global range_y
                    global range_x
                    global between_file
                    global between_row
                    if self.piece_name != "knight":
                        if self.steps_x > -1:
                            range_x = range(1, self.steps_x)
                        elif self.steps_x < 1:
                            range_x = range(-1, self.steps_x, -1)
                        if self.steps_y > -1:
                            range_y = range(1, self.steps_y)
                        elif self.steps_y < 1:
                            range_y = range(-1, self.steps_y, -1)
                        if self.steps_x == 0:
                            for i in range_y:
                                between_file = self.new_file
                                between_file_list.append(between_file)
                                if turn % 2 == 0:
                                    between_row = row_number[(row_number.index(self.new_row) + i)]
                                elif turn % 2 == 1:
                                    between_row = row_number[(row_number.index(self.new_row) - i)]
                                between_row_list.append(between_row)
                        elif self.steps_y == 0:
                            for i in range_x:
                                between_row = self.new_row
                                between_row_list.append(between_row)
                                if turn % 2 == 0:
                                    between_file = file_letter[(file_letter.index(self.new_file) - i)]
                                elif turn % 2 == 1:
                                    between_file = file_letter[(file_letter.index(self.new_file) + i)]
                                between_file_list.append(between_file)
                        else:
                            for i in range_x:
                                if turn % 2 == 0:
                                    between_file = file_letter[(file_letter.index(self.new_file) - i)]
                                elif turn  % 2 == 1:
                                    between_file = file_letter[(file_letter.index(self.new_file) + i)]
                                between_file_list.append(between_file)
                            for i in range_y:
                                if turn % 2 == 0:
                                    between_row = row_number[(row_number.index(self.new_row) + i)]
                                elif turn % 2 == 1:
                                    between_row = row_number[(row_number.index(self.new_row) - i)]
                                between_row_list.append(between_row)
                    for between_square in range(len(between_file_list)):
                        between_square = str(between_file_list[between_square]) + str(between_row_list[between_square])
                        between_square_list.append(between_square)

                # before placing piece check if square is occupied by own piece color
                # IF block handles placing if the destination square is not occupied by own pieces or other pieces
                # First if/and block (in IF) handles if destination square is not occupied and the traveled squares are not occupied
                # knight and pawn are later addressed because the knight can jump over own pieces, and the pawn can move diagonally
                # but only with taking pieces which is addressed in the elif block
                # The second or/and block (in IF) handles if the between values don't exist(moves 1 square). because between_squares_list has a value this
                # has to be addressed
                # The third or/and block (in IF) handles pawn moves if only moved vertically
                # The fourth or/and block handles knight since it can jump over pieces and therefore is not dependent on between_files_list
                # The fifth or/and block handles king castling. Kinda hacky solution but because te rook moves earlier than the king the
                # between square gets occupied bij the rook. therefore, we make an exception for the occupied between squares (between king and rook)

                global last_file
                global last_row
                global last_piece
                global before_row
                if self.piece_color == "white" \
                        and "OCCUPIED" not in square_list[self.new_square] \
                        and self.piece_color not in square_list[self.new_square] \
                        and self.piece_name != "pawn" \
                        and self.piece_name != "knight" \
                        and turn % 2 == 0 \
                        and between_square_list != [] \
                        and all("OCCUPIED" not in square_list[square] for square in between_square_list) \
                        or self.piece_color == "white" \
                        and "OCCUPIED" not in square_list[self.new_square] \
                        and self.piece_color not in square_list[self.new_square] \
                        and self.piece_name != "pawn" \
                        and self.piece_name != "knight" \
                        and turn % 2 == 0 \
                        and between_square_list == [] \
                        or self.piece_color == "white" \
                        and self.piece_name == "pawn" \
                        and turn % 2 == 0 \
                        and "OCCUPIED" not in square_list[self.new_square] \
                        and self.piece_color not in square_list[self.new_square] \
                        and self.steps_x == 0 \
                        and all("OCCUPIED" not in square_list[square] for square in between_square_list) \
                        or self.piece_color == "white" \
                        and self.piece_name == "knight" \
                        and "OCCUPIED" not in square_list[self.new_square] \
                        and self.piece_color not in square_list[self.new_square] \
                        and turn % 2 == 0 \
                        or self.piece_color == "white" \
                        and self.piece_name == "king" \
                        and turn % 2 == 0 \
                        and "MOVED" not in square_list[self.square] \
                        and any("OCCUPIED" in square_list[square] for square in between_square_list):

                    turn += 1


                    print("WHITE MOVES")
                    #print("turn: " + str(turn))

                    self.old_square = self.square
                    self.old_file = self.file
                    self.old_row = self.row

                    # this before row we need to know for en passant taking. To check if the before row is the begin_row
                    # in the elif block for en passant we put that the before_row has to be 7.
                    # This means en passant move is only possible if the last move of black is from row 7
                    before_row = self.row

                    del square_list[self.square][2:]

                    square_list[self.new_square].append("OCCUPIED")
                    square_list[self.new_square].append(self.piece_color)
                    square_list[self.new_square].append(self.piece_name)

                    Piece.check_check_white(self, self.old_square, self.new_file, self.new_row)
                    Piece.check_check_black(self, self.old_square, self.new_file, self.new_row)

                    if self.black_king_check:
                        self.check_checkmate_black()

                    if not self.black_king_check:
                        last_file = self.new_file
                        last_row = self.new_row
                        last_piece = self.piece_name
                        self.stale_mate_black()

                    if not self.white_king_check:
                        if self.piece_name == "king" \
                                or self.piece_name == "rook" \
                                or self.piece_name == "pawn":
                            square_list[self.new_square].append("MOVED")
                        self.threefold_repetition()
                        last_file = self.new_file
                        last_row = self.new_row
                        last_piece = self.piece_name
                        capture = "no capture "
                        self.fifty_move_rule(capture, last_piece)
                    if self.white_king_check:
                        self.place_back_white(self.new_square, self.old_square)

                    self.square = self.new_square
                    self.place_pieces_on_board(self.new_square)
                    self.file = self.new_file
                    self.row = self.new_row
                    last_file = self.new_file
                    last_row = self.row
                    last_piece = self.piece_name


                elif self.piece_color == "black" \
                        and "OCCUPIED" not in square_list[self.new_square] \
                        and self.piece_color not in square_list[self.new_square] \
                        and self.piece_name != "pawn" \
                        and self.piece_name != "knight" \
                        and turn % 2 == 1 \
                        and between_square_list != [] \
                        and all("OCCUPIED" not in square_list[square] for square in between_square_list) \
                        or self.piece_color == "black" \
                        and "OCCUPIED" not in square_list[self.new_square] \
                        and self.piece_color not in square_list[self.new_square] \
                        and self.piece_name != "pawn" \
                        and self.piece_name != "knight" \
                        and turn % 2 == 1 \
                        and between_square_list == [] \
                        or self.piece_color == "black" \
                        and self.piece_name == "pawn" \
                        and turn % 2 == 1 \
                        and "OCCUPIED" not in square_list[self.new_square] \
                        and self.piece_color not in square_list[self.new_square] \
                        and self.steps_x == 0 \
                        and all("OCCUPIED" not in square_list[square] for square in between_square_list) \
                        or self.piece_color == "black" \
                        and self.piece_name == "knight" \
                        and "OCCUPIED" not in square_list[self.new_square] \
                        and self.piece_color not in square_list[self.new_square] \
                        and turn % 2 == 1 \
                        or self.piece_color == "black" \
                        and self.piece_name == "king" \
                        and turn % 2 == 1 \
                        and "MOVED" not in square_list[self.square] \
                        and any("OCCUPIED" in square_list[square] for square in between_square_list):


                    print("BLACK MOVES")
                    turn += 1
                    try:
                        if black_a_pawn.new_row == 1 and black_a_pawn in black_pieces_list:
                            turn = 3
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if black_b_pawn.new_row == 1 and black_b_pawn in black_pieces_list:
                            turn = 3
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if black_c_pawn.new_row == 1 and black_c_pawn in black_pieces_list:
                            turn = 3
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if black_d_pawn.new_row == 1 and black_d_pawn in black_pieces_list:
                            turn = 3
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if black_e_pawn.new_row == 1 and black_e_pawn in black_pieces_list:
                            turn = 3
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if black_f_pawn.new_row == 1 and black_f_pawn in black_pieces_list:
                            turn = 3
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if  black_g_pawn.new_row == 1 and black_g_pawn in black_pieces_list:
                            turn = 3
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if black_h_pawn.new_row == 1 and black_h_pawn in black_pieces_list:
                            turn = 3
                            pawn_promo = True
                    except AttributeError:
                        pass

                    self.old_square = self.square
                    self.old_file = self.file
                    self.old_row = self.row
                    # this before row we need to know for en passant taking. To check if the before row is the begin_row
                    before_row = self.row

                    del square_list[self.square][2:]


                    square_list[self.new_square].append("OCCUPIED")
                    square_list[self.new_square].append(self.piece_color)
                    square_list[self.new_square].append(self.piece_name)

                    Piece.check_check_white(self, self.old_square, self.new_file, self.new_row)
                    Piece.check_check_black(self, self.old_square, self.new_file, self.new_row)
                    if self.white_king_check:
                        Piece.check_checkmate_white(self)
                    if not self.white_king_check:
                        last_file = self.new_file
                        last_row = self.new_row
                        last_piece = self.piece_name
                        self.stale_mate_white()
                    if not self.black_king_check:
                        if self.piece_name == "king" \
                                or self.piece_name == "rook" \
                                or self.piece_name == "pawn":
                            square_list[self.new_square].append("MOVED")
                        last_piece = self.piece_name
                        capture = "no capture "
                        self.fifty_move_rule(capture, last_piece)
                        self.threefold_repetition()
                    if self.black_king_check:
                        self.place_back_black(self.new_square, self.old_square)
                    self.square = self.new_square
                    self.place_pieces_on_board(self.new_square)
                    self.file = self.new_file
                    self.row = self.new_row
                    last_file = self.new_file
                    last_row = self.row
                    last_piece = self.piece_name


                # IF anything is to take
                elif self.piece_color == "white" \
                        and "OCCUPIED" in square_list[self.new_square] \
                        and "black" in square_list[self.new_square] \
                        and self.piece_name != "pawn" \
                        and turn % 2 == 0 \
                        and all("OCCUPIED" not in square_list[square] for square in between_square_list) \
                        or self.piece_color == "white" \
                        and "OCCUPIED" in square_list[self.new_square] \
                        and "black" in square_list[self.new_square] \
                        and self.piece_name == "pawn" \
                        and turn % 2 == 0 \
                        and all("OCCUPIED" not in square_list[square] for square in between_square_list) \
                        and abs(self.steps_x) == 1:
                    print("WHITE TAKES")
                    turn += 1
                    try:
                        if white_a_pawn.new_row == 8 and white_a_pawn in white_pieces_list:
                            turn = 2
                            pawn_promo =  True
                    except AttributeError:
                        pass
                    try:
                        if white_b_pawn.new_row == 8 and white_b_pawn in white_pieces_list:
                            turn = 2
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if white_c_pawn.new_row == 8 and white_c_pawn in white_pieces_list:
                            turn = 2
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if white_d_pawn.new_row == 8 and white_d_pawn in white_pieces_list:
                            turn = 2
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if white_e_pawn.new_row == 8 and white_e_pawn in white_pieces_list:
                            turn = 2
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if white_f_pawn.new_row == 8 and white_f_pawn in white_pieces_list:
                            turn = 2
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if white_g_pawn.new_row == 8 and white_g_pawn in white_pieces_list:
                            turn = 2
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if white_h_pawn.new_row == 8 and white_h_pawn in white_pieces_list:
                            turn = 2
                            pawn_promo = True
                    except AttributeError:
                        pass

                    self.old_square = self.square
                    # self.old versions are for check checking
                    self.old_file = self.file
                    self.old_row = self.row

                    old_take_square = self.new_square
                    old_values = square_list[self.new_square][2:]

                    del square_list[self.square][2:]
                    del square_list[self.new_square][2:]
                    square_list[self.new_square].append("OCCUPIED")
                    square_list[self.new_square].append(self.piece_color)
                    square_list[self.new_square].append(self.piece_name)


                    Piece.check_check_white(self, self.old_square, self.new_file, self.new_row)
                    Piece.check_check_black(self, self.old_square, self.new_file, self.new_row)
                    if self.black_king_check:
                        self.check_checkmate_black()
                    if not self.white_king_check:
                        if self.piece_name == "king" \
                                or self.piece_name == "rook" \
                                or self.piece_name == "pawn":
                            square_list[self.new_square].append("MOVED")
                        for piece in black_pieces_list:
                            if piece.square == self.new_square:
                                black_pieces_list.remove(piece)
                        self.threefold_repetition()
                        last_file = self.new_file
                        last_row = self.new_row
                        last_piece = self.piece_name
                        capture = "capture "
                        self.fifty_move_rule(capture, last_piece)
                    if not self.black_king_check:
                        last_file = self.new_file
                        last_row = self.new_row
                        last_piece = self.piece_name
                        self.stale_mate_black()
                    if self.white_king_check:
                        self.place_back_white(self.new_square, self.old_square)
                        for values in old_values:
                            square_list[old_take_square].append(values)

                    self.square = self.new_square
                    self.place_pieces_on_board(self.new_square)
                    before_last_row = self.row
                    self.file = self.new_file
                    self.row = self.new_row
                    last_file = self.new_file
                    last_row = self.row
                    last_piece = self.piece_name

                elif self.piece_color == "black" \
                        and "OCCUPIED" in square_list[self.new_square] \
                        and "white" in square_list[self.new_square] \
                        and self.piece_name != "pawn" \
                        and turn % 2 == 1 \
                        and all("OCCUPIED" not in square_list[square] for square in between_square_list) \
                        or self.piece_color == "black" \
                        and "OCCUPIED" in square_list[self.new_square] \
                        and "white" in square_list[self.new_square] \
                        and self.piece_name == "pawn" \
                        and turn % 2 == 1 \
                        and all("OCCUPIED" not in square_list[square] for square in between_square_list) \
                        and abs(self.steps_x) == 1:
                    print("BLACK TAKES")
                    turn += 1
                    try:
                        if black_a_pawn.new_row == 1 and black_a_pawn in black_pieces_list:
                            turn = 3
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if black_b_pawn.new_row == 1 and black_b_pawn in black_pieces_list:
                            turn = 3
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if black_c_pawn.new_row == 1 and black_c_pawn in black_pieces_list:
                            turn = 3
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if black_d_pawn.new_row == 1 and black_d_pawn in black_pieces_list:
                            turn = 3
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if black_e_pawn.new_row == 1 and black_e_pawn in black_pieces_list:
                            turn = 3
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if black_f_pawn.new_row == 1 and black_f_pawn in black_pieces_list:
                            turn = 3
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if  black_g_pawn.new_row == 1 and black_g_pawn in black_pieces_list:
                            turn = 3
                            pawn_promo = True
                    except AttributeError:
                        pass
                    try:
                        if black_h_pawn.new_row == 1 and black_h_pawn in black_pieces_list:
                            turn = 3
                            pawn_promo = True
                    except AttributeError:
                        pass

                    self.old_square = self.square
                    # self.old versions are for check checking
                    self.old_file = self.file
                    self.old_row = self.row

                    old_take_square = self.new_square
                    old_values = square_list[self.new_square][2:]

                    del square_list[self.square][2:]
                    del square_list[self.new_square][2:]
                    square_list[self.new_square].append("OCCUPIED")
                    square_list[self.new_square].append(self.piece_color)
                    square_list[self.new_square].append(self.piece_name)

                    Piece.check_check_white(self, self.old_square, self.new_file, self.new_row)
                    Piece.check_check_black(self, self.old_square, self.new_file, self.new_row)

                    if self.white_king_check:
                        Piece.check_checkmate_white(self)
                    if not self.black_king_check:
                        if self.piece_name == "king" \
                                or self.piece_name == "rook" \
                                or self.piece_name == "pawn":
                            square_list[self.new_square].append("MOVED")
                        for piece in white_pieces_list:
                            if piece.square == self.new_square:
                                white_pieces_list.remove(piece)
                        self.threefold_repetition()
                        last_piece = self.piece_name
                        capture = "capture "
                        self.fifty_move_rule(capture, last_piece)
                    if not self.white_king_check:
                        last_file = self.new_file
                        last_row = self.new_row
                        last_piece = self.piece_name
                        self.stale_mate_white()
                    if self.black_king_check:
                        self.place_back_black(self.new_square, self.old_square)
                        for values in old_values:
                            square_list[old_take_square].append(values)

                    self.square = self.new_square
                    self.place_pieces_on_board(self.new_square)
                    self.file = self.new_file
                    self.row = self.new_row
                    last_file = self.new_file
                    last_row = self.row
                    last_piece = self.piece_name

                #This elif block handles taking en passant for white is taking
                elif self.piece_color == "white" \
                         and self.piece_name == "pawn" \
                         and turn % 2 == 0 \
                         and "OCCUPIED" not in square_list[self.new_square] \
                         and "OCCUPIED" in square_list[file_letter[(file_letter.index(self.file) + self.steps_x)] + str(self.row)] \
                         and abs(self.steps_x) == 1 \
                         and last_piece == "pawn" \
                         and last_row == 5 \
                         and str(last_file) == str(file_letter[(file_letter.index(self.file) + self.steps_x)]) \
                         and self.row == 5 \
                         and before_row == 7:
                    print("WHITE TAKES EN PASSANT")
                    turn += 1

                    self.old_square = self.square
                    # self.old versions are for check checking
                    self.old_file = self.file
                    self.old_row = self.row

                    old_take_square = file_letter[(file_letter.index(self.file) + self.steps_x)] + str(self.row)
                    old_values = square_list[file_letter[(file_letter.index(self.file) + self.steps_x)] + str(self.row)][2:]

                    del square_list[file_letter[(file_letter.index(self.file) + self.steps_x)] + str(self.row)][2:]
                    del square_list[self.square][2:]


                    square_list[self.new_square].append("OCCUPIED")
                    square_list[self.new_square].append(self.piece_color)
                    square_list[self.new_square].append(self.piece_name)


                    Piece.check_check_white(self, self.old_square, self.new_file, self.new_row)
                    Piece.check_check_black(self, self.old_square, self.new_file, self.new_row)
                    if self.black_king_check:
                        self.check_checkmate_black()
                    if not self.white_king_check:
                        pawn_file = file_letter[(file_letter.index(self.file) + self.steps_x)]
                        white_king_check = False
                        for file in file_letter:
                            if pawn_file == 'a':
                                black_pieces_list.remove(black_a_pawn)
                            elif pawn_file == 'b':
                                black_pieces_list.remove(black_b_pawn)
                            elif pawn_file == 'c':
                                black_pieces_list.remove(black_c_pawn)
                            elif pawn_file == 'd':
                                black_pieces_list.remove(black_d_pawn)
                            elif pawn_file == 'e':
                                black_pieces_list.remove(black_e_pawn)
                            elif pawn_file == 'f':
                                black_pieces_list.remove(black_f_pawn)
                            elif pawn_file == 'g':
                                black_pieces_list.remove(black_g_pawn)
                            elif pawn_file == 'h':
                                black_pieces_list.remove(black_h_pawn)
                        square_list[self.new_square].append("MOVED")
                        self.threefold_repetition()
                        last_piece = self.piece_name
                        capture = "capture "
                        self.fifty_move_rule(capture, last_piece)
                    if not self.black_king_check:
                        last_file = self.new_file
                        last_row = self.new_row
                        last_piece = self.piece_name
                        self.stale_mate_black()
                    if self.white_king_check:
                        for values in old_values:
                            square_list[old_take_square].append(values)


                    self.square = self.new_square
                    self.place_pieces_on_board(self.new_square)
                    self.file = self.new_file
                    self.row = self.new_row
                    last_file = self.new_file
                    last_row = self.row
                    last_piece = self.piece_name

                # handles en passant if pawn is black = taking
                elif self.piece_color == "black" \
                         and self.piece_name == "pawn" \
                         and turn % 2 == 1 \
                         and "OCCUPIED" not in square_list[self.new_square] \
                         and "OCCUPIED" in square_list[file_letter[(file_letter.index(self.file) - self.steps_x)] + str(self.row)] \
                         and abs(self.steps_x) == 1 \
                         and last_piece == "pawn" \
                         and last_row == 4 \
                         and str(last_file) == str(file_letter[(file_letter.index(self.file) - self.steps_x)]) \
                         and self.row == 4 \
                         and before_row == 2:
                    print("BLACK TAKES EN PASSANT")
                    turn += 1

                    self.old_square = self.square
                    # self.old versions are for check checking
                    self.old_file = self.file
                    self.old_row = self.row

                    old_take_square = file_letter[(file_letter.index(self.file) - self.steps_x)] + str(self.row)
                    old_values = square_list[file_letter[(file_letter.index(self.file) - self.steps_x)] + str(self.row)][2:]

                    del square_list[self.square][2:]
                    del square_list[file_letter[(file_letter.index(self.file) - self.steps_x)] + str(self.row)][2:]

                    square_list[self.new_square].append("OCCUPIED")
                    square_list[self.new_square].append(self.piece_color)
                    square_list[self.new_square].append(self.piece_name)


                    Piece.check_check_white(self, self.old_square, self.new_file, self.new_row)
                    Piece.check_check_black(self, self.old_square, self.new_file, self.new_row)
                    if self.white_king_check:
                        self.check_checkmate_white()
                    if not self.black_king_check:
                        black_king_check = False
                        pawn_file = file_letter[(file_letter.index(self.file) - self.steps_x)]
                        for file in file_letter:
                            if pawn_file == 'a':
                                white_pieces_list.remove(white_a_pawn)
                            elif pawn_file == 'b':
                                white_pieces_list.remove(white_b_pawn)
                            elif pawn_file == 'c':
                                white_pieces_list.remove(white_c_pawn)
                            elif pawn_file == 'd':
                                white_pieces_list.remove(white_d_pawn)
                            elif pawn_file == 'e':
                                white_pieces_list.remove(white_e_pawn)
                            elif pawn_file == 'f':
                                white_pieces_list.remove(white_f_pawn)
                            elif pawn_file == 'g':
                                white_pieces_list.remove(white_g_pawn)
                            elif pawn_file == 'h':
                                white_pieces_list.remove(white_h_pawn)
                        square_list[self.new_square].append("MOVED")
                        self.threefold_repetition()
                        last_piece = self.piece_name
                        capture = "capture "
                        self.fifty_move_rule(capture, last_piece)
                    if not self.white_king_check:
                        last_file = self.new_file
                        last_row = self.row
                        last_piece = self.piece_name
                        self.stale_mate_white()
                    if self.black_king_check:
                        for values in old_values:
                            square_list[old_take_square].append(values)

                    self.square = self.new_square
                    self.place_pieces_on_board(self.new_square)
                    self.file = self.new_file
                    self.row = self.new_row
                    last_file = self.new_file
                    last_row = self.row
                    last_piece = self.piece_name

                    # If for some reason can't move to the new square, piece goes back to original square
                else:
                    print("ELSE")
                    self.square = str(self.file + str(self.row))
                    self.place_pieces_on_board(self.square)
                #print(square_list)
                #print("self.square = "+self.square)

    def check_check_white(self, old_square, new_file, new_row):
        file_list = "abcdefgh"
        file_letter = []
        row_number = []
        for file in file_list:
            file_letter.append(file)
        for row in range(1, 9):
            row_number.append(row)

        if self.piece_name == "king" \
                and self.piece_color == "white" \
                and self.white_king_castle:
            white_king_square = (new_file + str(new_row))
            white_king_file = new_file
            white_king_row = new_row
            king_file_index = file_letter.index(white_king_file)
            king_row_number = row_number.index(white_king_row)
        elif self.piece_name == "king" \
                and self.piece_color == "white" \
                and not self.white_king_castle:
            try:
                white_king_square = (self.new_file + str(self.new_row))
                white_king_file = self.new_file
                white_king_row = self.new_row
                king_file_index = file_letter.index(white_king_file)
                king_row_number = row_number.index(white_king_row)
            except AttributeError:
                white_king_square = white_king.file + str(white_king.row)
                white_king_file = white_king.file
                white_king_row = white_king.row
                king_file_index = file_letter.index(white_king_file)
                king_row_number = row_number.index(white_king_row)
        else:
            white_king_square = white_king.file + str(white_king.row)
            white_king_file = white_king.file
            white_king_row = white_king.row
            king_file_index = file_letter.index(white_king_file)
            king_row_number = row_number.index(white_king.row)



        global turn
        global white_king_check


        between_check_square_list = []
        charlistje = "abcdefgh"
        for charje in charlistje:
            for cifje in range(1, 9):
                square_bet = charje + str(cifje)
                between_check_square_list.append(square_bet)

        king_index = between_check_square_list.index(white_king_square)


        self.white_check_list = list()

        # we make a few lists of squares in which the king can be "touched" by other pieces
        # these squares can be checked if they're occupied by pieces that potentially check the king


        # this next block addresses moving own pieces and thereby self checking for if black piece is bishop, pawn or queen on the diagonal
        # by checking if any pieces are blocking the check, or if the distance is one square(diagonal)
        # the king has to move out of check or the check piece has to be taken.
        # This definition is called after a new move has been made, it evaluates this move and places it back if the king is (still) in check
        # make list of diagonal line right up from king position

        diagonal_check_list = []
        for i in [check_square for check_square in range(-8, 8)]:
            try:
                if king_file_index - i > -1 \
                        and king_row_number + i > -1 \
                        and file_letter[king_file_index - i] != white_king_file:
                    check_square = (file_letter[king_file_index - i] + str(row_number[king_row_number + i]))
                    if check_square not in diagonal_check_list:
                        diagonal_check_list.append(check_square)
            except IndexError:
                pass
        # make list of diagonal line right down from king position
        for i in [check_square for check_square in range(-8, 8)]:
            try:
                if king_file_index + i > -1 \
                        and king_row_number + i > -1 \
                        and file_letter[king_file_index + i] != white_king_file:
                    check_square = (file_letter[king_file_index + i] + str(row_number[king_row_number + i]))
                    if check_square not in diagonal_check_list:
                        diagonal_check_list.append(check_square)
            except IndexError:
                pass
        #print("diagonal checklist for "+str(king_index)+"is list "+ str(diagonal_check_list))

        self.between_bishop_squares_list = dict()
        for check_square in diagonal_check_list:
            if "bishop" in square_list[check_square] \
                    and "black" in square_list[check_square] \
                    or "queen" in square_list[check_square] \
                    and "black" in square_list[check_square] \
                    or "pawn" in square_list[check_square] \
                    and "black" in square_list[check_square] \
                    or "king" in square_list[check_square] \
                    and "black" in square_list[check_square]:
                bishop_queen_index = between_check_square_list.index(check_square)
                if abs(king_index - bishop_queen_index) > 7 \
                        and abs(king_index - bishop_queen_index) != 9 \
                        and "bishop" in square_list[check_square] \
                        or abs(king_index - bishop_queen_index) > 7 \
                        and abs(king_index - bishop_queen_index) != 9 \
                        and "queen" in square_list[check_square]:
                    between_bishop_squares = list()
                    if king_index > bishop_queen_index:
                        if (king_index - bishop_queen_index) % 7 == 0:
                            for squares in range(bishop_queen_index + 7, king_index, 7):
                                if between_check_square_list[squares] not in between_bishop_squares:
                                    between_bishop_squares.append(between_check_square_list[squares])
                        elif (king_index - bishop_queen_index) % 9 == 0:
                            for squares in range(bishop_queen_index + 9, king_index, 9):
                                if between_check_square_list[squares] not in between_bishop_squares:
                                    between_bishop_squares.append(between_check_square_list[squares])
                    elif king_index < bishop_queen_index:
                        if abs((king_index - bishop_queen_index) % 7) == 0:
                            for squares in range(king_index + 7, bishop_queen_index, 7):
                                if between_check_square_list[squares] not in between_bishop_squares:
                                    between_bishop_squares.append(between_check_square_list[squares])
                        elif abs(king_index - bishop_queen_index) % 9 == 0:
                            for squares in range(king_index + 9, bishop_queen_index, 9):
                                if between_check_square_list[squares] not in between_bishop_squares:
                                    between_bishop_squares.append(between_check_square_list[squares])
                    block_squares = between_bishop_squares.copy()
                    block_squares.append(between_check_square_list[bishop_queen_index])
                    self.between_bishop_squares_list.setdefault(str(square_list[check_square][4]), []).append(block_squares)
                    if any(("OCCUPIED" and "white") in square_list[square] for square in between_bishop_squares) \
                            or between_bishop_squares == []:
                        white_check = "FALSE"
                        self.white_check_list.append(white_check)
                    elif any(("OCCUPIED" and "black" and "pawn") in square_list[square] for square in between_bishop_squares) \
                            or any(("OCCUPIED" and "black" and "king") in square_list[square] for square in between_bishop_squares) \
                            or any(("OCCUPIED" and "black" and "knight") in square_list[square] for square in between_bishop_squares) \
                            or any(("OCCUPIED" and "black" and "rook") in square_list[square] for square in between_bishop_squares):
                        white_check = "FALSE"
                        self.white_check_list.append(white_check)
                    else:
                        if turn % 2 == 1 and self.piece_color == "white" and self.white_king_castle:
                            white_check = "TRUE"
                            self.white_check_list.append(white_check)
                        elif turn % 2 == 1 and self.piece_color == "white" and not self.white_king_castle:
                            white_check = "TRUE"
                            self.white_check_list.append(white_check)
                        elif turn % 2 == 0 and self.piece_color == "black":
                            white_check = "TRUE"
                            self.white_check_list.append(white_check)
                elif  "bishop" in square_list[check_square] \
                        and abs(king_index - bishop_queen_index) == 7 \
                        or "bishop" in square_list[check_square] \
                        and abs(king_index - bishop_queen_index) == 9 \
                        or "pawn" in square_list[check_square] \
                        and king_index - bishop_queen_index == 7 \
                        or "pawn" in square_list[check_square] \
                        and bishop_queen_index - king_index == 9 \
                        or "king" in square_list[check_square] \
                        and abs(king_index - bishop_queen_index) == 9 \
                        or "king" in square_list[check_square] \
                        and abs(king_index - bishop_queen_index) == 7 \
                        or "queen" in square_list[check_square] \
                        and abs(king_index - bishop_queen_index) == 9 \
                        or "queen" in square_list[check_square] \
                        and abs(king_index - bishop_queen_index) == 7:
                    self.between_bishop_squares_list.setdefault(str(square_list[check_square][4]), []).append([check_square])
                    if turn % 2 == 1 and self.piece_color == "white" and self.white_king_castle:
                        white_check = "TRUE"
                        self.white_check_list.append(white_check)
                    elif turn % 2 == 1 and self.piece_color == "white" and not self.white_king_castle:
                        white_check = "TRUE"
                        self.white_check_list.append(white_check)
                    elif turn % 2 == 0 and self.piece_color == "black":
                        white_check = "TRUE"
                        self.white_check_list.append(white_check)


        # make list of horizontal line
        straight_check_list = []
        for i in [check_square_straight for check_square_straight in range(0, 8) if check_square_straight != king_file_index]:
            try:
                check_square_straight = (file_letter[i] + str(white_king_row))
                if check_square_straight not in straight_check_list:
                    straight_check_list.append(check_square_straight)
            except IndexError:
                pass
        # add vertical lines
        for i in [check_square_straight for check_square_straight in range(0, 8) if check_square_straight != king_row_number]:
            try:
                check_square_straight = (white_king_file + str(row_number[i]))
                if check_square_straight not in straight_check_list:
                    straight_check_list.append(check_square_straight)
            except IndexError:
                pass
        #print("straight checklist for " + str(king_index) + " is list " + str(straight_check_list))

        for check_square_straight in straight_check_list:
            if "rook" in square_list[check_square_straight] \
                    and "black" in square_list[check_square_straight] \
                    or "queen" in square_list[check_square_straight] \
                    and "black" in square_list[check_square_straight] \
                    or "king" in square_list[check_square_straight] \
                    and "black" in square_list[check_square_straight]:
                check_piece_index = between_check_square_list.index(check_square_straight)
                if abs(king_index - check_piece_index) > 1 \
                        and abs(king_index - check_piece_index) != 8 \
                        and "rook" in square_list[check_square_straight] \
                        or abs(king_index - check_piece_index) > 1 \
                        and abs(king_index - check_piece_index) != 8 \
                        and "queen" in square_list[check_square_straight]:
                    between_rook_queen_squares = list()
                    if king_index > check_piece_index:
                        if 8 > (king_index - check_piece_index) > 0:
                            for squares2 in range(check_piece_index + 1, king_index,  1):
                                if between_check_square_list[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(between_check_square_list[squares2])
                        if abs(king_index - check_piece_index) % 8 == 0:
                            for squares2 in range(check_piece_index + 8, king_index, 8):
                                if between_check_square_list[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(between_check_square_list[squares2])
                    elif king_index < check_piece_index:
                        if 8 > abs(king_index - check_piece_index) > 0:
                            for squares2 in range(king_index + 1, check_piece_index, 1):
                                if between_check_square_list[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(between_check_square_list[squares2])
                        elif abs(king_index - check_piece_index) % 8 == 0:
                            for squares2 in range(king_index + 8, check_piece_index, 8):
                                if between_check_square_list[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(between_check_square_list[squares2])
                    #print("check squares between rook or queen and king: " + str(between_rook_queen_squares))
                    block_squares_2 = between_rook_queen_squares.copy()
                    block_squares_2.append(between_check_square_list[check_piece_index])
                    self.between_bishop_squares_list.setdefault(str(square_list[check_square_straight][4]), []).append(block_squares_2)
                    if any(("OCCUPIED" and "white") in square_list[square] for square in between_rook_queen_squares) \
                            or between_rook_queen_squares == []:
                        white_check = "FALSE"
                        self.white_check_list.append(white_check)
                    elif any(("OCCUPIED" and "black" and "pawn") in square_list[square] for square in between_rook_queen_squares) \
                            or any(("OCCUPIED" and "black" and "king") in square_list[square] for square in between_rook_queen_squares) \
                            or any(("OCCUPIED" and "black" and "bishop") in square_list[square] for square in between_rook_queen_squares) \
                            or any(("OCCUPIED" and "black" and "knight") in square_list[square] for square in between_rook_queen_squares):
                        #print("bishop or queen blocked by own pawn")
                        white_check = "FALSE"
                        self.white_check_list.append(white_check)
                    else:
                        if turn % 2 == 1 and self.piece_color == "white" and self.white_king_castle:
                            white_check = "TRUE"
                            self.white_check_list.append(white_check)
                        elif turn %  2 == 1 and self.piece_color == "white":
                            white_check = "TRUE"
                            self.white_check_list.append(white_check)
                        elif turn % 2 == 0:
                            white_check = "TRUE"
                            self.white_check_list.append(white_check)

                elif abs(king_index - check_piece_index) == 1 \
                            and "rook" in square_list[check_square_straight] \
                            or abs(king_index - check_piece_index) == 8 \
                            and "rook"  in square_list[check_square_straight] \
                            or abs(king_index - check_piece_index) == 1 \
                            and "queen" in square_list[check_square_straight] \
                            or abs(king_index - check_piece_index) == 8 \
                            and "queen" in square_list[check_square_straight] \
                            or abs(king_index - check_piece_index) == 1 \
                            and "king"  in square_list[check_square_straight] \
                            or abs(king_index - check_piece_index) == 8 \
                            and "king" in square_list[check_square_straight]:
                    self.between_bishop_squares_list.setdefault(str(square_list[check_square_straight][4]), []).append([check_square_straight])
                    if turn % 2 == 1 and self.piece_color == "white" and self.white_king_castle:
                        white_check = "TRUE"
                        self.white_check_list.append(white_check)
                    elif turn % 2 == 1 and self.piece_color == "white":
                        white_check = "TRUE"
                        self.white_check_list.append(white_check)
                        turn = 2
                        #print("self check no occupied squares between king and check piece")
                    elif turn % 2 == 0 and self.piece_color == "black":
                        white_check = "TRUE"
                        self.white_check_list.append(white_check)


        knight_check_list = []
        # add the potential knight squares
        if 8 > king_file_index + 1 > -1 \
                and 8 > king_row_number + 2 > -1:
            check_square_knight = (file_letter[king_file_index + 1] + str(row_number[king_row_number + 2]))
            if check_square_knight not in knight_check_list:
                knight_check_list.append(check_square_knight)
        if 8 > king_file_index - 1 > -1 \
                and 8 >king_row_number + 2 > -1:
            check_square_knight = (file_letter[king_file_index - 1] + str(row_number[king_row_number + 2]))
            if check_square_knight not in knight_check_list:
                knight_check_list.append(check_square_knight)
        if 8 >king_file_index + 1 > -1 \
                and 8 >king_row_number - 2 > -1:
            check_square_knight = (file_letter[king_file_index + 1] + str(row_number[king_row_number - 2]))
            if check_square_knight not in knight_check_list:
                knight_check_list.append(check_square_knight)
        if 8 > king_file_index - 1 > -1 \
                and 8 > king_row_number - 2 > -1:
            check_square_knight = (file_letter[king_file_index - 1] + str(row_number[king_row_number - 2]))
            if check_square_knight not in knight_check_list:
                knight_check_list.append(check_square_knight)
        if 8 > king_file_index + 2 > -1 \
                and 8 > king_row_number - 1 > -1:
            check_square_knight = (file_letter[king_file_index + 2] + str(row_number[king_row_number - 1]))
            if check_square_knight not in knight_check_list:
                knight_check_list.append(check_square_knight)
        if 8 > king_file_index - 2 > -1 \
                and 8 > king_row_number - 1 > -1:
            check_square_knight = (file_letter[king_file_index - 2] + str(row_number[king_row_number - 1]))
            if check_square_knight not in knight_check_list:
                knight_check_list.append(check_square_knight)
        if 8 > king_file_index + 2 > -1 \
                and 8 > king_row_number + 1 > -1:
            check_square_knight = (file_letter[king_file_index + 2] + str(row_number[king_row_number + 1]))
            if check_square_knight not in knight_check_list:
                knight_check_list.append(check_square_knight)
        if 8 > king_file_index - 2 > -1 \
                and 8 > king_row_number + 1 > -1:
            check_square_knight = (file_letter[king_file_index - 2] + str(row_number[king_row_number + 1]))
            if check_square_knight not in knight_check_list:
                knight_check_list.append(check_square_knight)


        for check_square_knight in knight_check_list:
            if "knight" in square_list[check_square_knight] \
                    and "black" in square_list[check_square_knight]:
                knight_index = between_check_square_list.index(check_square_knight)
                if abs(king_index - knight_index) == 17 \
                        or abs(king_index - knight_index) == 15 \
                        or abs(king_index - knight_index) == 10 \
                        or abs(king_index - knight_index) == 6:
                    self.between_bishop_squares_list.setdefault(str(square_list[check_square_knight][4]), []).append([check_square_knight])
                    if turn % 2 == 1 and self.piece_color == "white" and self.white_king_castle:
                        white_check = "TRUE"
                        self.white_check_list.append(white_check)
                    elif turn % 2 == 1 and self.piece_color == "white" and not self.white_king_castle:
                        white_check = "TRUE"
                        self.white_check_list.append(white_check)
                    elif turn % 2 == 0 and self.piece_color == "black":
                        white_check = "TRUE"
                        self.white_check_list.append(white_check)
                else:
                    white_check = "FALSE"
                    self.white_check_list.append(white_check)
        if "TRUE" in self.white_check_list:
            self.white_king_check = True
            white_king_check = True
        elif "TRUE" not in self.white_check_list:
            self.white_king_check = False
            white_king_check = False

    def place_back_white(self, new_square, old_square):
        global turn
        del square_list[new_square][2:]
        square_list[self.old_square].append("OCCUPIED")
        square_list[self.old_square].append(self.piece_color)
        square_list[self.old_square].append(self.piece_name)
        if self.piece_name == "king" \
                and "MOVED" in square_list[old_square]:
            square_list[self.old_square].append("MOVED")
        if self.piece_name == "rook" \
                and "MOVED" in square_list[self.old_square]:
            square_list[self.old_square].append("MOVED")
        if self.piece_name == "pawn" \
                and "MOVED" in square_list[self.old_square]:
            square_list[self.old_square].append("MOVED")
        self.new_square = old_square
        self.square = old_square
        self.new_file = self.old_file
        self.new_row = self.old_row
        turn = 2

    def check_checkmate_white(self):
        global white_king_check
        self.checkmate_check = True
        legal_moves_list = list()
        king_moves_list = list()
        full_board_index = list()

        charlistje = "abcdefgh"
        for charje in charlistje:
            for cifje in range(1, 9):
                square_bet = charje + str(cifje)
                full_board_index.append(square_bet)

        filelist = "abcdefgh"
        file_letter = []
        row_number = []
        for file in filelist:
            file_letter.append(file)
        for row in range(1, 9):
            row_number.append(row)

        if self.piece_name == "king" \
                and self.piece_color == "white":
            try:
                white_king_square = (self.new_file + str(self.new_row))
                white_king_file = self.new_file
                white_king_row = self.new_row
                king_file_index = file_letter.index(white_king_file)
                king_row_number = row_number.index(white_king_row)
            except AttributeError:
                white_king_square = white_king.file + str(white_king.row)
                white_king_file = white_king.file
                white_king_row = white_king.row
                king_file_index = file_letter.index(white_king_file)
                king_row_number = row_number.index(white_king_row)
        else:
            white_king_square = white_king.file + str(white_king.row)
            white_king_file = white_king.file
            white_king_row = white_king.row
            king_file_index = file_letter.index(white_king_file)
            king_row_number = row_number.index(white_king_row)
        # print("kingfileindex " + str(king_file_index))
        old_white_king_values = square_list[white_king_square][2:]
        del square_list[white_king_square][2:]
        if 8 > king_file_index + 1 > -1 \
                and 8 > king_row_number + 1 > -1:
            king_square = file_letter[king_file_index + 1] + str(row_number[king_row_number + 1])
            king_moves_list.append(king_square)
        if 8 > king_file_index + 1 > 0 \
                and 8 > king_row_number - 1 > -1:
            king_square = file_letter[king_file_index + 1] + str(row_number[king_row_number - 1])
            king_moves_list.append(king_square)
        if 8 > king_file_index - 1 > -1 \
                and 8 > king_row_number + 1 > -1:
            king_square = file_letter[king_file_index - 1] + str(row_number[king_row_number + 1])
            king_moves_list.append(king_square)
        if 8 > king_file_index - 1 > -1 \
                and 8 > king_row_number - 1 > -1:
            king_square = file_letter[king_file_index - 1] + str(row_number[king_row_number - 1])
            king_moves_list.append(king_square)
        if 8 > king_file_index + 1 > -1:
            king_square = file_letter[king_file_index + 1] + str(row_number[king_row_number])
            king_moves_list.append(king_square)
        if 8 > king_file_index - 1 > -1:
            king_square = file_letter[king_file_index - 1] + str(row_number[king_row_number])
            king_moves_list.append(king_square)
        if 8 > king_row_number + 1 > -1:
            king_square = file_letter[king_file_index] + str(row_number[king_row_number + 1])
            king_moves_list.append(king_square)
        if 8 > king_row_number - 1 > -1:
            king_square = file_letter[king_file_index] + str(row_number[king_row_number - 1])
            king_moves_list.append(king_square)



        for occupied_square in [square for square in king_moves_list if "OCCUPIED" and "white" in square_list[square]]:
            king_moves_list.remove(occupied_square)

        for square in king_moves_list:
            check_list = list()
            square_letter = square[0]
            square_cijfer = int(square[1])
            king_file_check = file_letter.index(square_letter)
            king_row_check = row_number.index(square_cijfer)
            straight_check_list = []
            for i in [check_square_straight for check_square_straight in range(0, 8) if
                      check_square_straight != king_file_check]:
                try:
                    check_square_straight = (file_letter[i] + str(square_cijfer))
                    if check_square_straight not in straight_check_list:
                        straight_check_list.append(check_square_straight)
                except IndexError:
                    pass
            # add vertical lines
            for i in [check_square_straight for check_square_straight in range(0, 8) if
                      check_square_straight != king_row_check]:
                try:
                    check_square_straight = (square_letter + str(row_number[i]))
                    if check_square_straight not in straight_check_list:
                        straight_check_list.append(check_square_straight)
                except IndexError:
                    pass
            # print("straight checklist for " + square + " is list " + str(straight_check_list))
            king_index = full_board_index.index(square)
            check_piece_index_list = dict()

            for check_square_straight in [squares for squares in straight_check_list if "black" in square_list[squares]
                                                                                        and "rook" in square_list[
                                                                                            squares]
                                                                                        or "queen" in square_list[
                                                                                            squares]
                                                                                        and "black" in square_list[
                                                                                            squares]
                                                                                        or "king" in square_list[
                                                                                            squares]
                                                                                        and "black" in square_list[
                                                                                            squares]]:


                check_piece_index = full_board_index.index(check_square_straight)
                if abs(king_index - check_piece_index) > 1 \
                        and abs(king_index - check_piece_index) != 8 \
                        and "rook" in square_list[check_square_straight] \
                        or abs(king_index - check_piece_index) > 1 \
                        and abs(king_index - check_piece_index) != 8 \
                        and "queen" in square_list[check_square_straight]:
                    between_rook_queen_squares = list()
                    if king_index > check_piece_index:
                        if 0 < (king_index - check_piece_index) < 8:
                            for squares2 in range(check_piece_index + 1, king_index, 1):
                                if full_board_index[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(full_board_index[squares2])
                        elif (king_index - check_piece_index) % 8 == 0:
                            for squares2 in range(check_piece_index + 8, king_index, 8):
                                if full_board_index[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(full_board_index[squares2])
                    elif king_index < check_piece_index:
                        if 0 < abs(king_index - check_piece_index) < 8:
                            for squares2 in range(king_index + 1, check_piece_index, 1):
                                if full_board_index[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(full_board_index[squares2])
                        elif abs(king_index - check_piece_index) % 8 == 0:
                            for squares2 in range(king_index + 8, check_piece_index, 8):
                                if full_board_index[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(full_board_index[squares2])
                    check_piece_index_list.setdefault(square, []).append(between_rook_queen_squares)
                    for i in range(0, len(check_piece_index_list[square])):
                        if any({"OCCUPIED", "white"}.issubset(set(square_list[square])) for square in
                               check_piece_index_list[square][i]):
                            check_list.append("FALSE")
                        elif any({"OCCUPIED", "black", "pawn"}.issubset(set(square_list[square])) for square in check_piece_index_list[square][i]) \
                                or any({"OCCUPIED", "black", "king"}.issubset(set(square_list[square])) for square in check_piece_index_list[square][i]) \
                                or any({"OCCUPIED", "black", "bishop"}.issubset(set(square_list[square])) for square in check_piece_index_list[square][i]) \
                                or any({"OCCUPIED", "black", "knight"}.issubset(set(square_list[square])) for square in check_piece_index_list[square][i]):
                            check_list.append("FALSE")
                        elif not any({"OCCUPIED"}.issubset(set(square_list[square])) for square in check_piece_index_list[square][i]):
                            check_list.append("TRUE")
                elif abs(king_index - check_piece_index) == 1 \
                         and "rook" in square_list[check_square_straight] \
                         or abs(king_index - check_piece_index) == 8 \
                         and "rook" in square_list[check_square_straight] \
                         or abs(king_index - check_piece_index) == 1 \
                         and "queen"  in square_list[check_square_straight] \
                         or abs(king_index - check_piece_index) == 8 \
                         and "queen" in square_list[check_square_straight] \
                         or abs(king_index - check_piece_index) == 1 \
                         and "king" in square_list[check_square_straight] \
                         or abs(king_index - check_piece_index) == 8 \
                         and "king"  in square_list[check_square_straight]:
                    check_list.append("TRUE")
            if not any({"black", "rook"}.issubset(set(square_list[square])) for square in straight_check_list) \
                    and not any({"black", "queen"}.issubset(set(square_list[square])) for square in straight_check_list):
                check_list.append("FALSE")



            diagonal_check_list = []
            for i in [check_square for check_square in range(-8, 8)]:
                try:
                    if king_file_check - i > -1 \
                            and king_row_check + i > -1 \
                            and file_letter[king_file_check - i] != square_letter:
                        check_square = (file_letter[king_file_check - i] + str(row_number[king_row_check + i]))
                        if check_square not in diagonal_check_list:
                            diagonal_check_list.append(check_square)
                except IndexError:
                    pass
            # make list of diagonal line right down from king position
            for i in [check_square for check_square in range(-8, 8)]:
                try:
                    if king_file_check + i > -1 \
                            and king_row_check + i > -1 \
                            and file_letter[king_file_check + i] != square_letter:
                        check_square = (file_letter[king_file_check + i] + str(row_number[king_row_check + i]))
                        if check_square not in diagonal_check_list:
                            diagonal_check_list.append(check_square)
                except IndexError:
                    pass

            between_squares_list_list = dict()
            #print("De diagonal voor de square: " + square +" is "+ str(diagonal_check_list))
            for check_square in diagonal_check_list:
                if "bishop" in square_list[check_square] \
                        and "black" in square_list[check_square] \
                        or "queen" in square_list[check_square] \
                        and "black" in square_list[check_square] \
                        or "pawn" in square_list[check_square] \
                        and "black" in square_list[check_square] \
                        or "king" in square_list[check_square] \
                        and "black" in square_list[check_square]:
                    bishop_queen_index = full_board_index.index(check_square)
                    if abs(king_index - bishop_queen_index) > 7 \
                            and abs(king_index - bishop_queen_index) != 9 \
                            and "bishop" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) > 7 \
                            and abs(king_index - bishop_queen_index) != 9 \
                            and "queen" in square_list[check_square]:
                        between_bishop_squares = list()
                        if king_index > bishop_queen_index:
                            if (king_index - bishop_queen_index) % 7 == 0:
                                for squares in range(bishop_queen_index + 7, king_index, 7):
                                    if full_board_index[squares] not in between_bishop_squares:
                                        between_bishop_squares.append(full_board_index[squares])
                            elif (king_index - bishop_queen_index) % 9 == 0:
                                for squares in range(bishop_queen_index + 9, king_index, 9):
                                    if full_board_index[squares] not in between_bishop_squares:
                                        between_bishop_squares.append(full_board_index[squares])
                        elif king_index < bishop_queen_index:
                            if abs((king_index - bishop_queen_index) % 7) == 0:
                                for squares in range(king_index + 7, bishop_queen_index, 7):
                                    if full_board_index[squares] not in between_bishop_squares:
                                        between_bishop_squares.append(full_board_index[squares])
                            elif abs(king_index - bishop_queen_index) % 9 == 0:
                                for squares in range(king_index + 9, bishop_queen_index, 9):
                                    if full_board_index[squares] not in between_bishop_squares:
                                        between_bishop_squares.append(full_board_index[squares])
                        between_squares_list_list.setdefault(square, []).append(between_bishop_squares)
                        for i in range(0, len(between_squares_list_list[square])):
                            if any({"OCCUPIED", "white"}.issubset(set(square_list[square])) for square in between_squares_list_list[square][i]):
                                check_list.append("FALSE")
                            elif any({"OCCUPIED", "black", "pawn"}.issubset(set(square_list[square])) for square in between_squares_list_list[square][i]) \
                                    or any({"OCCUPIED", "black", "king"}.issubset(set(square_list[square])) for square in between_squares_list_list[square][i]) \
                                    or any({"OCCUPIED", "black", "rook"}.issubset(set(square_list[square])) for square in between_squares_list_list[square][i]) \
                                    or any({"OCCUPIED", "black", "knight"}.issubset(set(square_list[square])) for square in between_squares_list_list[square][i]):
                                check_list.append("FALSE")
                            elif not any({"OCCUPIED"}.issubset(set(square_list[square])) for square in between_squares_list_list[square][i]):
                                check_list.append("TRUE")
                    elif abs(king_index - bishop_queen_index) == 7 \
                            and "pawn" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 9 \
                            and "pawn" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 7 \
                            and "bishop" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 9 \
                            and "bishop" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 7 \
                            and "queen" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 9 \
                            and "queen" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 7 \
                            and "king" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 9 \
                            and "king" in square_list[check_square]:
                        check_list.append("TRUE")
            if not any({"black", "bishop"}.issubset(set(square_list[square])) for square in diagonal_check_list) \
                    and not any({"black", "queen"}.issubset(set(square_list[square])) for square in diagonal_check_list):
                check_list.append("FALSE")


            knight_check_list = list()
            if 8 > king_file_check + 1 > -1 \
                    and 8 > king_row_check + 2 > -1:
                check_square_knight = (file_letter[king_file_check + 1] + str(row_number[king_row_check + 2]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check - 1 > -1 \
                    and 8 > king_row_check + 2 > -1:
                check_square_knight = (file_letter[king_file_check - 1] + str(row_number[king_row_check + 2]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check + 1 > -1 \
                    and 8 > king_row_check - 2 > -1:
                check_square_knight = (file_letter[king_file_check + 1] + str(row_number[king_row_check - 2]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check - 1 > -1 \
                    and 8 > king_row_check - 2 > -1:
                check_square_knight = (file_letter[king_file_check - 1] + str(row_number[king_row_check - 2]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check + 2 > -1 \
                    and 8 > king_row_check - 1 > -1:
                check_square_knight = (file_letter[king_file_check + 2] + str(row_number[king_row_check - 1]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check - 2 > -1 \
                    and 8 > king_row_check - 1 > -1:
                check_square_knight = (file_letter[king_file_check - 2] + str(row_number[king_row_check - 1]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check + 2 > -1 \
                    and 8 > king_row_check + 1 > -1:
                check_square_knight = (file_letter[king_file_check + 2] + str(row_number[king_row_check + 1]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check - 2 > -1 \
                    and 8 > king_row_check + 1 > -1:
                check_square_knight = (file_letter[king_file_check - 2] + str(row_number[king_row_check + 1]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)

            for check_square_knight in knight_check_list:
                if "knight" in square_list[check_square_knight] \
                        and "black" in square_list[check_square_knight]:
                    knight_index = full_board_index.index(check_square_knight)
                    if abs(king_index - knight_index) == 17 \
                            or abs(king_index - knight_index) == 15 \
                            or abs(king_index - knight_index) == 10 \
                            or abs(king_index - knight_index) == 6:
                        check_list.append("TRUE")
            if not any({"black", "knight"}.issubset(set(square_list[square3])) for square3 in knight_check_list):
                check_list.append("FALSE")

            # print("check checklist for square: "+ square + " is " + str(check_list))


            if "TRUE" in check_list:
                if "K" + square in legal_moves_list:
                    legal_moves_list.remove("K" +  square)
            if "TRUE" not in check_list:
                if "K" +  square not in legal_moves_list:
                    legal_moves_list.append("K" + square)

        for value in old_white_king_values:
            square_list[white_king_square].append(value)

        # WE MAKE A LIST OF THE BETWEEN SQUARES AND CHECK IF THESE CAN BE BLOCKED BY OWN PIECES
        for piece, squares in self.between_bishop_squares_list.items():
            for squares_4 in self.between_bishop_squares_list[piece]:
                if any("OCCUPIED" in square_list[square] for square in squares_4[:-1]):
                    pass
                else:
                    pass
                    for squares_5 in squares_4:
                        piece_letter = squares_5[0]
                        piece_row = int(squares_5[1])
                        square_index = full_board_index.index(squares_5)
                        piece_file_check = file_letter.index(piece_letter)
                        piece_row_check = row_number.index(piece_row)
                        piece_straight_check_list = list()

                        for i in [check_square_straight for check_square_straight in range(0, 8) if
                                  check_square_straight != piece_file_check]:
                            try:
                                check_square_straight = (file_letter[i] + str(piece_row))
                                if check_square_straight not in piece_straight_check_list:
                                    piece_straight_check_list.append(check_square_straight)
                            except IndexError:
                                pass
                        # add vertical lines
                        for i in [check_square_straight for check_square_straight in range(0, 8) if
                                  check_square_straight != piece_row_check]:
                            try:
                                check_square_straight = (piece_letter + str(row_number[i]))
                                if check_square_straight not in piece_straight_check_list:
                                    piece_straight_check_list.append(check_square_straight)
                            except IndexError:
                                pass
                        piece_index_list = dict()
                        for square_6 in piece_straight_check_list:
                            if "rook" in square_list[square_6] \
                                    and "white" in square_list[square_6] \
                                    or "pawn" in square_list[square_6] \
                                    and "white" in square_list[square_6] \
                                    or "queen" in square_list[square_6] \
                                    and "white" in square_list[square_6]:
                                piece_index = full_board_index.index(square_6)
                                if abs(square_index - piece_index) > 1 \
                                        and abs(square_index - piece_index) != 8 \
                                        and "rook" in square_list[square_6] \
                                        or abs(square_index - piece_index) > 1 \
                                        and abs(square_index - piece_index) != 8 \
                                        and "queen" in square_list[square_6]:
                                    between_rook_queen_squares = list()
                                    if square_index > piece_index:
                                        if 0 < (square_index - piece_index) < 8:
                                            for squares2 in range(piece_index + 1, square_index, 1):
                                                if full_board_index[squares2] not in between_rook_queen_squares:
                                                    between_rook_queen_squares.append(full_board_index[squares2])
                                        elif (square_index - piece_index) % 8 == 0:
                                            for squares2 in range(piece_index + 8, square_index, 8):
                                                if full_board_index[squares2] not in between_rook_queen_squares:
                                                    between_rook_queen_squares.append(full_board_index[squares2])
                                    elif square_index < piece_index:
                                        if 0 < abs(square_index - piece_index) < 8:
                                            for squares2 in range(square_index + 1, piece_index, 1):
                                                if full_board_index[squares2] not in between_rook_queen_squares:
                                                    between_rook_queen_squares.append(full_board_index[squares2])
                                        elif abs(square_index - piece_index) % 8 == 0:
                                            for squares2 in range(square_index + 8, piece_index, 8):
                                                if full_board_index[squares2] not in between_rook_queen_squares:
                                                    between_rook_queen_squares.append(full_board_index[squares2])
                                    piece_index_list.setdefault(squares_5, []).append(between_rook_queen_squares)
                                    if len(piece_index_list[squares_5]) > 1:
                                        for i in range(0, len(piece_index_list[squares_5])):
                                            if not any({"OCCUPIED"}.issubset(set(square_list[square_6])) for square_6 in piece_index_list[squares_5][i]):
                                                if "OCCUPIED" in square_list[squares_5]:
                                                    old_square_6_values = square_list[square_6][2:]
                                                    old_square_5_values = square_list[squares_5][2:]
                                                    del square_list[square_6][2:]
                                                    del square_list[squares_5][2:]
                                                    square_list[squares_5].append("OCCUPIED")
                                                    square_list[squares_5].append("white")
                                                    if "rook" in old_square_6_values:
                                                        square_list[squares_5].append("rook")
                                                    elif "queen" in old_square_6_values:
                                                        square_list[squares_5].append("queen")
                                                    self.check_check_white(white_king.square, white_king.file, white_king.row)
                                                    if not self.white_king_check:
                                                        del square_list[square_6][2:]
                                                        del square_list[squares_5][2:]
                                                        for values in old_square_6_values:
                                                            square_list[square_6].append(values)
                                                        for values in old_square_5_values:
                                                            square_list[squares_5].append(values)
                                                        if "rook" in square_list[square_6]:
                                                            if "R" + square_6[0] +"x"+ squares_5 not in legal_moves_list:
                                                                legal_moves_list.append("R" + square_6[0] + "x" + squares_5)
                                                        elif "queen" in square_list[square_6]:
                                                            if "Qx"+ squares_5 not in legal_moves_list:
                                                                legal_moves_list.append("Qx" + squares_5)
                                                        self.white_king_check = True
                                                        white_king_check = True
                                                    else:
                                                        del square_list[square_6][2:]
                                                        del square_list[squares_5][2:]
                                                        for values in old_square_6_values:
                                                            square_list[square_6].append(values)
                                                        for values in old_square_5_values:
                                                            square_list[squares_5].append(values)
                                                        self.white_king_check = True
                                                        white_king_check = True
                                                else:
                                                    old_square_6_values = square_list[square_6][2:]
                                                    del square_list[square_6][2:]
                                                    square_list[squares_5].append("OCCUPIED")
                                                    square_list[squares_5].append("white")
                                                    if "rook" in old_square_6_values:
                                                        square_list[squares_5].append("rook")
                                                    elif "queen" in old_square_6_values:
                                                        square_list[squares_5].append("queen")
                                                    self.check_check_white(white_king.square, white_king.file, white_king.row)
                                                    if not self.white_king_check:
                                                        del square_list[square_6][2:]
                                                        del square_list[squares_5][2:]
                                                        for values in old_square_6_values:
                                                            square_list[square_6].append(values)
                                                        if "rook" in square_list[square_6]:
                                                            if "R" + square_6[0] + squares_5 not in legal_moves_list:
                                                                legal_moves_list.append("R" + square_6[0] + squares_5)
                                                        elif "queen" in square_list[square_6]:
                                                            if "Q"+ squares_5 not in legal_moves_list:
                                                                legal_moves_list.append("Q" + squares_5)
                                                        self.white_king_check = True
                                                        white_king_check = True
                                                    else:
                                                        del square_list[square_6][2:]
                                                        del square_list[squares_5][2:]
                                                        for values in old_square_6_values:
                                                            square_list[square_6].append(values)
                                                        self.white_king_check = True
                                                        white_king_check = True
                                    elif len(piece_index_list[squares_5]) < 2:
                                        if not any({"OCCUPIED"}.issubset(set(square_list[square_6])) for square_6 in between_rook_queen_squares):
                                            if "OCCUPIED" in square_list[squares_5]:
                                                old_square_6_values = square_list[square_6][2:]
                                                old_square_5_values = square_list[squares_5][2:]
                                                del square_list[square_6][2:]
                                                del square_list[squares_5][2:]
                                                square_list[squares_5].append("OCCUPIED")
                                                square_list[squares_5].append("white")
                                                if "rook" in old_square_6_values:
                                                    square_list[squares_5].append("rook")
                                                elif "queen" in old_square_6_values:
                                                    square_list[squares_5].append("queen")
                                                self.check_check_white(white_king.square, white_king.file, white_king.row)
                                                if not self.white_king_check:
                                                    del square_list[square_6][2:]
                                                    del square_list[squares_5][2:]
                                                    for values in old_square_6_values:
                                                        square_list[square_6].append(values)
                                                    for values in old_square_5_values:
                                                        square_list[squares_5].append(values)
                                                    if "rook" in square_list[square_6]:
                                                        if "Rx" + square_6[0] + squares_5 not in legal_moves_list:
                                                            legal_moves_list.append("Rx" + squares_5)
                                                    elif "queen" in square_list[square_6]:
                                                        if "Qx" + squares_5 not in legal_moves_list:
                                                            legal_moves_list.append("Qx" + squares_5)
                                                    self.white_king_check = True
                                                    white_king_check = True
                                                else:
                                                    del square_list[square_6][2:]
                                                    del square_list[squares_5][2:]
                                                    for values in old_square_6_values:
                                                        square_list[square_6].append(values)
                                                    for values in old_square_5_values:
                                                        square_list[squares_5].append(values)
                                                    self.white_king_check = True
                                                    white_king_check = True
                                            else:
                                                old_square_6_values = square_list[square_6][2:]
                                                del square_list[square_6][2:]
                                                square_list[squares_5].append("OCCUPIED")
                                                square_list[squares_5].append("white")
                                                if "rook" in old_square_6_values:
                                                    square_list[squares_5].append("rook")
                                                elif "queen" in old_square_6_values:
                                                    square_list[squares_5].append("queen")
                                                self.check_check_white(white_king.square, white_king.file, white_king.row)
                                                if not self.white_king_check:
                                                    del square_list[square_6][2:]
                                                    del square_list[squares_5][2:]
                                                    for values in old_square_6_values:
                                                        square_list[square_6].append(values)
                                                    if "rook" in square_list[square_6]:
                                                        if "R" + squares_5 not in legal_moves_list:
                                                            legal_moves_list.append("R"+ squares_5)
                                                    elif "queen" in square_list[square_6]:
                                                        if "Q" + squares_5 not in legal_moves_list:
                                                            legal_moves_list.append("Q" + squares_5)
                                                    self.white_king_check = True
                                                    white_king_check = True
                                                else:
                                                    del square_list[square_6][2:]
                                                    del square_list[squares_5][2:]
                                                    for values in old_square_6_values:
                                                        square_list[square_6].append(values)
                                                    self.white_king_check = True
                                                    white_king_check = True
                                elif abs(square_index - piece_index) == 1 \
                                        and "pawn" in square_list[square_6] \
                                        and "OCCUPIED" not in square_list[squares_5]:
                                    if square_index > piece_index:
                                        old_square_6_values = square_list[square_6][2:]
                                        del square_list[square_6][2:]
                                        square_list[squares_5].append("OCCUPIED")
                                        square_list[squares_5].append("white")
                                        square_list[squares_5].append("pawn")
                                        self.check_check_white(white_king.square, white_king.file, white_king.row)
                                        if not self.white_king_check:
                                            del square_list[square_6][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_6_values:
                                                square_list[square_6].append(values)
                                            if squares_5 not in legal_moves_list:
                                                legal_moves_list.append(squares_5)
                                            self.white_king_check = True
                                            white_king_check = True
                                        else:
                                            del square_list[square_6][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_6_values:
                                                square_list[square_6].append(values)
                                            self.white_king_check = True
                                            white_king_check = True
                                elif abs(square_index - piece_index) == 2 \
                                        and "pawn" in square_list[square_6] \
                                        and "MOVED" not in square_list[square_6]:
                                    if square_index > piece_index:
                                        if "OCCUPIED" not in square_list[full_board_index[piece_index+1]] \
                                                and "OCCUPIED" not in square_list[squares_5]:
                                            old_square_6_values = square_list[square_6][2:]
                                            del square_list[square_6][2:]
                                            square_list[squares_5].append("OCCUPIED")
                                            square_list[squares_5].append("white")
                                            square_list[squares_5].append("pawn")
                                            self.check_check_white(white_king.square, white_king.file, white_king.row)
                                            if not self.white_king_check:
                                                del square_list[square_6][2:]
                                                del square_list[squares_5][2:]
                                                for values in old_square_6_values:
                                                    square_list[square_6].append(values)
                                                if squares_5 not in legal_moves_list:
                                                    legal_moves_list.append(squares_5)
                                                self.white_king_check = True
                                                white_king_check = True
                                            else:
                                                del square_list[square_6][2:]
                                                del square_list[squares_5][2:]
                                                for values in old_square_6_values:
                                                    square_list[square_6].append(values)
                                                self.white_king_check = True
                                                white_king_check = True
                                elif abs(square_index - piece_index) == 1 \
                                        and "rook" in square_list[square_6] \
                                        or abs(square_index - piece_index) == 8 \
                                        and "rook" in square_list[square_6] \
                                        or abs(square_index - piece_index) == 1 \
                                        and "queen" in square_list[square_6] \
                                        or abs(square_index - piece_index) == 8 \
                                        and "queen" in square_list[square_6]:
                                    if "OCCUPIED" in square_list[squares_5]:
                                        old_square_6_values = square_list[square_6][2:]
                                        old_square_5_values = square_list[squares_5][2:]
                                        del square_list[square_6][2:]
                                        del square_list[squares_5][2:]
                                        square_list[squares_5].append("OCCUPIED")
                                        square_list[squares_5].append("white")
                                        if "rook" in old_square_6_values:
                                            square_list[squares_5].append("rook")
                                        elif "queen" in old_square_6_values:
                                            square_list[squares_5].append("queen")
                                        self.check_check_white(white_king.square, white_king.file, white_king.row)
                                        if not self.white_king_check:
                                            del square_list[square_6][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_6_values:
                                                square_list[square_6].append(values)
                                            for values in old_square_5_values:
                                                square_list[squares_5].append(values)
                                            if "rook" in square_list[square_6]:
                                                if "Rx" + square_6[0] + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("Rx" + squares_5)
                                            elif "queen" in square_list[square_6]:
                                                if "Qx" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("Qx" + squares_5)
                                            self.white_king_check = True
                                            white_king_check = True
                                        else:
                                            del square_list[square_6][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_6_values:
                                                square_list[square_6].append(values)
                                            for values in old_square_5_values:
                                                square_list[squares_5].append(values)
                                            self.white_king_check = True
                                            white_king_check = True
                                    else:
                                        old_square_6_values = square_list[square_6][2:]
                                        del square_list[square_6][2:]
                                        square_list[squares_5].append("OCCUPIED")
                                        square_list[squares_5].append("white")
                                        if "rook" in old_square_6_values:
                                            square_list[squares_5].append("rook")
                                        elif "queen" in old_square_6_values:
                                            square_list[squares_5].append("queen")
                                        self.check_check_white(white_king.square, white_king.file, white_king.row)
                                        if not self.white_king_check:
                                            del square_list[square_6][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_6_values:
                                                square_list[square_6].append(values)
                                            if "rook" in square_list[square_6]:
                                                if "R" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("R" + squares_5)
                                            elif "queen" in square_list[square_6]:
                                                if "Q" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("Q" + squares_5)
                                            self.white_king_check = True
                                            white_king_check = True
                                        else:
                                            del square_list[square_6][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_6_values:
                                                square_list[square_6].append(values)
                                            self.white_king_check = True
                                            white_king_check = True


                        diagonal_check_list = list()
                        for i in [check_square for check_square in range(-8, 8)]:
                            try:
                                if piece_file_check - i > -1 \
                                        and piece_row_check + i > -1 \
                                        and file_letter[piece_file_check - i] != piece_letter:
                                    check_square = (file_letter[piece_file_check - i] + str(row_number[piece_row_check + i]))
                                    if check_square not in diagonal_check_list:
                                        diagonal_check_list.append(check_square)
                            except IndexError:
                                pass
                        # make list of diagonal line right down from king position
                        for i in [check_square for check_square in range(-8, 8)]:
                            try:
                                if piece_file_check + i > -1 \
                                        and piece_row_check + i > -1 \
                                        and file_letter[piece_file_check + i] != piece_letter:
                                    check_square = (file_letter[piece_file_check + i] + str(row_number[piece_row_check + i]))
                                    if check_square not in diagonal_check_list:
                                        diagonal_check_list.append(check_square)
                            except IndexError:
                                pass

                        between_diagonals_list_list = dict()
                        for square_7 in diagonal_check_list:
                            if "bishop" in square_list[square_7] \
                                    and "white" in square_list[square_7] \
                                    or "queen" in square_list[square_7] \
                                    and "white" in square_list[square_7] \
                                    or "pawn" in square_list[square_7] \
                                    and "white" in square_list[square_7]:
                                diagonal_piece_index = full_board_index.index(square_7)
                                if abs(square_index - diagonal_piece_index) > 7 \
                                        and abs(square_index - diagonal_piece_index) != 9 \
                                        and "bishop" in square_list[square_7] \
                                        or abs(square_index - diagonal_piece_index) > 7 \
                                        and abs(square_index - diagonal_piece_index) != 9 \
                                        and "queen" in square_list[square_7]:
                                    between_diagonal_squares = list()
                                    if square_index > diagonal_piece_index:
                                        if (square_index - diagonal_piece_index) % 7 == 0:
                                            for squares_7 in range(diagonal_piece_index + 7, square_index, 7):
                                                if full_board_index[squares_7] not in between_diagonal_squares:
                                                    between_diagonal_squares.append(full_board_index[squares_7])
                                        elif (square_index - diagonal_piece_index) % 9 == 0:
                                            for squares_7 in range(diagonal_piece_index + 9, square_index, 9):
                                                if full_board_index[squares_7] not in between_diagonal_squares:
                                                    between_diagonal_squares.append(full_board_index[squares_7])
                                    elif square_index < diagonal_piece_index:
                                        if abs((square_index - diagonal_piece_index) % 7) == 0:
                                            for squares_7 in range(square_index + 7, diagonal_piece_index, 7):
                                                if full_board_index[squares_7] not in between_diagonal_squares:
                                                    between_diagonal_squares.append(full_board_index[squares_7])
                                        elif abs(square_index - diagonal_piece_index) % 9 == 0:
                                            for squares_7 in range(square_index + 9, diagonal_piece_index, 9):
                                                if full_board_index[squares_7] not in between_diagonal_squares:
                                                    between_diagonal_squares.append(full_board_index[squares_7])
                                    between_diagonals_list_list.setdefault(squares_5, []).append(between_diagonal_squares)
                                    if len(between_diagonals_list_list[squares_5]) > 1:
                                        for i in range(0, len(between_diagonals_list_list[squares_5])):
                                            if not any({"OCCUPIED"}.issubset(set(square_list[square_7])) for square_7 in between_diagonals_list_list[squares_5][i]):
                                                if "OCCUPIED" in square_list[squares_5]:
                                                    old_square_7_values = square_list[square_7][2:]
                                                    old_square_5_values = square_list[squares_5][2:]
                                                    del square_list[square_7][2:]
                                                    del square_list[squares_5][2:]
                                                    square_list[squares_5].append("OCCUPIED")
                                                    square_list[squares_5].append("white")
                                                    if "bishop" in old_square_7_values:
                                                        square_list[squares_5].append("bishop")
                                                    elif "queen" in old_square_7_values:
                                                        square_list[squares_5].append("queen")
                                                    self.check_check_white(white_king.square, white_king.file, white_king.row)
                                                    if not self.white_king_check:
                                                        del square_list[square_7][2:]
                                                        del square_list[squares_5][2:]
                                                        for values in old_square_7_values:
                                                            square_list[square_7].append(values)
                                                        for values in old_square_5_values:
                                                            square_list[squares_5].append(values)
                                                        if "bishop" in square_list[square_7]:
                                                            if "Bx" + squares_5 not in legal_moves_list:
                                                                legal_moves_list.append("Bx" + squares_5)
                                                        elif "queen" in square_list[square_7]:
                                                            if "Qx" + squares_5 not in legal_moves_list:
                                                                legal_moves_list.append("Qx" + squares_5)
                                                        self.white_king_check = True
                                                        white_king_check = True
                                                    else:
                                                        del square_list[square_7][2:]
                                                        del square_list[squares_5][2:]
                                                        for values in old_square_7_values:
                                                            square_list[square_7].append(values)
                                                        for values in old_square_5_values:
                                                            square_list[squares_5].append(values)
                                                        self.white_king_check = True
                                                        white_king_check = True
                                                else:
                                                    old_square_7_values = square_list[square_7][2:]
                                                    del square_list[square_7][2:]
                                                    square_list[squares_5].append("OCCUPIED")
                                                    square_list[squares_5].append("white")
                                                    if "bishop" in old_square_7_values:
                                                        square_list[squares_5].append("bishop")
                                                    elif "queen" in old_square_7_values:
                                                        square_list[squares_5].append("queen")
                                                    self.check_check_white(white_king.square, white_king.file, white_king.row)
                                                    if not self.white_king_check:
                                                        del square_list[square_7][2:]
                                                        del square_list[squares_5][2:]
                                                        for values in old_square_7_values:
                                                            square_list[square_7].append(values)
                                                        if "bishop" in square_list[square_7]:
                                                            if "B" + squares_5 not in legal_moves_list:
                                                                legal_moves_list.append("B" + squares_5)
                                                        elif "queen" in square_list[square_7]:
                                                            if "Q" + squares_5 not in legal_moves_list:
                                                                legal_moves_list.append("Q" + squares_5)
                                                        self.white_king_check = True
                                                        white_king_check = True
                                                    else:
                                                        del square_list[square_7][2:]
                                                        del square_list[squares_5][2:]
                                                        for values in old_square_7_values:
                                                            square_list[square_7].append(values)
                                                        self.white_king_check = True
                                                        white_king_check = True
                                    if len(between_diagonals_list_list[squares_5]) < 2:
                                        if not any({"OCCUPIED"}.issubset(set(square_list[square_7])) for square_7 in between_diagonal_squares):
                                            if "OCCUPIED" in square_list[squares_5]:
                                                old_square_7_values = square_list[square_7][2:]
                                                old_square_5_values = square_list[squares_5][2:]
                                                del square_list[square_7][2:]
                                                del square_list[squares_5][2:]
                                                square_list[squares_5].append("OCCUPIED")
                                                square_list[squares_5].append("white")
                                                if "bishop" in old_square_7_values:
                                                    square_list[squares_5].append("bishop")
                                                elif "queen" in old_square_7_values:
                                                    square_list[squares_5].append("queen")
                                                self.check_check_white(white_king.square, white_king.file, white_king.row)
                                                if not self.white_king_check:
                                                    del square_list[square_7][2:]
                                                    del square_list[squares_5][2:]
                                                    for values in old_square_7_values:
                                                        square_list[square_7].append(values)
                                                    for values in old_square_5_values:
                                                        square_list[squares_5].append(values)
                                                    if "bishop" in square_list[square_7]:
                                                        if "Bx" + squares_5 not in legal_moves_list:
                                                            legal_moves_list.append("Bx" + squares_5)
                                                    elif "queen" in square_list[square_7]:
                                                        if "Qx" + squares_5 not in legal_moves_list:
                                                            legal_moves_list.append("Qx" + squares_5)
                                                    self.white_king_check = True
                                                    white_king_check = True
                                                else:
                                                    del square_list[square_7][2:]
                                                    del square_list[squares_5][2:]
                                                    for values in old_square_7_values:
                                                        square_list[square_7].append(values)
                                                    for values in old_square_5_values:
                                                        square_list[squares_5].append(values)
                                                    self.white_king_check = True
                                                    white_king_check = True
                                            else:
                                                old_square_7_values = square_list[square_7][2:]
                                                del square_list[square_7][2:]
                                                square_list[squares_5].append("OCCUPIED")
                                                square_list[squares_5].append("white")
                                                if "bishop" in old_square_7_values:
                                                    square_list[squares_5].append("bishop")
                                                elif "queen" in old_square_7_values:
                                                    square_list[squares_5].append("queen")
                                                self.check_check_white(white_king.square, white_king.file, white_king.row)
                                                if not self.white_king_check:
                                                    del square_list[square_7][2:]
                                                    del square_list[squares_5][2:]
                                                    for values in old_square_7_values:
                                                        square_list[square_7].append(values)
                                                    if "bishop" in square_list[square_7]:
                                                        if "B" + squares_5 not in legal_moves_list:
                                                            legal_moves_list.append("B" + squares_5)
                                                    elif "queen" in square_list[square_7]:
                                                        if "Q" + squares_5 not in legal_moves_list:
                                                            legal_moves_list.append("Q" + squares_5)
                                                    self.white_king_check = True
                                                    white_king_check = True
                                                else:
                                                    del square_list[square_7][2:]
                                                    del square_list[squares_5][2:]
                                                    for values in old_square_7_values:
                                                        square_list[square_7].append(values)
                                                    self.white_king_check = True
                                                    white_king_check = True
                                elif abs(square_index - diagonal_piece_index) == 7 \
                                        and "bishop" in square_list[square_7] \
                                        or abs(square_index - diagonal_piece_index) == 9 \
                                        and "bishop" in square_list[square_7] \
                                        or abs(square_index - diagonal_piece_index) == 7 \
                                        and "queen" in square_list[square_7] \
                                        or abs(square_index - diagonal_piece_index) == 9 \
                                        and "queen" in square_list[square_7]:
                                    if "OCCUPIED" in square_list[squares_5]:
                                        old_square_7_values = square_list[square_7][2:]
                                        old_square_5_values = square_list[squares_5][2:]
                                        del square_list[square_7][2:]
                                        del square_list[squares_5][2:]
                                        square_list[squares_5].append("OCCUPIED")
                                        square_list[squares_5].append("white")
                                        if "bishop" in old_square_7_values:
                                            square_list[squares_5].append("bishop")
                                        elif "queen" in old_square_7_values:
                                            square_list[squares_5].append("queen")
                                        self.check_check_white(white_king.square, white_king.file, white_king.row)
                                        if not self.white_king_check:
                                            del square_list[square_7][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_7_values:
                                                square_list[square_7].append(values)
                                            for values in old_square_5_values:
                                                square_list[squares_5].append(values)
                                            if "bishop" in square_list[square_7]:
                                                if "Bx" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("Bx" + squares_5)
                                            elif "queen" in square_list[square_7]:
                                                if "Qx" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("Qx" + squares_5)
                                            self.white_king_check = True
                                            white_king_check = True
                                        else:
                                            del square_list[square_7][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_7_values:
                                                square_list[square_7].append(values)
                                            for values in old_square_5_values:
                                                square_list[squares_5].append(values)
                                            self.white_king_check = True
                                            white_king_check = True
                                    else:
                                        old_square_7_values = square_list[square_7][2:]
                                        del square_list[square_7][2:]
                                        square_list[squares_5].append("OCCUPIED")
                                        square_list[squares_5].append("white")
                                        if "bishop" in old_square_7_values:
                                            square_list[squares_5].append("bishop")
                                        elif "queen" in old_square_7_values:
                                            square_list[squares_5].append("queen")
                                        self.check_check_white(white_king.square, white_king.file, white_king.row)
                                        if not self.white_king_check:
                                            del square_list[square_7][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_7_values:
                                                square_list[square_7].append(values)
                                            if "bishop" in square_list[square_7]:
                                                if "B" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("B" + squares_5)
                                            elif "queen" in square_list[square_7]:
                                                if "Q" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("Q" + squares_5)
                                            self.white_king_check = True
                                            white_king_check = True
                                        else:
                                            del square_list[square_7][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_7_values:
                                                square_list[square_7].append(values)
                                            self.white_king_check = True
                                            white_king_check = True
                                elif (square_index - diagonal_piece_index) == 9 \
                                        and "pawn" in square_list[square_7] \
                                        and "OCCUPIED" in square_list[squares_5] \
                                        or (diagonal_piece_index - square_index) == 7 \
                                        and "pawn" in square_list[square_7] \
                                        and "OCCUPIED" in square_list[squares_5]:
                                    old_square_7_values = square_list[square_7][2:]
                                    old_square_5_values = square_list[squares_5][2:]
                                    del square_list[square_7][2:]
                                    del square_list[squares_5][2:]
                                    square_list[squares_5].append("OCCUPIED")
                                    square_list[squares_5].append("white")
                                    square_list[squares_5].append("pawn")
                                    self.check_check_white(white_king.square, white_king.file, white_king.row)
                                    if not self.white_king_check:
                                        del square_list[square_7][2:]
                                        del square_list[squares_5][2:]
                                        for values in old_square_7_values:
                                            square_list[square_7].append(values)
                                        for values in old_square_5_values:
                                            square_list[squares_5].append(values)
                                        if square_7[0] + "x" + squares_5 not in legal_moves_list:
                                            legal_moves_list.append(square_7[0] + "x" + squares_5)
                                        self.white_king_check = True
                                        white_king_check = True
                                    else:
                                        del square_list[square_7][2:]
                                        del square_list[squares_5][2:]
                                        for values in old_square_7_values:
                                            square_list[square_7].append(values)
                                        for values in old_square_5_values:
                                            square_list[squares_5].append(values)
                                        self.white_king_check = True
                                        white_king_check = True


                        knight_check_list = list()
                        if 8 > piece_file_check + 1 > -1 \
                                and 8 > piece_row_check + 2 > -1:
                            check_square_knight = (
                                        file_letter[piece_file_check + 1] + str(row_number[piece_row_check + 2]))
                            if check_square_knight not in knight_check_list:
                                knight_check_list.append(check_square_knight)
                        if 8 > piece_file_check - 1 > -1 \
                                and 8 > piece_row_check + 2 > -1:
                            check_square_knight = (
                                        file_letter[piece_file_check - 1] + str(row_number[piece_row_check + 2]))
                            if check_square_knight not in knight_check_list:
                                knight_check_list.append(check_square_knight)
                        if 8 > piece_file_check + 1 > -1 \
                                and 8 > piece_row_check - 2 > -1:
                            check_square_knight = (
                                        file_letter[piece_file_check + 1] + str(row_number[piece_row_check - 2]))
                            if check_square_knight not in knight_check_list:
                                knight_check_list.append(check_square_knight)
                        if 8 > piece_file_check - 1 > -1 \
                                and 8 > piece_row_check - 2 > -1:
                            check_square_knight = (
                                        file_letter[piece_file_check - 1] + str(row_number[piece_row_check - 2]))
                            if check_square_knight not in knight_check_list:
                                knight_check_list.append(check_square_knight)
                        if 8 > piece_file_check + 2 > -1 \
                                and 8 > piece_row_check - 1 > -1:
                            check_square_knight = (
                                        file_letter[piece_file_check + 2] + str(row_number[piece_row_check - 1]))
                            if check_square_knight not in knight_check_list:
                                knight_check_list.append(check_square_knight)
                        if 8 > piece_file_check - 2 > -1 \
                                and 8 > piece_row_check - 1 > -1:
                            check_square_knight = (
                                        file_letter[piece_file_check - 2] + str(row_number[piece_row_check - 1]))
                            if check_square_knight not in knight_check_list:
                                knight_check_list.append(check_square_knight)
                        if 8 > piece_file_check + 2 > -1 \
                                and 8 > piece_row_check + 1 > -1:
                            check_square_knight = (
                                        file_letter[piece_file_check + 2] + str(row_number[piece_row_check + 1]))
                            if check_square_knight not in knight_check_list:
                                knight_check_list.append(check_square_knight)
                        if 8 > piece_file_check - 2 > -1 \
                                and 8 > piece_row_check + 1 > -1:
                            check_square_knight = (
                                        file_letter[piece_file_check - 2] + str(row_number[piece_row_check + 1]))
                            if check_square_knight not in knight_check_list:
                                knight_check_list.append(check_square_knight)

                        for check_square_knight in knight_check_list:
                            if "knight" in square_list[check_square_knight] \
                                    and "white" in square_list[check_square_knight]:
                                knight_index = full_board_index.index(check_square_knight)
                                if abs(square_index - knight_index) == 17 \
                                        or abs(square_index - knight_index) == 15 \
                                        or abs(square_index - knight_index) == 10 \
                                        or abs(square_index - knight_index) == 6:
                                    if "OCCUPIED" in square_list[squares_5]:
                                        check_square_knight_values = square_list[check_square_knight][2:]
                                        old_square_5_values = square_list[squares_5][2:]
                                        del square_list[check_square_knight][2:]
                                        del square_list[squares_5][2:]
                                        square_list[squares_5].append("OCCUPIED")
                                        square_list[squares_5].append("white")
                                        square_list[squares_5].append("knight")
                                        self.check_check_white(white_king.square, white_king.file, white_king.row)
                                        if not self.white_king_check:
                                            del square_list[check_square_knight][2:]
                                            del square_list[squares_5][2:]
                                            for values in check_square_knight_values:
                                                square_list[check_square_knight].append(values)
                                            for values in old_square_5_values:
                                                square_list[squares_5].append(values)
                                            if white_knight.file == white_knight2.file:
                                                if "N" + check_square_knight[1] + "x" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("N" + check_square_knight[1] + "x" + squares_5)
                                            elif white_knight.row == white_knight2.row:
                                                if "N" + check_square_knight[0] + "x" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("N" + check_square_knight[0] + "x" + squares_5)
                                            else:
                                                if "Nx" +  squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("Nx" + squares_5)
                                            self.white_king_check = True
                                            white_king_check = True
                                        else:
                                            del square_list[check_square_knight][2:]
                                            del square_list[squares_5][2:]
                                            for values in check_square_knight_values:
                                                square_list[check_square_knight].append(values)
                                            for values in old_square_5_values:
                                                square_list[squares_5].append(values)
                                            self.white_king_check = True
                                            white_king_check = True
                                    else:
                                        check_square_knight_values = square_list[check_square_knight][2:]
                                        del square_list[check_square_knight][2:]
                                        square_list[squares_5].append("OCCUPIED")
                                        square_list[squares_5].append("white")
                                        square_list[squares_5].append("knight")
                                        self.check_check_white(white_king.square, white_king.file, white_king.row)
                                        if not self.white_king_check:
                                            del square_list[check_square_knight][2:]
                                            del square_list[squares_5][2:]
                                            for values in check_square_knight_values:
                                                square_list[check_square_knight].append(values)
                                            if white_knight.file == white_knight2.file:
                                                if "N" + check_square_knight[1] + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("N" + check_square_knight[1] + squares_5)
                                            elif white_knight.row == white_knight2.row:
                                                if "N" + check_square_knight[0] + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("N" + check_square_knight[0] + squares_5)
                                            else:
                                                if "N" +  squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("N" + squares_5)
                                            self.white_king_check = True
                                            white_king_check = True
                                        else:
                                            del square_list[check_square_knight][2:]
                                            del square_list[squares_5][2:]
                                            for values in check_square_knight_values:
                                                square_list[check_square_knight].append(values)
                                            self.white_king_check = True
                                            white_king_check = True
        print("LEGAL MOVES: "+str(legal_moves_list))
        if legal_moves_list == []:
            global white_checkmate
            white_checkmate = True

    def check_check_black(self, old_square, new_file, new_row):
        file_list = "abcdefgh"
        file_letter = []
        row_number = []
        for file in file_list:
            file_letter.append(file)
        for row in range(1, 9):
            row_number.append(row)

        if self.piece_name == "king" \
                and self.piece_color == "black" \
                and self.black_king_castle:
            black_king_square = (new_file + str(new_row))
            black_king_file = new_file
            black_king_row = new_row
            king_file_index = file_letter.index(black_king_file)
            king_row_number = row_number.index(black_king_row)
        elif self.piece_name == "king" \
                and self.piece_color == "black" \
                and not self.black_king_castle:
            try:
                black_king_square = (self.new_file + str(self.new_row))
                black_king_file = self.new_file
                black_king_row = self.new_row
                king_file_index = file_letter.index(black_king_file)
                king_row_number = row_number.index(black_king_row)
            except AttributeError:
                black_king_square = black_king.file + str(black_king.row)
                black_king_file = black_king.file
                black_king_row = black_king.row
                king_file_index = file_letter.index(black_king_file)
                king_row_number = row_number.index(black_king_row)
        else:
            black_king_square = black_king.file + str(black_king.row)
            black_king_file = black_king.file
            black_king_row = black_king.row
            king_file_index = file_letter.index(black_king_file)
            king_row_number = row_number.index(black_king.row)



        global turn
        global black_king_check


        between_check_square_list = []
        charlistje = "abcdefgh"
        for charje in charlistje:
            for cifje in range(1, 9):
                square_bet = charje + str(cifje)
                between_check_square_list.append(square_bet)

        king_index = between_check_square_list.index(black_king_square)


        self.black_check_list = list()

        # we make a few lists of squares in which the king can be "touched" by other pieces
        # these squares can be checked if they're occupied by pieces that potentially check the king


        # this next block addresses moving own pieces and thereby self checking for if black piece is bishop, pawn or queen on the diagonal
        # by checking if any pieces are blocking the check, or if the distance is one square(diagonal)
        # the king has to move out of check or the check piece has to be taken.
        # This definition is called after a new move has been made, it evaluates this move and places it back if the king is (still) in check
        # make list of diagonal line right up from king position

        diagonal_check_list = []
        for i in [check_square for check_square in range(-8, 8)]:
            try:
                if king_file_index - i > -1 \
                        and king_row_number + i > -1 \
                        and file_letter[king_file_index - i] != black_king_file:
                    check_square = (file_letter[king_file_index - i] + str(row_number[king_row_number + i]))
                    if check_square not in diagonal_check_list:
                        diagonal_check_list.append(check_square)
            except IndexError:
                pass
        # make list of diagonal line right down from king position
        for i in [check_square for check_square in range(-8, 8)]:
            try:
                if king_file_index + i > -1 \
                        and king_row_number + i > -1 \
                        and file_letter[king_file_index + i] != black_king_file:
                    check_square = (file_letter[king_file_index + i] + str(row_number[king_row_number + i]))
                    if check_square not in diagonal_check_list:
                        diagonal_check_list.append(check_square)
            except IndexError:
                pass
        #print("diagonal checklist for "+str(king_index)+"is list "+ str(diagonal_check_list))

        self.between_bishop_squares_list2 = dict()
        for check_square in diagonal_check_list:
            if "bishop" in square_list[check_square] \
                    and "white" in square_list[check_square] \
                    or "queen" in square_list[check_square] \
                    and "white" in square_list[check_square] \
                    or "pawn" in square_list[check_square] \
                    and "white" in square_list[check_square] \
                    or "king" in square_list[check_square] \
                    and "white" in square_list[check_square]:
                bishop_queen_index = between_check_square_list.index(check_square)
                if abs(king_index - bishop_queen_index) > 7 \
                        and abs(king_index - bishop_queen_index) != 9 \
                        and "bishop" in square_list[check_square] \
                        or abs(king_index - bishop_queen_index) > 7 \
                        and abs(king_index - bishop_queen_index) != 9 \
                        and "queen" in square_list[check_square]:
                    between_bishop_squares = list()
                    if king_index > bishop_queen_index:
                        if (king_index - bishop_queen_index) % 7 == 0:
                            for squares in range(bishop_queen_index + 7, king_index, 7):
                                if between_check_square_list[squares] not in between_bishop_squares:
                                    between_bishop_squares.append(between_check_square_list[squares])
                        elif (king_index - bishop_queen_index) % 9 == 0:
                            for squares in range(bishop_queen_index + 9, king_index, 9):
                                if between_check_square_list[squares] not in between_bishop_squares:
                                    between_bishop_squares.append(between_check_square_list[squares])
                    elif king_index < bishop_queen_index:
                        if abs((king_index - bishop_queen_index) % 7) == 0:
                            for squares in range(king_index + 7, bishop_queen_index, 7):
                                if between_check_square_list[squares] not in between_bishop_squares:
                                    between_bishop_squares.append(between_check_square_list[squares])
                        elif abs(king_index - bishop_queen_index) % 9 == 0:
                            for squares in range(king_index + 9, bishop_queen_index, 9):
                                if between_check_square_list[squares] not in between_bishop_squares:
                                    between_bishop_squares.append(between_check_square_list[squares])
                    block_squares = between_bishop_squares.copy()
                    block_squares.append(between_check_square_list[bishop_queen_index])
                    self.between_bishop_squares_list2.setdefault(str(square_list[check_square][4]), []).append(block_squares)
                    if any(("OCCUPIED" and "black") in square_list[square] for square in between_bishop_squares) \
                            or between_bishop_squares == []:
                        black_check = "FALSE"
                        self.black_check_list.append(black_check)
                    elif any(("OCCUPIED" and "white" and "pawn") in square_list[square] for square in between_bishop_squares) \
                            or any(("OCCUPIED" and "white" and "king") in square_list[square] for square in between_bishop_squares) \
                            or any(("OCCUPIED" and "white" and "knight") in square_list[square] for square in between_bishop_squares) \
                            or any(("OCCUPIED" and "white" and "rook") in square_list[square] for square in between_bishop_squares):
                        black_check = "FALSE"
                        self.black_check_list.append(black_check)
                    else:
                        if turn % 2 == 0 and self.piece_color == "black" and self.black_king_castle:
                            black_check = "TRUE"
                            self.black_check_list.append(black_check)
                        elif turn % 2 == 0 and self.piece_color == "black" and not self.black_king_castle:
                            black_check = "TRUE"
                            self.black_check_list.append(black_check)
                        elif turn % 2 == 1 and self.piece_color == "white":
                            black_check = "TRUE"
                            self.black_check_list.append(black_check)
                elif king_index - bishop_queen_index == 9 \
                            and "pawn"  in square_list[check_square] \
                            or bishop_queen_index - king_index == 7 \
                            and "pawn" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 7\
                            and "bishop" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 9 \
                            and "bishop" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 7 \
                            and "queen" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 9 \
                            and "queen" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 7 \
                            and "king" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 9 \
                            and "king" in square_list[check_square]:
                    self.between_bishop_squares_list2.setdefault(str(square_list[check_square][4]), []).append([check_square])
                    if turn % 2 == 0 and self.piece_color == "black" and self.black_king_castle:
                        black_check = "TRUE"
                        self.black_check_list.append(black_check)
                    elif turn % 2 == 0 and self.piece_color == "black" and not self.black_king_castle:
                        black_check = "TRUE"
                        self.black_check_list.append(black_check)
                    elif turn % 2 == 1 and self.piece_color == "white":
                        black_check = "TRUE"
                        self.black_check_list.append(black_check)




        # make list of horizontal line
        straight_check_list = []
        for i in [check_square_straight for check_square_straight in range(0, 8) if check_square_straight != king_file_index]:
            try:
                check_square_straight = (file_letter[i] + str(black_king_row))
                if check_square_straight not in straight_check_list:
                    straight_check_list.append(check_square_straight)
            except IndexError:
                pass
        # add vertical lines
        for i in [check_square_straight for check_square_straight in range(0, 8) if check_square_straight != king_row_number]:
            try:
                check_square_straight = (black_king_file + str(row_number[i]))
                if check_square_straight not in straight_check_list:
                    straight_check_list.append(check_square_straight)
            except IndexError:
                pass
        #print("straight checklist for " + str(king_index) + " is list " + str(straight_check_list))

        for check_square_straight in straight_check_list:
            if "rook" in square_list[check_square_straight] \
                    and "white" in square_list[check_square_straight] \
                    or "queen" in square_list[check_square_straight] \
                    and "white" in square_list[check_square_straight] \
                    or "king" in square_list[check_square_straight] \
                    and "white" in square_list[check_square_straight]:
                check_piece_index = between_check_square_list.index(check_square_straight)
                if abs(king_index - check_piece_index) > 1 \
                        and abs(king_index - check_piece_index) != 8 \
                        and "rook" in square_list[check_square_straight] \
                        or abs(king_index - check_piece_index) > 1 \
                        and abs(king_index - check_piece_index) != 8 \
                        and "queen" in square_list[check_square_straight]:
                    between_rook_queen_squares = list()
                    if king_index > check_piece_index:
                        if 8 > (king_index - check_piece_index) > 0:
                            for squares2 in range(check_piece_index + 1, king_index,  1):
                                if between_check_square_list[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(between_check_square_list[squares2])
                        if abs(king_index - check_piece_index) % 8 == 0:
                            for squares2 in range(check_piece_index + 8, king_index, 8):
                                if between_check_square_list[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(between_check_square_list[squares2])
                    elif king_index < check_piece_index:
                        if 8 > abs(king_index - check_piece_index) > 0:
                            for squares2 in range(king_index + 1, check_piece_index, 1):
                                if between_check_square_list[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(between_check_square_list[squares2])
                        elif abs(king_index - check_piece_index) % 8 == 0:
                            for squares2 in range(king_index + 8, check_piece_index, 8):
                                if between_check_square_list[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(between_check_square_list[squares2])
                    block_squares_2 = between_rook_queen_squares.copy()
                    block_squares_2.append(between_check_square_list[check_piece_index])
                    self.between_bishop_squares_list2.setdefault(str(square_list[check_square_straight][4]), []).append(block_squares_2)
                    if any(("OCCUPIED" and "black") in square_list[square] for square in between_rook_queen_squares) \
                            or between_rook_queen_squares == []:
                        black_check = "FALSE"
                        self.black_check_list.append(black_check)
                    elif any(("OCCUPIED" and "white" and "pawn") in square_list[square] for square in between_rook_queen_squares) \
                            or any(("OCCUPIED" and "white" and "king") in square_list[square] for square in between_rook_queen_squares) \
                            or any(("OCCUPIED" and "white" and "bishop") in square_list[square] for square in between_rook_queen_squares) \
                            or any(("OCCUPIED" and "white" and "knight") in square_list[square] for square in between_rook_queen_squares):
                        black_check = "FALSE"
                        self.black_check_list.append(black_check)
                    else:
                        if turn % 2 == 0 and self.piece_color == "black" and self.black_king_castle:
                            black_check = "TRUE"
                            self.black_check_list.append(black_check)
                        elif turn %  2 == 0 and self.piece_color == "black" and not self.black_king_castle:
                            black_check = "TRUE"
                            self.black_check_list.append(black_check)
                        elif turn % 2 == 1 and self.piece_color == "white":
                            black_check = "TRUE"
                            self.black_check_list.append(black_check)

                elif abs(king_index - check_piece_index) == 1 \
                            and "rook" in square_list[check_square_straight] \
                            or abs(king_index - check_piece_index) == 8 \
                            and "rook" in square_list[check_square_straight] \
                            or abs(king_index - check_piece_index) == 1 \
                            and "queen" in square_list[check_square_straight] \
                            or abs(king_index - check_piece_index) == 8 \
                            and "queen" in square_list[check_square_straight] \
                            or abs(king_index - check_piece_index) == 1 \
                            and "king" in square_list[check_square_straight] \
                            or abs(king_index - check_piece_index) == 8 \
                            and "king" in square_list[check_square_straight]:
                    self.between_bishop_squares_list2.setdefault(str(square_list[check_square_straight][4]), []).append([check_square_straight])
                    if turn % 2 == 0 and self.piece_color == "black" and self.black_king_castle:
                        black_check = "TRUE"
                        self.black_check_list.append(black_check)
                    elif turn % 2 == 0 and self.piece_color == "black" and not self.black_king_castle:
                        black_check = "TRUE"
                        self.black_check_list.append(black_check)
                    elif turn % 2 == 1 and self.piece_color == "white":
                        black_check = "TRUE"
                        self.black_check_list.append(black_check)


        knight_check_list = []
        # add the potential knight squares
        if 8 > king_file_index + 1 > -1 \
                and 8 > king_row_number + 2 > -1:
            check_square_knight = (file_letter[king_file_index + 1] + str(row_number[king_row_number + 2]))
            if check_square_knight not in knight_check_list:
                knight_check_list.append(check_square_knight)
        if 8 > king_file_index - 1 > -1 \
                and 8 >king_row_number + 2 > -1:
            check_square_knight = (file_letter[king_file_index - 1] + str(row_number[king_row_number + 2]))
            if check_square_knight not in knight_check_list:
                knight_check_list.append(check_square_knight)
        if 8 >king_file_index + 1 > -1 \
                and 8 >king_row_number - 2 > -1:
            check_square_knight = (file_letter[king_file_index + 1] + str(row_number[king_row_number - 2]))
            if check_square_knight not in knight_check_list:
                knight_check_list.append(check_square_knight)
        if 8 > king_file_index - 1 > -1 \
                and 8 > king_row_number - 2 > -1:
            check_square_knight = (file_letter[king_file_index - 1] + str(row_number[king_row_number - 2]))
            if check_square_knight not in knight_check_list:
                knight_check_list.append(check_square_knight)
        if 8 > king_file_index + 2 > -1 \
                and 8 > king_row_number - 1 > -1:
            check_square_knight = (file_letter[king_file_index + 2] + str(row_number[king_row_number - 1]))
            if check_square_knight not in knight_check_list:
                knight_check_list.append(check_square_knight)
        if 8 > king_file_index - 2 > -1 \
                and 8 > king_row_number - 1 > -1:
            check_square_knight = (file_letter[king_file_index - 2] + str(row_number[king_row_number - 1]))
            if check_square_knight not in knight_check_list:
                knight_check_list.append(check_square_knight)
        if 8 > king_file_index + 2 > -1 \
                and 8 > king_row_number + 1 > -1:
            check_square_knight = (file_letter[king_file_index + 2] + str(row_number[king_row_number + 1]))
            if check_square_knight not in knight_check_list:
                knight_check_list.append(check_square_knight)
        if 8 > king_file_index - 2 > -1 \
                and 8 > king_row_number + 1 > -1:
            check_square_knight = (file_letter[king_file_index - 2] + str(row_number[king_row_number + 1]))
            if check_square_knight not in knight_check_list:
                knight_check_list.append(check_square_knight)



        for check_square_knight in knight_check_list:
            if "knight" in square_list[check_square_knight] \
                    and "white" in square_list[check_square_knight]:
                knight_index = between_check_square_list.index(check_square_knight)
                if abs(king_index - knight_index) == 17 \
                        or abs(king_index - knight_index) == 15 \
                        or abs(king_index - knight_index) == 10 \
                        or abs(king_index - knight_index) == 6:
                    self.between_bishop_squares_list2.setdefault(str(square_list[check_square_knight][4]), []).append([check_square_knight])
                    if turn % 2 == 0 and self.piece_color == "black" and self.black_king_castle:
                        black_check = "TRUE"
                        self.black_check_list.append(black_check)
                    elif turn % 2 == 0 and self.piece_color == "black" and not self.black_king_castle:
                        black_check = "TRUE"
                        self.black_check_list.append(black_check)
                    elif turn % 2 == 1 and self.piece_color == "white":
                        black_check = "TRUE"
                        self.black_check_list.append(black_check)
                else:
                    black_check = "FALSE"
                    self.black_check_list.append(black_check)

        if "TRUE" in self.black_check_list:
            self.black_king_check = True
            black_king_check = True
        elif "TRUE" not in self.black_check_list:
            self.black_king_check = False
            black_king_check = False

    def place_back_black(self, new_square, old_square):
        global turn
        del square_list[new_square][2:]
        square_list[self.old_square].append("OCCUPIED")
        square_list[self.old_square].append(self.piece_color)
        square_list[self.old_square].append(self.piece_name)
        if self.piece_name == "king" \
                and "MOVED" in square_list[old_square]:
            square_list[self.old_square].append("MOVED")
        if self.piece_name == "rook" \
                and "MOVED" in square_list[self.old_square]:
            square_list[self.old_square].append("MOVED")
        if self.piece_name == "pawn" \
                and "MOVED" in square_list[self.old_square]:
            square_list[self.old_square].append("MOVED")
        self.new_square = old_square
        self.square = old_square
        self.new_file = self.old_file
        self.new_row = self.old_row
        turn = 3

    def check_checkmate_black(self):
        global black_king_check
        self.checkmate_check = True
        legal_moves_list = list()
        king_moves_list = list()
        full_board_index = list()

        charlistje = "abcdefgh"
        for charje in charlistje:
            for cifje in range(1, 9):
                square_bet = charje + str(cifje)
                full_board_index.append(square_bet)

        filelist = "abcdefgh"
        file_letter = []
        row_number = []
        for file in filelist:
            file_letter.append(file)
        for row in range(1, 9):
            row_number.append(row)

        if self.piece_name == "king" \
                and self.piece_color == "black":
            try:
                black_king_square = (self.new_file + str(self.new_row))
                black_king_file = self.new_file
                black_king_row = self.new_row
                king_file_index = file_letter.index(black_king_file)
                king_row_number = row_number.index(black_king_row)
            except AttributeError:
                black_king_square = black_king.file + str(black_king.row)
                black_king_file = black_king.file
                black_king_row = black_king.row
                king_file_index = file_letter.index(black_king_file)
                king_row_number = row_number.index(black_king_row)
        else:
            black_king_square = black_king.file + str(black_king.row)
            black_king_file = black_king.file
            black_king_row = black_king.row
            king_file_index = file_letter.index(black_king_file)
            king_row_number = row_number.index(black_king_row)
        # print("kingfileindex " + str(king_file_index))
        old_black_king_values = square_list[black_king_square][2:]
        del square_list[black_king_square][2:]
        if 8 > king_file_index + 1 > -1 \
                and 8 > king_row_number + 1 > -1:
            king_square = file_letter[king_file_index + 1] + str(row_number[king_row_number + 1])
            king_moves_list.append(king_square)
        if 8 > king_file_index + 1 > 0 \
                and 8 > king_row_number - 1 > -1:
            king_square = file_letter[king_file_index + 1] + str(row_number[king_row_number - 1])
            king_moves_list.append(king_square)
        if 8 > king_file_index - 1 > -1 \
                and 8 > king_row_number + 1 > -1:
            king_square = file_letter[king_file_index - 1] + str(row_number[king_row_number + 1])
            king_moves_list.append(king_square)
        if 8 > king_file_index - 1 > -1 \
                and 8 > king_row_number - 1 > -1:
            king_square = file_letter[king_file_index - 1] + str(row_number[king_row_number - 1])
            king_moves_list.append(king_square)
        if 8 > king_file_index + 1 > -1:
            king_square = file_letter[king_file_index + 1] + str(row_number[king_row_number])
            king_moves_list.append(king_square)
        if 8 > king_file_index - 1 > -1:
            king_square = file_letter[king_file_index - 1] + str(row_number[king_row_number])
            king_moves_list.append(king_square)
        if 8 > king_row_number + 1 > -1:
            king_square = file_letter[king_file_index] + str(row_number[king_row_number + 1])
            king_moves_list.append(king_square)
        if 8 > king_row_number - 1 > -1:
            king_square = file_letter[king_file_index] + str(row_number[king_row_number - 1])
            king_moves_list.append(king_square)



        for occupied_square in [square for square in king_moves_list if "OCCUPIED" and "black" in square_list[square]]:
            king_moves_list.remove(occupied_square)

        for square in king_moves_list:
            check_list = list()
            square_letter = square[0]
            square_cijfer = int(square[1])
            king_file_check = file_letter.index(square_letter)
            king_row_check = row_number.index(square_cijfer)
            straight_check_list = []
            for i in [check_square_straight for check_square_straight in range(0, 8) if
                      check_square_straight != king_file_check]:
                try:
                    check_square_straight = (file_letter[i] + str(square_cijfer))
                    if check_square_straight not in straight_check_list:
                        straight_check_list.append(check_square_straight)
                except IndexError:
                    pass
            # add vertical lines
            for i in [check_square_straight for check_square_straight in range(0, 8) if
                      check_square_straight != king_row_check]:
                try:
                    check_square_straight = (square_letter + str(row_number[i]))
                    if check_square_straight not in straight_check_list:
                        straight_check_list.append(check_square_straight)
                except IndexError:
                    pass
            # print("straight checklist for " + square + " is list " + str(straight_check_list))
            king_index = full_board_index.index(square)
            check_piece_index_list = dict()

            for check_square_straight in [squares for squares in straight_check_list if "white" in square_list[squares]
                                                                                        and "rook" in square_list[
                                                                                            squares]
                                                                                        or "queen" in square_list[
                                                                                            squares]
                                                                                        and "white" in square_list[
                                                                                            squares]
                                                                                        or "king" in square_list[
                                                                                            squares]
                                                                                        and "white" in square_list[
                                                                                            squares]]:


                check_piece_index = full_board_index.index(check_square_straight)
                if abs(king_index - check_piece_index) > 1 \
                        and abs(king_index - check_piece_index) != 8 \
                        and "rook" in square_list[check_square_straight] \
                        or abs(king_index - check_piece_index) > 1 \
                        and abs(king_index - check_piece_index) != 8 \
                        and "queen" in square_list[check_square_straight]:
                    between_rook_queen_squares = list()
                    if king_index > check_piece_index:
                        if 0 < (king_index - check_piece_index) < 8:
                            for squares2 in range(check_piece_index + 1, king_index, 1):
                                if full_board_index[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(full_board_index[squares2])
                        elif (king_index - check_piece_index) % 8 == 0:
                            for squares2 in range(check_piece_index + 8, king_index, 8):
                                if full_board_index[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(full_board_index[squares2])
                    elif king_index < check_piece_index:
                        if 0 < abs(king_index - check_piece_index) < 8:
                            for squares2 in range(king_index + 1, check_piece_index, 1):
                                if full_board_index[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(full_board_index[squares2])
                        elif abs(king_index - check_piece_index) % 8 == 0:
                            for squares2 in range(king_index + 8, check_piece_index, 8):
                                if full_board_index[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(full_board_index[squares2])
                    check_piece_index_list.setdefault(square, []).append(between_rook_queen_squares)
                    for i in range(0, len(check_piece_index_list[square])):
                        if any({"OCCUPIED", "black"}.issubset(set(square_list[square])) for square in
                               check_piece_index_list[square][i]):
                            check_list.append("FALSE")
                        elif any({"OCCUPIED", "white", "pawn"}.issubset(set(square_list[square])) for square in check_piece_index_list[square][i]) \
                                or any({"OCCUPIED", "white", "king"}.issubset(set(square_list[square])) for square in check_piece_index_list[square][i]) \
                                or any({"OCCUPIED", "white", "bishop"}.issubset(set(square_list[square])) for square in check_piece_index_list[square][i]) \
                                or any({"OCCUPIED", "white", "knight"}.issubset(set(square_list[square])) for square in check_piece_index_list[square][i]):
                            check_list.append("FALSE")
                        elif not any({"OCCUPIED"}.issubset(set(square_list[square])) for square in check_piece_index_list[square][i]):
                            check_list.append("TRUE")
                elif abs(king_index - check_piece_index) == 1 \
                         and "rook" in square_list[check_square_straight] \
                         or abs(king_index - check_piece_index) == 8 \
                         and "rook" in square_list[check_square_straight] \
                         or abs(king_index - check_piece_index) == 1 \
                         and "queen"  in square_list[check_square_straight] \
                         or abs(king_index - check_piece_index) == 8 \
                         and "queen" in square_list[check_square_straight] \
                         or abs(king_index - check_piece_index) == 1 \
                         and "king" in square_list[check_square_straight] \
                         or abs(king_index - check_piece_index) == 8 \
                         and "king"  in square_list[check_square_straight]:
                    check_list.append("TRUE")
            if not any({"white", "rook"}.issubset(set(square_list[square])) for square in straight_check_list) \
                    and not any({"white", "queen"}.issubset(set(square_list[square])) for square in straight_check_list):
                check_list.append("FALSE")



            diagonal_check_list = []
            for i in [check_square for check_square in range(-8, 8)]:
                try:
                    if king_file_check - i > -1 \
                            and king_row_check + i > -1 \
                            and file_letter[king_file_check - i] != square_letter:
                        check_square = (file_letter[king_file_check - i] + str(row_number[king_row_check + i]))
                        if check_square not in diagonal_check_list:
                            diagonal_check_list.append(check_square)
                except IndexError:
                    pass
            # make list of diagonal line right down from king position
            for i in [check_square for check_square in range(-8, 8)]:
                try:
                    if king_file_check + i > -1 \
                            and king_row_check + i > -1 \
                            and file_letter[king_file_check + i] != square_letter:
                        check_square = (file_letter[king_file_check + i] + str(row_number[king_row_check + i]))
                        if check_square not in diagonal_check_list:
                            diagonal_check_list.append(check_square)
                except IndexError:
                    pass

            between_squares_list_list = dict()
            #print("De diagonal voor de square: " + square +" is "+ str(diagonal_check_list))
            for check_square in diagonal_check_list:
                if "bishop" in square_list[check_square] \
                        and "white" in square_list[check_square] \
                        or "queen" in square_list[check_square] \
                        and "white" in square_list[check_square] \
                        or "pawn" in square_list[check_square] \
                        and "white" in square_list[check_square] \
                        or "king" in square_list[check_square] \
                        and "white" in square_list[check_square]:
                    bishop_queen_index = full_board_index.index(check_square)
                    if abs(king_index - bishop_queen_index) > 7 \
                            and abs(king_index - bishop_queen_index) != 9 \
                            and "bishop" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) > 7 \
                            and abs(king_index - bishop_queen_index) != 9 \
                            and "queen" in square_list[check_square]:
                        between_bishop_squares = list()
                        if king_index > bishop_queen_index:
                            if (king_index - bishop_queen_index) % 7 == 0:
                                for squares in range(bishop_queen_index + 7, king_index, 7):
                                    if full_board_index[squares] not in between_bishop_squares:
                                        between_bishop_squares.append(full_board_index[squares])
                            elif (king_index - bishop_queen_index) % 9 == 0:
                                for squares in range(bishop_queen_index + 9, king_index, 9):
                                    if full_board_index[squares] not in between_bishop_squares:
                                        between_bishop_squares.append(full_board_index[squares])
                        elif king_index < bishop_queen_index:
                            if abs((king_index - bishop_queen_index) % 7) == 0:
                                for squares in range(king_index + 7, bishop_queen_index, 7):
                                    if full_board_index[squares] not in between_bishop_squares:
                                        between_bishop_squares.append(full_board_index[squares])
                            elif abs(king_index - bishop_queen_index) % 9 == 0:
                                for squares in range(king_index + 9, bishop_queen_index, 9):
                                    if full_board_index[squares] not in between_bishop_squares:
                                        between_bishop_squares.append(full_board_index[squares])
                        between_squares_list_list.setdefault(square, []).append(between_bishop_squares)
                        for i in range(0, len(between_squares_list_list[square])):
                            if any({"OCCUPIED", "black"}.issubset(set(square_list[square])) for square in between_squares_list_list[square][i]):
                                check_list.append("FALSE")
                            elif any({"OCCUPIED", "white", "pawn"}.issubset(set(square_list[square])) for square in between_squares_list_list[square][i]) \
                                    or any({"OCCUPIED", "white", "king"}.issubset(set(square_list[square])) for square in between_squares_list_list[square][i]) \
                                    or any({"OCCUPIED", "white", "rook"}.issubset(set(square_list[square])) for square in between_squares_list_list[square][i]) \
                                    or any({"OCCUPIED", "white", "knight"}.issubset(set(square_list[square])) for square in between_squares_list_list[square][i]):
                                check_list.append("FALSE")
                            elif not any({"OCCUPIED"}.issubset(set(square_list[square])) for square in between_squares_list_list[square][i]):
                                check_list.append("TRUE")
                    elif abs(king_index - bishop_queen_index) == 7 \
                            and "pawn" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 9 \
                            and "pawn" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 7 \
                            and "bishop" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 9 \
                            and "bishop" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 7 \
                            and "queen" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 9 \
                            and "queen" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 7 \
                            and "king" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 9 \
                            and "king" in square_list[check_square]:
                        check_list.append("TRUE")
            if not any({"white", "bishop"}.issubset(set(square_list[square])) for square in diagonal_check_list) \
                    and not any({"white", "queen"}.issubset(set(square_list[square])) for square in diagonal_check_list):
                check_list.append("FALSE")


            knight_check_list = list()
            if 8 > king_file_check + 1 > -1 \
                    and 8 > king_row_check + 2 > -1:
                check_square_knight = (file_letter[king_file_check + 1] + str(row_number[king_row_check + 2]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check - 1 > -1 \
                    and 8 > king_row_check + 2 > -1:
                check_square_knight = (file_letter[king_file_check - 1] + str(row_number[king_row_check + 2]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check + 1 > -1 \
                    and 8 > king_row_check - 2 > -1:
                check_square_knight = (file_letter[king_file_check + 1] + str(row_number[king_row_check - 2]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check - 1 > -1 \
                    and 8 > king_row_check - 2 > -1:
                check_square_knight = (file_letter[king_file_check - 1] + str(row_number[king_row_check - 2]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check + 2 > -1 \
                    and 8 > king_row_check - 1 > -1:
                check_square_knight = (file_letter[king_file_check + 2] + str(row_number[king_row_check - 1]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check - 2 > -1 \
                    and 8 > king_row_check - 1 > -1:
                check_square_knight = (file_letter[king_file_check - 2] + str(row_number[king_row_check - 1]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check + 2 > -1 \
                    and 8 > king_row_check + 1 > -1:
                check_square_knight = (file_letter[king_file_check + 2] + str(row_number[king_row_check + 1]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check - 2 > -1 \
                    and 8 > king_row_check + 1 > -1:
                check_square_knight = (file_letter[king_file_check - 2] + str(row_number[king_row_check + 1]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)

            for check_square_knight in knight_check_list:
                if "knight" in square_list[check_square_knight] \
                        and "white" in square_list[check_square_knight]:
                    knight_index = full_board_index.index(check_square_knight)
                    if abs(king_index - knight_index) == 17 \
                            or abs(king_index - knight_index) == 15 \
                            or abs(king_index - knight_index) == 10 \
                            or abs(king_index - knight_index) == 6:
                        check_list.append("TRUE")
            if not any({"white", "knight"}.issubset(set(square_list[square3])) for square3 in knight_check_list):
                check_list.append("FALSE")

            # print("check checklist for square: "+ square + " is " + str(check_list))


            if "TRUE" in check_list:
                if "K" + square in legal_moves_list:
                    legal_moves_list.remove("K" +  square)
            if "TRUE" not in check_list:
                if "K" +  square not in legal_moves_list:
                    legal_moves_list.append("K" + square)

        for value in old_black_king_values:
            square_list[black_king_square].append(value)


        # self.check_check_white(white_king_square, white_king_file, white_king_row)
        #print("SELF.BETWEEN BISHOP SQUARES UIT CHECKCHECK IN CHECMATE CHECK " + str(self.between_bishop_squares_list))

        # LETS TRY TO SEE IF WE CAN MAKE A LIST OF THE BETWEEN SQUARES AND IF THESE CAN BE BLOCKED BY OWN PIECES
        for piece, squares in self.between_bishop_squares_list2.items():
            for squares_4 in self.between_bishop_squares_list2[piece]:
                print(self.between_bishop_squares_list2[piece])
                if any("OCCUPIED" in square_list[square] for square in squares_4[:-1]):
                    pass
                else:
                    pass
                    for squares_5 in squares_4:
                        print(squares_5)
                        piece_letter = squares_5[0]
                        piece_row = int(squares_5[1])
                        square_index = full_board_index.index(squares_5)
                        piece_file_check = file_letter.index(piece_letter)
                        piece_row_check = row_number.index(piece_row)
                        piece_straight_check_list = list()

                        for i in [check_square_straight for check_square_straight in range(0, 8) if
                                  check_square_straight != piece_file_check]:
                            try:
                                check_square_straight = (file_letter[i] + str(piece_row))
                                if check_square_straight not in piece_straight_check_list:
                                    piece_straight_check_list.append(check_square_straight)
                            except IndexError:
                                pass
                        # add vertical lines
                        for i in [check_square_straight for check_square_straight in range(0, 8) if
                                  check_square_straight != piece_row_check]:
                            try:
                                check_square_straight = (piece_letter + str(row_number[i]))
                                if check_square_straight not in piece_straight_check_list:
                                    piece_straight_check_list.append(check_square_straight)
                            except IndexError:
                                pass
                        piece_index_list = dict()
                        for square_6 in piece_straight_check_list:
                            if "rook" in square_list[square_6] \
                                    and "black" in square_list[square_6] \
                                    or "pawn" in square_list[square_6] \
                                    and "black" in square_list[square_6] \
                                    or "queen" in square_list[square_6] \
                                    and "black" in square_list[square_6]:
                                piece_index = full_board_index.index(square_6)
                                if abs(square_index - piece_index) > 1 \
                                        and abs(square_index - piece_index) != 8 \
                                        and "rook" in square_list[square_6] \
                                        or abs(square_index - piece_index) > 1 \
                                        and abs(square_index - piece_index) != 8 \
                                        and "queen" in square_list[square_6]:
                                    between_rook_queen_squares = list()
                                    if square_index > piece_index:
                                        if 0 < (square_index - piece_index) < 8:
                                            for squares2 in range(piece_index + 1, square_index, 1):
                                                if full_board_index[squares2] not in between_rook_queen_squares:
                                                    between_rook_queen_squares.append(full_board_index[squares2])
                                        elif (square_index - piece_index) % 8 == 0:
                                            for squares2 in range(piece_index + 8, square_index, 8):
                                                if full_board_index[squares2] not in between_rook_queen_squares:
                                                    between_rook_queen_squares.append(full_board_index[squares2])
                                    elif square_index < piece_index:
                                        if 0 < abs(square_index - piece_index) < 8:
                                            for squares2 in range(square_index + 1, piece_index, 1):
                                                if full_board_index[squares2] not in between_rook_queen_squares:
                                                    between_rook_queen_squares.append(full_board_index[squares2])
                                        elif abs(square_index - piece_index) % 8 == 0:
                                            for squares2 in range(square_index + 8, piece_index, 8):
                                                if full_board_index[squares2] not in between_rook_queen_squares:
                                                    between_rook_queen_squares.append(full_board_index[squares2])
                                    piece_index_list.setdefault(squares_5, []).append(between_rook_queen_squares)
                                    if len(piece_index_list[squares_5]) > 1:
                                        for i in range(0, len(piece_index_list[squares_5])):
                                            if not any({"OCCUPIED"}.issubset(set(square_list[square_6])) for square_6 in piece_index_list[squares_5][i]):
                                                if "OCCUPIED" in square_list[squares_5]:
                                                    old_square_6_values = square_list[square_6][2:]
                                                    old_square_5_values = square_list[squares_5][2:]
                                                    del square_list[square_6][2:]
                                                    del square_list[squares_5][2:]
                                                    square_list[squares_5].append("OCCUPIED")
                                                    square_list[squares_5].append("black")
                                                    if "rook" in old_square_6_values:
                                                        square_list[squares_5].append("rook")
                                                    elif "queen" in old_square_6_values:
                                                        square_list[squares_5].append("queen")
                                                    self.check_check_black(black_king.square, black_king.file, black_king.row)
                                                    if not self.black_king_check:
                                                        del square_list[square_6][2:]
                                                        del square_list[squares_5][2:]
                                                        for values in old_square_6_values:
                                                            square_list[square_6].append(values)
                                                        for values in old_square_5_values:
                                                            square_list[squares_5].append(values)
                                                        if "rook" in square_list[square_6]:
                                                            if "R" + square_6[0] +"x"+ squares_5 not in legal_moves_list:
                                                                legal_moves_list.append("R" + square_6[0] + "x" + squares_5)
                                                        elif "queen" in square_list[square_6]:
                                                            if "Qx"+ squares_5 not in legal_moves_list:
                                                                legal_moves_list.append("Qx" + squares_5)
                                                        self.black_king_check = True
                                                        black_king_check = True
                                                    else:
                                                        del square_list[square_6][2:]
                                                        del square_list[squares_5][2:]
                                                        for values in old_square_6_values:
                                                            square_list[square_6].append(values)
                                                        for values in old_square_5_values:
                                                            square_list[squares_5].append(values)
                                                        self.black_king_check = True
                                                        black_king_check = True
                                                else:
                                                    old_square_6_values = square_list[square_6][2:]
                                                    del square_list[square_6][2:]
                                                    square_list[squares_5].append("OCCUPIED")
                                                    square_list[squares_5].append("black")
                                                    if "rook" in old_square_6_values:
                                                        square_list[squares_5].append("rook")
                                                    elif "queen" in old_square_6_values:
                                                        square_list[squares_5].append("queen")
                                                    self.check_check_black(black_king.square, black_king.file, black_king.row)
                                                    if not self.black_king_check:
                                                        del square_list[square_6][2:]
                                                        del square_list[squares_5][2:]
                                                        for values in old_square_6_values:
                                                            square_list[square_6].append(values)
                                                        if "rook" in square_list[square_6]:
                                                            if "R" + square_6[0] + squares_5 not in legal_moves_list:
                                                                legal_moves_list.append("R" + square_6[0] + squares_5)
                                                        elif "queen" in square_list[square_6]:
                                                            if "Q"+ squares_5 not in legal_moves_list:
                                                                legal_moves_list.append("Q" + squares_5)
                                                        self.black_king_check = True
                                                        black_king_check = True
                                                    else:
                                                        del square_list[square_6][2:]
                                                        del square_list[squares_5][2:]
                                                        for values in old_square_6_values:
                                                            square_list[square_6].append(values)
                                                        self.black_king_check = True
                                                        black_king_check = True
                                    elif len(piece_index_list[squares_5]) < 2:
                                        if not any({"OCCUPIED"}.issubset(set(square_list[square_6])) for square_6 in between_rook_queen_squares):
                                            if "OCCUPIED" in square_list[squares_5]:
                                                old_square_6_values = square_list[square_6][2:]
                                                old_square_5_values = square_list[squares_5][2:]
                                                del square_list[square_6][2:]
                                                del square_list[squares_5][2:]
                                                square_list[squares_5].append("OCCUPIED")
                                                square_list[squares_5].append("black")
                                                if "rook" in old_square_6_values:
                                                    square_list[squares_5].append("rook")
                                                elif "queen" in old_square_6_values:
                                                    square_list[squares_5].append("queen")
                                                self.check_check_black(black_king.square, black_king.file, black_king.row)
                                                if not self.black_king_check:
                                                    del square_list[square_6][2:]
                                                    del square_list[squares_5][2:]
                                                    for values in old_square_6_values:
                                                        square_list[square_6].append(values)
                                                    for values in old_square_5_values:
                                                        square_list[squares_5].append(values)
                                                    if "rook" in square_list[square_6]:
                                                        if "Rx" + square_6[0] + squares_5 not in legal_moves_list:
                                                            legal_moves_list.append("Rx" + squares_5)
                                                    elif "queen" in square_list[square_6]:
                                                        if "Qx" + squares_5 not in legal_moves_list:
                                                            legal_moves_list.append("Qx" + squares_5)
                                                    self.black_king_check = True
                                                    black_king_check = True
                                                else:
                                                    del square_list[square_6][2:]
                                                    del square_list[squares_5][2:]
                                                    for values in old_square_6_values:
                                                        square_list[square_6].append(values)
                                                    for values in old_square_5_values:
                                                        square_list[squares_5].append(values)
                                                    self.black_king_check = True
                                                    black_king_check = True
                                            else:
                                                old_square_6_values = square_list[square_6][2:]
                                                del square_list[square_6][2:]
                                                square_list[squares_5].append("OCCUPIED")
                                                square_list[squares_5].append("black")
                                                if "rook" in old_square_6_values:
                                                    square_list[squares_5].append("rook")
                                                elif "queen" in old_square_6_values:
                                                    square_list[squares_5].append("queen")
                                                self.check_check_black(black_king.square, black_king.file, black_king.row)
                                                if not self.black_king_check:
                                                    del square_list[square_6][2:]
                                                    del square_list[squares_5][2:]
                                                    for values in old_square_6_values:
                                                        square_list[square_6].append(values)
                                                    if "rook" in square_list[square_6]:
                                                        if "R" + squares_5 not in legal_moves_list:
                                                            legal_moves_list.append("R"+ squares_5)
                                                    elif "queen" in square_list[square_6]:
                                                        if "Q" + squares_5 not in legal_moves_list:
                                                            legal_moves_list.append("Q" + squares_5)
                                                    self.black_king_check = True
                                                    black_king_check = True
                                                else:
                                                    del square_list[square_6][2:]
                                                    del square_list[squares_5][2:]
                                                    for values in old_square_6_values:
                                                        square_list[square_6].append(values)
                                                    self.black_king_check = True
                                                    black_king_check = True
                                elif abs(piece_index - square_index) == 1 \
                                        and "pawn" in square_list[square_6] \
                                        and "OCCUPIED" not in square_list[squares_5]:
                                    if piece_index > square_index:
                                        old_square_6_values = square_list[square_6][2:]
                                        del square_list[square_6][2:]
                                        square_list[squares_5].append("OCCUPIED")
                                        square_list[squares_5].append("black")
                                        square_list[squares_5].append("pawn")
                                        self.check_check_black(black_king.square, black_king.file, black_king.row)
                                        if not self.black_king_check:
                                            del square_list[square_6][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_6_values:
                                                square_list[square_6].append(values)
                                            if squares_5 not in legal_moves_list:
                                                legal_moves_list.append(squares_5)
                                            self.black_king_check = True
                                            black_king_check = True
                                        else:
                                            del square_list[square_6][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_6_values:
                                                square_list[square_6].append(values)
                                            self.black_king_check = True
                                            black_king_check = True
                                elif abs(piece_index - square_index) == 2 \
                                        and "pawn" in square_list[square_6] \
                                        and "MOVED" not in square_list[square_6]:
                                    if piece_index > square_index:
                                        if "OCCUPIED" not in square_list[full_board_index[piece_index+1]] \
                                                and "OCCUPIED" not in square_list[squares_5]:
                                            old_square_6_values = square_list[square_6][2:]
                                            del square_list[square_6][2:]
                                            square_list[squares_5].append("OCCUPIED")
                                            square_list[squares_5].append("black")
                                            square_list[squares_5].append("pawn")
                                            self.check_check_black(black_king.square, black_king.file, black_king.row)
                                            if not self.black_king_check:
                                                del square_list[square_6][2:]
                                                del square_list[squares_5][2:]
                                                for values in old_square_6_values:
                                                    square_list[square_6].append(values)
                                                if squares_5 not in legal_moves_list:
                                                    legal_moves_list.append(squares_5)
                                                self.black_king_check = True
                                                black_king_check = True
                                            else:
                                                del square_list[square_6][2:]
                                                del square_list[squares_5][2:]
                                                for values in old_square_6_values:
                                                    square_list[square_6].append(values)
                                                self.black_king_check = True
                                                black_king_check = True
                                elif abs(square_index - piece_index) == 1 \
                                        and "rook" in square_list[square_6] \
                                        or abs(square_index - piece_index) == 8 \
                                        and "rook" in square_list[square_6] \
                                        or abs(square_index - piece_index) == 1 \
                                        and "queen" in square_list[square_6] \
                                        or abs(square_index - piece_index) == 8 \
                                        and "queen" in square_list[square_6]:
                                    if "OCCUPIED" in square_list[squares_5]:
                                        old_square_6_values = square_list[square_6][2:]
                                        old_square_5_values = square_list[squares_5][2:]
                                        del square_list[square_6][2:]
                                        del square_list[squares_5][2:]
                                        square_list[squares_5].append("OCCUPIED")
                                        square_list[squares_5].append("black")
                                        if "rook" in old_square_6_values:
                                            square_list[squares_5].append("rook")
                                        elif "queen" in old_square_6_values:
                                            square_list[squares_5].append("queen")
                                        self.check_check_black(black_king.square, black_king.file, black_king.row)
                                        if not self.black_king_check:
                                            del square_list[square_6][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_6_values:
                                                square_list[square_6].append(values)
                                            for values in old_square_5_values:
                                                square_list[squares_5].append(values)
                                            if "rook" in square_list[square_6]:
                                                if "R" + square_6[0] + "x" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("R" + square_6[0] + "x" + squares_5)
                                            elif "queen" in square_list[square_6]:
                                                if "Qx" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("Qx" + squares_5)
                                            self.black_king_check = True
                                            black_king_check = True
                                        else:
                                            del square_list[square_6][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_6_values:
                                                square_list[square_6].append(values)
                                            for values in old_square_5_values:
                                                square_list[squares_5].append(values)
                                            self.black_king_check = True
                                            black_king_check = True
                                    else:
                                        old_square_6_values = square_list[square_6][2:]
                                        del square_list[square_6][2:]
                                        square_list[squares_5].append("OCCUPIED")
                                        square_list[squares_5].append("black")
                                        if "rook" in old_square_6_values:
                                            square_list[squares_5].append("rook")
                                        elif "queen" in old_square_6_values:
                                            square_list[squares_5].append("queen")
                                        self.check_check_black(black_king.square, black_king.file, black_king.row)
                                        if not self.black_king_check:
                                            del square_list[square_6][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_6_values:
                                                square_list[square_6].append(values)
                                            if "rook" in square_list[square_6]:
                                                if "R" + square_6[0] + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("R" + square_6[0] + squares_5)
                                            elif "queen" in square_list[square_6]:
                                                if "Q" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("Q" + squares_5)
                                            self.black_king_check = True
                                            black_king_check = True
                                        else:
                                            del square_list[square_6][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_6_values:
                                                square_list[square_6].append(values)
                                            self.black_king_check = True
                                            black_king_check = True


                        diagonal_check_list = list()
                        for i in [check_square for check_square in range(-8, 8)]:
                            try:
                                if piece_file_check - i > -1 \
                                        and piece_row_check + i > -1 \
                                        and file_letter[piece_file_check - i] != piece_letter:
                                    check_square = (file_letter[piece_file_check - i] + str(row_number[piece_row_check + i]))
                                    if check_square not in diagonal_check_list:
                                        diagonal_check_list.append(check_square)
                            except IndexError:
                                pass
                        # make list of diagonal line right down from king position
                        for i in [check_square for check_square in range(-8, 8)]:
                            try:
                                if piece_file_check + i > -1 \
                                        and piece_row_check + i > -1 \
                                        and file_letter[piece_file_check + i] != piece_letter:
                                    check_square = (file_letter[piece_file_check + i] + str(row_number[piece_row_check + i]))
                                    if check_square not in diagonal_check_list:
                                        diagonal_check_list.append(check_square)
                            except IndexError:
                                pass

                        between_diagonals_list_list = dict()
                        for square_7 in diagonal_check_list:
                            if "bishop" in square_list[square_7] \
                                    and "black" in square_list[square_7] \
                                    or "queen" in square_list[square_7] \
                                    and "black" in square_list[square_7] \
                                    or "pawn" in square_list[square_7] \
                                    and "black" in square_list[square_7]:
                                diagonal_piece_index = full_board_index.index(square_7)
                                if abs(square_index - diagonal_piece_index) > 7 \
                                        and abs(square_index - diagonal_piece_index) != 9 \
                                        and "bishop" in square_list[square_7] \
                                        or abs(square_index - diagonal_piece_index) > 7 \
                                        and abs(square_index - diagonal_piece_index) != 9 \
                                        and "queen" in square_list[square_7]:
                                    between_diagonal_squares = list()
                                    if square_index > diagonal_piece_index:
                                        if (square_index - diagonal_piece_index) % 7 == 0:
                                            for squares_7 in range(diagonal_piece_index + 7, square_index, 7):
                                                if full_board_index[squares_7] not in between_diagonal_squares:
                                                    between_diagonal_squares.append(full_board_index[squares_7])
                                        elif (square_index - diagonal_piece_index) % 9 == 0:
                                            for squares_7 in range(diagonal_piece_index + 9, square_index, 9):
                                                if full_board_index[squares_7] not in between_diagonal_squares:
                                                    between_diagonal_squares.append(full_board_index[squares_7])
                                    elif square_index < diagonal_piece_index:
                                        if abs((square_index - diagonal_piece_index) % 7) == 0:
                                            for squares_7 in range(square_index + 7, diagonal_piece_index, 7):
                                                if full_board_index[squares_7] not in between_diagonal_squares:
                                                    between_diagonal_squares.append(full_board_index[squares_7])
                                        elif abs(square_index - diagonal_piece_index) % 9 == 0:
                                            for squares_7 in range(square_index + 9, diagonal_piece_index, 9):
                                                if full_board_index[squares_7] not in between_diagonal_squares:
                                                    between_diagonal_squares.append(full_board_index[squares_7])
                                    between_diagonals_list_list.setdefault(squares_5, []).append(between_diagonal_squares)
                                    if len(between_diagonals_list_list[squares_5]) > 1:
                                        for i in range(0, len(between_diagonals_list_list[squares_5])):
                                            if not any({"OCCUPIED"}.issubset(set(square_list[square_7])) for square_7 in between_diagonals_list_list[squares_5][i]):
                                                if "OCCUPIED" in square_list[squares_5]:
                                                    old_square_7_values = square_list[square_7][2:]
                                                    old_square_5_values = square_list[squares_5][2:]
                                                    del square_list[square_7][2:]
                                                    del square_list[squares_5][2:]
                                                    square_list[squares_5].append("OCCUPIED")
                                                    square_list[squares_5].append("black")
                                                    if "bishop" in old_square_7_values:
                                                        square_list[squares_5].append("bishop")
                                                    elif "queen" in old_square_7_values:
                                                        square_list[squares_5].append("queen")
                                                    self.check_check_black(black_king.square, black_king.file, black_king.row)
                                                    if not self.black_king_check:
                                                        del square_list[square_7][2:]
                                                        del square_list[squares_5][2:]
                                                        for values in old_square_7_values:
                                                            square_list[square_7].append(values)
                                                        for values in old_square_5_values:
                                                            square_list[squares_5].append(values)
                                                        if "bishop" in square_list[square_7]:
                                                            if "Bx" + squares_5 not in legal_moves_list:
                                                                legal_moves_list.append("Bx" + squares_5)
                                                        elif "queen" in square_list[square_7]:
                                                            if "Qx" + squares_5 not in legal_moves_list:
                                                                legal_moves_list.append("Qx" + squares_5)
                                                        self.black_king_check = True
                                                        black_king_check = True
                                                    else:
                                                        del square_list[square_7][2:]
                                                        del square_list[squares_5][2:]
                                                        for values in old_square_7_values:
                                                            square_list[square_7].append(values)
                                                        for values in old_square_5_values:
                                                            square_list[squares_5].append(values)
                                                        self.black_king_check = True
                                                        black_king_check = True
                                                else:
                                                    old_square_7_values = square_list[square_7][2:]
                                                    del square_list[square_7][2:]
                                                    square_list[squares_5].append("OCCUPIED")
                                                    square_list[squares_5].append("black")
                                                    if "bishop" in old_square_7_values:
                                                        square_list[squares_5].append("bishop")
                                                    elif "queen" in old_square_7_values:
                                                        square_list[squares_5].append("queen")
                                                    self.check_check_black(black_king.square, black_king.file, black_king.row)
                                                    if not self.black_king_check:
                                                        del square_list[square_7][2:]
                                                        del square_list[squares_5][2:]
                                                        for values in old_square_7_values:
                                                            square_list[square_7].append(values)
                                                        if "bishop" in square_list[square_7]:
                                                            if "B" + squares_5 not in legal_moves_list:
                                                                legal_moves_list.append("B" + squares_5)
                                                        elif "queen" in square_list[square_7]:
                                                            if "Q" + squares_5 not in legal_moves_list:
                                                                legal_moves_list.append("Q" + squares_5)
                                                        self.black_king_check = True
                                                        black_king_check = True
                                                    else:
                                                        del square_list[square_7][2:]
                                                        del square_list[squares_5][2:]
                                                        for values in old_square_7_values:
                                                            square_list[square_7].append(values)
                                                        self.black_king_check = True
                                                        black_king_check = True
                                    if len(between_diagonals_list_list[squares_5]) < 2:
                                        if not any({"OCCUPIED"}.issubset(set(square_list[square_7])) for square_7 in between_diagonal_squares):
                                            if "OCCUPIED" in square_list[squares_5]:
                                                old_square_7_values = square_list[square_7][2:]
                                                old_square_5_values = square_list[squares_5][2:]
                                                del square_list[square_7][2:]
                                                del square_list[squares_5][2:]
                                                square_list[squares_5].append("OCCUPIED")
                                                square_list[squares_5].append("black")
                                                if "bishop" in old_square_7_values:
                                                    square_list[squares_5].append("bishop")
                                                elif "queen" in old_square_7_values:
                                                    square_list[squares_5].append("queen")
                                                self.check_check_black(black_king.square, black_king.file, black_king.row)
                                                if not self.black_king_check:
                                                    del square_list[square_7][2:]
                                                    del square_list[squares_5][2:]
                                                    for values in old_square_7_values:
                                                        square_list[square_7].append(values)
                                                    for values in old_square_5_values:
                                                        square_list[squares_5].append(values)
                                                    if "bishop" in square_list[square_7]:
                                                        if "Bx" + squares_5 not in legal_moves_list:
                                                            legal_moves_list.append("Bx" + squares_5)
                                                    elif "queen" in square_list[square_7]:
                                                        if "Qx" + squares_5 not in legal_moves_list:
                                                            legal_moves_list.append("Qx" + squares_5)
                                                    self.black_king_check = True
                                                    black_king_check = True
                                                else:
                                                    del square_list[square_7][2:]
                                                    del square_list[squares_5][2:]
                                                    for values in old_square_7_values:
                                                        square_list[square_7].append(values)
                                                    for values in old_square_5_values:
                                                        square_list[squares_5].append(values)
                                                    self.black_king_check = True
                                                    black_king_check = True
                                            else:
                                                old_square_7_values = square_list[square_7][2:]
                                                del square_list[square_7][2:]
                                                square_list[squares_5].append("OCCUPIED")
                                                square_list[squares_5].append("black")
                                                if "bishop" in old_square_7_values:
                                                    square_list[squares_5].append("bishop")
                                                elif "queen" in old_square_7_values:
                                                    square_list[squares_5].append("queen")
                                                self.check_check_black(black_king.square, black_king.file, black_king.row)
                                                if not self.black_king_check:
                                                    del square_list[square_7][2:]
                                                    del square_list[squares_5][2:]
                                                    for values in old_square_7_values:
                                                        square_list[square_7].append(values)
                                                    if "bishop" in square_list[square_7]:
                                                        if "B" + squares_5 not in legal_moves_list:
                                                            legal_moves_list.append("B" + squares_5)
                                                    elif "queen" in square_list[square_7]:
                                                        if "Q" + squares_5 not in legal_moves_list:
                                                            legal_moves_list.append("Q" + squares_5)
                                                    self.black_king_check = True
                                                    black_king_check = True
                                                else:
                                                    del square_list[square_7][2:]
                                                    del square_list[squares_5][2:]
                                                    for values in old_square_7_values:
                                                        square_list[square_7].append(values)
                                                    self.black_king_check = True
                                                    black_king_check = True
                                elif abs(square_index - diagonal_piece_index) == 7 \
                                        and "bishop" in square_list[square_7] \
                                        or abs(square_index - diagonal_piece_index) == 9 \
                                        and "bishop" in square_list[square_7] \
                                        or abs(square_index - diagonal_piece_index) == 7 \
                                        and "queen" in square_list[square_7] \
                                        or abs(square_index - diagonal_piece_index) == 9 \
                                        and "queen" in square_list[square_7]:
                                    if "OCCUPIED" in square_list[squares_5]:
                                        old_square_7_values = square_list[square_7][2:]
                                        old_square_5_values = square_list[squares_5][2:]
                                        del square_list[square_7][2:]
                                        del square_list[squares_5][2:]
                                        square_list[squares_5].append("OCCUPIED")
                                        square_list[squares_5].append("black")
                                        if "bishop" in old_square_7_values:
                                            square_list[squares_5].append("bishop")
                                        elif "queen" in old_square_7_values:
                                            square_list[squares_5].append("queen")
                                        self.check_check_black(black_king.square, black_king.file, black_king.row)
                                        if not self.black_king_check:
                                            del square_list[square_7][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_7_values:
                                                square_list[square_7].append(values)
                                            for values in old_square_5_values:
                                                square_list[squares_5].append(values)
                                            if "bishop" in square_list[square_7]:
                                                if "Bx" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("Bx" + squares_5)
                                            elif "queen" in square_list[square_7]:
                                                if "Qx" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("Qx" + squares_5)
                                            self.black_king_check = True
                                            black_king_check = True
                                        else:
                                            del square_list[square_7][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_7_values:
                                                square_list[square_7].append(values)
                                            for values in old_square_5_values:
                                                square_list[squares_5].append(values)
                                            self.black_king_check = True
                                            black_king_check = True
                                    else:
                                        old_square_7_values = square_list[square_7][2:]
                                        del square_list[square_7][2:]
                                        square_list[squares_5].append("OCCUPIED")
                                        square_list[squares_5].append("black")
                                        if "bishop" in old_square_7_values:
                                            square_list[squares_5].append("bishop")
                                        elif "queen" in old_square_7_values:
                                            square_list[squares_5].append("queen")
                                        self.check_check_black(black_king.square, black_king.file, black_king.row)
                                        if not self.black_king_check:
                                            del square_list[square_7][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_7_values:
                                                square_list[square_7].append(values)
                                            if "bishop" in square_list[square_7]:
                                                if "B" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("B" + squares_5)
                                            elif "queen" in square_list[square_7]:
                                                if "Q" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("Q" + squares_5)
                                            self.black_king_check = True
                                            black_king_check = True
                                        else:
                                            del square_list[square_7][2:]
                                            del square_list[squares_5][2:]
                                            for values in old_square_7_values:
                                                square_list[square_7].append(values)
                                            self.black_king_check = True
                                            black_king_check = True
                                elif (square_index - diagonal_piece_index)  == 7\
                                        and "pawn" in square_list[square_7] \
                                        and "OCCUPIED" in square_list[squares_5] \
                                        or (diagonal_piece_index - square_index) == 9 \
                                        and "pawn" in square_list[square_7] \
                                        and "OCCUPIED" in square_list[squares_5]:
                                    old_square_7_values = square_list[square_7][2:]
                                    old_square_5_values = square_list[squares_5][2:]
                                    del square_list[square_7][2:]
                                    del square_list[squares_5][2:]
                                    square_list[squares_5].append("OCCUPIED")
                                    square_list[squares_5].append("black")
                                    square_list[squares_5].append("pawn")
                                    self.check_check_black(black_king.square, black_king.file, black_king.row)
                                    if not self.black_king_check:
                                        del square_list[square_7][2:]
                                        del square_list[squares_5][2:]
                                        for values in old_square_7_values:
                                            square_list[square_7].append(values)
                                        for values in old_square_5_values:
                                            square_list[squares_5].append(values)
                                        if square_7[0] + "x" + squares_5 not in legal_moves_list:
                                            legal_moves_list.append(square_7[0] + "x" + squares_5)
                                        self.black_king_check = True
                                        black_king_check = True

                                    else:
                                        del square_list[square_7][2:]
                                        del square_list[squares_5][2:]
                                        for values in old_square_7_values:
                                            square_list[square_7].append(values)
                                        for values in old_square_5_values:
                                            square_list[squares_5].append(values)
                                        self.black_king_check = True
                                        black_king_check = True


                        knight_check_list = list()
                        if 8 > piece_file_check + 1 > -1 \
                                and 8 > piece_row_check + 2 > -1:
                            check_square_knight = (
                                        file_letter[piece_file_check + 1] + str(row_number[piece_row_check + 2]))
                            if check_square_knight not in knight_check_list:
                                knight_check_list.append(check_square_knight)
                        if 8 > piece_file_check - 1 > -1 \
                                and 8 > piece_row_check + 2 > -1:
                            check_square_knight = (
                                        file_letter[piece_file_check - 1] + str(row_number[piece_row_check + 2]))
                            if check_square_knight not in knight_check_list:
                                knight_check_list.append(check_square_knight)
                        if 8 > piece_file_check + 1 > -1 \
                                and 8 > piece_row_check - 2 > -1:
                            check_square_knight = (
                                        file_letter[piece_file_check + 1] + str(row_number[piece_row_check - 2]))
                            if check_square_knight not in knight_check_list:
                                knight_check_list.append(check_square_knight)
                        if 8 > piece_file_check - 1 > -1 \
                                and 8 > piece_row_check - 2 > -1:
                            check_square_knight = (
                                        file_letter[piece_file_check - 1] + str(row_number[piece_row_check - 2]))
                            if check_square_knight not in knight_check_list:
                                knight_check_list.append(check_square_knight)
                        if 8 > piece_file_check + 2 > -1 \
                                and 8 > piece_row_check - 1 > -1:
                            check_square_knight = (
                                        file_letter[piece_file_check + 2] + str(row_number[piece_row_check - 1]))
                            if check_square_knight not in knight_check_list:
                                knight_check_list.append(check_square_knight)
                        if 8 > piece_file_check - 2 > -1 \
                                and 8 > piece_row_check - 1 > -1:
                            check_square_knight = (
                                        file_letter[piece_file_check - 2] + str(row_number[piece_row_check - 1]))
                            if check_square_knight not in knight_check_list:
                                knight_check_list.append(check_square_knight)
                        if 8 > piece_file_check + 2 > -1 \
                                and 8 > piece_row_check + 1 > -1:
                            check_square_knight = (
                                        file_letter[piece_file_check + 2] + str(row_number[piece_row_check + 1]))
                            if check_square_knight not in knight_check_list:
                                knight_check_list.append(check_square_knight)
                        if 8 > piece_file_check - 2 > -1 \
                                and 8 > piece_row_check + 1 > -1:
                            check_square_knight = (
                                        file_letter[piece_file_check - 2] + str(row_number[piece_row_check + 1]))
                            if check_square_knight not in knight_check_list:
                                knight_check_list.append(check_square_knight)

                        for check_square_knight in knight_check_list:
                            if "knight" in square_list[check_square_knight] \
                                    and "black" in square_list[check_square_knight]:
                                knight_index = full_board_index.index(check_square_knight)
                                if abs(square_index - knight_index) == 17 \
                                        or abs(square_index - knight_index) == 15 \
                                        or abs(square_index - knight_index) == 10 \
                                        or abs(square_index - knight_index) == 6:
                                    if "OCCUPIED" in square_list[squares_5]:
                                        check_square_knight_values = square_list[check_square_knight][2:]
                                        old_square_5_values = square_list[squares_5][2:]
                                        del square_list[check_square_knight][2:]
                                        del square_list[squares_5][2:]
                                        square_list[squares_5].append("OCCUPIED")
                                        square_list[squares_5].append("black")
                                        square_list[squares_5].append("knight")
                                        self.check_check_black(black_king.square, black_king.file, black_king.row)
                                        if not self.black_king_check:
                                            del square_list[check_square_knight][2:]
                                            del square_list[squares_5][2:]
                                            for values in check_square_knight_values:
                                                square_list[check_square_knight].append(values)
                                            for values in old_square_5_values:
                                                square_list[squares_5].append(values)
                                            if black_knight.file == black_knight2.file:
                                                if "N" + check_square_knight[1] + "x" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("N" + check_square_knight[1] + "x" + squares_5)
                                            elif black_knight.row == black_knight2.row:
                                                if "N" + check_square_knight[0] + "x" + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("N" + check_square_knight[0] + "x" + squares_5)
                                            else:
                                                if "Nx" +  squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("Nx" + squares_5)
                                            self.black_king_check = True
                                            black_king_check = True
                                        else:
                                            del square_list[check_square_knight][2:]
                                            del square_list[squares_5][2:]
                                            for values in check_square_knight_values:
                                                square_list[check_square_knight].append(values)
                                            for values in old_square_5_values:
                                                square_list[squares_5].append(values)
                                            self.black_king_check = True
                                            black_king_check = True
                                    else:
                                        check_square_knight_values = square_list[check_square_knight][2:]
                                        del square_list[check_square_knight][2:]
                                        square_list[squares_5].append("OCCUPIED")
                                        square_list[squares_5].append("black")
                                        square_list[squares_5].append("knight")
                                        self.check_check_black(black_king.square, black_king.file, black_king.row)
                                        if not self.black_king_check:
                                            del square_list[check_square_knight][2:]
                                            del square_list[squares_5][2:]
                                            for values in check_square_knight_values:
                                                square_list[check_square_knight].append(values)
                                            if black_knight.file == black_knight2.file:
                                                if "N" + check_square_knight[1] + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("N" + check_square_knight[1] + squares_5)
                                            elif black_knight.row == black_knight2.row:
                                                if "N" + check_square_knight[0] + squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("N" + check_square_knight[0] + squares_5)
                                            else:
                                                if "N" +  squares_5 not in legal_moves_list:
                                                    legal_moves_list.append("N" + squares_5)
                                            self.black_king_check = True
                                            black_king_check = True
                                        else:
                                            del square_list[check_square_knight][2:]
                                            del square_list[squares_5][2:]
                                            for values in check_square_knight_values:
                                                square_list[check_square_knight].append(values)
                                            self.black_king_check = True
                                            black_king_check = True

        #print("LEGAL MOVES: " + str(legal_moves_list))
        if legal_moves_list == []:
            global black_checkmate
            black_checkmate = True

    def pawn_promotion(surface, event):

        global turn
        global pawn_promotion
        global pawn_x
        global pawn_y
        global prom_square

        if white_a_pawn.row == 8 and white_a_pawn in white_pieces_list:
            pawn_promotion = True
            pawn_x = white_a_pawn.x
            pawn_y = white_a_pawn.y
            prom_square = white_a_pawn.square
            white_pieces_list.remove(white_a_pawn)
        if white_b_pawn.row == 8 and white_b_pawn in white_pieces_list:
            pawn_promotion = True
            pawn_x = white_b_pawn.x
            pawn_y = white_b_pawn.y
            prom_square = white_b_pawn.square
            white_pieces_list.remove(white_b_pawn)
        if white_c_pawn.row == 8 and white_c_pawn in white_pieces_list:
            pawn_promotion = True
            pawn_x = white_c_pawn.x
            pawn_y = white_c_pawn.y
            prom_square = white_c_pawn.square
            white_pieces_list.remove(white_c_pawn)
        if white_d_pawn.row == 8 and white_d_pawn in white_pieces_list:
            pawn_promotion = True
            pawn_x = white_d_pawn.x
            pawn_y = white_d_pawn.y
            prom_square = white_d_pawn.square
            white_pieces_list.remove(white_d_pawn)
        if white_e_pawn.row == 8 and white_e_pawn in white_pieces_list:
            pawn_promotion = True
            pawn_x = white_e_pawn.x
            pawn_y = white_e_pawn.y
            prom_square = white_e_pawn.square
            white_pieces_list.remove(white_e_pawn)
        if white_f_pawn.row == 8 and white_f_pawn in white_pieces_list:
            pawn_promotion = True
            pawn_x = white_f_pawn.x
            pawn_y = white_f_pawn.y
            prom_square = white_f_pawn.square
            white_pieces_list.remove(white_f_pawn)
        if white_g_pawn.row == 8 and white_g_pawn in white_pieces_list:
            pawn_promotion = True
            pawn_x = white_g_pawn.x
            pawn_y = white_g_pawn.y
            prom_square = white_g_pawn.square
            white_pieces_list.remove(white_g_pawn)
        if white_h_pawn.row == 8 and white_h_pawn in white_pieces_list:
            pawn_promotion = True
            pawn_x = white_h_pawn.x
            pawn_y = white_h_pawn.y
            prom_square = white_h_pawn.square
            white_pieces_list.remove(white_h_pawn)

        if black_a_pawn.row == 1 and black_a_pawn in black_pieces_list:
            pawn_promotion = True
            pawn_x = black_a_pawn.x
            pawn_y = black_a_pawn.y
            prom_square = black_a_pawn.square
            black_pieces_list.remove(black_a_pawn)
        if black_b_pawn.row == 1 and black_b_pawn in black_pieces_list:
            pawn_promotion = True
            pawn_x = black_b_pawn.x
            pawn_y = black_b_pawn.y
            prom_square = black_b_pawn.square
            black_pieces_list.remove(black_b_pawn)
        if black_c_pawn.row == 1 and black_c_pawn in black_pieces_list:
            pawn_promotion = True
            pawn_x = black_c_pawn.x
            pawn_y = black_c_pawn.y
            prom_square = black_c_pawn.square
            black_pieces_list.remove(black_c_pawn)
        if black_d_pawn.row == 1 and black_d_pawn in black_pieces_list:
            pawn_promotion = True
            pawn_x = black_d_pawn.x
            pawn_y = black_d_pawn.y
            prom_square = black_d_pawn.square
            black_pieces_list.remove(black_d_pawn)
        if black_e_pawn.row == 1 and black_e_pawn in black_pieces_list:
            pawn_promotion = True
            pawn_x = black_e_pawn.x
            pawn_y = black_e_pawn.y
            prom_square = black_e_pawn.square
            black_pieces_list.remove(black_e_pawn)
        if black_e_pawn.row == 1 and black_e_pawn in black_pieces_list:
            pawn_promotion = True
            pawn_x = black_e_pawn.x
            pawn_y = black_e_pawn.y
            prom_square = black_e_pawn.square
            black_pieces_list.remove(black_e_pawn)
        if black_f_pawn.row == 1 and black_f_pawn in black_pieces_list:
            pawn_promotion = True
            pawn_x = black_f_pawn.x
            pawn_y = black_f_pawn.y
            prom_square = black_f_pawn.square
            black_pieces_list.remove(black_f_pawn)
        if black_g_pawn.row == 1 and black_g_pawn in black_pieces_list:
            pawn_promotion = True
            pawn_x = black_g_pawn.x
            pawn_y = black_g_pawn.y
            prom_square = black_g_pawn.square
            black_pieces_list.remove(black_g_pawn)
        if black_h_pawn.row == 1 and black_h_pawn in black_pieces_list:
            pawn_promotion = True
            pawn_x = black_h_pawn.x
            pawn_y = black_h_pawn.y
            prom_square = black_h_pawn.square
            black_pieces_list.remove(black_h_pawn)


        if pawn_promotion:
            global prom_row
            prom_row = prom_square[1]
            pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(pawn_x, pawn_y, 256, 80))
            if int(prom_row) == 8:
                queen_image = Image(pawn_x + 20, pawn_y + 3, 37, 74, "/white_queenpiece.png")
                rook_image = Image(pawn_x + 77, pawn_y + 3, 37, 74,  "/white_rookpiece.png")
                bishop_image = Image(pawn_x + 134, pawn_y + 3, 37, 74, "/white_bishoppiece.png")
                knight_image = Image(pawn_x + 191, pawn_y + 3, 45, 74,"/white_knightpiece2.png" )
                queen_image.draw_image(surface)
                rook_image.draw_image(surface)
                bishop_image.draw_image(surface)
                knight_image.draw_image(surface)
            elif int(prom_row) == 1:
                queen_image = Image(pawn_x + 20, pawn_y + 3, 37, 74, "/black_queenpiece.png")
                rook_image = Image(pawn_x + 77, pawn_y + 3, 37, 74,  "/black_rookpiece.png")
                bishop_image = Image(pawn_x + 134, pawn_y + 3, 37, 74, "/black_bishoppiece.png")
                knight_image = Image(pawn_x + 191, pawn_y + 3, 45, 74,"/black_knightpiece.png")
                queen_image.draw_image(surface)
                rook_image.draw_image(surface)
                bishop_image.draw_image(surface)
                knight_image.draw_image(surface)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if queen_image.rect.collidepoint(pos):
                    del square_list[prom_square][2:]
                    prom_file = prom_square[0]
                    prom_row = prom_square[1]
                    if int(prom_row) == 8:
                        white_prom_queen = Piece("queen", "white", "/white_queenpiece.png", prom_file, int(prom_row))
                        white_pieces_list.add(white_prom_queen)
                        white_prom_queen.check_check_black(black_king.square, black_king.file, black_king.row)
                        turn += 1
                        white_prom_queen.place_pieces_on_board(prom_square)
                        if black_king_check:
                            white_prom_queen.check_checkmate_black()
                    if int(prom_row) == 1:
                        black_prom_queen = Piece("queen", "black", "/black_queenpiece.png", prom_file, int(prom_row))
                        black_pieces_list.add(black_prom_queen)
                        black_prom_queen.check_check_white(white_king.square, white_king.file, white_king.row)
                        turn += 1
                        black_prom_queen.place_pieces_on_board(prom_square)
                        if black_king_check:
                            black_prom_queen.check_checkmate_white()
                    pawn_promotion = False
                if rook_image.rect.collidepoint(pos):
                    del square_list[prom_square][2:]
                    prom_file = prom_square[0]
                    prom_row = prom_square[1]
                    if int(prom_row) == 8:
                        white_prom_rook = Piece("queen", "white", "/white_rookpiece.png", prom_file, int(prom_row))
                        white_pieces_list.add(white_prom_rook)
                        white_prom_rook.check_check_black(black_king.square, black_king.file, black_king.row)
                        turn += 1
                        white_prom_rook.place_pieces_on_board(prom_square)
                        if black_king_check:
                            white_prom_rook.check_checkmate_black()
                    if int(prom_row) == 1:
                        black_prom_rook = Piece("queen", "black", "/black_rookpiece.png", prom_file, int(prom_row))
                        black_pieces_list.add(black_prom_rook)
                        black_prom_rook.check_check_white(white_king.square, white_king.file, white_king.row)
                        turn += 1
                        black_prom_rook.place_pieces_on_board(prom_square)
                        if black_king_check:
                            black_prom_rook.check_checkmate_white()
                    pawn_promotion = False
                if bishop_image.rect.collidepoint(pos):
                    del square_list[prom_square][2:]
                    prom_file = prom_square[0]
                    prom_row = prom_square[1]
                    if int(prom_row) == 8:
                        white_prom_bishop = Piece("queen", "white", "/white_bishoppiece.png", prom_file, int(prom_row))
                        white_pieces_list.add(white_prom_bishop)
                        white_prom_bishop.check_check_black(black_king.square, black_king.file, black_king.row)
                        turn += 1
                        white_prom_bishop.place_pieces_on_board(prom_square)
                        if black_king_check:
                            white_prom_bishop.check_checkmate_black()
                    if int(prom_row) == 1:
                        black_prom_bishop = Piece("queen", "black", "/black_bishoppiece.png", prom_file, int(prom_row))
                        black_pieces_list.add(black_prom_bishop)
                        black_prom_bishop.check_check_white(white_king.square, white_king.file, white_king.row)
                        turn += 1
                        black_prom_bishop.place_pieces_on_board(prom_square)
                        if black_king_check:
                            black_prom_bishop.check_checkmate_white()
                    pawn_promotion = False
                if knight_image.rect.collidepoint(pos):
                    del square_list[prom_square][2:]
                    prom_file = prom_square[0]
                    prom_row = prom_square[1]
                    if int(prom_row) == 8:
                        white_prom_knight = Piece("queen", "white", "/white_knightpiece2.png", prom_file, int(prom_row))
                        white_pieces_list.add(white_prom_knight)
                        white_prom_knight.check_check_black(black_king.square, black_king.file, black_king.row)
                        turn += 1
                        white_prom_knight.place_pieces_on_board(prom_square)
                        if black_king_check:
                            white_prom_knight.check_checkmate_black()
                    if int(prom_row) == 1:
                        black_prom_knight = Piece("queen", "black", "/black_knightpiece.png", prom_file, int(prom_row))
                        black_pieces_list.add(black_prom_knight)
                        black_prom_knight.check_check_white(white_king.square, white_king.file, white_king.row)
                        turn += 1
                        black_prom_knight.place_pieces_on_board(prom_square)
                        if black_king_check:
                            black_prom_knight.check_checkmate_white()
                    pawn_promotion = False

    def threefold_repetition(self):
        """check if same position occurs three times on the board, if so, it's a draw by repetition"""
        global color_turn
        global castle
        global caslte_king
        global en_passant_rights
        full_board_index = list()
        charlistje = "abcdefgh"
        for charje in charlistje:
            for cifje in range(1, 9):
                square_bet = charje + str(cifje)
                full_board_index.append(square_bet)

        filelist = "abcdefgh"
        file_letter = []
        row_number = []
        for file in filelist:
            file_letter.append(file)
        for row in range(1, 9):
            row_number.append(row)

        if turn % 2 == 0:
            color_turn =  " white "
            if "OCCUPIED" not in square_list['b1'] \
                    and "OCCUPIED" not in square_list['c1'] \
                    and "OCCUPIED" not in square_list['d1'] \
                    and "MOVED" not in square_list[white_king.square] \
                    and "MOVED" not in square_list['a1'] \
                    and "white" in square_list['a1'] \
                    and "rook" in square_list['a1']:
                        castle = " has_queen_castle_rights "
            else:
                castle = " has_no_queen_castle_rights "
            if "OCCUPIED" not in square_list['f1'] \
                    and "OCCUPIED" not in square_list['g1'] \
                    and "MOVED" not in square_list[white_king.square] \
                    and "MOVED" not in square_list['h1'] \
                    and "white" in square_list['h1'] \
                    and "rook" in square_list['h1']:
                        castle_king = " has_king_castle_rights "
            else:
                castle_king = " has_no_king_castle_rights "
            for i in range(4 , 61, 8):
                if "pawn" in square_list[full_board_index[i]] \
                        and "white" in square_list[full_board_index[i]] \
                        and "OCCUPIED" not in square_list[full_board_index[i + 9]] \
                        and "OCCUPIED" in square_list[full_board_index[i + 8]] \
                        and "black" in square_list[full_board_index[i + 8]] \
                        and "pawn" in square_list[full_board_index[i + 8]] \
                        and last_row == 5 \
                        and before_row == 7 \
                        and last_piece == "pawn" \
                        and last_file == file_letter[file_letter.index(full_board_index[i][0]) + 1]:
                    en_passant_rights = " has en passant rights "
                    break
                else:
                    en_passant_rights = " has no en passant rights "
                if "pawn" in square_list[full_board_index[i]] \
                        and "white" in square_list[full_board_index[i]] \
                        and "OCCUPIED" not in square_list[full_board_index[i - 7]] \
                        and "OCCUPIED" in square_list[full_board_index[i - 8]] \
                        and "black" in square_list[full_board_index[i - 8]] \
                        and "pawn" in square_list[full_board_index[i - 8]] \
                        and last_row == 5 \
                        and before_row == 7 \
                        and last_piece == "pawn" \
                        and last_file == file_letter[file_letter.index(full_board_index[i][0]) - 1]:
                    en_passant_rights = " has en passant rights "
                    break
                else:
                    en_passant_rights = " has no en passant rights "
            square_list_list.append(color_turn + castle + castle_king + en_passant_rights+ str(square_list))
        elif turn % 2 == 1:
            color_turn = " black "
            if "OCCUPIED" not in square_list['b8'] \
                    and "OCCUPIED" not in square_list['c8'] \
                    and "OCCUPIED" not in square_list['d8'] \
                    and "MOVED" not in square_list[black_king.square] \
                    and "MOVED" not in square_list['a8'] \
                    and "black" in square_list['a8'] \
                    and "rook" in square_list['a8']:
                        castle = " has_queen_castle_rights "
            else:
                castle = " has_no_queen_castle_rights "
            if "OCCUPIED" not in square_list['f8'] \
                    and "OCCUPIED" not in square_list['g8'] \
                    and "MOVED" not in square_list[black_king.square] \
                    and "MOVED" not in square_list['h8'] \
                    and "black" in square_list['h8'] \
                    and "rook" in square_list['h8']:
                        castle_king = " has_king_castle_rights "
            else:
                castle_king = " has_no_king_castle_rights "
            for i in range(3, 60, 8):
                if "pawn" in square_list[full_board_index[i]] \
                        and "black" in square_list[full_board_index[i]] \
                        and "OCCUPIED" not in square_list[full_board_index[i + 7]] \
                        and "OCCUPIED" in square_list[full_board_index[i + 8]] \
                        and "white" in square_list[full_board_index[i+ 8]] \
                        and "pawn" in square_list[full_board_index[i + 8]] \
                        and last_row == 4 \
                        and before_row == 2 \
                        and last_piece == "pawn" \
                        and last_file == file_letter[file_letter.index(full_board_index[i][0]) + 1]:
                    en_passant_rights = " has en passant rights "
                    break
                else:
                    en_passant_rights = " has no en passant rights "
                if "pawn" in square_list[full_board_index[i]] \
                        and "black" in square_list[full_board_index[i]] \
                        and "OCCUPIED" not in square_list[full_board_index[i - 9]] \
                        and "OCCUPIED" in square_list[full_board_index[i - 8]] \
                        and "white" in square_list[full_board_index[i - 8]] \
                        and "pawn" in square_list[full_board_index[i - 8]] \
                        and last_row == 4 \
                        and before_row == 2 \
                        and last_piece == "pawn" \
                        and last_file == file_letter[file_letter.index(full_board_index[i][0]) - 1]:
                    en_passant_rights = " has en passant rights "
                    break
                else:
                    en_passant_rights = " has no en passant rights "
            square_list_list.append(color_turn + castle + castle_king + en_passant_rights + str(square_list))

        k = 0
        for item in square_list_list:
            k += 1
        for sq_list in square_list_list[:-1]:
            if square_list_list[-1] in sq_list:
                if sq_list in rep_pos_list:
                    rep_pos_list[sq_list] += 1
                    if rep_pos_list[sq_list] == 3:
                        global draw
                        draw = True
                    break
                if sq_list not in rep_pos_list:
                    rep_pos_list[sq_list] = 2
                    break

    def stale_mate_white(self):
        """ check if king can't move but is also not in check. And if other pieces can't move. In other words, if the
        player in his turn has no legal moves but is not in check or checkmate it's a draw """
        stale_mate_legal_moves = list()
        king_moves_list = list()
        full_board_index = list()

        charlistje = "abcdefgh"
        for charje in charlistje:
            for cifje in range(1, 9):
                square_bet = charje + str(cifje)
                full_board_index.append(square_bet)

        filelist = "abcdefgh"
        file_letter = []
        row_number = []
        for file in filelist:
            file_letter.append(file)
        for row in range(1, 9):
            row_number.append(row)
            
        if self.piece_name == "king" \
                and self.piece_color == "white":
            try:
                white_king_square = (self.new_file + str(self.new_row))
                white_king_file = self.new_file
                white_king_row = self.new_row
                king_file_index = file_letter.index(white_king_file)
                king_row_number = row_number.index(white_king_row)
            except AttributeError:
                white_king_square = white_king.file + str(white_king.row)
                white_king_file = white_king.file
                white_king_row = white_king.row
                king_file_index = file_letter.index(white_king_file)
                king_row_number = row_number.index(white_king_row)
        else:
            white_king_square = white_king.file + str(white_king.row)
            white_king_file = white_king.file
            white_king_row = white_king.row
            king_file_index = file_letter.index(white_king_file)
            king_row_number = row_number.index(white_king_row)
        old_king_values = square_list[white_king_square][2:]
        del square_list[white_king_square][2:]

        if 8 > king_file_index + 1 > -1 \
                and 8 > king_row_number + 1 > -1:
            king_square = file_letter[king_file_index + 1] + str(row_number[king_row_number + 1])
            king_moves_list.append(king_square)
        if 8 > king_file_index + 1 > 0 \
                and 8 > king_row_number - 1 > -1:
            king_square = file_letter[king_file_index + 1] + str(row_number[king_row_number - 1])
            king_moves_list.append(king_square)
        if 8 > king_file_index - 1 > -1 \
                and 8 > king_row_number + 1 > -1:
            king_square = file_letter[king_file_index - 1] + str(row_number[king_row_number + 1])
            king_moves_list.append(king_square)
        if 8 > king_file_index - 1 > -1 \
                and 8 > king_row_number - 1 > -1:
            king_square = file_letter[king_file_index - 1] + str(row_number[king_row_number - 1])
            king_moves_list.append(king_square)
        if 8 > king_file_index + 1 > -1:
            king_square = file_letter[king_file_index + 1] + str(row_number[king_row_number])
            king_moves_list.append(king_square)
        if 8 > king_file_index - 1 > -1:
            king_square = file_letter[king_file_index - 1] + str(row_number[king_row_number])
            king_moves_list.append(king_square)
        if 8 > king_row_number + 1 > -1:
            king_square = file_letter[king_file_index] + str(row_number[king_row_number + 1])
            king_moves_list.append(king_square)
        if 8 > king_row_number - 1 > -1:
            king_square = file_letter[king_file_index] + str(row_number[king_row_number - 1])
            king_moves_list.append(king_square)

        for occupied_square in [square for square in king_moves_list if "OCCUPIED" and "white" in square_list[square]]:
            king_moves_list.remove(occupied_square)

        for square in king_moves_list:
            check_list = list()
            square_letter = square[0]
            square_cijfer = int(square[1])
            king_file_check = file_letter.index(square_letter)
            king_row_check = row_number.index(square_cijfer)
            straight_check_list = []
            for i in [check_square_straight for check_square_straight in range(0, 8) if
                      check_square_straight != king_file_check]:
                try:
                    check_square_straight = (file_letter[i] + str(square_cijfer))
                    if check_square_straight not in straight_check_list:
                        straight_check_list.append(check_square_straight)
                except IndexError:
                    pass
            # add vertical lines
            for i in [check_square_straight for check_square_straight in range(0, 8) if
                      check_square_straight != king_row_check]:
                try:
                    check_square_straight = (square_letter + str(row_number[i]))
                    if check_square_straight not in straight_check_list:
                        straight_check_list.append(check_square_straight)
                except IndexError:
                    pass

            king_index = full_board_index.index(square)
            check_piece_index_list = dict()

            for check_square_straight in [squares for squares in straight_check_list if "black" in square_list[squares]
                                                                                        and "rook" in square_list[
                                                                                            squares]
                                                                                        or "queen" in square_list[
                                                                                            squares]
                                                                                        and "black" in square_list[
                                                                                            squares]
                                                                                        or "king" in square_list[
                                                                                            squares]
                                                                                        and "black" in square_list[
                                                                                            squares]]:

                check_piece_index = full_board_index.index(check_square_straight)
                if abs(king_index - check_piece_index) > 1 \
                        and abs(king_index - check_piece_index) != 8 \
                        and "rook" in square_list[check_square_straight] \
                        or abs(king_index - check_piece_index) > 1 \
                        and abs(king_index - check_piece_index) != 8 \
                        and "queen" in square_list[check_square_straight]:
                    between_rook_queen_squares = list()
                    if king_index > check_piece_index:
                        if 0 < (king_index - check_piece_index) < 8:
                            for squares2 in range(check_piece_index + 1, king_index, 1):
                                if full_board_index[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(full_board_index[squares2])
                        elif (king_index - check_piece_index) % 8 == 0:
                            for squares2 in range(check_piece_index + 8, king_index, 8):
                                if full_board_index[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(full_board_index[squares2])
                    elif king_index < check_piece_index:
                        if 0 < abs(king_index - check_piece_index) < 8:
                            for squares2 in range(king_index + 1, check_piece_index, 1):
                                if full_board_index[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(full_board_index[squares2])
                        elif abs(king_index - check_piece_index) % 8 == 0:
                            for squares2 in range(king_index + 8, check_piece_index, 8):
                                if full_board_index[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(full_board_index[squares2])
                    check_piece_index_list.setdefault(square, []).append(between_rook_queen_squares)
                    for i in range(0, len(check_piece_index_list[square])):
                        if any({"OCCUPIED", "white"}.issubset(set(square_list[square])) for square in
                               check_piece_index_list[square][i]):
                            check_list.append("FALSE")
                        elif any({"OCCUPIED", "black", "pawn"}.issubset(set(square_list[square])) for square in
                                 check_piece_index_list[square][i]) \
                                or any({"OCCUPIED", "black", "king"}.issubset(set(square_list[square])) for square in
                                       check_piece_index_list[square][i]) \
                                or any({"OCCUPIED", "black", "bishop"}.issubset(set(square_list[square])) for square in
                                       check_piece_index_list[square][i]) \
                                or any({"OCCUPIED", "black", "knight"}.issubset(set(square_list[square])) for square in
                                       check_piece_index_list[square][i]):
                            check_list.append("FALSE")
                        elif not any({"OCCUPIED"}.issubset(set(square_list[square])) for square in
                                     check_piece_index_list[square][i]):
                            check_list.append("TRUE")
                elif abs(king_index - check_piece_index) == 1 \
                        and "rook" in square_list[check_square_straight] \
                        or abs(king_index - check_piece_index) == 8 \
                        and "rook" in square_list[check_square_straight] \
                        or abs(king_index - check_piece_index) == 1 \
                        and "queen" in square_list[check_square_straight] \
                        or abs(king_index - check_piece_index) == 8 \
                        and "queen" in square_list[check_square_straight] \
                        or abs(king_index - check_piece_index) == 1 \
                        and "king" in square_list[check_square_straight] \
                        or abs(king_index - check_piece_index) == 8 \
                        and "king" in square_list[check_square_straight]:
                    check_list.append("TRUE")
            if not any({"black", "rook"}.issubset(set(square_list[square])) for square in straight_check_list) \
                    and not any(
                {"black", "queen"}.issubset(set(square_list[square])) for square in straight_check_list):
                check_list.append("FALSE")

            diagonal_check_list = []
            for i in [check_square for check_square in range(-8, 8)]:
                try:
                    if king_file_check - i > -1 \
                            and king_row_check + i > -1 \
                            and file_letter[king_file_check - i] != square_letter:
                        check_square = (file_letter[king_file_check - i] + str(row_number[king_row_check + i]))
                        if check_square not in diagonal_check_list:
                            diagonal_check_list.append(check_square)
                except IndexError:
                    pass
            # make list of diagonal line right down from king position
            for i in [check_square for check_square in range(-8, 8)]:
                try:
                    if king_file_check + i > -1 \
                            and king_row_check + i > -1 \
                            and file_letter[king_file_check + i] != square_letter:
                        check_square = (file_letter[king_file_check + i] + str(row_number[king_row_check + i]))
                        if check_square not in diagonal_check_list:
                            diagonal_check_list.append(check_square)
                except IndexError:
                    pass

            between_squares_list_list = dict()
            for check_square in diagonal_check_list:
                if "bishop" in square_list[check_square] \
                        and "black" in square_list[check_square] \
                        or "queen" in square_list[check_square] \
                        and "black" in square_list[check_square] \
                        or "pawn" in square_list[check_square] \
                        and "black" in square_list[check_square] \
                        or "king" in square_list[check_square] \
                        and "black" in square_list[check_square]:
                    bishop_queen_index = full_board_index.index(check_square)
                    if abs(king_index - bishop_queen_index) > 7 \
                            and abs(king_index - bishop_queen_index) != 9 \
                            and "bishop" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) > 7 \
                            and abs(king_index - bishop_queen_index) != 9 \
                            and "queen" in square_list[check_square]:
                        between_bishop_squares = list()
                        if king_index > bishop_queen_index:
                            if (king_index - bishop_queen_index) % 7 == 0:
                                for squares in range(bishop_queen_index + 7, king_index, 7):
                                    if full_board_index[squares] not in between_bishop_squares:
                                        between_bishop_squares.append(full_board_index[squares])
                            elif (king_index - bishop_queen_index) % 9 == 0:
                                for squares in range(bishop_queen_index + 9, king_index, 9):
                                    if full_board_index[squares] not in between_bishop_squares:
                                        between_bishop_squares.append(full_board_index[squares])
                        elif king_index < bishop_queen_index:
                            if abs((king_index - bishop_queen_index) % 7) == 0:
                                for squares in range(king_index + 7, bishop_queen_index, 7):
                                    if full_board_index[squares] not in between_bishop_squares:
                                        between_bishop_squares.append(full_board_index[squares])
                            elif abs(king_index - bishop_queen_index) % 9 == 0:
                                for squares in range(king_index + 9, bishop_queen_index, 9):
                                    if full_board_index[squares] not in between_bishop_squares:
                                        between_bishop_squares.append(full_board_index[squares])
                        between_squares_list_list.setdefault(square, []).append(between_bishop_squares)
                        for i in range(0, len(between_squares_list_list[square])):
                            if any({"OCCUPIED", "white"}.issubset(set(square_list[square])) for square in
                                   between_squares_list_list[square][i]):
                                check_list.append("FALSE")
                            elif any({"OCCUPIED", "black", "pawn"}.issubset(set(square_list[square])) for square in
                                     between_squares_list_list[square][i]) \
                                    or any(
                                {"OCCUPIED", "black", "king"}.issubset(set(square_list[square])) for square in
                                between_squares_list_list[square][i]) \
                                    or any(
                                {"OCCUPIED", "black", "rook"}.issubset(set(square_list[square])) for square in
                                between_squares_list_list[square][i]) \
                                    or any(
                                {"OCCUPIED", "black", "knight"}.issubset(set(square_list[square])) for square in
                                between_squares_list_list[square][i]):
                                check_list.append("FALSE")
                            elif not any({"OCCUPIED"}.issubset(set(square_list[square])) for square in
                                         between_squares_list_list[square][i]):
                                check_list.append("TRUE")
                    elif abs(king_index - bishop_queen_index) == 7 \
                            and "pawn" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 9 \
                            and "pawn" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 7 \
                            and "bishop" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 9 \
                            and "bishop" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 7 \
                            and "queen" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 9 \
                            and "queen" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 7 \
                            and "king" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) == 9 \
                            and "king" in square_list[check_square]:
                        check_list.append("TRUE")
            if not any({"black", "bishop"}.issubset(set(square_list[square])) for square in diagonal_check_list) \
                    and not any(
                {"black", "queen"}.issubset(set(square_list[square])) for square in diagonal_check_list):
                check_list.append("FALSE")

            knight_check_list = list()
            if 8 > king_file_check + 1 > -1 \
                    and 8 > king_row_check + 2 > -1:
                check_square_knight = (file_letter[king_file_check + 1] + str(row_number[king_row_check + 2]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check - 1 > -1 \
                    and 8 > king_row_check + 2 > -1:
                check_square_knight = (file_letter[king_file_check - 1] + str(row_number[king_row_check + 2]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check + 1 > -1 \
                    and 8 > king_row_check - 2 > -1:
                check_square_knight = (file_letter[king_file_check + 1] + str(row_number[king_row_check - 2]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check - 1 > -1 \
                    and 8 > king_row_check - 2 > -1:
                check_square_knight = (file_letter[king_file_check - 1] + str(row_number[king_row_check - 2]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check + 2 > -1 \
                    and 8 > king_row_check - 1 > -1:
                check_square_knight = (file_letter[king_file_check + 2] + str(row_number[king_row_check - 1]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check - 2 > -1 \
                    and 8 > king_row_check - 1 > -1:
                check_square_knight = (file_letter[king_file_check - 2] + str(row_number[king_row_check - 1]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check + 2 > -1 \
                    and 8 > king_row_check + 1 > -1:
                check_square_knight = (file_letter[king_file_check + 2] + str(row_number[king_row_check + 1]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check - 2 > -1 \
                    and 8 > king_row_check + 1 > -1:
                check_square_knight = (file_letter[king_file_check - 2] + str(row_number[king_row_check + 1]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)

            for check_square_knight in knight_check_list:
                if "knight" in square_list[check_square_knight] \
                        and "black" in square_list[check_square_knight]:
                    knight_index = full_board_index.index(check_square_knight)
                    if abs(king_index - knight_index) == 17 \
                            or abs(king_index - knight_index) == 15 \
                            or abs(king_index - knight_index) == 10 \
                            or abs(king_index - knight_index) == 6:
                        check_list.append("TRUE")
            if not any({"black", "knight"}.issubset(set(square_list[square3])) for square3 in knight_check_list):
                check_list.append("FALSE")


            if "TRUE" in check_list:
                if "K" + square in stale_mate_legal_moves:
                    stale_mate_legal_moves.remove("K" + square)
            if "TRUE" not in check_list:
                if "K" + square not in stale_mate_legal_moves:
                    stale_mate_legal_moves.append("K" + square)
        # print("WHITE KING MOVES LIST: "+ str(stale_mate_legal_moves))
        for value in old_king_values:
            square_list[white_king_square].append(value)
            
        if "OCCUPIED" not in square_list['b1'] \
                and "OCCUPIED" not in square_list['c1'] \
                and "OCCUPIED" not in square_list['d1'] \
                and "MOVED" not in square_list[white_king_square] \
                and "MOVED" not in square_list['a1'] \
                and "white" in square_list['a1'] \
                and "rook" in square_list['a1']:
            self.check_check_white(white_king_square, 'd', 1)
            if not self.white_king_check:
                self.check_check_white(white_king_square, 'c', 1)
                if not self.white_king_check:
                    stale_mate_legal_moves.append("0-0-0")

        if "OCCUPIED" not in square_list['f1'] \
                and "OCCUPIED" not in square_list['g1'] \
                and "MOVED" not in square_list[white_king_square] \
                and "MOVED" not in square_list['h1'] \
                and "white" in square_list['h1'] \
                and "rook" in square_list['h1']:
            self.check_check_white(white_king_square, 'f', 1)
            if not self.white_king_check:
                self.check_check_white(white_king_square, 'g', 1)
                if not self.white_king_check:
                    stale_mate_legal_moves.append("0-0")
            
        for squares in full_board_index:
            if "OCCUPIED" in square_list[squares] \
                    and "white" in square_list[squares]:
                if "pawn" in square_list[squares]:
                    if "MOVED" not in square_list[squares]:
                        # check if the white pawn is able to move forwards, first for if the pawn has not moved yet
                        row_plus_one = row_number.index(int(squares[1])) + 2
                        pawn_moves = list()
                        pawn_moves.append(squares[0]+ str(row_plus_one))
                        for move in pawn_moves:
                            if "OCCUPIED" not in square_list[move]:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append(move)
                        row_plus_two = row_number.index(int(squares[1])) + 3
                        pawn_moves.append(squares[0] + str(row_plus_two))
                        print("PAWN MOVES IN STALE MATE WHITE: "+str(pawn_moves))
                        for move in pawn_moves:
                            if "OCCUPIED" not in square_list[pawn_moves[0]] \
                                    and "OCCUPIED" not in square_list[pawn_moves[1]]:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    if pawn_moves[1] not in stale_mate_legal_moves:
                                        stale_mate_legal_moves.append(pawn_moves[1])
                    if "MOVED" in square_list[squares]:
                        row_plus_one = row_number.index(int(squares[1])) + 2
                        pawn_moves = list()
                        pawn_moves.append(squares[0] + str(row_plus_one))
                        for move in pawn_moves:
                            if "OCCUPIED" not in square_list[move]:
                                if move not in stale_mate_legal_moves:
                                    self.virtual_move(move, squares, "white")
                                    if self.legal_move:
                                        stale_mate_legal_moves.append(move)
                        # THESE NEXT TWO BLOCKS HANDLE EN PASSANT ON EITHER SIDE OF THE PAWN
                        if int(squares[1]) == 5 \
                                and "OCCUPIED" not in square_list[full_board_index[full_board_index.index(squares) + 9]] \
                                and "OCCUPIED" in square_list[full_board_index[full_board_index.index(squares) + 8]] \
                                and "black" in square_list[full_board_index[full_board_index.index(squares) + 8]] \
                                and "pawn" in square_list[full_board_index[full_board_index.index(squares) + 8]] \
                                and last_row == 5 \
                                and before_row == 7 \
                                and last_piece == "pawn" \
                                and last_file == file_letter[file_letter.index(squares[0]) + 1]:
                            if (full_board_index.index(squares) + 9) < 63:
                                old_ep_square = last_file + str(last_row)
                                old_ep_values = square_list[old_ep_square][2:]
                                old_self_values = square_list[squares][2:] 
                                new_self_square =  full_board_index[full_board_index.index(squares) + 9]
                                del square_list[old_ep_square][2:]
                                del square_list[squares][2:]
                                for value in old_self_values:
                                    square_list[new_self_square].append(value)
                                self.check_check_white(white_king.square, white_king.file, white_king.row)
                                if not self.white_king_check:
                                    stale_mate_legal_moves.append(squares[0]+ "x" + new_self_square + " e.p")
                                del square_list[new_self_square][2:]
                                for value in old_self_values:
                                    square_list[squares].append(value)
                                for value in old_ep_values:
                                    square_list[old_ep_square].append(value)
                        if int(squares[1]) == 5 \
                                and "OCCUPIED" not in square_list[full_board_index[full_board_index.index(squares) - 7]] \
                                and "OCCUPIED" in square_list[full_board_index[full_board_index.index(squares) - 8]] \
                                and "black" in square_list[full_board_index[full_board_index.index(squares) - 8]] \
                                and "pawn" in square_list[full_board_index[full_board_index.index(squares) - 8]] \
                                and last_row == 5 \
                                and before_row == 7 \
                                and last_piece == "pawn" \
                                and last_file == file_letter[file_letter.index(squares[0]) - 1]:
                            if (full_board_index.index(squares) - 7) > 0:
                                old_ep_square = last_file + str(last_row)
                                old_ep_values = square_list[old_ep_square][2:]
                                old_self_values = square_list[squares][2:]
                                new_self_square =  full_board_index[full_board_index.index(squares) - 7]
                                del square_list[old_ep_square][2:]
                                del square_list[squares][2:]
                                for value in old_self_values:
                                    square_list[new_self_square].append(value)
                                self.check_check_white(white_king.square, white_king.file, white_king.row)
                                if not self.white_king_check:
                                    stale_mate_legal_moves.append(squares[0]+ "x" + new_self_square + " e.p")
                                del square_list[new_self_square][2:]
                                for value in old_self_values:
                                    square_list[squares].append(value)
                                for value in old_ep_values:
                                    square_list[old_ep_square].append(value)
                    # check if pawn can take a piece or pawn
                    take_squares = list()
                    if -1 < (full_board_index.index(squares) + 9) < 63:
                        take_square_1 = full_board_index[full_board_index.index(squares) + 9]
                        take_squares.append(take_square_1)
                    if -1 < (full_board_index.index(squares)  -7) < 63:
                        take_square_2 = full_board_index[full_board_index.index(squares) - 7]
                        take_squares.append(take_square_2)
                    for take_square in take_squares:
                        if "OCCUPIED" in square_list[take_square] \
                                and "black" in square_list[take_square]:
                            self.virtual_move(take_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append(squares[0]+"x"+ take_square)
                if "bishop" in square_list[squares]:
                    bishop_file = squares[0]
                    bishop_row = int(squares[1])
                    bishop_sm_list = list()
                    for i in range(1,9):
                        if -1 < (file_letter.index(bishop_file) - i) < 8 \
                                and -1 < (row_number.index(bishop_row) - i) < 8:
                            new_bishop_file = file_letter[file_letter.index(bishop_file) - i]
                            new_bishop_row = row_number[row_number.index(bishop_row) - i]
                            new_bishop_square = new_bishop_file + str(new_bishop_row)
                            bishop_sm_list.append(new_bishop_square)
                    for move in bishop_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "B" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("B"+ move)
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            if "Bx" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Bx" + move)
                            break
                    bishop_sm_list = list()
                    for i in range(1,9):
                        if -1 < (file_letter.index(bishop_file) + i) < 8 \
                                and -1 < (row_number.index(bishop_row) + i) < 8:
                            new_bishop_file = file_letter[file_letter.index(bishop_file) + i]
                            new_bishop_row = row_number[row_number.index(bishop_row) + i]
                            new_bishop_square = new_bishop_file + str(new_bishop_row)
                            bishop_sm_list.append(new_bishop_square)
                    for move in bishop_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "B" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("B"+ move)
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            if "Bx" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Bx" + move)
                            break
                    bishop_sm_list = list()
                    for i in range(1,9):
                        if -1 < (file_letter.index(bishop_file) + i) < 8 \
                                and -1 < (row_number.index(bishop_row) - i) < 8:
                            new_bishop_file = file_letter[file_letter.index(bishop_file) + i]
                            new_bishop_row = row_number[row_number.index(bishop_row) - i]
                            new_bishop_square = new_bishop_file + str(new_bishop_row)
                            bishop_sm_list.append(new_bishop_square)
                    for move in bishop_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "B" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("B"+ move)
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            if "Bx" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Bx" + move)
                            break
                    bishop_sm_list = list()
                    for i in range(1,9):
                        if -1 < (file_letter.index(bishop_file) - i) < 8 \
                                and -1 < (row_number.index(bishop_row) + i) < 8:
                            new_bishop_file = file_letter[file_letter.index(bishop_file) - i]
                            new_bishop_row = row_number[row_number.index(bishop_row) + i]
                            new_bishop_square = new_bishop_file + str(new_bishop_row)
                            bishop_sm_list.append(new_bishop_square)
                    for move in bishop_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "B" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("B"+ move)
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            if "Bx" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Bx" + move)
                            break
                # CHECKS FOR WHITE ROOK IN ALL SQUARES AND DETERMINE IF IT CAN MOVE
                if "rook" in square_list[squares]:
                    rook_file = squares[0]
                    rook_row = int(squares[1])
                    rook_sm_list = list()
                    for i in range(1,9):
                        if -1 < (file_letter.index(rook_file) + i) < 8:
                            new_rook_file = file_letter[file_letter.index(rook_file) + i]
                            new_rook_square = new_rook_file + str(rook_row)
                            rook_sm_list.append(new_rook_square)
                    for move in rook_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "R" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("R"+move)
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            if "Rx" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Rx"+move)
                            break
                    rook_sm_list = list()
                    for i in range(1,9):
                        if -1 < (file_letter.index(rook_file) - i) < 8:
                            new_rook_file = file_letter[file_letter.index(rook_file) - i]
                            new_rook_square = new_rook_file + str(rook_row)
                            rook_sm_list.append(new_rook_square)
                    for move in rook_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "R" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("R" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            if "Rx" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Rx" + move)
                            break
                    rook_sm_list = list()
                    for i in range(1,9):
                        if -1 < (row_number.index(rook_row) - i) < 8:
                            new_rook_row = row_number[row_number.index(rook_row) - i]
                            new_rook_square = rook_file + str(new_rook_row)
                            rook_sm_list.append(new_rook_square)
                    for move in rook_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "R" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("R" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            if "Rx" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Rx" + move)
                            break
                    for i in range(1,9):
                        if -1 < (row_number.index(rook_row) + i) < 8:
                            new_rook_row = row_number[row_number.index(rook_row) + i]
                            new_rook_square = rook_file + str(new_rook_row)
                            rook_sm_list.append(new_rook_square)
                    for move in rook_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "R" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("R" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            if "Rx" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Rx" + move)
                            break
                if "queen" in square_list[squares]:
                    queen_file = squares[0]
                    queen_row = int(squares[1])
                    queen_sm_list = list()
                    for i in range(1,9):
                        if -1 < (file_letter.index(queen_file) - i) < 8 \
                                and -1 < (row_number.index(queen_row) - i) < 8:
                            new_queen_file = file_letter[file_letter.index(queen_file) - i]
                            new_queen_row = row_number[row_number.index(queen_row) - i]
                            new_queen_square = new_queen_file + str(new_queen_row)
                            queen_sm_list.append(new_queen_square)
                    for move in queen_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "Q" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Q"+ move)
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            if "Qx" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Qx" + move)
                            break
                    queen_sm_list = list()
                    for i in range(1,9):
                        if -1 < (file_letter.index(queen_file) + i) < 8 \
                                and -1 < (row_number.index(queen_row) - i) < 8:
                            new_queen_file = file_letter[file_letter.index(queen_file) + i]
                            new_queen_row = row_number[row_number.index(queen_row) - i]
                            new_queen_square = new_queen_file + str(new_queen_row)
                            queen_sm_list.append(new_queen_square)
                    for move in queen_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "Q" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Q"+ move)
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            if "Qx" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Qx" + move)
                            break
                    queen_sm_list = list()
                    for i in range(1,9):
                        if -1 < (file_letter.index(queen_file) - i) < 8 \
                                and -1 < (row_number.index(queen_row) + i) < 8:
                            new_queen_file = file_letter[file_letter.index(queen_file) - i]
                            new_queen_row = row_number[row_number.index(queen_row) + i]
                            new_queen_square = new_queen_file + str(new_queen_row)
                            queen_sm_list.append(new_queen_square)
                    for move in queen_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "Q" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Q"+ move)
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            if "Qx" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Qx" + move)
                            break
                    queen_sm_list = list()
                    for i in range(1,9):
                        if -1 < (file_letter.index(queen_file) + i) < 8 \
                                and -1 < (row_number.index(queen_row) + i) < 8:
                            new_queen_file = file_letter[file_letter.index(queen_file) + i]
                            new_queen_row = row_number[row_number.index(queen_row) + i]
                            new_queen_square = new_queen_file + str(new_queen_row)
                            queen_sm_list.append(new_queen_square)
                    for move in queen_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "Q" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Q"+ move)
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            if "Qx" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Qx" + move)
                            break
                    # QUEEN MOVES FOR THE HORIZONTALS
                    queen_sm_list = list()
                    for i in range(1,9):
                        if -1 < (file_letter.index(queen_file) + i) < 8:
                            new_queen_file = file_letter[file_letter.index(queen_file) + i]
                            new_queen_square = new_queen_file + str(queen_row)
                            queen_sm_list.append(new_queen_square)
                    for move in queen_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "Q" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Q"+ move)
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            if "Qx" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Qx" + move)
                            break
                    queen_sm_list = list()
                    for i in range(1,9):
                        if -1 < (file_letter.index(queen_file) - i) < 8:
                            new_queen_file = file_letter[file_letter.index(queen_file) - i]
                            new_queen_square = new_queen_file + str(queen_row)
                            queen_sm_list.append(new_queen_square)
                    for move in queen_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "Q" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Q"+ move)
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            if "Qx" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Qx" + move)
                            break
                    # QUEEN MOVES FOR THE VERTICALS
                    queen_sm_list = list()
                    for i in range(1,9):
                        if -1 < (row_number.index(queen_row) - i) < 8:
                            new_queen_row = row_number[row_number.index(queen_row) - i]
                            new_queen_square = queen_file + str(new_queen_row)
                            queen_sm_list.append(new_queen_square)
                    for move in queen_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "Q" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Q"+ move)
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            if "Qx" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Qx" + move)
                            break
                    queen_sm_list = list()
                    for i in range(1,9):
                        if -1 < (row_number.index(queen_row) + i) < 8:
                            new_queen_row = row_number[row_number.index(queen_row) + i]
                            new_queen_square = queen_file + str(new_queen_row)
                            queen_sm_list.append(new_queen_square)
                    for move in queen_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "Q" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Q"+ move)
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            if "Qx" + move not in stale_mate_legal_moves:
                                self.virtual_move(move, squares, "white")
                                if self.legal_move:
                                    stale_mate_legal_moves.append("Qx" + move)
                            break
                if "knight" in square_list[squares]:
                    knight_index = full_board_index.index(squares)
                    knight_file = squares[0]
                    knight_row = int(squares[1])
                    knight_file_index = file_letter.index(knight_file)
                    knight_row_index = row_number.index(knight_row)

                    if 8 > knight_file_index +  1 > -1 \
                            and 8 > knight_row_index + 2 > -1:
                        new_knight_file =  file_letter[file_letter.index(knight_file) + 1]
                        new_knight_row =  row_number[row_number.index(knight_row) + 2]
                        new_knight_square = new_knight_file + str(new_knight_row)
                        if "OCCUPIED" in square_list[new_knight_square] \
                                and "white" in square_list[new_knight_square]:
                            pass
                        elif "OCCUPIED" in square_list[new_knight_square] \
                                and "black" in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append("Nx"+ new_knight_square)
                        elif "OCCUPIED" not in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append("N" +  new_knight_square)
                    if 8 > knight_file_index -  1 > -1 \
                            and 8 > knight_row_index + 2 > -1:
                        new_knight_file =  file_letter[file_letter.index(knight_file) - 1]
                        new_knight_row =  row_number[row_number.index(knight_row) + 2]
                        new_knight_square = new_knight_file + str(new_knight_row)
                        if "OCCUPIED" in square_list[new_knight_square] \
                                and "white" in square_list[new_knight_square]:
                            pass
                        elif "OCCUPIED" in square_list[new_knight_square] \
                                and "black" in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append("Nx"+ new_knight_square)
                        elif "OCCUPIED" not in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append("N" +  new_knight_square)
                    if 8 > knight_file_index +  1 > -1 \
                            and 8 > knight_row_index - 2 > -1:
                        new_knight_file =  file_letter[file_letter.index(knight_file) + 1]
                        new_knight_row =  row_number[row_number.index(knight_row) - 2]
                        new_knight_square = new_knight_file + str(new_knight_row)
                        if "OCCUPIED" in square_list[new_knight_square] \
                                and "white" in square_list[new_knight_square]:
                            pass
                        elif "OCCUPIED" in square_list[new_knight_square] \
                                and "black" in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append("Nx"+ new_knight_square)
                        elif "OCCUPIED" not in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append("N" +  new_knight_square)
                    if 8 > knight_file_index -  1 > -1 \
                            and 8 > knight_row_index - 2 > -1:
                        new_knight_file =  file_letter[file_letter.index(knight_file) - 1]
                        new_knight_row =  row_number[row_number.index(knight_row) - 2]
                        new_knight_square = new_knight_file + str(new_knight_row)
                        if "OCCUPIED" in square_list[new_knight_square] \
                                and "white" in square_list[new_knight_square]:
                            pass
                        elif "OCCUPIED" in square_list[new_knight_square] \
                                and "black" in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append("Nx"+ new_knight_square)
                        elif "OCCUPIED" not in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append("N" +  new_knight_square)
                    if 8 > knight_file_index +  2 > -1 \
                            and 8 > knight_row_index - 1 > -1:
                        new_knight_file =  file_letter[file_letter.index(knight_file) + 2]
                        new_knight_row =  row_number[row_number.index(knight_row) - 1]
                        new_knight_square = new_knight_file + str(new_knight_row)
                        if "OCCUPIED" in square_list[new_knight_square] \
                                and "white" in square_list[new_knight_square]:
                            pass
                        elif "OCCUPIED" in square_list[new_knight_square] \
                                and "black" in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append("Nx"+ new_knight_square)
                        elif "OCCUPIED" not in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append("N" +  new_knight_square)
                    if 8 > knight_file_index - 2 > -1 \
                            and 8 > knight_row_index - 1 > -1:
                        new_knight_file =  file_letter[file_letter.index(knight_file) - 2]
                        new_knight_row =  row_number[row_number.index(knight_row) - 1]
                        new_knight_square = new_knight_file + str(new_knight_row)
                        if "OCCUPIED" in square_list[new_knight_square] \
                                and "white" in square_list[new_knight_square]:
                            pass
                        elif "OCCUPIED" in square_list[new_knight_square] \
                                and "black" in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append("Nx"+ new_knight_square)
                        elif "OCCUPIED" not in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append("N" +  new_knight_square)
                    if 8 > knight_file_index + 2 > -1 \
                            and 8 > knight_row_index + 1 > -1:
                        new_knight_file =  file_letter[file_letter.index(knight_file) + 2]
                        new_knight_row =  row_number[row_number.index(knight_row) + 1]
                        new_knight_square = new_knight_file + str(new_knight_row)
                        if "OCCUPIED" in square_list[new_knight_square] \
                                and "white" in square_list[new_knight_square]:
                            pass
                        elif "OCCUPIED" in square_list[new_knight_square] \
                                and "black" in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append("Nx"+ new_knight_square)
                        elif "OCCUPIED" not in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append("N" +  new_knight_square)
                    if 8 > knight_file_index - 2 > -1 \
                            and 8 > knight_row_index + 1 > -1:
                        new_knight_file =  file_letter[file_letter.index(knight_file) - 2]
                        new_knight_row =  row_number[row_number.index(knight_row) + 1]
                        new_knight_square = new_knight_file + str(new_knight_row)
                        if "OCCUPIED" in square_list[new_knight_square] \
                                and "white" in square_list[new_knight_square]:
                            pass
                        elif "OCCUPIED" in square_list[new_knight_square] \
                                and "black" in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append("Nx"+ new_knight_square)
                        elif "OCCUPIED" not in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "white")
                            if self.legal_move:
                                stale_mate_legal_moves.append("N" +  new_knight_square)


        print("Stale_mate_moves: "+ str(stale_mate_legal_moves))
        if stale_mate_legal_moves == []:
            print("STALEMATE")
            global stale_mate
            stale_mate = True
            
    def stale_mate_black(self):
        """ check if king can't move but is also not in check. And if other pieces can't move. In other words, if the
               player in his turn has no legal moves but is not in check or checkmate it's a draw """
        stale_mate_legal_moves_black = list()
        king_moves_list = list()
        full_board_index = list()

        charlistje = "abcdefgh"
        for charje in charlistje:
            for cifje in range(1, 9):
                square_bet = charje + str(cifje)
                full_board_index.append(square_bet)

        filelist = "abcdefgh"
        file_letter = []
        row_number = []
        for file in filelist:
            file_letter.append(file)
        for row in range(1, 9):
            row_number.append(row)

        if self.piece_name == "king" \
                and self.piece_color == "black":
            try:
                black_king_square = (self.new_file + str(self.new_row))
                black_king_file = self.new_file
                black_king_row = self.new_row
                king_file_index = file_letter.index(black_king_file)
                king_row_number = row_number.index(black_king_row)
            except AttributeError:
                black_king_square = black_king.file + str(black_king.row)
                black_king_file = black_king.file
                black_king_row = black_king.row
                king_file_index = file_letter.index(black_king_file)
                king_row_number = row_number.index(black_king_row)
        else:
            black_king_square = black_king.file + str(black_king.row)
            black_king_file = black_king.file
            black_king_row = black_king.row
            king_file_index = file_letter.index(black_king_file)
            king_row_number = row_number.index(black_king_row)
        
        old_bk_values = square_list[black_king_square][2:]
        del square_list[black_king_square][2:]

        if 8 > king_file_index + 1 > -1 \
                and 8 > king_row_number + 1 > -1:
            king_square = file_letter[king_file_index + 1] + str(row_number[king_row_number + 1])
            king_moves_list.append(king_square)
        if 8 > king_file_index + 1 > 0 \
                and 8 > king_row_number - 1 > -1:
            king_square = file_letter[king_file_index + 1] + str(row_number[king_row_number - 1])
            king_moves_list.append(king_square)
        if 8 > king_file_index - 1 > -1 \
                and 8 > king_row_number + 1 > -1:
            king_square = file_letter[king_file_index - 1] + str(row_number[king_row_number + 1])
            king_moves_list.append(king_square)
        if 8 > king_file_index - 1 > -1 \
                and 8 > king_row_number - 1 > -1:
            king_square = file_letter[king_file_index - 1] + str(row_number[king_row_number - 1])
            king_moves_list.append(king_square)
        if 8 > king_file_index + 1 > -1:
            king_square = file_letter[king_file_index + 1] + str(row_number[king_row_number])
            king_moves_list.append(king_square)
        if 8 > king_file_index - 1 > -1:
            king_square = file_letter[king_file_index - 1] + str(row_number[king_row_number])
            king_moves_list.append(king_square)
        if 8 > king_row_number + 1 > -1:
            king_square = file_letter[king_file_index] + str(row_number[king_row_number + 1])
            king_moves_list.append(king_square)
        if 8 > king_row_number - 1 > -1:
            king_square = file_letter[king_file_index] + str(row_number[king_row_number - 1])
            king_moves_list.append(king_square)
            
        for occupied_square in [square for square in king_moves_list if "OCCUPIED" and "black" in square_list[square]]:
            king_moves_list.remove(occupied_square)
        
        for square in king_moves_list:
            check_list = list()
            square_letter = square[0]
            square_cijfer = int(square[1])
            king_file_check = file_letter.index(square_letter)
            king_row_check = row_number.index(square_cijfer)
            straight_check_list = []
            for i in [check_square_straight for check_square_straight in range(0, 8) if
                      check_square_straight != king_file_check]:
                try:
                    check_square_straight = (file_letter[i] + str(square_cijfer))
                    if check_square_straight not in straight_check_list:
                        straight_check_list.append(check_square_straight)
                except IndexError:
                    pass
            # add vertical lines
            for i in [check_square_straight for check_square_straight in range(0, 8) if
                      check_square_straight != king_row_check]:
                try:
                    check_square_straight = (square_letter + str(row_number[i]))
                    if check_square_straight not in straight_check_list:
                        straight_check_list.append(check_square_straight)
                except IndexError:
                    pass

            king_index = full_board_index.index(square)
            check_piece_index_list = dict()

            for check_square_straight in [squares for squares in straight_check_list if "white" in square_list[squares]
                                                                                        and "rook" in square_list[
                                                                                            squares]
                                                                                        or "queen" in square_list[
                                                                                            squares]
                                                                                        and "white" in square_list[
                                                                                            squares]
                                                                                        or "king" in square_list[
                                                                                            squares]
                                                                                        and "white" in square_list[
                                                                                            squares]]:
                check_piece_index = full_board_index.index(check_square_straight)
                if abs(king_index - check_piece_index) > 1 \
                        and abs(king_index - check_piece_index) != 8 \
                        and "rook" in square_list[check_square_straight] \
                        or abs(king_index - check_piece_index) > 1 \
                        and abs(king_index - check_piece_index) != 8 \
                        and "queen" in square_list[check_square_straight]:
                    between_rook_queen_squares = list()
                    if king_index > check_piece_index:
                        if 0 < (king_index - check_piece_index) < 8:
                            for squares2 in range(check_piece_index + 1, king_index, 1):
                                if full_board_index[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(full_board_index[squares2])
                        elif (king_index - check_piece_index) % 8 == 0:
                            for squares2 in range(check_piece_index + 8, king_index, 8):
                                if full_board_index[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(full_board_index[squares2])
                    elif king_index < check_piece_index:
                        if 0 < abs(king_index - check_piece_index) < 8:
                            for squares2 in range(king_index + 1, check_piece_index, 1):
                                if full_board_index[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(full_board_index[squares2])
                        elif abs(king_index - check_piece_index) % 8 == 0:
                            for squares2 in range(king_index + 8, check_piece_index, 8):
                                if full_board_index[squares2] not in between_rook_queen_squares:
                                    between_rook_queen_squares.append(full_board_index[squares2])
                    check_piece_index_list.setdefault(square, []).append(between_rook_queen_squares)
                    for i in range(0, len(check_piece_index_list[square])):
                        if any({"OCCUPIED", "black"}.issubset(set(square_list[square])) for square in
                               check_piece_index_list[square][i]):
                            check_list.append("FALSE")
                        elif any({"OCCUPIED", "white", "pawn"}.issubset(set(square_list[square])) for square in
                                 check_piece_index_list[square][i]) \
                                or any({"OCCUPIED", "white", "king"}.issubset(set(square_list[square])) for square in
                                       check_piece_index_list[square][i]) \
                                or any({"OCCUPIED", "white", "bishop"}.issubset(set(square_list[square])) for square in
                                       check_piece_index_list[square][i]) \
                                or any({"OCCUPIED", "white", "knight"}.issubset(set(square_list[square])) for square in
                                       check_piece_index_list[square][i]):
                            check_list.append("FALSE")
                        elif not any({"OCCUPIED"}.issubset(set(square_list[square])) for square in
                                     check_piece_index_list[square][i]):
                            check_list.append("TRUE")
                elif abs(king_index - check_piece_index) == 1 \
                         and "rook" in square_list[check_square_straight] \
                         or abs(king_index - check_piece_index) == 8 \
                         and "rook" in square_list[check_square_straight] \
                         or abs(king_index - check_piece_index) == 1 \
                         and "queen" in square_list[check_square_straight] \
                         or abs(king_index - check_piece_index) == 8 \
                         and "queen" in square_list[check_square_straight] \
                         or abs(king_index - check_piece_index) == 1 \
                         and "king" in square_list[check_square_straight] \
                         or abs(king_index - check_piece_index) == 8 \
                         and "king" in square_list[check_square_straight]:
                    check_list.append("TRUE")
            if not any({"white", "rook"}.issubset(set(square_list[square])) for square in straight_check_list) \
                    and not any(
                {"white", "queen"}.issubset(set(square_list[square])) for square in straight_check_list):
                check_list.append("FALSE")
                
            diagonal_check_list = []
            for i in [check_square for check_square in range(-8, 8)]:
                try:
                    if king_file_check - i > -1 \
                            and king_row_check + i > -1 \
                            and file_letter[king_file_check - i] != square_letter:
                        check_square = (file_letter[king_file_check - i] + str(row_number[king_row_check + i]))
                        if check_square not in diagonal_check_list:
                            diagonal_check_list.append(check_square)
                except IndexError:
                    pass
            # make list of diagonal line right down from king position
            for i in [check_square for check_square in range(-8, 8)]:
                try:
                    if king_file_check + i > -1 \
                            and king_row_check + i > -1 \
                            and file_letter[king_file_check + i] != square_letter:
                        check_square = (file_letter[king_file_check + i] + str(row_number[king_row_check + i]))
                        if check_square not in diagonal_check_list:
                            diagonal_check_list.append(check_square)
                except IndexError:
                    pass
                
            between_squares_list_list = dict()
            for check_square in diagonal_check_list:
                if "bishop" in square_list[check_square] \
                        and "white" in square_list[check_square] \
                        or "queen" in square_list[check_square] \
                        and "white" in square_list[check_square] \
                        or "pawn" in square_list[check_square] \
                        and "white" in square_list[check_square] \
                        or "king" in square_list[check_square] \
                        and "white" in square_list[check_square]:
                    bishop_queen_index = full_board_index.index(check_square)
                    if abs(king_index - bishop_queen_index) > 7 \
                            and abs(king_index - bishop_queen_index) != 9 \
                            and "bishop" in square_list[check_square] \
                            or abs(king_index - bishop_queen_index) > 7 \
                            and abs(king_index - bishop_queen_index) != 9 \
                            and "queen" in square_list[check_square]:
                        between_bishop_squares = list()
                        if king_index > bishop_queen_index:
                            if (king_index - bishop_queen_index) % 7 == 0:
                                for squares in range(bishop_queen_index + 7, king_index, 7):
                                    if full_board_index[squares] not in between_bishop_squares:
                                        between_bishop_squares.append(full_board_index[squares])
                            elif (king_index - bishop_queen_index) % 9 == 0:
                                for squares in range(bishop_queen_index + 9, king_index, 9):
                                    if full_board_index[squares] not in between_bishop_squares:
                                        between_bishop_squares.append(full_board_index[squares])
                        elif king_index < bishop_queen_index:
                            if abs((king_index - bishop_queen_index) % 7) == 0:
                                for squares in range(king_index + 7, bishop_queen_index, 7):
                                    if full_board_index[squares] not in between_bishop_squares:
                                        between_bishop_squares.append(full_board_index[squares])
                            elif abs(king_index - bishop_queen_index) % 9 == 0:
                                for squares in range(king_index + 9, bishop_queen_index, 9):
                                    if full_board_index[squares] not in between_bishop_squares:
                                        between_bishop_squares.append(full_board_index[squares])
                        between_squares_list_list.setdefault(square, []).append(between_bishop_squares)
                        for i in range(0, len(between_squares_list_list[square])):
                            if any({"OCCUPIED", "black"}.issubset(set(square_list[square])) for square in
                                   between_squares_list_list[square][i]):
                                check_list.append("FALSE")
                            elif any({"OCCUPIED", "white", "pawn"}.issubset(set(square_list[square])) for square in
                                     between_squares_list_list[square][i]) \
                                    or any(
                                {"OCCUPIED", "white", "king"}.issubset(set(square_list[square])) for square in
                                between_squares_list_list[square][i]) \
                                    or any(
                                {"OCCUPIED", "white", "rook"}.issubset(set(square_list[square])) for square in
                                between_squares_list_list[square][i]) \
                                    or any(
                                {"OCCUPIED", "white", "knight"}.issubset(set(square_list[square])) for square in
                                between_squares_list_list[square][i]):
                                check_list.append("FALSE")
                            elif not any({"OCCUPIED"}.issubset(set(square_list[square])) for square in
                                         between_squares_list_list[square][i]):
                                check_list.append("TRUE")
                    elif abs(king_index - bishop_queen_index) == 7 \
                             and "pawn" in square_list[check_square] \
                             or abs(king_index - bishop_queen_index) == 9 \
                             and "pawn" in square_list[check_square] \
                             or abs(king_index - bishop_queen_index) == 7 \
                             and "bishop" in square_list[check_square] \
                             or abs(king_index - bishop_queen_index) == 9 \
                             and "bishop" in square_list[check_square] \
                             or abs(king_index - bishop_queen_index) == 7 \
                             and "queen" in square_list[check_square] \
                             or abs(king_index - bishop_queen_index) == 9 \
                             and "queen" in square_list[check_square] \
                             or abs(king_index - bishop_queen_index) == 7 \
                             and "king" in square_list[check_square] \
                             or abs(king_index - bishop_queen_index) == 9 \
                             and "king" in square_list[check_square]:
                        check_list.append("TRUE")
            if not any({"white", "bishop"}.issubset(set(square_list[square])) for square in diagonal_check_list) \
                    and not any(
                {"white", "queen"}.issubset(set(square_list[square])) for square in diagonal_check_list):
                check_list.append("FALSE")
                

            knight_check_list = list()
            if 8 > king_file_check + 1 > -1 \
                    and 8 > king_row_check + 2 > -1:
                check_square_knight = (file_letter[king_file_check + 1] + str(row_number[king_row_check + 2]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check - 1 > -1 \
                    and 8 > king_row_check + 2 > -1:
                check_square_knight = (file_letter[king_file_check - 1] + str(row_number[king_row_check + 2]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check + 1 > -1 \
                    and 8 > king_row_check - 2 > -1:
                check_square_knight = (file_letter[king_file_check + 1] + str(row_number[king_row_check - 2]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check - 1 > -1 \
                    and 8 > king_row_check - 2 > -1:
                check_square_knight = (file_letter[king_file_check - 1] + str(row_number[king_row_check - 2]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check + 2 > -1 \
                    and 8 > king_row_check - 1 > -1:
                check_square_knight = (file_letter[king_file_check + 2] + str(row_number[king_row_check - 1]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check - 2 > -1 \
                    and 8 > king_row_check - 1 > -1:
                check_square_knight = (file_letter[king_file_check - 2] + str(row_number[king_row_check - 1]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check + 2 > -1 \
                    and 8 > king_row_check + 1 > -1:
                check_square_knight = (file_letter[king_file_check + 2] + str(row_number[king_row_check + 1]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)
            if 8 > king_file_check - 2 > -1 \
                    and 8 > king_row_check + 1 > -1:
                check_square_knight = (file_letter[king_file_check - 2] + str(row_number[king_row_check + 1]))
                if check_square_knight not in knight_check_list:
                    knight_check_list.append(check_square_knight)

            for check_square_knight in knight_check_list:
                if "knight" in square_list[check_square_knight] \
                        and "white" in square_list[check_square_knight]:
                    knight_index = full_board_index.index(check_square_knight)
                    if abs(king_index - knight_index) == 17 \
                            or abs(king_index - knight_index) == 15 \
                            or abs(king_index - knight_index) == 10 \
                            or abs(king_index - knight_index) == 6:
                        check_list.append("TRUE")
            if not any({"white", "knight"}.issubset(set(square_list[square3])) for square3 in knight_check_list):
                check_list.append("FALSE")


            if "TRUE" in check_list:
                if "K" + square in stale_mate_legal_moves_black:
                    stale_mate_legal_moves_black.remove("K" +  square)
            if "TRUE" not in check_list:
                if "K" +  square not in stale_mate_legal_moves_black:
                    stale_mate_legal_moves_black.append("K" + square)

        for value in old_bk_values:
            square_list[black_king_square].append(value)

        if "OCCUPIED" not in square_list['b8'] \
                and "OCCUPIED" not in square_list['c8'] \
                and "OCCUPIED" not in square_list['d8'] \
                and "MOVED" not in square_list[black_king_square] \
                and "MOVED" not in square_list['a8'] \
                and "black" in square_list['a8'] \
                and "rook" in square_list['a8']:
            self.check_check_black(black_king_square, 'd', 8)
            if not self.black_king_check:
                self.check_check_black(black_king_square, 'c', 8)
                if not self.black_king_check:
                    stale_mate_legal_moves_black.append("0-0-0")

        if "OCCUPIED" not in square_list['f8'] \
                and "OCCUPIED" not in square_list['g8'] \
                and "MOVED" not in square_list[black_king_square] \
                and "MOVED" not in square_list['h8'] \
                and "black" in square_list['h8'] \
                and "rook" in square_list['h8']:
            self.check_check_black(black_king_square, 'f', 8)
            if not self.black_king_check:
                self.check_check_black(black_king_square, 'g', 8)
                if not self.black_king_check:
                    stale_mate_legal_moves_black.append("0-0")

            
        for squares in full_board_index:
            if "OCCUPIED" in square_list[squares] \
                    and "black" in square_list[squares]:
                if "pawn" in square_list[squares]:
                    if "MOVED" not in square_list[squares]:
                        # check if the white pawn is able to move forwards, first for if the pawn has not moved yet
                        pawn_moves = list()
                        row_plus_one = row_number.index(int(squares[1]))
                        pawn_moves.append(squares[0] + str(row_plus_one))
                        for move in pawn_moves:
                            if "OCCUPIED" not in square_list[move]:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append(move)
                        row_plus_two = row_number.index(int(squares[1])) - 1
                        pawn_moves.append(squares[0]+ str(row_plus_two))
                        for move in pawn_moves:
                            if "OCCUPIED" not in square_list[pawn_moves[0]] \
                                    and "OCCUPIED" not in square_list[pawn_moves[1]]:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    if pawn_moves[1] not in stale_mate_legal_moves_black:
                                        stale_mate_legal_moves_black.append(pawn_moves[1])

                    if "MOVED" in square_list[squares]:
                        row_plus_one = row_number.index(int(squares[1]))
                        pawn_moves = list()
                        pawn_moves.append(squares[0] + str(row_plus_one))
                        for move in pawn_moves:
                            if "OCCUPIED" not in square_list[move]:
                                if move not in stale_mate_legal_moves_black:
                                    self.virtual_move(move, squares, "black")
                                    if self.legal_move:
                                            stale_mate_legal_moves_black.append(move)
                        # THESE NEXT TWO BLOCKS HANDLE EN PASSANT ON EITHER SIDE OF THE PAWN
                        if int(squares[1]) == 4 \
                                and "OCCUPIED" not in square_list[full_board_index[full_board_index.index(squares) + 7]] \
                                and "OCCUPIED" in square_list[full_board_index[full_board_index.index(squares) + 8]] \
                                and "white" in square_list[full_board_index[full_board_index.index(squares) + 8]] \
                                and "pawn" in square_list[full_board_index[full_board_index.index(squares) + 8]] \
                                and last_row == 4 \
                                and before_row == 2 \
                                and last_piece == "pawn" \
                                and last_file == file_letter[file_letter.index(squares[0]) + 1]:
                            if (full_board_index.index(squares) + 7) < 63:
                                old_ep_square = last_file + str(last_row)
                                old_ep_values = square_list[old_ep_square][2:]
                                old_self_values = square_list[squares][2:]
                                new_self_square = full_board_index[full_board_index.index(squares) + 7]
                                del square_list[old_ep_square][2:]
                                del square_list[squares][2:]
                                for value in old_self_values:
                                    square_list[new_self_square].append(value)
                                self.check_check_black(black_king.square, black_king.file, black_king.row)
                                if not self.black_king_check:
                                    stale_mate_legal_moves_black.append(squares[0] + "x" + new_self_square + " e.p")
                                del square_list[new_self_square][2:]
                                for value in old_self_values:
                                    square_list[squares].append(value)
                                for value in old_ep_values:
                                    square_list[old_ep_square].append(value)
                        if int(squares[1]) == 4 \
                                and "OCCUPIED" not in square_list[full_board_index[full_board_index.index(squares) - 9]] \
                                and "OCCUPIED" in square_list[full_board_index[full_board_index.index(squares) - 8]] \
                                and "white" in square_list[full_board_index[full_board_index.index(squares) - 8]] \
                                and "pawn" in square_list[full_board_index[full_board_index.index(squares) - 8]] \
                                and last_row == 4 \
                                and before_row == 2 \
                                and last_piece == "pawn" \
                                and last_file == file_letter[file_letter.index(squares[0]) - 1]:
                            if (full_board_index.index(squares) - 9) > 0:
                                old_ep_square = last_file + str(last_row)
                                old_ep_values = square_list[old_ep_square][2:]
                                old_self_values = square_list[squares][2:]
                                new_self_square = full_board_index[full_board_index.index(squares) - 9]
                                del square_list[old_ep_square][2:]
                                del square_list[squares][2:]
                                for value in old_self_values:
                                    square_list[new_self_square].append(value)
                                self.check_check_black(black_king.square, black_king.file, black_king.row)
                                if not self.black_king_check:
                                    stale_mate_legal_moves_black.append(squares[0] + "x" + new_self_square + " e.p")
                                del square_list[new_self_square][2:]
                                for value in old_self_values:
                                    square_list[squares].append(value)
                                for value in old_ep_values:
                                    square_list[old_ep_square].append(value)
                    # check if pawn can take a piece or pawn
                    take_squares = list()
                    if -1 < (full_board_index.index(squares) - 9) < 63:
                        take_square_1 = full_board_index[full_board_index.index(squares) - 9]
                        take_squares.append(take_square_1)
                    if -1 < (full_board_index.index(squares) + 7) < 63:
                        take_square_2 = full_board_index[full_board_index.index(squares) + 7]
                        take_squares.append(take_square_2)
                    for take_square in take_squares:
                        if "OCCUPIED" in square_list[take_square] \
                                and "white" in square_list[take_square]:
                            self.virtual_move(take_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append(squares[0] + "x" + take_square)
                if "bishop" in square_list[squares]:
                    bishop_file = squares[0]
                    bishop_row = int(squares[1])
                    bishop_sm_list = list()
                    for i in range(1, 9):
                        if -1 < (file_letter.index(bishop_file) - i) < 8 \
                                and -1 < (row_number.index(bishop_row) - i) < 8:
                            new_bishop_file = file_letter[file_letter.index(bishop_file) - i]
                            new_bishop_row = row_number[row_number.index(bishop_row) - i]
                            new_bishop_square = new_bishop_file + str(new_bishop_row)
                            bishop_sm_list.append(new_bishop_square)
                    for move in bishop_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "B" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("B" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            if "Bx" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Bx" + move)
                            break
                    bishop_sm_list = list()
                    for i in range(1, 9):
                        if -1 < (file_letter.index(bishop_file) + i) < 8 \
                                and -1 < (row_number.index(bishop_row) + i) < 8:
                            new_bishop_file = file_letter[file_letter.index(bishop_file) + i]
                            new_bishop_row = row_number[row_number.index(bishop_row) + i]
                            new_bishop_square = new_bishop_file + str(new_bishop_row)
                            bishop_sm_list.append(new_bishop_square)
                    for move in bishop_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "B" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("B" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            if "Bx" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Bx" + move)
                            break
                    bishop_sm_list = list()
                    for i in range(1, 9):
                        if -1 < (file_letter.index(bishop_file) + i) < 8 \
                                and -1 < (row_number.index(bishop_row) - i) < 8:
                            new_bishop_file = file_letter[file_letter.index(bishop_file) + i]
                            new_bishop_row = row_number[row_number.index(bishop_row) - i]
                            new_bishop_square = new_bishop_file + str(new_bishop_row)
                            bishop_sm_list.append(new_bishop_square)
                    for move in bishop_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "B" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("B" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            if "Bx" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Bx" + move)
                            break
                    bishop_sm_list = list()
                    for i in range(1, 9):
                        if -1 < (file_letter.index(bishop_file) - i) < 8 \
                                and -1 < (row_number.index(bishop_row) + i) < 8:
                            new_bishop_file = file_letter[file_letter.index(bishop_file) - i]
                            new_bishop_row = row_number[row_number.index(bishop_row) + i]
                            new_bishop_square = new_bishop_file + str(new_bishop_row)
                            bishop_sm_list.append(new_bishop_square)
                    for move in bishop_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "B" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("B" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            if "Bx" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Bx" + move)
                            break

                if "rook" in square_list[squares]:
                    rook_file = squares[0]
                    rook_row = int(squares[1])
                    rook_sm_list = list()
                    for i in range(1, 9):
                        if -1 < (file_letter.index(rook_file) + i) < 8:
                            new_rook_file = file_letter[file_letter.index(rook_file) + i]
                            new_rook_square = new_rook_file + str(rook_row)
                            rook_sm_list.append(new_rook_square)
                    for move in rook_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "R" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("R" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            if "Rx" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Rx" + move)
                            break
                    rook_sm_list = list()
                    for i in range(1, 9):
                        if -1 < (file_letter.index(rook_file) - i) < 8:
                            new_rook_file = file_letter[file_letter.index(rook_file) - i]
                            new_rook_square = new_rook_file + str(rook_row)
                            rook_sm_list.append(new_rook_square)
                    for move in rook_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "R" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("R" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            if "Rx" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Rx" + move)
                            break
                    rook_sm_list = list()
                    for i in range(1, 9):
                        if -1 < (row_number.index(rook_row) - i) < 8:
                            new_rook_row = row_number[row_number.index(rook_row) - i]
                            new_rook_square = rook_file + str(new_rook_row)
                            rook_sm_list.append(new_rook_square)
                    for move in rook_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "R" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("R" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            if "Rx" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Rx" + move)
                            break
                    for i in range(1, 9):
                        if -1 < (row_number.index(rook_row) + i) < 8:
                            new_rook_row = row_number[row_number.index(rook_row) + i]
                            new_rook_square = rook_file + str(new_rook_row)
                            rook_sm_list.append(new_rook_square)
                    for move in rook_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "R" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("R" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            if "Rx" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Rx" + move)
                            break
                if "queen" in square_list[squares]:
                    queen_file = squares[0]
                    queen_row = int(squares[1])
                    queen_sm_list = list()
                    for i in range(1, 9):
                        if -1 < (file_letter.index(queen_file) - i) < 8 \
                                and -1 < (row_number.index(queen_row) - i) < 8:
                            new_queen_file = file_letter[file_letter.index(queen_file) - i]
                            new_queen_row = row_number[row_number.index(queen_row) - i]
                            new_queen_square = new_queen_file + str(new_queen_row)
                            queen_sm_list.append(new_queen_square)
                    for move in queen_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "Q" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Q" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            if "Qx" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Qx" + move)
                            break
                    queen_sm_list = list()
                    for i in range(1, 9):
                        if -1 < (file_letter.index(queen_file) + i) < 8 \
                                and -1 < (row_number.index(queen_row) - i) < 8:
                            new_queen_file = file_letter[file_letter.index(queen_file) + i]
                            new_queen_row = row_number[row_number.index(queen_row) - i]
                            new_queen_square = new_queen_file + str(new_queen_row)
                            queen_sm_list.append(new_queen_square)
                    for move in queen_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "Q" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Q" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            if "Qx" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Qx" + move)
                            break
                    queen_sm_list = list()
                    for i in range(1, 9):
                        if -1 < (file_letter.index(queen_file) - i) < 8 \
                                and -1 < (row_number.index(queen_row) + i) < 8:
                            new_queen_file = file_letter[file_letter.index(queen_file) - i]
                            new_queen_row = row_number[row_number.index(queen_row) + i]
                            new_queen_square = new_queen_file + str(new_queen_row)
                            queen_sm_list.append(new_queen_square)
                    for move in queen_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "Q" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Q" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            if "Qx" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Qx" + move)
                            break
                    queen_sm_list = list()
                    for i in range(1, 9):
                        if -1 < (file_letter.index(queen_file) + i) < 8 \
                                and -1 < (row_number.index(queen_row) + i) < 8:
                            new_queen_file = file_letter[file_letter.index(queen_file) + i]
                            new_queen_row = row_number[row_number.index(queen_row) + i]
                            new_queen_square = new_queen_file + str(new_queen_row)
                            queen_sm_list.append(new_queen_square)
                    for move in queen_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "Q" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Q" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            if "Qx" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Qx" + move)
                            break
                    # QUEEN MOVES FOR THE HORIZONTALS
                    queen_sm_list = list()
                    for i in range(1, 9):
                        if -1 < (file_letter.index(queen_file) + i) < 8:
                            new_queen_file = file_letter[file_letter.index(queen_file) + i]
                            new_queen_square = new_queen_file + str(queen_row)
                            queen_sm_list.append(new_queen_square)
                    for move in queen_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "Q" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Q" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            if "Qx" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Qx" + move)
                            break
                    queen_sm_list = list()
                    for i in range(1, 9):
                        if -1 < (file_letter.index(queen_file) - i) < 8:
                            new_queen_file = file_letter[file_letter.index(queen_file) - i]
                            new_queen_square = new_queen_file + str(queen_row)
                            queen_sm_list.append(new_queen_square)
                    for move in queen_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "Q" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Q" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            if "Qx" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Qx" + move)
                            break
                    # QUEEN MOVES FOR THE VERTICALS
                    queen_sm_list = list()
                    for i in range(1, 9):
                        if -1 < (row_number.index(queen_row) - i) < 8:
                            new_queen_row = row_number[row_number.index(queen_row) - i]
                            new_queen_square = queen_file + str(new_queen_row)
                            queen_sm_list.append(new_queen_square)
                    for move in queen_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "Q" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Q" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            if "Qx" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Qx" + move)
                            break
                    queen_sm_list = list()
                    for i in range(1, 9):
                        if -1 < (row_number.index(queen_row) + i) < 8:
                            new_queen_row = row_number[row_number.index(queen_row) + i]
                            new_queen_square = queen_file + str(new_queen_row)
                            queen_sm_list.append(new_queen_square)
                    for move in queen_sm_list:
                        if "OCCUPIED" not in square_list[move]:
                            if "Q" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Q" + move)
                        elif "OCCUPIED" in square_list[move] \
                                and "black" in square_list[move]:
                            break
                        elif "OCCUPIED" in square_list[move] \
                                and "white" in square_list[move]:
                            if "Qx" + move not in stale_mate_legal_moves_black:
                                self.virtual_move(move, squares, "black")
                                if self.legal_move:
                                    stale_mate_legal_moves_black.append("Qx" + move)
                            break
                if "knight" in square_list[squares]:
                    knight_index = full_board_index.index(squares)
                    knight_file = squares[0]
                    knight_row = int(squares[1])
                    knight_file_index = file_letter.index(knight_file)
                    knight_row_index = row_number.index(knight_row)

                    if 8 > knight_file_index + 1 > -1 \
                            and 8 > knight_row_index + 2 > -1:
                        new_knight_file = file_letter[file_letter.index(knight_file) + 1]
                        new_knight_row = row_number[row_number.index(knight_row) + 2]
                        new_knight_square = new_knight_file + str(new_knight_row)
                        if "OCCUPIED" in square_list[new_knight_square] \
                                and "black" in square_list[new_knight_square]:
                            pass
                        elif "OCCUPIED" in square_list[new_knight_square] \
                                and "white" in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append("Nx" + new_knight_square)
                        elif "OCCUPIED" not in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append("N" + new_knight_square)
                    if 8 > knight_file_index - 1 > -1 \
                            and 8 > knight_row_index + 2 > -1:
                        new_knight_file = file_letter[file_letter.index(knight_file) - 1]
                        new_knight_row = row_number[row_number.index(knight_row) + 2]
                        new_knight_square = new_knight_file + str(new_knight_row)
                        if "OCCUPIED" in square_list[new_knight_square] \
                                and "black" in square_list[new_knight_square]:
                            pass
                        elif "OCCUPIED" in square_list[new_knight_square] \
                                and "white" in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append("Nx" + new_knight_square)
                        elif "OCCUPIED" not in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append("N" + new_knight_square)
                    if 8 > knight_file_index + 1 > -1 \
                            and 8 > knight_row_index - 2 > -1:
                        new_knight_file = file_letter[file_letter.index(knight_file) + 1]
                        new_knight_row = row_number[row_number.index(knight_row) - 2]
                        new_knight_square = new_knight_file + str(new_knight_row)
                        if "OCCUPIED" in square_list[new_knight_square] \
                                and "black" in square_list[new_knight_square]:
                            pass
                        elif "OCCUPIED" in square_list[new_knight_square] \
                                and "white" in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append("Nx" + new_knight_square)
                        elif "OCCUPIED" not in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append("N" + new_knight_square)
                    if 8 > knight_file_index - 1 > -1 \
                            and 8 > knight_row_index - 2 > -1:
                        new_knight_file = file_letter[file_letter.index(knight_file) - 1]
                        new_knight_row = row_number[row_number.index(knight_row) - 2]
                        new_knight_square = new_knight_file + str(new_knight_row)
                        if "OCCUPIED" in square_list[new_knight_square] \
                                and "black" in square_list[new_knight_square]:
                            pass
                        elif "OCCUPIED" in square_list[new_knight_square] \
                                and "white" in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append("Nx" + new_knight_square)
                        elif "OCCUPIED" not in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append("N" + new_knight_square)
                    if 8 > knight_file_index + 2 > -1 \
                            and 8 > knight_row_index - 1 > -1:
                        new_knight_file = file_letter[file_letter.index(knight_file) + 2]
                        new_knight_row = row_number[row_number.index(knight_row) - 1]
                        new_knight_square = new_knight_file + str(new_knight_row)
                        if "OCCUPIED" in square_list[new_knight_square] \
                                and "black" in square_list[new_knight_square]:
                            pass
                        elif "OCCUPIED" in square_list[new_knight_square] \
                                and "white" in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append("Nx " + new_knight_square)
                        elif "OCCUPIED" not in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append("N" + new_knight_square)
                    if 8 > knight_file_index - 2 > -1 \
                            and 8 > knight_row_index - 1 > -1:
                        new_knight_file = file_letter[file_letter.index(knight_file) - 2]
                        new_knight_row = row_number[row_number.index(knight_row) - 1]
                        new_knight_square = new_knight_file + str(new_knight_row)
                        if "OCCUPIED" in square_list[new_knight_square] \
                                and "black" in square_list[new_knight_square]:
                            pass
                        elif "OCCUPIED" in square_list[new_knight_square] \
                                and "white" in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append("Nx" + new_knight_square)
                        elif "OCCUPIED" not in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append("N" + new_knight_square)
                    if 8 > knight_file_index + 2 > -1 \
                            and 8 > knight_row_index + 1 > -1:
                        new_knight_file = file_letter[file_letter.index(knight_file) + 2]
                        new_knight_row = row_number[row_number.index(knight_row) + 1]
                        new_knight_square = new_knight_file + str(new_knight_row)
                        if "OCCUPIED" in square_list[new_knight_square] \
                                and "black" in square_list[new_knight_square]:
                            pass
                        elif "OCCUPIED" in square_list[new_knight_square] \
                                and "white" in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append("Nx" + new_knight_square)
                        elif "OCCUPIED" not in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append("N" + new_knight_square)
                    if 8 > knight_file_index - 2 > -1 \
                            and 8 > knight_row_index + 1 > -1:
                        new_knight_file = file_letter[file_letter.index(knight_file) - 2]
                        new_knight_row = row_number[row_number.index(knight_row) + 1]
                        new_knight_square = new_knight_file + str(new_knight_row)
                        if "OCCUPIED" in square_list[new_knight_square] \
                                and "black" in square_list[new_knight_square]:
                            pass
                        elif "OCCUPIED" in square_list[new_knight_square] \
                                and "white" in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append("Nx" + new_knight_square)
                        elif "OCCUPIED" not in square_list[new_knight_square]:
                            self.virtual_move(new_knight_square, squares, "black")
                            if self.legal_move:
                                stale_mate_legal_moves_black.append("N" + new_knight_square)
                                    
        print("Stale_mate_moves FOR THE BLACK KINGIE: "+ str(stale_mate_legal_moves_black))
        if stale_mate_legal_moves_black == []:
            print("STALEMATE")
            global stale_mate
            stale_mate = True

    def fifty_move_rule(self, capture, piece):
        """make a list of the last move and if the move is a capture, if no pawn moves of captures are made in fifty
        moves it is a draw"""
        global fifty_count
        global fifty_move_draw
        if capture == "no capture " \
                and piece != "pawn":
            fifty_count += 1
        if capture == "capture " \
                or piece == "pawn":
            fifty_count = 0
        if fifty_count == 100:
            fifty_move_draw = True
        print("FIFTY COUNT: " + str(fifty_count))

    def draw_by_material(self):
        """check if the game is drawn by insufficient material"""
        global instant_draw
        global white_draw_TO
        global black_draw_TO
        instant_draw = False
        white_draw_TO = False
        black_draw_TO = False
        full_board_squares = []
        charlistje = "abcdefgh"
        for charje in charlistje:
            for cifje in range(1, 9):
                square_bet = charje + str(cifje)
                full_board_squares.append(square_bet)

        light_square_list = list()
        dark_square_list = list()
        global count_dark
        global dark_square
        global light_square
        global even
        global uneven
        even = True
        uneven = False
        dark_square = -2
        light_square = -1
        for i in range(0, 64, 2):
            if even:
                for j in range(4):
                    dark_square += 2
                    dark_square_list.append(full_board_squares[dark_square])
                if dark_square > 62:
                    break
                else:
                    dark_square += 1
                    even = False
                    uneven = True
            if uneven:
                for k in range(4):
                    dark_square += 2
                    dark_square_list.append(full_board_squares[dark_square])
                if dark_square > 62:
                    break
                else:
                    dark_square -= 1
                    uneven = False
                    even = True
        even = True
        uneven = False
        print(str(dark_square_list))
        for i in range(0, 64, 2):
            if even:
                for j in range(4):
                    light_square += 2
                    light_square_list.append(full_board_squares[light_square])
                if light_square > 61:
                    break
                else:
                    light_square -=1
                    even = False
                    uneven = True
            if uneven:
                for k in range(4):
                    light_square += 2
                    light_square_list.append(full_board_squares[light_square])
                if light_square > 61:
                    break
                else:
                    light_square += 1
                    uneven = False
                    even = True


        white_pieces_draw_list = list()
        black_pieces_draw_list = list()
        for squares in square_list:
            if "white" in square_list[squares]:
                white_pieces_draw_list.append(square_list[squares][4])
            if "black" in square_list[squares]:
                black_pieces_draw_list.append(square_list[squares][4])

        # If two line kings
        if {"king"} == set(white_pieces_draw_list) \
                and {"king"} == set(black_pieces_draw_list):
            instant_draw = True
        # IF lone white king
        if {"king"} == set(white_pieces_draw_list):
            if {"king", "knight"} == set(black_pieces_draw_list):
                instant_draw = True
            if {"king", "bishop"} == set(black_pieces_draw_list) \
                    and len(black_pieces_draw_list) == 2:
                instant_draw = True

        # If lone black king
        if {"king"} ==  set(black_pieces_draw_list):
            if {"king", "knight"} == set(white_pieces_draw_list):
                instant_draw = True
            if {"king", "bishop"} == set(white_pieces_draw_list) \
                    and len(white_pieces_draw_list) == 2:
                instant_draw = True

        # if king + bishop vs king + bishop, bishops on same color. its a draw
        if {"king", "bishop"} == set(white_pieces_draw_list) \
                and len(white_pieces_draw_list) == 2 \
                and {"king", "bishop"} == set(black_pieces_draw_list) \
                and len(white_pieces_draw_list) == 2:
            if any({"white", "bishop"}.issubset(set(square_list[squares])) for squares in light_square_list) \
                    and any({"black", "bishop"}.issubset(set(square_list[squares])) for squares in light_square_list):
                instant_draw = True
            if any({"white", "bishop"}.issubset(set(square_list[squares])) for squares in dark_square_list) \
                    and any({"black", "bishop"}.issubset(set(square_list[squares])) for squares in dark_square_list):
                instant_draw = True


        # white material draw if black times out
        if {"king", "knight"} == set(white_pieces_draw_list):
            white_draw_TO = True

        if {"king", "bishop"} == set(white_pieces_draw_list) \
            and len(white_pieces_draw_list) == 2:
            white_draw_TO = True

        # black material draw if white times out
        if {"king", "knight"} == set(black_pieces_draw_list):
            black_draw_TO = True

        if {"king", "bishop"} == set(black_pieces_draw_list) \
            and len(white_pieces_draw_list) == 2:
            black_draw_TO = True

    def virtual_move(self, dest_square, source_square, color):

        global old_dest_square_values
        self.occupied = False
        self.legal_move = False
        if "OCCUPIED" in square_list[dest_square]:
            old_dest_square_values = square_list[dest_square][2:]
            self.occupied = True
        old_source_square_values = square_list[source_square][2:]
        del square_list[dest_square][2:]
        del square_list[source_square][2:]
        for new_values in old_source_square_values:
            square_list[dest_square].append(new_values)
        if color == "white":
            self.check_check_white(white_king.square, white_king.file, white_king.row)
            if not self.white_king_check:
                self.legal_move = True
            else:
                self.legal_move = False
        if color == "black":
            self.check_check_black(black_king.square, black_king.file, black_king.row)
            if not self.black_king_check:
                self.legal_move = True
            else:
                self.legal_move = False
        del square_list[dest_square][2:]
        for old_value in old_source_square_values:
            square_list[source_square].append(old_value)

        if self.occupied:
            for old_value in old_dest_square_values:
                square_list[dest_square].append(old_value)
        self.occupied = False





if __name__ == "__main__":
    Piece.check_checkmate()