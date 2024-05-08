import random
# double digits ka bhi batana h 
def load_dictionary(file_path):
    with open(file_path) as f:
        words=[lines.strip() for lines in f]
    return words

def valid_guess(gs,guess):
    return gs in guess

def evaluate_guess(gs,word):
    str=""
    for i in range(5):
        if gs[i]==word[i]:
            str+="\33[32m"+gs[i]
        else:
            if gs[i] in word:
                str+="\33[32m" +gs[i]
            else:
                str+="\33[0m"+gs[i]
    return str+"\33[0m"            

def wordle(guess,answer):
    print("welcome to wordle.")
    secret_word=random.choice(answer)
    atm=1
    matm=6
    while atm<= matm:
        gs=input("enter the #"+str(atm)+" 5 letter word:").lower()
        if valid_guess(gs,guess):
            print("invalid guess")
            continue
        if gs==secret_word:
            print("congratulation you won!")
            break
        atm+=1
        feedback=evaluate_guess(gs,secret_word)
        print(feedback)
    if atm>matm:
        print("Game over. The word was",secret_word)    
guess=load_dictionary("guess.txt")
answer=load_dictionary("answer.txt")

wordle(guess,answer)
