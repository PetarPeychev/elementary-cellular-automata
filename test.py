import eca
while True:
    id = int(input('ECM ID: '))
    ec = eca.ECA(id)
    print(ec.array)
    print(ec.id)
    print(ec.dict)

    while True:
        inp = input("")
        if inp == 'x':
            break
        for i in ec.array:
            if i == 0:
                print('   ', end='')
                #print(' ◻ ', end='')
            else:
                print(' ◼ ', end='')
        print()
        ec.step()x`
