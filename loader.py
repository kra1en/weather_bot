from utils import WebhookModel, PollingModel, parse_config
from storage import Storage
import argparse

from weather import WeatherService


__all__ = ['dp', 'engine', 'bot', 'storage', 'weather']

parser = argparse.ArgumentParser("main.py")

parser.add_argument("--mode", "-m", nargs=1,
                    help="Run the application in polling mode or webhook mode.",
                    default='polling',
                    choices=['polling', 'webhook']
                    )

parser.add_argument("--database", "-d", nargs=1,
                    help="Run the application with sqlite or postgres.",
                    default='sqlite',
                    choices=['sqlite', 'postgres']
                    )

parser.add_argument("--in-memory", action='store_true',
                    help="Run in-memory mode for sqlite.",
                    )

args = parser.parse_args()
cfg = parse_config('project.json')

weather = WeatherService()

storage = Storage(
    database=Storage.SQLITE if args.database == 'sqlite' else Storage.POSTGRESQL,
    in_memory=args.in_memory,
    source_file=cfg.src.file,
    db_name=cfg.db.sqlite.file if args.database == 'sqlite' else cfg.db.postgres.name,
    db_port=cfg.db.postgres.port
)


engine = WebhookModel() if 'webhook' == args.mode[0] else PollingModel()
memory_storage = engine.get_storage()
dp = engine.get_dispatcher()
bot = engine.get_bot()
