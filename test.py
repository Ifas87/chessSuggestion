import chess
from stockfish import Stockfish
import requests
from bs4 import BeautifulSoup
from copiedcode import pgn_to_moves
import time


translations = {"N" : "knight", "B" : "bishop", "Q" : "Queen", "R" : "rook", "K" : "king", "n" : "knight", "b" : "bishop", "q" : "Queen", "r" : "rook", "k" : "king"}


def main(pgn):
    dafish = Stockfish(path="stocksifh/stockfish-windows-2022-x86-64-modern", depth=20, parameters={"Threads": 2}) 
    all_turns = []

    for turn in pgn_steps:
        turn = list(turn)
        if(turn[0][0] == "P" or turn[0][0] == "p"):
            turn[0] = turn[0][1:]
            all_turns.append(turn[0])
        else:
            all_turns.append(turn[0])
        if(len(turn) > 1):
            if(turn[1][0] == "P" or turn[1][0] == "p"):
                turn[1] = turn[1][1:]
                all_turns.append(turn[1])
            else:
                all_turns.append(turn[1])

    bg = chess.Board()
    changed = False

    translated_turns = []
    castle = False

    for turn in all_turns:
        
        pushed_turn = ""

        if not(len(turn) > 2 and turn[0] in translations):
            pushed_turn = turn.strip()
        else:
            changed = True
            pushed_turn = (turn[0].upper()+turn[1:]).strip()

        if turn.strip() == "oo" or turn.strip() == "OO":
            pushed_turn = "O-O"
        if turn.strip() == "ooo" or turn.strip()=="OOO":
            pushed_turn = "O-O-O"


        try:
            lan = str(bg.push_san(pushed_turn))
        except (chess.IllegalMoveError, chess.InvalidMoveError) as c:
            if changed:
                lan = str(bg.push_san(turn.strip()))
            else:
                raise chess.IllegalMoveError

        translated_turns.append(lan)

    
    dafish.set_position(translated_turns)
    best_move = dafish.get_best_move()

    if len(translated_turns) % 2 == 0:
        print("White reccomendation: ", best_move)
    else:
        print("Black reccomendation: ", best_move)

    # piece_symbol = best_move[:2]
    # piece = str(bg.piece_at(chess.parse_square(piece_symbol)))

    # if translations.get(piece):
    #     print(translations[piece], best_move)
    #     # print(translations[piece])
    # else:
    #     print("Pawn", best_move)
    #     # print('Pawn')


if __name__ == "__main__":
    moveCount=0
    while True: 
        stuff = requests.get("https://lichess.org/4TkATtxB")
        bstuff = BeautifulSoup(stuff.text, 'html.parser')
        results = bstuff.find('div', 'pgn')
        bresults = results.text.split("\n",1)[1]
        pgn_steps = pgn_to_moves(bresults)
        main(pgn_steps)
        time.sleep(1)