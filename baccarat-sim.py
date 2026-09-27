"""Run batch simulations and write hand-level results to a text file."""

import datetime
import argparse
from rules import Game

def output_filename(decks, shoes):
    """Return the timestamped filename for a simulation report."""
    timestamp = datetime.datetime.now().strftime('%d%m%y%H%M%S')
    return f'{decks}_{shoes}_{timestamp}.txt'

def hand_values(hand):
    """Creates a list of strings with the values of a hand."""
    values = []
    for i in range(3):
        try:
            values.append(str(hand[i]))
        except IndexError:
            values.append('x')
    return values

def write_totals(sim_file, total_wins, game_count):
    """Write final winner counts and percentages to the simulation report."""
    sim_file.write('\nTotal results:\n')
    for winner, count in total_wins.items():
        percentage = round((count / game_count) * 100, 4)
        sim_file.write(f'{winner.title()}:\t{count}\t({percentage}%)\n')

def main():
    """Parse simulation options, run shoes, and write summary statistics."""

    # Counters
    shoe_count = 0
    game_count = 0
    total_wins = {'banco': 0, 'punto': 0, 'tie': 0}

    # Argument parser
    parser = argparse.ArgumentParser(description='Simulates baccarat games to a text file.')
    parser.add_argument('-s', action='store', dest='shoes', default=10000,
                        type=int, help='number of shoes to be simulated, default 10000')
    parser.add_argument('-d', action='store', dest='decks', default=8,
                        type=int, help='number of decks per shoe, default 8')
    args = parser.parse_args()

    # Create game object
    sim = Game()
    sim.create_shoe(args.decks)

    # Set file name
    file_name = output_filename(args.decks, args.shoes)

    # Open file
    with open(file_name, 'w', encoding='utf-8') as sim_file:

        # Run through num_shoes
        for i in range(args.shoes):
            shoe_wins = {'banco': 0, 'punto': 0, 'tie': 0}
            shoe_count += 1
            sim_file.write(f'\nShoe number {i + 1}\n\n')

            # While the shoe has more than 5 cards
            while sim.num_cards >= 6:
                result = []
                game_count += 1

                # Baccarat game
                sim.deal_hands()
                if not sim.is_natural():
                    sim.draw_thirds()
                game_result = sim.game_result()
                shoe_wins[game_result] += 1
                total_wins[game_result] += 1

                # Append to results list
                result.append(game_result.title()[0])
                result.append(str(sim.banco_value))
                result.append(str(sim.punto_value))
                result.extend(hand_values(sim.banco_values))
                result.extend(hand_values(sim.punto_values))
                sim_file.write(','.join(result) + '\n')

                # Progress
                progress = round((shoe_count / args.shoes) * 100, 1)
                print(f'Progress: {progress}%', end='\r')

            # Shoe results
            sim_file.write('\nShoe results:\n')
            for win, count in shoe_wins.items():
                sim_file.write(f'{win.title()}:\t{count}\n')
            sim.create_shoe(args.decks)

        write_totals(sim_file, total_wins, game_count)

if __name__ == '__main__':
    main()
