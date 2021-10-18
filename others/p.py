lower = 900
upper = 1000
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if (num % 2) == 0: 
        print()    
    else:
        print(num)