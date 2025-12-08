from itertools import groupby


def solve(input_text: str) -> int:
    """Solve Day 6 Part 1: Numbers read horizontally, space-separated."""
    lines = input_text.strip().split('\n')
    rows = [line.split() for line in lines]
    columns = list(zip(*rows))
    
    grand_total = 0
    for column in columns:
        operator = column[-1]
        numbers = [int(n) for n in column[:-1]]
        
        if operator == '+':
            grand_total += sum(numbers)
        elif operator == '*':
            product = 1
            for num in numbers:
                product *= num
            grand_total += product
    
    return grand_total


def solve_part2(input_text: str) -> int:
    """
    Solve Day 6 Part 2: Numbers read vertically within each problem.
    
    - Read digit columns right-to-left within each problem
    - Read digits top-to-bottom to form each number
    - Problems separated by all-space columns
    - Operator (+/*) in bottom row
    """
    lines = input_text.strip().split('\n')
    
    max_line_length = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_line_length) for line in lines]
    
    operator_row = padded_lines[-1]
    digit_rows = padded_lines[:-1]
    
    # Mark each column as separator (all spaces) or part of a problem
    column_is_separator = [
        all(line[col] == ' ' for line in padded_lines)
        for col in range(max_line_length)
    ]
    columns_with_separator_flag = list(enumerate(column_is_separator))
    
    grand_total = 0
    
    # Group consecutive columns by separator status
    for is_separator, column_group in groupby(columns_with_separator_flag, key=lambda x: x[1]):
        if is_separator:
            continue
        
        problem_column_indices = [col_idx for col_idx, _ in column_group]
        
        # Find operator for this problem
        operator = None
        for col_idx in problem_column_indices:
            if operator_row[col_idx] in '+*':
                operator = operator_row[col_idx]
                break
        
        # Build numbers: read columns right-to-left, digits top-to-bottom
        numbers_in_problem = []
        for col_idx in reversed(problem_column_indices):
            vertical_digits = ''.join(
                row[col_idx] for row in digit_rows if row[col_idx].isdigit()
            )
            if vertical_digits:
                numbers_in_problem.append(int(vertical_digits))
        
        # Apply operator
        if operator == '+':
            grand_total += sum(numbers_in_problem)
        elif operator == '*':
            product = 1
            for num in numbers_in_problem:
                product *= num
            grand_total += product
    
    return grand_total
    
    return total


if __name__ == "__main__":
    # Read input from file
    with open(".\\day_6\\input_day_6.txt", "r") as f:
        input_text = f.read()
    
    print(f"Part 1: {solve(input_text)}")
    print(f"Part 2: {solve_part2(input_text)}")
