import os
from stockfish import Stockfish

def main():
    dafish = Stockfish(path="stocksifh/stockfish-windows-2022-x86-64-modern")
    dafish.set_position(["e2e4", "e7e6"])
    print(dafish.get_best_move())

if __name__=='__main__':
    main()