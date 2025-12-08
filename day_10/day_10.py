def solve(input_text: str) -> int:
    """
    Solve the Day 10 puzzle.
    
    Args:
        input_text: The puzzle input
    """
    pass


if __name__ == "__main__":
    # Read input from file
    with open(".\\day_10\\input_day_10.txt", "r") as f:
        input_text = f.read()
    
    print(f"Part 1: {solve(input_text)}")
