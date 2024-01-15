from match import get_game_winner, get_set_winner, get_match_winner
from processor import get_row_result

row_nothing = ['20230905-W-US_Open-QF-Jelena_Ostapenko-Cori_Gauff', '1', '0', '0', '0', '0', '0-0', '1 (1)', '1', '0', '', '1', '2', 'JO', '4n', '4f1n#', '', '0', '0', '0', '1', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'FALSE', 'FALSE', '1', '1', '1']
row_match_winner = ['20230905-W-US_Open-QF-Jelena_Ostapenko-Cori_Gauff', '93', '0', '1', '2', '5', '40-AD', '14 (10)', '1', '0', '', '2', '1', 'CG', '6w', '5f38b1f1f2f1f1f1f1f1f1f1f2b3b3b1f1*', '', '0', '0', '0', '1', 'FALSE', 'FALSE', 'TRUE', 'FALSE', 'FALSE', 'FALSE', '2', '1', '17']
row_set_winner = ['20230903-W-US_Open-R16-Cori_Gauff-Caroline_Wozniacki', '22', '0', '0', '5', '2', '40-15', '3 (5)', '1', '0', '', '1', '2', 'CG', '5d', '4b1d#', '', '0', '0', '0', '1', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'FALSE', 'FALSE', '1', '1', '1']
row_game_winner = ['20230903-W-US_Open-R16-Cori_Gauff-Caroline_Wozniacki', '5', '0', '0', '0', '0', '15-40', '1 (5)', '1', '0', '', '1', '2', 'CG', '4n', '4f18f2b2b2d@', '', '0', '0', '0', '1', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'FALSE', '2', '0', '4']


# Test get_game_winner
class TestGameSuite:

    def test_game_40_0_P1_wins(self):
        winner = get_game_winner(40, 0, 1)
        assert winner == 1

    def test_game_40_15_P1_wins(self):
        winner = get_game_winner(40, 15, 1)
        assert winner == 1
    
    def test_game_40_30_P1_wins(self):
        winner = get_game_winner(40, 30, 1)
        assert winner == 1

    def test_game_AD_40_P1_wins(self):
        winner = get_game_winner('AD', 40, 1)
        assert winner == 1

    def test_game_0_40_P2_wins(self):
        winner = get_game_winner(0, 40, 2)
        assert winner == 2
    
    def test_game_15_40_P2_wins(self):
        winner = get_game_winner(15, 40, 2)
        assert winner == 2
    
    def test_game_30_40_P2_wins(self):
        winner = get_game_winner(30, 40, 2)
        assert winner == 2
    def test_game_40_AD_P2_wins(self):
        winner = get_game_winner(40, 'AD', 2)
        assert winner == 2

    def test_tiebreak_7_5_P1_wins(self):
        winner = get_game_winner(7, 5, 1)
        assert winner == 1

    def test_tiebreak_7_0_P1_wins(self):
        winner = get_game_winner(7, 0, 1)
        assert winner == 1

    def test_tiebreak_9_7_P1_wins(self):
        winner = get_game_winner(9, 7, 1)
        assert winner == 1
    
    def test_tiebreak_0_7_P2_wins(self):
        winner = get_game_winner(0, 7, 2)
        assert winner == 2
    
    def test_tiebreak_5_7_P2_wins(self):
        winner = get_game_winner(5, 7, 2)
        assert winner == 2
    
    
    def test_tiebreak_9_11_P2_wins(self):
        winner = get_game_winner(9, 11, 2)
        assert winner == 2
    
class TestSetSuite:

    def test_6_5_P1_wins(self):
        winner = get_set_winner(6, 5, 1)
        assert winner == 1

    def test_5_4_P1_wins(self):
        winner = get_set_winner(5, 4, 1)
        assert winner == 1
    
    def test_5_3_P1_wins(self):
        winner = get_set_winner(5, 3, 1)
        assert winner == 1
    
    def test_5_2_P1_wins(self):
        winner = get_set_winner(5, 2 ,1)
        assert winner == 1
    
    def test_5_1_P1_wins(self):
        winner = get_set_winner(5,1,1)
        assert winner == 1
    
    def test_5_0_P1_wins(self):
        winner = get_set_winner(5, 0, 1)
        assert winner == 1
    
    def test_5_6_P2_wins(self):
        winner = get_set_winner(5, 6, 2)
        assert winner == 2
    
    def test_4_5_P2_wins(self):
        winner = get_set_winner(4, 5, 2)
        assert winner == 2
    
    def test_3_5_P2_wins(self):
        winner = get_set_winner(3, 5, 2)
        assert winner == 2
    
    def test_2_5_P2_wins(self):
        winner = get_set_winner(2, 5, 2)
        assert winner == 2
    
    def test_1_5_P2_wins(self):
        winner = get_set_winner(1, 5, 2)
        assert winner == 2
    
    def test_0_5_P2_wins(self):
        winner = get_set_winner(0, 5, 2)
        assert winner == 2

class TestMatchSuite:

    def test_sets_1_1_P1_wins(self):
        winner = get_match_winner(1, 1, 1)
        assert winner == 1
    
    def test_sets_1_0_P1_wins(self):
        winner = get_match_winner(1, 0, 1)
        assert winner == 1
    
    def test_sets_0_1_P2_wins(self):
        winner = get_match_winner(0, 1, 2)
        assert winner == 2
    
    def test_sets_1_1_P2_wins(self):
        winner = get_match_winner(1, 1, 2)
        assert winner == 2

# Test processor
class TestRowGameResultSuite:

    def test_game_P1_wins_P1_serving(self):
        row_game_winner = ['20230903-W-US_Open-R16-Cori_Gauff-Caroline_Wozniacki', '5', '0', '0', '0', '0', '40-30', '1 (5)', '1', '0', '', '1', '2', 'CG', '4n', '4f18f2b2b2d@', '', '0', '0', '0', '1', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'FALSE', '1', '0', '4']
        row_result = get_row_result(row_game_winner)
        assert row_result == (1, '', '')

    def test_game_P1_wins_P2_serving(self):
        row_game_winner = ['20230903-W-US_Open-R16-Cori_Gauff-Caroline_Wozniacki', '5', '0', '0', '0', '0', '40-AD', '1 (5)', '1', '0', '', '2', '2', 'CG', '4n', '4f18f2b2b2d@', '', '0', '0', '0', '1', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'FALSE', '1', '0', '4']
        row_result = get_row_result(row_game_winner)
        assert row_result == (1, '', '')

    def test_game_P2_wins_P1_serving(self):
        row_game_winner = ['20230903-W-US_Open-R16-Cori_Gauff-Caroline_Wozniacki', '5', '0', '0', '0', '0', '30-40', '1 (5)', '1', '0', '', '1', '2', 'CG', '4n', '4f18f2b2b2d@', '', '0', '0', '0', '1', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'FALSE', '2', '0', '4']
        row_result = get_row_result(row_game_winner)
        assert row_result == (2, '', '')

    def test_game_P2_wins_P2_serving(self):
        row_game_winner = ['20230903-W-US_Open-R16-Cori_Gauff-Caroline_Wozniacki', '5', '0', '0', '0', '0', 'AD-40', '1 (5)', '1', '0', '', '2', '2', 'CG', '4n', '4f18f2b2b2d@', '', '0', '0', '0', '1', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'FALSE', '2', '0', '4']
        row_result = get_row_result(row_game_winner)
        assert row_result == (2, '', '')

class TestRowSetResultSuite:
    
    def test_set_P1_wins(self):
        row_set_winner = ['20230903-W-US_Open-R16-Cori_Gauff-Caroline_Wozniacki', '5', '0', '0', '5', '0', 'AD-40', '1 (5)', '1', '0', '', '1', '2', 'CG', '4n', '4f18f2b2b2d@', '', '0', '0', '0', '1', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'FALSE', '1', '0', '4']
        row_result = get_row_result(row_set_winner)
        assert row_result == (1, 1, '')

    def test_set_P2_wins(self):
        row_set_winner = ['20230903-W-US_Open-R16-Cori_Gauff-Caroline_Wozniacki', '5', '0', '0', '5', '6', 'AD-40', '1 (5)', '1', '0', '', '2', '2', 'CG', '4n', '4f18f2b2b2d@', '', '0', '0', '0', '1', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'FALSE', '2', '0', '4']
        row_result = get_row_result(row_set_winner)
        assert row_result == (2, 2, '')

class TestRowMatchResultSuite:

    def test_match_P1_wins_serving(self):
        row_match_winner = ['20230903-W-US_Open-R16-Cori_Gauff-Caroline_Wozniacki', '5', '1', '0', '5', '3', 'AD-40', '1 (5)', '1', '0', '', '1', '2', 'CG', '4n', '4f18f2b2b2d@', '', '0', '0', '0', '1', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'FALSE', '1', '0', '4']
        row_result = get_row_result(row_match_winner)
        assert row_result == (1, 1, 1)

    def test_match_P1_wins_receiving(self):
        row_match_winner = ['20230903-W-US_Open-R16-Cori_Gauff-Caroline_Wozniacki', '5', '1', '0', '6', '5', '40-AD', '1 (5)', '1', '0', '', '2', '2', 'CG', '4n', '4f18f2b2b2d@', '', '0', '0', '0', '1', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'FALSE', '1', '0', '4']
        row_result = get_row_result(row_match_winner)
        assert row_result == (1, 1, 1)

    def test_match_P2_wins_serving(self):
        row_match_winner = ['20230903-W-US_Open-R16-Cori_Gauff-Caroline_Wozniacki', '5', '1', '1', '5', '6', 'AD-40', '1 (5)', '1', '0', '', '2', '2', 'CG', '4n', '4f18f2b2b2d@', '', '0', '0', '0', '1', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'FALSE', '2', '0', '4']
        row_result = get_row_result(row_match_winner)
        assert row_result == (2, 2, 2)

    def test_match_P2_wins_receiving(self):
        row_match_winner = ['20230903-W-US_Open-R16-Cori_Gauff-Caroline_Wozniacki', '5', '0', '1', '3', '5', '40-AD', '1 (5)', '1', '0', '', '1', '2', 'CG', '4n', '4f18f2b2b2d@', '', '0', '0', '0', '1', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'FALSE', '2', '0', '4']
        row_result = get_row_result(row_match_winner)
        assert row_result == (2, 2, 2)

# Test tiebreakers

    def test_match_P1_wins_tiebreaker_P1_serving(self):
        row_match_winner = "20230831-W-US_Open-R64-Caroline_Wozniacki-Petra_Kvitova,175,1,0,6,6,6-5,25 (12),1,1,12,1,2,CW,6n,5f2d@,,0,0,0,1,FALSE,FALSE,FALSE,FALSE,TRUE,FALSE,1,1,1"
        row_match_winner = row_match_winner.split(",")
        row_result = get_row_result(row_match_winner)
        assert row_result == (1, 1, 1)

    def test_match_P2_wins_tiebreaker_P2_serving(self):
        row_match_winner = "20230831-W-US_Open-R64-Caroline_Wozniacki-Petra_Kvitova,175,1,1,6,6,6-5,25 (12),1,1,12,2,2,CW,6n,5f2d@,,0,0,0,1,FALSE,FALSE,FALSE,FALSE,TRUE,FALSE,2,1,1"
        row_match_winner = row_match_winner.split(",")
        row_result = get_row_result(row_match_winner)
        assert row_result == (2, 2, 2)

    def test_set_P1_wins_tiebreaker_P2_serving(self):
        row_set_winner = "20230826-W-US_Open-Q3-Elsa_Jacquemot-Arianne_Hartono,72,0,0,6,6,3-6,13 (10),1,1,10,2,1,AH,6l38b3d@,,,0,,1,,FALSE,FALSE,FALSE,FALSE,TRUE,FALSE,1,0,2"
        row_set_winner = row_set_winner.split(",")
        row_result = get_row_result(row_set_winner)
        assert row_result == (1, 1, '')

    def test_set_P1_wins_tiebreaker_P1_serving(self):
        row_set_winner = "20230713-W-Wimbledon-SF-Aryna_Sabalenka-Ons_Jabeur,96,0,0,6,6,6-5,13 (12),1,1,12,1,2,AS,5r2d#,,,0,,1,,FALSE,FALSE,FALSE,TRUE,FALSE,FALSE,1,1,1"
        row_set_winner = row_set_winner.split(",")
        row_result = get_row_result(row_set_winner)
        assert row_result == (1, 1, '')


    def test_match_P1_wins_tiebreaker_P1_serving(self):
        row_match_winner = "20230709-W-Wimbledon-R16-Elina_Svitolina-Victoria_Azarenka,217,1,1,6,6,10-9,31 (20),1,S,20,1,2,ES,4*,,,0,,1,,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,1,1,1"
        row_match_winner = row_match_winner.split(",")
        row_result = get_row_result(row_match_winner)
        assert row_result == (1, 1, 1)