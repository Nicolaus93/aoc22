# -*- coding: utf-8 -*-

from __future__ import annotations
from dataclasses import dataclass, field
from aocd.models import Puzzle
import utils


@dataclass
class Dir:
    name: str
    parent: Dir | None = None
    size: int = 0
    files: list[File] = field(default_factory=list)
    dirs: list[Dir] = field(default_factory=list)

    def __repr__(self, parent="", level=0):
        pattern = "|-"
        spacing = "  "
        parent += "\n" + spacing * level + f"{pattern}{self.name}"
        for d in self.dirs:
            parent += d.__repr__(level=level + 1)
        for f in self.files:
            parent += "\n" + spacing * (level + 1) + f"{pattern}{f.name}: {f.size}"
        return parent


@dataclass
class File:
    name: str
    size: int


@utils.timeit
def build_tree(input_f=None):
    if not input_f:
        puzzle = Puzzle(year=2022, day=7)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()

    root = Dir(name="/")
    cur_dir = root
    i = 0
    while i < len(data):
        line = data[i].strip()
        if line.startswith("$ cd"):
            if line.startswith("$ cd /"):
                cur_dir = root
            elif line.startswith("$ cd .."):
                cur_dir = cur_dir.parent
            else:
                args = line.split()
                new_dir = Dir(name=args[-1], parent=cur_dir)
                cur_dir.dirs.append(new_dir)
                cur_dir = new_dir
        elif line.startswith("$ ls"):
            pass
        else:
            args = line.split()
            if args[0] != "dir":
                new_file = File(name=args[-1], size=int(args[0]))
                cur_dir.files.append(new_file)

        i += 1
    return root


PART1 = 0
PART2 = dict()


def compute_size(cur_dir: Dir):
    global PART1, PART2
    for child_dir in cur_dir.dirs:
        cur_dir.size += compute_size(child_dir)
    for child_file in cur_dir.files:
        cur_dir.size += child_file.size

    if cur_dir.name not in PART2:
        PART2[cur_dir.name] = cur_dir.size
    else:
        i = 0
        new_name = f"{cur_dir.name}_{i}"
        while new_name in PART2:
            i += 1
            new_name = f"{cur_dir.name}_{i}"
        PART2[new_name] = cur_dir.size

    if cur_dir.size <= 100000:
        PART1 += cur_dir.size
    return cur_dir.size


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    # temp = build_tree("test.txt")
    temp = build_tree()
    print(temp)
    tot_size = compute_size(temp)
    print("PART1:", PART1)
    needed_space = 30000000
    sorted_by_size = sorted([v for v in PART2.values()])
    for v in sorted_by_size:
        if 70000000 - PART2["/"] + v > needed_space:
            print("PART2:", v)
            break
