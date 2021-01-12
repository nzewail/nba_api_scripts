#!usr/bin/python3

from nbapy import player
import argparse
from typing import Iterator
from utils import output, format_season, TODAY
import logging

OUTPUT_FILE = 'players_%s.json' % (TODAY)


def parse():
    parser = argparse.ArgumentParser(description='return basic information on every nba player for a given season')
    parser.add_argument('--season', type=int, default=2020,
                        help='beginning year of a season (i.e. 2020 for 2020-21 season)')
    parser.add_argument('--active', type=int, default=1, help='must be 0 or 1')
    parser.add_argument('--output', '-o', default=OUTPUT_FILE)
    return parser.parse_args()


def player_list(season: int, active_only: int = 1) -> Iterator[int]:
    '''Given season and active flag return list of nba player ids

    :param season: integer representing start of season (i.e. 2020 for 2020-21 season)
    :type season: int

    :param active_only: flag for only active players
    :param active_only: int (must be 1 or 0)

    :return player: Iterator of player ids
    :type player: Iterator[int]
    '''
    formatted_season = format_season(season)
    players = player.PlayerList(season=formatted_season, active_only=active_only)
    for p in players.api.json['resultSets'][0]['rowSet']:
        yield p[0]


def player_summary(pid: int) -> list:
    '''Given nba player_id return list of info

    '''
    return player.Summary(pid).api.json['resultSets'][0]


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)

    args = parse()
    ids = player_list(season=args.season, active_only=args.active)

    with open(args.output, 'a') as outfile:
        for pid in ids:
            summary = player_summary(pid)
            logging.info(f"outputting {summary}")
            output(summary, outfile)
