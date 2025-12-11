from itertools import combinations
import math


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # [0, 1, 2, 3, 4, ...]
        self.size = [1] * n  # [1, 1, 1, 1, 1, ...]

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # Path compression
            x = self.parent[x] # Move up the chain
        return x

    def union(self, box_one, box_two):
        leader_one = self.find(box_one)
        leader_two = self.find(box_two)
        if leader_one == leader_two:
            return False
        if self.size[leader_one] < self.size[leader_two]:
            self.parent[leader_one] = leader_two
            self.size[leader_two] += self.size[leader_one]
        else:
            self.parent[leader_two] = leader_one
            self.size[leader_one] += self.size[leader_two]
        return True


def paired_boxes(input_text):
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
    
    pairs.sort() # Uses the distance variable for sorting

    return boxes, pairs, UnionFind(len(boxes))


def part1(input_text: str) -> int:
    """
    Solve the Day 8 puzzle.
    
    Args:
        input_text: The puzzle input
    """
    boxes, pairs, uf = paired_boxes(input_text)
    
    for _, box_one, box_two in pairs[:1000]:
        uf.union(box_one, box_two)
    
    circuit_sizes = []
    for i in range(len(boxes)):
        if uf.parent[i] == i: # This box is the leader of its circuit
            circuit_sizes.append(uf.size[i])
    
    circuit_sizes.sort(reverse=True)
    return circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]


def part2(input_text: str) -> int:
    """
    Solve the Day 8 puzzle part 2.
    
    Args:
        input_text: The puzzle input
    """
    
    boxes, pairs, uf = paired_boxes(input_text)

    for _, box_one, box_two in pairs:
        if uf.union(box_one, box_two):
            leading_box = uf.find(box_one)
            # If the leading box's group contains all boxes,
            # then that means all boxes but one are connected,
            # leaving the last two junction boxes to connect,
            # so multiply the x coordinates of those two boxes.
            if uf.size[leading_box] == len(boxes):
                return boxes[box_one][0] * boxes[box_two][0] # Multiply together the x coordinates


if __name__ == "__main__":
    # Read input from file
    with open(".\\day_8\\input_day_8.txt", "r") as f:
        input_text = f.read()

    print(f"Part 1: {part1(input_text)}")
    print(f"Part 2: {part2(input_text)}")
