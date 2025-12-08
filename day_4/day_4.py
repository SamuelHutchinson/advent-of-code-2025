# 8 directions: up, down, left, right, and 4 diagonals
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1)]


def parse_grid(input_text: str) -> list[list[str]]:
    """Parse input into a 2D array (list of lists)."""
    return [list(line) for line in input_text.strip().split('\n')]


def find_accessible_rolls(grid: list[list[str]]) -> list[tuple[int, int]]:
    """
    Find all paper rolls that can be accessed by a forklift.
    A roll is accessible if it has fewer than 4 neighboring rolls.
    
    Returns:
        List of (row, col) positions of accessible rolls.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    accessible = []
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '@':
                # Count neighboring paper rolls
                neighbor_count = 0
                for row_offset, col_offset in DIRECTIONS:
                    neighbor_row = row + row_offset
                    neighbor_col = col + col_offset
                    
                    # Check if neighbor is within grid bounds
                    is_valid_row = 0 <= neighbor_row < rows
                    is_valid_col = 0 <= neighbor_col < cols
                    
                    if is_valid_row and is_valid_col:
                        # Check if neighbor is a paper roll
                        if grid[neighbor_row][neighbor_col] == '@':
                            neighbor_count += 1
                
                # Forklift can access if fewer than 4 neighboring rolls
                if neighbor_count < 4:
                    accessible.append((row, col))
    
    return accessible


def solve_part1(input_text: str) -> int:
    """
    Solve Day 4 Part 1: Count rolls accessible in initial state.
    
    Args:
        input_text: The puzzle input
    """
    grid = parse_grid(input_text)
    return len(find_accessible_rolls(grid))


def solve_part2(input_text: str) -> int:
    """
    Solve Day 4 Part 2: Count total rolls removed via batch removal.
    
    Args:
        input_text: The puzzle input
    """
    grid = parse_grid(input_text)
    total_removed = 0
    
    while True:
        # Find all accessible rolls in this pass
        to_remove = find_accessible_rolls(grid)
        
        # If nothing to remove, we're done
        if not to_remove:
            break
        
        # Remove all accessible rolls from the grid
        for row, col in to_remove:
            grid[row][col] = '.'
        
        total_removed += len(to_remove)
    
    return total_removed


if __name__ == "__main__":
    # Read input from file
    with open(".\\day_4\\input_day_4.txt", "r") as f:
        input_text = f.read()
    
    print(f"Part 1: {solve_part1(input_text)}")
    print(f"Part 2: {solve_part2(input_text)}")