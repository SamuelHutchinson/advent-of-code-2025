from typing import Callable


def generate_invalid_ids_part1(start: int, end: int) -> list[int]:
    """Generate all invalid IDs (pattern repeated exactly twice) within the range."""
    invalid_ids = []
    
    min_digits = len(str(start))
    max_digits = len(str(end))
    
    # Only even-length numbers can be "repeated twice"
    for num_digits in range(min_digits, max_digits + 1):
        if num_digits % 2 != 0:
            continue
        
        pattern_len = num_digits // 2
        pattern_start = 10 ** (pattern_len - 1)
        pattern_end = 10 ** pattern_len
        
        for pattern in range(pattern_start, pattern_end):
            repeated_id = int(str(pattern) * 2)
            if start <= repeated_id <= end:
                invalid_ids.append(repeated_id)
    
    return invalid_ids


def generate_invalid_ids_part2(start: int, end: int) -> list[int]:
    """Generate all invalid IDs (pattern repeated 2+ times) within the range."""
    invalid_ids = set()  # Use set to avoid duplicates
    
    min_digits = len(str(start))
    max_digits = len(str(end))
    
    for num_digits in range(min_digits, max_digits + 1):
        # Try all pattern lengths that divide evenly into num_digits
        for pattern_len in range(1, num_digits // 2 + 1):
            if num_digits % pattern_len != 0:
                continue
            
            repeat_count = num_digits // pattern_len
            if repeat_count < 2:
                continue
            
            pattern_start = 10 ** (pattern_len - 1)
            pattern_end = 10 ** pattern_len
            print("size ", pattern_end - pattern_start)
            for pattern in range(pattern_start, pattern_end):
                repeated_id = int(str(pattern) * repeat_count)
                if start <= repeated_id <= end:
                    invalid_ids.add(repeated_id)
    
    return list(invalid_ids)


def solve(input_text: str, generator: Callable[[int, int], list[int]]) -> int:
    """Sum all invalid IDs in the given ranges using the provided generator."""
    total = 0
    for value in input_text.strip().split(','):
        start, end = map(int, value.split('-'))
        total += sum(generator(start, end))
    return total


if __name__ == "__main__":
    with open(".\\day_2\\input_day_2.txt", "r") as f:
        input_text = f.read()
    
    print(f"Part 1 - The sum of all invalid IDs: {solve(input_text, generate_invalid_ids_part1)}")
    print(f"Part 2 - The sum of all invalid IDs: {solve(input_text, generate_invalid_ids_part2)}")