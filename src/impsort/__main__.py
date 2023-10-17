from __future__ import annotations

from io import TextIOWrapper

import impsort.parser as parser
from impsort.sort import sort_imports
from impsort.load import read_top_imports


def main():
    args = parser.parse_args()

    if args.command == "sort":
        sort_command(args.fp)


def sort_command(fp: TextIOWrapper) -> None:
    with fp:
        for imp in sort_imports(read_top_imports(fp)):
            print(imp)


if __name__ == "__main__":
    main()
