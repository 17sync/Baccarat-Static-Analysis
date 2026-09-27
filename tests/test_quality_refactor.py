"""Regression checks for behavior touched by the static-analysis refactor."""

import unittest

from cards import Card, Shoe
from players import Player
from rules import Game, GameError, Table


class CardAndShoeTests(unittest.TestCase):
    def test_card_values_and_repr(self):
        self.assertEqual(Card('ace', 'hearts').value, 1)
        self.assertEqual(Card(10, 'spades').value, 0)
        self.assertEqual(repr(Card('king', 'clubs')), "Card('king', 'clubs')")

    def test_shoe_has_52_cards_per_deck_and_draws(self):
        shoe = Shoe(1)
        self.assertEqual(shoe.num_cards, 52)
        self.assertEqual(len(shoe.draw_cards(2)), 2)
        self.assertEqual(shoe.num_cards, 50)

    def test_shoe_rejects_invalid_deck_and_draw_counts(self):
        for decks in (0, -1):
            with self.assertRaises(ValueError):
                Shoe(decks)
        with self.assertRaises(TypeError):
            Shoe('one')
        with self.assertRaises(ValueError):
            Shoe(1).draw_cards(-1)


class GameAndBetTests(unittest.TestCase):
    def test_game_requires_deal_before_result(self):
        game = Game(1)
        with self.assertRaises(GameError):
            game.game_result()

    def test_table_player_indexes_are_stable(self):
        table = Table(1)
        table.add_player(10)
        table.add_player(10)
        self.assertEqual(table.available_players, [0, 1])

    def test_player_payouts_preserve_integer_rules(self):
        player = Player(100)
        player.hand_bet = 'banco'
        player.amount_bet = 10
        player.win()
        self.assertEqual(player.balance, 109)
        player.hand_bet = 'tie'
        player.amount_bet = 10
        player.win()
        self.assertEqual(player.balance, 189)

    def test_player_rejects_bet_over_balance(self):
        player = Player(10)
        with self.assertRaises(ValueError):
            player.amount_bet = 11


if __name__ == '__main__':
    unittest.main()
