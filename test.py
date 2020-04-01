import main as hltv

def selectoption():
    print('Please select options from below:'
          '\n1. Top 5 Teams'
          '\n2. Top 30 Teams'
          '\n3. Top 10 Players'
          '\n4. Last 10 Matches')

def topfiveteams():
    top5 = hltv.top5teams()
    option1 = input()
    #if option1 == '1':
        #print ('\n'.join(map(str, top5[0:])))
    while True:
        try:
            option1 = int(input('Enter Here: '))
            if option1 < 1 or option1 > 5:
                raise ValueError
            break
        except ValueError:
            print("Invalid option, please try again!")
        else:
            if option1 == '1':
                print ('\n'.join(map(str, top5[0:])))


selectoption()
topfiveteams()

