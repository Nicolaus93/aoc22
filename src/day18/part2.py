# -*- coding: utf-8 -*-

from aocd.models import Puzzle
import utils
import numpy as np
from part1 import surface_area
from scipy.ndimage import binary_fill_holes


def get_exterior_voxels(voxels):
    dims: list[tuple[int, int]] = []
    for i in range(3):
        coords = sorted(voxels, key=lambda v: v[i])
        min_coord = coords[0][i]
        max_coord = coords[-1][i] + 1
        dims.append((min_coord, max_coord))

    shape = tuple(max_coord - min_coord for min_coord, max_coord in dims)
    boolgrid = np.zeros(shape=shape, dtype=bool)
    min_x = dims[0][0]
    min_y = dims[1][0]
    min_z = dims[2][0]
    for vox in voxels:
        x, y, z = vox
        boolgrid[x - min_x, y - min_y, z - min_z] = True

    filled = binary_fill_holes(boolgrid)
    return {tuple(v) for v in np.stack(np.where(filled)).T}


@utils.timeit
def solve(input_f=None):
    if not input_f:
        puzzle = Puzzle(year=2022, day=18)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()

    voxels = {tuple(utils.read_ints(line)) for line in data}
    voxels = get_exterior_voxels(voxels)
    return surface_area(voxels)


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    res = solve("test.txt")
    print("test answer: ", res)

    # real puzzle
    print("--------------PUZZLE--------------")
    res = solve()
    print("puzzle answer", res)
