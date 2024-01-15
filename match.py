# GAME WINNER
def get_game_winner(player1_points, player2_points, point_winner, tiebreaker):
    game_winner = ''

    # print(f'- ENTERED GET GAME WINNER WITH: {player1_points}, {player2_points}, {point_winner}\n')

        # TIEBREAKER SITUATION
    if tiebreaker == '1' or tiebreaker == 'S':
        if player1_points >= 6 and player2_points <= (player1_points - 1) and point_winner == 1:
            game_winner = 1

        elif player1_points <= (player2_points - 1) and player2_points >= 6 and point_winner == 2:
            game_winner = 2
    else:
        if player1_points == 'AD' or player2_points == 'AD':
            if player1_points == 'AD' and point_winner == 1:
                game_winner = 1
            elif player2_points == 'AD' and point_winner == 2:
                game_winner = 2
        else:
            if player1_points == 40 and player2_points <= 30 and point_winner == 1:
                game_winner = 1

            elif player1_points <= 30 and player2_points == 40 and point_winner == 2:
                game_winner = 2

    return game_winner

# SET WINNER
def get_set_winner(player1_games, player2_games, game_winner):
    set_winner = ''
    # print(f'-- ENTERED GET SET WINNER WITH: {player1_games}, {player2_games}, {game_winner}\n')

    if player1_games == 5 and player2_games <= 4 and game_winner == 1:
        set_winner = 1
    elif player1_games == 6 and player2_games >= 5 and game_winner == 1:
        set_winner = 1
    elif player1_games <= 4 and player2_games == 5 and game_winner == 2:
        set_winner = 2
    elif player1_games >= 5 and player2_games == 6 and game_winner == 2:
        set_winner = 2

    return set_winner
    
# MATCH WINNER
def get_match_winner(player1_sets, player2_sets, set_winner):
    match_winner = ''
    # print(f'--- ENTERED GET MATCH WINNER WITH: {player1_sets}, {player2_sets}, {set_winner}\n')
    
    if player1_sets == 1 and player2_sets <= 1 and set_winner == 1:
        match_winner = 1
    elif player1_sets <= 1 and player2_sets == 1 and set_winner == 2:
        match_winner = 2
    
    return match_winner