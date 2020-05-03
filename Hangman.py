import random
options=['magnificent','secret','happy','world','hilarious','computer','python','programming']
search=random.choice(options)
print("The word to be searched-")
for _ in search:
    print("*",end='')

print()
turns=10
count=0
guess=''
while turns>0:
    failed=0
    ch=input("Enter your character")
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
