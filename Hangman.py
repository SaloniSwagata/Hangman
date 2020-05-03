import random
print("--- Welcome To The Hangman Game ---")
print("Enter your name")
name=input()
print("Hello "+name+"!")
options=['magnificent','secret','happy','world','hilarious','computer','python','programming']
search=random.choice(options)
print("Your word to be searched - ")
for _ in search:
    print("*",end='')

print()
turns=len(search)+2
print("You have total "+turns+" chances to guess the correct word")
count=0
guess=''
while turns>0:
    failed=0
    ch=input("Enter your character- ")
    guess=guess+ch
    for c in search:
        if c in guess:
            print(c,end='')
        else:
            print('*',end='')
            failed+=1
            
    print()
    if failed==0:
        print("Hurray! You Won")
        break
    turns-=1
if turns==0:
    print("Better Luck next time!")
