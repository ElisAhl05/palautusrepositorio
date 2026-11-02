import unittest
from statistics_service import StatisticsService
from player import Player


class ReaderStub:
    def __init__(self):
        self._players = [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

    def get_players(self):
        return self._players


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            ReaderStub()
        )

    def test_search_returns_matching_player(self):
        player = self.stats.search("Gretzky")

        self.assertEqual(player.name, "Gretzky")

    def test_search_returns_none_when_no_player_matches(self):
        self.assertIsNone(self.stats.search("Selanne"))

    def test_team_returns_players_from_requested_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"]
        )

    def test_team_returns_empty_list_when_no_player_matches(self):
        self.assertEqual(self.stats.team("TOR"), [])

    def test_top_returns_players_in_descending_point_order(self):
        players = self.stats.top(2)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )
        
    def test_top_does_not_exceed_player_list_size(self):
        players = self.stats.top(10)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]
        )

    def test_statistic_service_can_return_average_goals(self):
        self.assertAlmostEqual(self.stats.average_goals("EDM"), 25.67, places=2)

    def test_statistic_service_returns_none_when_team_has_no_players(self):
        self.assertIsNone(self.stats.average_goals("ANA"))

    def test_statistic_service_can_return_most_valuable_player(self):
        self.assertEqual(self.stats.most_valuable_player().name, "Gretzky")

    def test_statistic_service_can_return_team_with_highest_score(self):
        self.assertEqual(self.stats.team_with_highest_score(), "EDM")