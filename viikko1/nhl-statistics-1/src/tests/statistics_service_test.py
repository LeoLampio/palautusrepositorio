import unittest
from statistics_service import StatisticsService
from statistics_service import SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        p = self.stats.search("Semenko")
        p : Player

        self.assertEqual(p.name, "Semenko")
        self.assertEqual(p.team, "EDM")
        self.assertEqual(p.goals, 4)
        self.assertEqual(p.assists, 12)

    def test_search_not(self):
        p = self.stats.search("LOL")

        self.assertEqual(p, None)

    def test_teams(self):
        t = self.stats.team("PIT")
        p = t[0]
        p : Player

        self.assertEqual(p.name, "Lemieux")
        self.assertEqual(p.team, "PIT")
        self.assertEqual(p.goals, 45)
        self.assertEqual(p.assists, 54)

    def test_top_points(self):
        t = self.stats.top(1, SortBy.POINTS)
        p = t[0]
        p : Player

        self.assertEqual(p.name, "Gretzky")
        self.assertEqual(p.team, "EDM")
        self.assertEqual(p.goals, 35)
        self.assertEqual(p.assists, 89)

    def test_top_goals(self):
        t = self.stats.top(1, SortBy.GOALS)
        p = t[0]
        p : Player
        
        self.assertEqual(p.name, "Lemieux")
        self.assertEqual(p.team, "PIT")
        self.assertEqual(p.goals, 45)
        self.assertEqual(p.assists, 54)

    def test_top_assists(self):
        t = self.stats.top(1, SortBy.ASSISTS)
        p = t[0]
        p : Player

        self.assertEqual(p.name, "Gretzky")
        self.assertEqual(p.team, "EDM")
        self.assertEqual(p.goals, 35)
        self.assertEqual(p.assists, 89)