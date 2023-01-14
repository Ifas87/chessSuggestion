import os
from stockfish import Stockfish

translations = {"N" : "knight", "B" : "bishop", "Q" : "Queen", "R" : "rook", "K" : "king"}

def main():
    dafish = Stockfish(path="stocksifh/stockfish-windows-2022-x86-64-modern")
    # dafish.set_position(["e2e4", "e7e6"])

    best_move = dafish.get_best_move()[0]

    if (best_move in translations):
        print(translations[best_move])
    else:
        print("pawn")

if __name__=='__main__':
    main()