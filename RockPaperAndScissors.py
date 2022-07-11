import random;

def play():
    user=input("What's your choice? 'r' for 'rock', 's' for stone, 'p' for paper\n")
    computer=random.choice(['r','s','p'])

    if user==computer:
        return "It's a tie"
    if win(user,computer):
        return "you Won!!"

    return "you Lost!"

def win(player,opponent):
    if((player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r')):
         return True

print(play())