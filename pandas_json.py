
"""

To turn the data from pandas -> numpy -> json

Lowkey doin too much

"""



import pandas as pd

import json

def grab_data(): 
    hashed_data = {}
    data = pd.DataFrame(pd.read_csv('data/Player Per Game.csv'))
    data = data.loc[:, ['player', 'season', 'team', 'g', 'stl_per_game', 
                    'blk_per_game', 'ast_per_game', 'trb_per_game', 'x3p_percent',
                    'fg_percent', 'pts_per_game']]
    data = data[data['season'] > 1997]
    data = data.fillna(0)

    data['player']=data['player'].str.lower()


    n = data.to_numpy()

    cols =['player','season', 'team', 'g', 'stl_per_game', 
        'blk_per_game', 'ast_per_game', 'trb_per_game', 'x3p_percent',
        'fg_percent', 'pts_per_game']


    hashed_data = {}


    """
    Checks if the player and season is there if so create a season hash inside a player hash
    """
    for i in range(len(n)):
        player = n[i][0]   # 'player'
        season = str(n[i][1])   # 'season' (cast to string for dict keys)

        if player not in hashed_data:
            hashed_data[player] = {}

        if season not in hashed_data[player]:
            hashed_data[player][season] = {}

        for x in range(2, len(cols)):
            stat_name = cols[x]
            stat_value = n[i][x]
            hashed_data[player][season][stat_name] = stat_value
        
    #with open("output.json", 'w') as j:
        #json.dump(hashed_data,j, indent=4)
    
    return hashed_data

n = grab_data()
print(n['stephen curry']['2025'])
    # data.loc[data['col_name'] == 'reoccuring_item', ['col1','col2',...,'coln']]