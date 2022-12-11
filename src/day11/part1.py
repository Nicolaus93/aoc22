# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from aocd.models import Puzzle
import utils


@dataclass
class Monkey:
    items: list[int] = field(default_factory=list)
    divisible_by: int = None
    if_true: int = None
    if_false: int = None
    op: str = ""

    def operation(self, old):
        return eval(self.op)


@utils.timeit
def solve(rounds, input_f=None):
    if not input_f:
        puzzle = Puzzle(year=2022, day=11)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()

    monkeys = []
    for line in data:
        if line.startswith("Monkey"):
            monkey = Monkey()
            monkeys.append(monkey)
        elif line.startswith("  Starting items"):
            items = utils.read_ints(line)
            monkey.items = items
        elif line.strip().startswith("Operation"):
            ops = line.strip().split(":")[1]
            ops = ops.split("=")[1]
            monkey.op = ops
        elif line.strip().startswith("Test"):
            divisible_by = utils.read_ints(line)[0]
            monkey.divisible_by = divisible_by
        elif line.strip().startswith("If true"):
            monkey.if_true = utils.read_ints(line)[0]
        elif line.strip().startswith("If false"):
            monkey.if_false = utils.read_ints(line)[0]
        else:
            continue

    num = 1
    for m in monkeys:
        num *= m.divisible_by

    times = [0] * len(monkeys)
    for round_ in range(rounds):
        for pos, monkey in enumerate(monkeys):
            while monkey.items:
                item = monkey.items.pop()
                new = monkey.operation(item)
                if rounds == 20:
                    new = new // 3
                new = new % num
                if new % monkey.divisible_by == 0:
                    monkeys[monkey.if_true].items.append(new)
                else:
                    monkeys[monkey.if_false].items.append(new)
                times[pos] += 1

    first, second = sorted(times, reverse=True)[:2]
    return first * second


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    res = solve(20, "test.txt")
    print("test answer: ", res)

    # real puzzle
    print("--------------Part 1--------------")
    res = solve(20)
    print("puzzle answer", res)

    # real puzzle
    print("--------------Part 2--------------")
    res = solve(10000)
    print("puzzle answer", res)
