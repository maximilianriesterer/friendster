a = input('A: ')
b = input('B: ')

try:
    a = int(a)
    x = a**2
    b = int(b)
    print(x/b)
    except:
        if type(a) is not int and type(b) is not int:
            print("Only integers are allowed")

            print(type(b))
            if b == 0:
                print ("You can't divide by zero")