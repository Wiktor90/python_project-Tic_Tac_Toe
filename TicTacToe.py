import itertools
from colorama import Fore, Back, Style, init
import os

init() # colors triger from colorama pip

def cls():
    os.system("cls")

def win(current_game):
    
    #wnner 0 value block
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    
    #player color sub
    def color(c):
        if c == 1:
            return Fore.GREEN + f"\t\tPlayer {c}" + Style.RESET_ALL
        else:
            return Fore.RED + f"\t\tPlayer {c}" + Style.RESET_ALL

    #horizontal
    for row in game:
        print (row)
        if all_same(row):
            print (color(row[0])+ " is the winner horizontally (--)!")
            return True

    #vertical
    for i in range(len(game)):
        check = []
        for row in game:
            check.append(row[i])
        if all_same(check):
            print (color(check[0]) + " is the winner vertically (|)!")
            return True

    #diagonal
    check = []
    for i in range(len(game)):
        check.append(game[i][i])
    if all_same(check):
        print (color(check[0]) + " is the winner diagonally (\\)!")
        return True

    check = []
    for row, col in enumerate(reversed(range(len(game)))):
        check.append(game[row][col])
    if all_same(check):
        print (color(check[0]) + " is the winner diagonally (/)!")
        return True

    #Tie
    tie = []
    for row in game:
        for i in range(len(row)):
            tie.append(row[i])
    if 0 not in tie:
        print ("\t\tTIE !!!")
        return True
    
    return False

def game_board(game_map, player=0, row=0, column=0, just_display = False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupated. Try again!")
            return game_map, False

        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player


        for count, row in enumerate(game):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.RED + ' O ' + Style.RESET_ALL
            print(count, colored_row)
        
        return game_map, True
        
    except IndexError as e:
        print("Error make sure you inpot row/col as 0,1 or 2",e)
        return game_map, False
    except Exception as e:
        print("Something went very wrong!",e)
        return game_map, False
    
play = True
players = [1,2]
while play:
    size = int(input("What game size of tic tac toe: "))
    game = [[0 for i in range(size)] for i in range(size)]

    game_won = False
    game, _= game_board(game, just_display = True)
    players_choice = itertools.cycle(players)

    while not game_won:
        current_player = next(players_choice)
        print(f"\nPLAYER: {current_player}")
        played = False

        while not played:
            while True:
                try:
                    column_choice = int(input("choose COL: "))
                    row_choice = int(input("choose ROW: "))
                    break
                except ValueError as e:
                    print("Invalid Input! Try again.\n", e)
                    continue
            game, played = game_board(game, player=current_player, row=row_choice, column=column_choice)
        
        if win(game):
            game_won = True
            print(Back.CYAN + '\t\tGAME OVER'  + Style.RESET_ALL)
            again = input("\t\tDo you want to play again (y/n) ?")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("\t\tTHE END")
                play = False
            else:
                print("Invalid value - THE END")
                play = False
