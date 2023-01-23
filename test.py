import chess
from stockfish import Stockfish


def main():
    dafish = Stockfish(path="stocksifh/stockfish-windows-2022-x86-64-modern", depth=20, parameters={"Threads": 2})
    dafish.set_position(['e2e4', 'c7c5'])
    print(dafish.get_best_move())

if __name__ == "__main__":
    main()