#!usr/bin/python3

from nbapy.player import GameLogs
from players import player_list
import argparse
import logging
from utils import output, format_season, TODAY

logging.getLogger().setLevel(logging.INFO)

OUTPUT_FILE = 'player_game_logs_%s.json' % (TODAY)


def parse():
    parser = argparse.ArgumentParser(description='return stats for every game a player has played in a given season')
    parser.add_argument('--season', type=int, default=2020, help='beginning year of a season (i.e. 2020 for 2020-21 season)')
    parser.add_argument('--player-id', type=int, help='player id from nba.com')
    parser.add_argument('--all', action='store_true', help='return all games for all players in that season')
    parser.add_argument('--output', '-o', default=OUTPUT_FILE)
    return parser.parse_args()


def game_log(player_id: int, season: int) -> dict:
    season_format = format_season(season)
    return GameLogs(player_id, season=season_format).api.json['resultSets'][0]


def run(player_id: int, season: int, outfile) -> None:
    logging.info(f"getting game logs for: {player_id}")
    game_logs = game_log(player_id, season)
    logging.info(f"outputting {game_logs}")
    output(game_logs, outfile)


if __name__ == '__main__':
    args = parse()

    with open(args.output, 'a') as outfile:
        if args.all:
            players = player_list(args.season)
            for player in players:
                run(player, args.season, outfile)
        else:
            run(args.player_id, args.season, outfile)
