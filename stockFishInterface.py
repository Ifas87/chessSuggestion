import os
from bs4 import BeautifulSoup
from stockfish import Stockfish
import requests
from copiedcode import pgn_to_moves

translations = {"N" : "knight", "B" : "bishop", "Q" : "Queen", "R" : "rook", "K" : "king"}

def main():
    dafish = Stockfish(path="stocksifh/stockfish-windows-2022-x86-64-modern")
    # dafish.set_position(["e2e4", "e7e6"])

    stuff = requests.get("https://lichess.org/ceGWgHJ8uSUb")
    bstuff = BeautifulSoup(stuff.text, 'html.parser')
    results = bstuff.find('div', 'pgn')
    # print(results.text)
    bresults = results.text.split("\n",1)[1]
    # print(bresults)
    # best_move = dafish.get_best_move()[0]

    # if (best_move in translations):
    #     print(translations[best_move])
    # else:
    #     print("pawn")

if __name__=='__main__':
    main()