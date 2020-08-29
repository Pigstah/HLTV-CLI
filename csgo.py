#!/usr/bin/python3
import main as hltv
import json
import pprint

pp = pprint.PrettyPrinter()

def selectoption():
    print('Please select options from below:'
       '\n############################'
       '\n#### 1. Top 5 Teams ########'
       '\n#### 2. Top 30 Teams #######'
       '\n#### 3. Top 10 Players #####'
       '\n#### 4. Last 10 Matches ####'
       '\n############################')

def options():
    top5 = hltv.top5teams()
    top30 = hltv.top30teams()
    topplayers = hltv.top_players()
    results = hltv.get_results()
    is_valid = 0
    while not is_valid:
        try:
            option = int(input('Enter Option Here: '))
            is_valid = 1
        except ValueError as e:
            print("'%s' is an invalid option, please try again!" % e.args[0].split(": ")[1])
    
    if option == 1:
       print('\n' '\n'.join(map(str, top5[0:])))

    elif option == 2:
        pp.pprint(top30[0:])
    
    elif option == 3:
        pp.pprint(topplayers)

    elif option == 4:
        pp.pprint(results)

selectoption()
options()
