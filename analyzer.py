from timeit import default_timer as timer
from processor import get_row_result


def update_table(winner_sets, table):
    # print(f'- - - - winner_sets: {winner_sets}')
    
    for set_index in range(len(winner_sets)):
        for game in winner_sets[set_index]:
            table[set_index][game - 1] += 1       

def generate_percentage_table(win_table, count_table):
    pct_table = [[0] * 13, [0] * 13, [0] * 13]
    for i in range(len(win_table)):
        for j in range(len(win_table[i])):
            pct_table[i][j] = win_table[i][j]/count_table[i][j]
    return pct_table

def process_file(file_path):
    # BELOW HAPPENING PER FILE
    # ...
    # DATA STRUCTURE DEFINITION
    total_table = [[0] * 13, [0] * 13, [0] * 13]
    match_table = [[0] * 13, [0] * 13, [0] * 13]

    match_counter = 0
    # set_counter = 1
    # game_counter = 1
    # player1_games = []
    # player2_games = []
    # player1_sets = []
    # player2_sets = []

    i = 1
    start_time = timer()

    try:
        with open(file_path, 'r') as file:
            for row in file:
                i += 1  # KEEP ROW COUNT

                # PROCESS ROW
                row = row.split(',')

                # SPECIAL CASE IN CASE PREVIOUS GAME WAS A RETIREMENT/DIDN'T FINISH
                if row[1] == '1':
                    match_counter += 1
                    game_counter = 1
                    games_played = []
                    player1_games = []
                    player2_games = []
                    set_counter = 1
                    sets_played = []
                    player1_sets = []
                    player2_sets = []

                game_winner, set_winner, match_winner = get_row_result(row) 

                # KEEP TRACK OF GAMES AND SETS WON PER PLAYER
                if game_winner == 1:
                    player1_games.append(game_counter)
                    games_played.append(game_counter)
                if game_winner == 2:
                    player2_games.append(game_counter)
                    games_played.append(game_counter)
                
                if set_winner != '':
                    # print(f'- - Set winner:')
                    # print(f'- - Player1 Sets: {player1_sets}')
                    # print(f'- - Player2 Sets: {player2_sets}')
                    player1_sets.append(player1_games) 
                    player2_sets.append(player2_games)
                    sets_played.append(games_played)

                # COUNTER INCREASERS
                if match_winner != '':
                    # print(f'- - - Match winner: Player {match_winner}')
                    # MATCH DONE:
                    # 1) INCREASE MATCH COUNTER
                    # 2) RESET GAMES AND SETS
                    # UPDATE FINAL COUNTER TABLE BASED ON MATCH WINNER
                    if match_winner == 1:
                        update_table(player1_sets, total_table)
                    elif match_winner == 2:
                        update_table(player2_sets, total_table)
                    update_table(sets_played, match_table)
                    
                    # match_counter += 1 
                    games_played = []                
                    game_counter = 1
                    player1_games = []
                    player2_games = []

                    sets_played = []
                    set_counter = 1
                    player1_sets = []
                    player2_sets = []
                
                elif set_winner != '':
                    # print(f'- - Set winner: Player {game_winner}')
                    # SET DONE:
                    # 1) INCREASE SET COUNTER
                    # 2) RESET GAMES
                    # 3) FLUSH GAMES PLAYED IN SET
                    set_counter += 1

                    games_played = []
                    game_counter = 1
                    player1_games = []
                    player2_games = []
                
                elif game_winner != '':
                    # print(f'- - Game winner: Player {game_winner}')
                    # GAME DONE:
                    # 1) INCREASE GAME COUNTER
                    game_counter += 1
    except Exception as err:
        print(f'\n! ERROR IN ROW: {i}')
        print(f'! ROW: {row}\n')
        raise err
    else:    
        end_time = timer()   
        print(f'\nPROCESSED: {i} rows and {match_counter} matches in {end_time - start_time} seconds\n')
        return generate_percentage_table(total_table, match_table)


def process_data(data):
    # BELOW HAPPENING PER FILE
    # ...
    # DATA STRUCTURE DEFINITION
    total_table = [[0] * 13, [0] * 13, [0] * 13]
    match_table = [[0] * 13, [0] * 13, [0] * 13]

    match_counter = 0
    # set_counter = 1
    # game_counter = 1
    # player1_games = []
    # player2_games = []
    # player1_sets = []
    # player2_sets = []

    i = 1
    start_time = timer()

    try:
        for row in data:
            i += 1  # KEEP ROW COUNT            

            # PROCESS ROW
            row = row.split(',')

            # SPECIAL CASE IN CASE PREVIOUS GAME WAS A RETIREMENT/DIDN'T FINISH
            if row[1] == '1':
                match_counter += 1
                game_counter = 1
                games_played = []
                player1_games = []
                player2_games = []
                set_counter = 1
                sets_played = []
                player1_sets = []
                player2_sets = []

            game_winner, set_winner, match_winner = get_row_result(row) 

            # KEEP TRACK OF GAMES AND SETS WON PER PLAYER
            if game_winner == 1:
                player1_games.append(game_counter)
                games_played.append(game_counter)
            if game_winner == 2:
                player2_games.append(game_counter)
                games_played.append(game_counter)
            
            if set_winner != '':
                # print(f'- - Set winner:')
                # print(f'- - Player1 Sets: {player1_sets}')
                # print(f'- - Player2 Sets: {player2_sets}')
                player1_sets.append(player1_games) 
                player2_sets.append(player2_games)
                sets_played.append(games_played)

            # COUNTER INCREASERS
            if match_winner != '':
                # print(f'- - - Match winner: Player {match_winner}')
                # MATCH DONE:
                # 1) INCREASE MATCH COUNTER
                # 2) RESET GAMES AND SETS
                # UPDATE FINAL COUNTER TABLE BASED ON MATCH WINNER
                if match_winner == 1:
                    update_table(player1_sets, total_table)
                elif match_winner == 2:
                    update_table(player2_sets, total_table)
                update_table(sets_played, match_table)
                
                # match_counter += 1 
                games_played = []                
                game_counter = 1
                player1_games = []
                player2_games = []

                sets_played = []
                set_counter = 1
                player1_sets = []
                player2_sets = []
            
            elif set_winner != '':
                # print(f'- - Set winner: Player {game_winner}')
                # SET DONE:
                # 1) INCREASE SET COUNTER
                # 2) RESET GAMES
                # 3) FLUSH GAMES PLAYED IN SET
                set_counter += 1

                games_played = []
                game_counter = 1
                player1_games = []
                player2_games = []
            
            elif game_winner != '':
                # print(f'- - Game winner: Player {game_winner}')
                # GAME DONE:
                # 1) INCREASE GAME COUNTER
                game_counter += 1
    except Exception as err:
        print(f'! ERROR IN ROW: {i}')
        print(f'! ROW: {row}\n')
        raise err
    else:    
        end_time = timer()   
        print(f'  - PROCESSED: {i} rows and {match_counter} matches in {(end_time - start_time):.2} seconds\n')
        return generate_percentage_table(total_table, match_table)
