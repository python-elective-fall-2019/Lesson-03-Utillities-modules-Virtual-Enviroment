while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


while True:
    try:    
        filename = input('What file would you like to open?: ')
        x = open(filename)
        break
    except Exception:
        print("No such file or directory ...")
        continue
    
    break