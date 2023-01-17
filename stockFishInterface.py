import os
from bs4 import BeautifulSoup
from stockfish import Stockfish
import requests
from copiedcode import pgn_to_moves
import chess
import chess.svg

translations = {"N" : "knight", "B" : "bishop", "Q" : "Queen", "R" : "rook", "K" : "king", "n" : "knight", "b" : "bishop", "q" : "Queen", "r" : "rook", "k" : "king"}
upperTranslations = {"N" : "knight", "B" : "bishop", "Q" : "Queen", "R" : "rook", "K" : "king"}

def main():
    dafish = Stockfish(path="stocksifh/stockfish-windows-2022-x86-64-modern")
    

    stuff = requests.get("https://lichess.org/D4VrxsvIe2yC")
    bstuff = BeautifulSoup(stuff.text, 'html.parser')
    results = bstuff.find('div', 'pgn')
    bresults = results.text.split("\n",1)[1]
    
    pgn_steps = pgn_to_moves(bresults)
    # print(pgn_steps)

    all_turns = []

    for turn in pgn_steps:
        turn = list(turn)
        # print(len(turn), len(turn)>1)
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

    if not all_turns:
        best_move = dafish.get_best_move()
        if (best_move in translations):
            print(translations[best_move])
        else:
            print("pawn")
    
    # print(all_turns)
    bg = chess.Board()

    for turn in all_turns:
        print(bg)
        lan = str(bg.push_san(turn))#turn.upper() if turn[0] in translations.keys() else turn ))
        print(turn, lan)

    # best_move = dafish.get_best_move()

    # print(best_move)

    # if (best_move[0] in translations):
    #     print(translations[best_move])
    # else:
    #     print("pawn")

if __name__=='__main__':
    main()