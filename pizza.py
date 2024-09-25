

string = f"Welcome to python pizza Daleveris!\nprice list:"
print(string.upper())

print(f"pizza,L 25$\npizza,M 20$\npizza,S 15$!")
print(f"Extra pepperoni,L & M 3$\nExtra pepperoni S 2$\n2Extra cheese 1$ for L-M-S")

size = input("what size pizza do you want ? S,M or L :")
pepperoni = input("Do you pepperoni on your pizza ? Y or N:")
extra_chece = input("Do you want extra chece ? Y or N:")
bill = 0

if size == "L":
    bill += 25
elif size == "M":
    bill += 20
elif size == "S":
    bill += 15
else:
    print("you typed the wrong inputs.")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_chece == "Y":
    bill += 1
    print(f"your final bill is : $ {bill}")             
    print("Thank you very much for buying Python Pizza")
    
    

          



       
       
       
           
       




