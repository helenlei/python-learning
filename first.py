largest = None
smallest = None
while True:
    val = input("Enter a number")
    if val == "done":
        break
    try:
        fval = float(val)
    except:
        print("Invalid input")
        continue

    if largest == None:
        largest = fval
    elif largest < fval:
         largest = fval
    if smallest == None:
        smallest = fval
    elif smallest > fval:
        smallest = fval

print('Maximum is', largest)
print('Minimum is', smallest)
