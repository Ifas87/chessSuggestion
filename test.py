import chess

def main():
    bg = chess.Board()

    print(bg, "\n")
    bg.push_san("e4")
    print(bg, "\n")
    bg.push_san("e5")
    print(bg, "\n")
    bg.push_san("Bc4")

if __name__ == "__main__":
    main()