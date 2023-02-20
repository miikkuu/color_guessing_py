import random
COLORS=["R","G","B","Y"]
TRIES=10
CODE_LENGTH=3

def generate_code():
    code=[]

    for a in range(CODE_LENGTH):
        color=random.choice(COLORS)
        code.append(color)
    return code

def guess_code():
   while True: 
     guess=input("Guess : ").upper().split(" ")
     if len(guess)!=CODE_LENGTH:
         print(f"Must guess {CODE_LENGTH} colors")
         continue

     for color in guess:
         if color not in COLORS:
             print(f"Invalid {color}")
             break
     else:
         break

   return guess

def check_code(guess,real_code):
    color_counts={}
    cor=0
    incor=0

    for color in real_code:
        if color not in color_counts:
            color_counts[color]=0
        color_counts[color]+=1    

    for guess_color ,real_color in zip(guess,real_code):
        if guess_color==real_color:
            cor+=1
            color_counts[guess_color]+=1

    for guess_color ,real_color in zip(guess,real_code):
        if guess_color in color_counts and color_counts[guess_color]>0:
            incor+=1
            color_counts[guess_color]-=1        
    return cor,incor

def game():
    print (f"you have {TRIES}")
    print( f"valid colors : {COLORS}")

    code=generate_code()
    for attempts in range(1,TRIES+1):
        guess=guess_code()
        cor,incor=check_code(guess, code)

        if cor==CODE_LENGTH:
            print(f"Right in {attempts} attempts") 
            break
        
        print(f"Correct : {cor} | Incorrect : {incor}") 
    else:
        print("Wronger , it was : ",*code)

if __name__=="__main__":
    game()