# NBA API Scripts

These are scripts that were initially used to populate a database that I was using for a now defunct basketball stats sites.
I changed them to instead output to json files that can be used for different purposes (including populating into a database).

Initially I was using the [nba_py](https://github.com/seemethere/nba_py) library but have now found it to be unsupported so migrated to the [nbapy](https://github.com/jtpavlock/nbapy) library which is being maintained.

The NBA stats API isn't the most well documented so I have found using these client libraries to be helpful in navigating it.

## Requirements

```
pip3 install -r requirements.txt
```

## Scripts

Just note that these scripts are written to only pull regular season stats and not playoff or preseason stats. Also generally the `--all` option will take a lot longer given that it will have to circle through about 500 API requests because it is cycling through every player.  

### `players.py`

```
python3 players.py --help
usage: players.py [-h] [--season SEASON] [--active ACTIVE] [--output OUTPUT]

return basic information on every nba player for a given season

optional arguments:
  -h, --help            show this help message and exit
  --season SEASON       beginning year of a season (i.e. 2020 for 2020-21
                        season)
  --active ACTIVE       must be 0 or 1
  --output OUTPUT, -o OUTPUT
```

### `player_seasons.py`

```
python3 player_seasons.py --help
usage: player_seasons.py [-h] [--player-id PLAYER_ID] [--all]
                         [--output OUTPUT]

get season stats for a given player from nba.com

optional arguments:
  -h, --help            show this help message and exit
  --player-id PLAYER_ID
                        player id from nba.com
  --all                 get all players for current season
  --output OUTPUT, -o OUTPUT
```

### `player_game_logs.py`

```
python3 player_game_logs.py --help
usage: player_game_logs.py [-h] [--season SEASON] [--player-id PLAYER_ID]
                           [--all] [--output OUTPUT]

return stats for every game a player has played in a given season

optional arguments:
  -h, --help            show this help message and exit
  --season SEASON       beginning year of a season (i.e. 2020 for 2020-21
                        season)
  --player-id PLAYER_ID
                        player id from nba.com
  --all                 return all games for all players in that season
  --output OUTPUT, -o OUTPUT
```

### `shot_chart.py`

```
python3 shot_chart.py --help
usage: shot_chart.py [-h] --player-id PLAYER_ID [--season SEASON]
                     [--output OUTPUT]

get all shot data for a given player in a given season

optional arguments:
  -h, --help            show this help message and exit
  --player-id PLAYER_ID
                        player id from nba.com
  --season SEASON       beginning year of a season (i.e. 2020 for 2020-21
                        season)
  --output OUTPUT, -o OUTPUT
```
