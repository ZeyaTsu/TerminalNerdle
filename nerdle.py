import random_calculus as rc
import replay 

word = None
guesses = []
max_errors = 5

def get_calculus():
    global word
    rc.choose()
    word = rc.calculus
    # print(word)



def main():
    
    global guesses
    global done
    global max_errors
    
    done = False
    guess = None
    guesses = []
    max_errors = 5


    get_calculus()

    while not done:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")
        

        print(f"|!| Lose in {max_errors} errors |!|")
        guess = input(f"Previous guess : {guess} > ")
        guesses.append(guess.lower())
        if guess.lower() not in word.lower():
            max_errors -= 1
            if max_errors == 0:
                break
        
        done = True
        for letter in word:
            if letter.lower() not in guesses:
                done = False
    
    if done:
        print("")
        print("You got it! GGs.")
        print(word)
        print("")
        replay.replay()
    else:
        print("Game over...")
        replay.replay()


if __name__ == '__main__':
    replay.play()


