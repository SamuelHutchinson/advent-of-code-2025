def solve(input_text: str, count_all_clicks: bool = False) -> int:
    """
    Solve the safe dial puzzle.
    
    Args:
        input_text: The puzzle input with rotation instructions
        count_all_clicks: If False (Part 1), only count when dial ends at 0.
                         If True (Part 2), count every click that lands on 0.
    """
    position = 50
    zero_count = 0
    
    for line in input_text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        
        direction = line[0]
        distance = int(line[1:])
        step = -1 if direction == 'L' else 1
        
        if count_all_clicks:
            # Count every click that lands on 0
            for _ in range(distance):
                position = (position + step) % 100
                if position == 0:
                    zero_count += 1
        else:
            # Only count if we end at 0
            position = (position + step * distance) % 100
            if position == 0:
                zero_count += 1
    
    return zero_count


if __name__ == "__main__":
    # Read input from file
    with open(".\\day_1\\input_day_1.txt", "r") as f:
        input_text = f.read()
    
    print(f"Part 1 - The password is: {solve(input_text)}")
    print(f"Part 2 - The password is: {solve(input_text, count_all_clicks=True)}")