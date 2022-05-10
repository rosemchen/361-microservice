import time

while True:
    userinput = int(input("1 to generate random cat names or 2 to exit: "))
    if userinput == 1:
        catnameswrite = open('catnames.json', 'w')
        print('open catnames.json')
        catnameswrite.write('run')
        print('write "run" in catnames.json')
        catnameswrite.close()
        print('close catnames.json and wait')
        time.sleep(5)

        output = open('catnames.json', 'r')
        write = output.readline()
        output.close()
        print(f"{write}")
    elif userinput == 2:
        break