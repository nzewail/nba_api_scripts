#!usr/bin/python3

from nbapy.player import YearOverYearSplits
from players import player_list
import argparse
import logging
from utils import output, TODAY

logging.getLogger().setLevel(logging.INFO)


OUTPUT_FILE = 'player_seasons_%s.json' % (TODAY)


def parse():
    parser = argparse.ArgumentParser(description='get season stats for a given player from nba.com')
    parser.add_argument('--player-id', type=int, help='player id from nba.com')
    parser.add_argument('--all', action='store_true', help='get all players for current season')
    parser.add_argument('--output', '-o', default=OUTPUT_FILE)

    return parser.parse_args()


def query_player_season(player_id: int) -> list:
    stats = YearOverYearSplits(player_id).api.json['resultSets'][1]
    stats['headers'] = ['PLAYER_ID'] + stats['headers']
    stats['rowSet'] = [[player_id] + stat for stat in stats['rowSet']]
    return stats


def run(player_id: int, outfile) -> None:
    stats = query_player_season(player_id)
    logging.info(f'outputting for {player_id}: {stats}')
    output(stats, outfile)


if __name__ == '__main__':
    args = parse()

    with open(args.output, 'a') as outfile:
        if args.all:
            players = player_list(2020)
            for player in players:
                run(player, outfile)
        else:
            run(args.player_id, outfile)
