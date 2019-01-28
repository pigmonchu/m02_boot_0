numComas = 0
value = input()

while value != '*':

    if value.isdigit():
        print('concatena')

    if value == ',':
        if numComas < 1:
            numComas += 1
            print('concatena')


    value = input()
