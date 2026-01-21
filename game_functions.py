import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    if len(poss_values)%2 ==0:
        x =len(poss_values)//2 
    else:
        x=(len(poss_values)+1)//2
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    user=user_input.lower()
    user=user.strip()
    if user=="h" and next_val>current_val:
        return True
    elif user=="l" and next_val<current_val:
        return True
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    letter=letter.lower().strip()
    word=list(word)
    valid=False
    for i in range(0,len(word)):
        if word[i]==letter:
            board[i]=letter
            print("well done!",letter,"is in the word")
            valid=True
    if valid ==True:
        return valid
    else:
        print("sorry",letter,"is not in the word")
        return valid        
