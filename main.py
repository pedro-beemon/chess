from engine.predict import get_predict, get_matrix, get_command, get_area
from __future__ import print_function
import cv2 as cv
from time import time
import numpy as np
from stockfish import Stockfish
import logging

stockfish = Stockfish(path='stockfish/stockfish-ubuntu-x86-64')
start_matrix = np.matrix(
    [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]
)

cap = cv.VideoCapture(2)
while True:
    numero_de_jogadas = 0
    # liga todos os leds, apresentação

    ret, frame = cap.read()
    cv.imshow('Capture - Face detection', frame)
    # detectAndDisplay(frame)
    loop_time = time()

    pecas = get_predict(frame)

    if numero_de_jogadas == 0:
        if len(pecas != 32):
            logging.error('Não encontrado 32 peças')
            continue

        area = get_area(pecas)
        quadrado = area[2] / 8, area[3] / 8

    matrix = get_matrix(pecas, quadrado)
    command = get_command(pecas)

    stockfish.make_moves_from_current_position([command])  # bot
    print(stockfish.get_board_visual())
    numero_de_jogadas += 1

    # pegas todas posições

    # confirma inicial

    # sorteia jogador

    # bot iniciando

    # Joga bot:
    # liga o led bot
    # aguarda movimento da player
    # confirma movimento do bot
    # apaga o led bot

    # Joga player:
    # aguarda movimento da player
    # confirma movimento do player
