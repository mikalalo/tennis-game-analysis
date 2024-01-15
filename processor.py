from match import get_game_winner, get_set_winner, get_match_winner

# 0 ('match_id', '20230905-W-US_Open-QF-Jelena_Ostapenko-Cori_Gauff')
# 1 ('Pt', '1')
# 2 ('Set1', '0')
# 3 ('Set2', '0')
# 4 ('Gm1', '0')
# 5 ('Gm2', '0')
# 6 ('Pts', '0-0')
# 7 ('Gm#', '1 (1)')
# 8 ('TbSet', '1')
# 9 ('TB?', '0')
# 10 ('TBpt', '')
# 11 ('Svr', '1')
# 12 ('Ret', '2')
# 13 ('Serving', 'JO')
# 14 ('1st', '4n')
# 15 ('2nd', '4f1n#')
# 16 ('Notes', '')
# 17 ('1stSV', '0')
# 18 ('2ndSV', '0')
# 19 ('1stIn', '0')
# 20 ('2ndIn', '1')
# 21 ('isAce', 'FALSE')
# 22 ('isUnret', 'FALSE')
# 23 ('isRallyWinner', 'FALSE')
# 24 ('isForced', 'TRUE')
# 25 ('isUnforced', 'FALSE')
# 26 ('isDouble', 'FALSE')
# 27 ('PtWinner', '1')
# 28 ('isSvrWinner', '1')
# 29 ('rallyCount', '1')

row_headers = ['match_id', 'Pt', 'Set1', 'Set2', 'Gm1', 'Gm2', 'Pts', 'Gm#', 'TbSet', 'TB?', 'TBpt', 'Svr', 'Ret', 'Serving', '1st', '2nd', 'Notes', '1stSV', '2ndSV', '1stIn', '2ndIn', 'isAce', 'isUnret', 'isRallyWinner', 'isForced', 'isUnforced', 'isDouble', 'PtWinner', 'isSvrWinner', 'rallyCount']

def get_row_result(row):
    row_points = row[6]
    svr = int(row[11])
    if svr == 1:
        pts1, pts2 = row_points.split("-")

    else:
        pts2, pts1 = row_points.split("-")
    
    if pts1 != 'AD':
        pts1 = int(pts1)
    if pts2 != 'AD':
        pts2 = int(pts2)

    row_pt_winner = int(row[27])
    tiebreaker = row[9]
    game_winner = get_game_winner(pts1, pts2, row_pt_winner, tiebreaker)   

    gm1 = int(row[4])
    gm2 = int(row[5])
    set_winner = get_set_winner(gm1, gm2, game_winner)
    
    set1 = int(row[2])
    set2 = int(row[3])
    match_winner = get_match_winner(set1, set2, set_winner)

    return game_winner, set_winner, match_winner