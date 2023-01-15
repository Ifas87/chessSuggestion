import re

string = """
[Event "Casual Correspondence game"]
[Site "https://lichess.org/ceGWgHJ8"]
[Date "2023.01.15"]
[White "lichess AI level 5"]
[Black "ifas87"]
[Result "0-1"]
[UTCDate "2023.01.15"]
[UTCTime "08:44:28"]
[WhiteElo "?"]
[BlackElo "1500"]
[Variant "Standard"]
[TimeControl "-"]
[ECO "B34"]
[Opening "Sicilian Defense: Accelerated Dragon, Modern Variation"]
[Termination "Normal"]
[Annotator "lichess.org"]

1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. Nc3 { B34 Sicilian Defense: Accelerated Dragon, Modern Variation } Bg7 6. Be3 d6 7. Bb5 Bd7 8. O-O a6 9. Ba4 b5 10. Bb3 Nf6 11. Qd2 O-O 12. Nxc6 Bxc6 13. f3 Qc7 14. Ne2 Nd7 15. Rad1 Ne5 16. Bd4 Nc4 17. Bxc4 bxc4 18. Bxg7 Kxg7 19. Kh1 Bb5 20. Nc3 Rfd8 21. h3 Bc6 22. f4 Rab8 23. f5 Rxb2 24. Kh2 Kg8 25. fxg6 hxg6 26. e5 Rbb8 27. Qf4 e6 28. exd6 Qb7 29. d7 f5 30. Rb1 Qa7 31. Qg3 Kf7 32. Rxb8 Rxb8 33. a4 Rd8 34. Rb1 Rxd7 35. Nb5 Bxb5 36. axb5 axb5 37. Qg5 Qc7+ 38. Qg3 Qxg3+ 39. Kxg3 Rd5 40. Rb2 Kf6 41. Rb4 Ke5 42. h4 Kd4 43. Rb2 Kc3 44. Rb1 Kxc2 45. Rf1 b4 46. Rf4 Kc3 47. Rf1 b3 48. Kf3 b2 49. Kf4 Kc2 50. g4 b1=Q 51. Rf2+ Kb3 52. Kg5 fxg4+ 53. Rf5 Qxf5+ 54. Kh6 Qf8+ 55. Kxg6 Qf2 56. h5 Rd8 57. Kg5 g3 58. Kg6 g2 59. Kh6 g1=Q 60. Kh7 Qf7+ 61. Kh6 Qf4+ 62. Kh7 Qg8# { Black wins by checkmate. } 0-1"""

def pgn_to_moves(strip):
    raw_pgn = strip#" ".join([line.strip() for line in open(gamefile)])

    comments_marked = raw_pgn.replace("{","<").replace("}",">")
    STRC = re.compile("<[^>]*>")
    comments_removed = STRC.sub(" ", comments_marked)

    STR_marked = comments_removed.replace("[","<").replace("]",">")
    str_removed = STRC.sub(" ", STR_marked)

    MOVE_NUM = re.compile("[1-9][0-9]* *\.")
    just_moves = [_.strip() for _ in MOVE_NUM.split(str_removed)]

    last_move = just_moves[-1]
    RESULT = re.compile("( *1 *- *0 *| *0 *- *1 *| *1/2 *- *1/2 *)")
    last_move = RESULT.sub("", last_move)
    moves = just_moves[:-1] + [last_move]
    moves = clean(moves)

    return pre_process_moves(moves)

def clean(moves):
    cleaned_moves = []
    for move in moves:
        if "e.p." in move:
            cleaned_move = move.replace("e.p.", "")
        SPECIAL_CHARS = re.compile("[^a-zA-Z0-9 ]")
        cleaned_move = SPECIAL_CHARS.sub("", move)
        cleaned_moves.append(cleaned_move)
    
    return cleaned_moves

def pre_process_a_move(move):
    if len(move.split()) == 1:
        wmove = move
        if wmove[0] in "abcdefgh":
            wmove = "P" + wmove
        return (wmove, )
    wmove, bmove = move.split()
    if wmove[0] in "abcdefgh":
        wmove = "P" + wmove
    if bmove[0] in "abcdefgh":
        bmove = "p" + bmove
    bmove = bmove.lower()
    
    return wmove, bmove

def pre_process_moves(moves):
    return [pre_process_a_move(move) for move in moves if len(move) > 0]

def main():
    solution = pgn_to_moves(strip=string)
    print(solution)

if __name__ == "__main__":
    main()