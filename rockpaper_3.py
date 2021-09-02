######

import random

def play():

    user1 = str(input("'r' for rock \n 'p' for paper \n 's' for scissors \n So what's your choice :  "))
    comp = random.choice(['r','p','s'])

    if user1 == comp:
        print(f"\n Computer choice : {comp}")
        return "\n\n  It's a tie\n\n"
    
    elif is_win(user1, comp):
        print(f"\n Computer choice : {comp}")
        return "\n\n  congrats, you won the match!\n\n"

    print(f"\n Computer choice : {comp}")
    return "\n\n  Sorry you lost the match!\n\n"

def is_win(player, opponent):
    if ( player == "r" and opponent == "s") or ( player == "p" and opponent == "r" ) or ( player == "s" and opponent == "p" ):
        return True

print(play())

#print(f"Summary \n You choosen {user1} and computer choosen {comp}")