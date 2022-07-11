import random;

def guess(x):
    random_number=random.randint(1,x);
    guess=0;

    while guess != random_number:
        guess=int(input('enter any number : '));

        if guess>random_number:
            print("Too high!, guess again");
        elif guess<random_number:
            print('Too low!, guess again');
    
    print(f'Yay!! you guessed the number {random_number} correctly!!');

def compGuess(x): # computer guessing the number choosen by the user

    low=1;
    high=x;
    feedback='';

    while feedback !='c':
        if low!=high:
            guess=random.randint(low,high);
        else:
            guess=low; # could also be high coz low = high

        feedback=input(f"Is number {guess} too high?(H), too low?(l) or correct?(c)").lower();

        if(feedback=='h'):
            high=guess-1;
        elif feedback=='l':
            low=guess+1;
    print(f'Yay the computer guessed the number {guess} correctly!')

compGuess(20);