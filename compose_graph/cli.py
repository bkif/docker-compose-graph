"""CLI for Docker Compose Graph."""

from __future__ import annotations

import argparse
from pathlib import Path
from compose_graph.parser import compose_to_mermaid


def main() -> int:
    parser = argparse.ArgumentParser(prog="compose-graph")
    parser.add_argument("compose_file")
    args = parser.parse_args()
    print(compose_to_mermaid(Path(args.compose_file).read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
