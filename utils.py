#!usr/bin/python3

import json
from datetime import datetime

TODAY = datetime.today().isoformat()


def output(data: dict, file) -> None:
    json.dump(data, file)
    file.write('\n')


def format_season(season: int) -> str:
    return f"{str(season)}-{str(season + 1)[2:]}"
