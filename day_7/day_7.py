def solve(input_text: str) -> int:
    """
    Solve the Day 7 puzzle.
    
    Args:
        input_text: The puzzle input
    """
    grid = [list(line) for line in input_text.strip().split('\n')]
    rows = len(grid)
    columns = len(grid[0])

    # Find 'S'
    start_row, start_column = next(
        (r, c)
        for r in range(rows)
        for c in range(columns)
        if grid[r][c] == 'S'
    )

    # Begin searching from 'S'
    timelines = {(start_row, start_column): 1}
    seen = set() # track beams already placed
    splits = 0
    timelines_finished = 0

    while timelines:
        new_timelines = {}
        for (beam_row, beam_column), timeline_count in timelines.items():
            # Move down a row
            new_row = beam_row + 1
            
            # Check if beam falls outside the grid
            if not (0 <= new_row < rows and 0 <= beam_column < columns):
                timelines_finished += timeline_count
                continue

            if grid[new_row][beam_column] == '^':
                # Split beam at the splitter
                if (beam_row, beam_column) not in seen:
                    splits += 1
                    seen.add((beam_row, beam_column))
                left_position = (new_row, beam_column - 1)
                right_position = (new_row, beam_column + 1)
                new_timelines[left_position] = new_timelines.get(left_position, 0) + timeline_count
                new_timelines[right_position] = new_timelines.get(right_position, 0) + timeline_count
            else:
                # Continue placing beams downwards
                new_positon = (new_row, beam_column)
                new_timelines[new_positon] = new_timelines.get(new_positon, 0) + timeline_count
        timelines = new_timelines
    return splits, timelines_finished


if __name__ == "__main__":
    # Read input from file
    with open(".\\day_7\\input_day_7.txt", "r") as f:
        input_text = f.read()
    
    part1, part2 = solve(input_text)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")