from __future__ import annotations

from io import TextIOWrapper
from argparse import ArgumentParser, Namespace, _SubParsersAction, FileType

import impsort.const as const


class Arguments(Namespace):
    fp: TextIOWrapper


def parse_args() -> Arguments:
    parser = ArgumentParser(const.NAME)

    parser.add_argument("-v", "--version", action="version", version=const.VERSION)

    subp = parser.add_subparsers(required=True, dest="command")

    _sort_parser(subp)

    return parser.parse_args()


def _sort_parser(subp: _SubParsersAction[ArgumentParser]) -> None:
    parser = subp.add_parser("sort", help="Sort imports of a file")

    parser.add_argument("fp", metavar="FILE", type=FileType("r", encoding="utf8"))

