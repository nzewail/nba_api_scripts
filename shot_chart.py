#!usr/bin/python3

from nbapy.shot_chart import ShotChart
import logging
from utils import output, format_season, TODAY
import argparse

logging.getLogger().setLevel(logging.INFO)

OUTPUT_FILE = 'shot_charts_%s.json' % (TODAY)


def parse():
    parser = argparse.ArgumentParser(description='get all shot data for a given player in a given season')
    parser.add_argument('--player-id', type=int, required=True, help='player id from nba.com')
    parser.add_argument('--season', type=int, default=2020, help='beginning year of a season (i.e. 2020 for 2020-21 season)')
    parser.add_argument('--output', '-o', default=OUTPUT_FILE)
    return parser.parse_args()


def shot_chart(player_id: int, season: int) -> dict:
    formatted_season = format_season(season)
    logging.info(f'getting shots for {player_id} in {formatted_season}')
    shots = ShotChart(player_id, season=formatted_season)
    return shots.api.json['resultSets'][0]


def main():
    args = parse()
    shots = shot_chart(args.player_id, args.season)
    logging.info(f'outputting {len(shots["rowSet"])} shots')
    with open(args.output, 'w') as outfile:
        output(shots, outfile)


if __name__ == '__main__':
    main()
