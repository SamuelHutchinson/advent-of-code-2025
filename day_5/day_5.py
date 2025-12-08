def solve(input_text: str) -> int:
    """
    Solve the Day 5 puzzle.
    
    Args:
        input_text: The puzzle input
    """
    # Split input into ranges section and ingredient IDs section
    sections = input_text.strip().split("\n\n")
    ranges_section = sections[0]
    ids_section = sections[1]
    
    # Parse ranges
    ranges = []
    for line in ranges_section.split("\n"):
        start, end = line.split("-")
        ranges.append((int(start), int(end)))
    
    # Parse ingredient IDs
    ingredient_ids = [int(line) for line in ids_section.split("\n")]
    
    # Count fresh ingredients
    fresh_count = 0
    for ingredient_id in ingredient_ids:
        # Check if this ID falls within any range
        for start, end in ranges:
            if start <= ingredient_id <= end:
                fresh_count += 1
                break  # No need to check other ranges once we find a match
    
    return fresh_count


def solve_part_2(input_text: str) -> int:
    """
    Solve Part 2 of the Day 5 puzzle.
    
    Args:
        input_text: The puzzle input
    """
    # Split input into ranges section and ingredient IDs section
    sections = input_text.strip().split("\n\n")
    ranges_section = sections[0]
    
    # Parse ranges
    ranges = []
    for line in ranges_section.split("\n"):
        start, end = line.split("-")
        ranges.append((int(start), int(end)))
    
    # Sort ranges by start value
    ranges.sort(key=lambda x: x[0])
    
    # Merge overlapping/adjacent ranges
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            # Overlaps or is adjacent to the last merged range - extend it
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            # No overlap - add as new range
            merged.append((start, end))
    
    # Count total unique IDs across all merged ranges
    total = 0
    for start, end in merged:
        total += end - start + 1
    
    return total


if __name__ == "__main__":
    # Read input from file
    with open(".\\day_5\\input_day_5.txt", "r") as f:
        input_text = f.read()
    
    print(f"Part 1: {solve(input_text)}")
    print(f"Part 2: {solve_part_2(input_text)}")
