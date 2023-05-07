import argparse
import sys
from . import rl, web


__version__ = "0.1.0"
__all__ = [
    "main",
    "rl",
    "web",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="rl",
        description="Fix broken links in a URL",
    )
    subparser = parser.add_subparsers(dest="command")
    subparser.required = True
    subparser.add_parser("version", help="Print current version")
    subparser.add_parser("web", help="Run the web server")
    subparser.add_parser("fix", help="Fix broken links in some content")

    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == "version":
        print(__version__)
    elif args.command == "web":
        web.app.run(debug=True)
    elif args.command == "fix":
        content = sys.stdin.read()
        print(rl.fix_generic(content))
