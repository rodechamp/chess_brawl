"""Play a test game between two players"""


from board import Board, Square


def main():
    print('MAIN START\t' + '=' * 20)
    
    brd = Board()
    brd.print_square_names()
    
    print('MAIN END\t' + '=' * 20)
    return None


if __name__ == '__main__':
    main()