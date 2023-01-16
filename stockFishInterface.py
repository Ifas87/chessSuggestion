import os
from bs4 import BeautifulSoup
from stockfish import Stockfish
import requests
from copiedcode import pgn_to_moves
import chess

translations = {"N" : "knight", "B" : "bishop", "Q" : "Queen", "R" : "rook", "K" : "king", "N" : "knight", "B" : "bishop", "Q" : "Queen", "R" : "rook", "K" : "king"}

def main():
    dafish = Stockfish(path="stocksifh/stockfish-windows-2022-x86-64-modern")
    

    stuff = requests.get("https://lichess.org/ceGWgHJ8uSUb")
    bstuff = BeautifulSoup(stuff.text, 'html.parser')
    results = bstuff.find('div', 'pgn')
    # print(results.text)
    bresults = results.text.split("\n",1)[1]
    
    pgn_steps = pgn_to_moves(bresults)
    
    all_turns = []
    for turn in pgn_steps:
        turn = list(turn)
        if(turn[0][0] == "P" or turn[0][0] == "p"):
            turn[0] = turn[0][1:]
        if(turn[1][0] == "P" or turn[1][0] == "p"):
            turn[1] = turn[1][1:]
        all_turns.append(turn[0])
        all_turns.append(turn[1])
    
    # print(all_turns)
    # dafish.set_position(all_turns)
    bg = chess.Board()
    lan = str(bg.push_san('e4'))
    print(lan)
    # best_move = dafish.get_best_move()[0]

    # print(best_move)

    # if (best_move in translations):
    #     print(translations[best_move])
    # else:
    #     print("pawn")

if __name__=='__main__':
    main()