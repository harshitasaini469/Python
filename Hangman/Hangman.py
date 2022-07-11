import random;
import string;
from words import words;

def get_valid_word(words):
    word=random.choice(words);
    while '-' in word or ' ' in word:
        word=random.choice(word);

    return word.upper();

def hangman():
    
    word=get_valid_word(words);
    word_letters=set(word); # letters in the word
    alphabet=set(string.ascii_uppercase); # list of upper case letters
    used_letters=set(); # what the user has guessed

    lives=7; # user have 7 lives to guess the correct letter

    #getting user input
    while len(word_letters) > 0 and lives > 0:

        #what current word is (i.e W-R D);
        wordList=[letter if letter in used_letters else '-' for letter in word ];
        print('Current Word : ', ' '.join(wordList));
       
        user_letter=input('Guess a letter : ').upper();

        if user_letter in alphabet-used_letters:   # adding the letter that is not used yet
            used_letters.add(user_letter);
            if user_letter in word_letters:
                word_letters.remove(user_letter); # removing the correctly guessed letter from word_letters
            else: 
                lives = lives - 1;
                print(f'{user_letter} letter not in the word, You have {lives} lives left\n')
        elif user_letter in used_letters:
            print('you have already guessed this character');
        else : print('invalid character');

         # letters used
        print(f'You have used these letters:',' '.join(used_letters),'\n');

    

    if(lives==0):
        print(f"Sorry, you died!\nThe word was \"{word}\"");
    else:
        print(f"Yay! you guessed the word {word} correctly!!!");

hangman()