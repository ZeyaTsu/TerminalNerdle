import nerdle

def play():
    print("- - - - - Nerdle Terminal - - - - -")
    print("- - - - - By ZeyaTsu | OpenO1 - - - - -")
    print("------> PLAY ? (1 or 2)")
    v = True
    while v:
        a = str(input("> "))
        if a == '1':
            nerdle.main()
            v = False
        elif a == '2':
            break

def replay():
    s = True
    while s:
        print("Replay ? y/n")
        g = str(input("> "))

        if g in ["y","Y","yes","YES"]:
            nerdle.main()
            s = False
        elif g in ["n", "N", "no", "NO"]:
            break
