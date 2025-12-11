from itertools import combinations
import math


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # [0, 1, 2, 3, 4, ...]
        self.size = [1] * n  # [1, 1, 1, 1, 1, ...]

    def _find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # Path compression
            x = self.parent[x] # Move up the chain
        return x

    def union(self, box_one, box_two):
        leader_one = self._find(box_one)
        leader_two = self._find(box_two)
        if leader_one == leader_two:
            return False
        if self.size[leader_one] < self.size[leader_two]:
            self.parent[leader_one] = leader_two
            self.size[leader_two] += self.size[leader_one]
        else:
            self.parent[leader_two] = leader_one
            self.size[leader_one] += self.size[leader_two]
        return True


def extract_sorted_coordinates(input_text):
    # Store all the boxes
    boxes = []
    for line in input_text.strip().split('\n'):
        x, y, z = map(int, line.split(','))
        boxes.append((x, y, z))
    
    # Generate all unique pairs with their distances
    pairs = []
    for first_box, second_box in combinations(range(len(boxes)), 2):
        distance = math.dist(boxes[first_box], boxes[second_box])
        pairs.append((distance, first_box, second_box))
    
    pairs.sort()

    return boxes, pairs, UnionFind(len(boxes))


def part1(boxes, pairs, uf) -> int:
    """
    Solve the Day 8 puzzle.
    
    Args:
        input_text: The puzzle input
    """
    for _, box_one, box_two in pairs[:1000]:
        uf.union(box_one, box_two)
    
    circuit_sizes = []
    for i in range(len(boxes)):
        if uf.parent[i] == i: # This box is the leader of its circuit
            circuit_sizes.append(uf.size[i])
    
    circuit_sizes.sort(reverse=True)
    return circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]


def part2(boxes, pairs, uf) -> int:
    """
    Solve the Day 8 puzzle part 2.
    
    Args:
        input_text: The puzzle input
    """

    for _, box_one, box_two in pairs:
        if uf.union(box_one, box_two):
            pass
    
    circuit_sizes = []
    for i in range(len(boxes)):
        if uf.parent[i] == i: # This box is the leader of its circuit
            circuit_sizes.append(uf.size[i])
    
    circuit_sizes.sort(reverse=True)
    return circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]


if __name__ == "__main__":
    # Read input from file
    with open(".\\day_8\\input_day_8.txt", "r") as f:
        input_text = f.read()
    boxes, pairs, uf = extract_sorted_coordinates(input_text)
    print(f"Part 1: {part1(boxes, pairs, uf)}")
    print(f"Part 2: {part2(boxes, pairs, uf)}")
