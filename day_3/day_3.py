def max_joltage(bank: str, keep: int) -> int:
    """
    Greedy monotonic stack approach to find the maximum joltage.
    Works for any number of digits to keep.
    """
    to_remove = len(bank) - keep
    stack = []

    for digit in bank:
        # While there are digits left to remove,
        # and the last digit in stack is less than the current digit,
        # pop it to make room for the larger digit
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    # Remove any remaining digits from the end if needed
    if to_remove > 0:
        stack = stack[:-to_remove]

    return int(''.join(stack))


def solve(input_text: str, keep: int) -> int:
    """Sum the maximum joltage from each bank, keeping 'keep' digits."""
    total = 0
    for line in input_text.strip().split('\n'):
        bank = line.strip()
        if bank:
            total += max_joltage(bank, keep)
    return total

if __name__ == "__main__":
    # Read input from file
    with open(".\\day_3\\input_day_3.txt", "r") as f:
        input_text = f.read()
    
    print(f"Part 1 - The Max Joltage is: {solve(input_text, keep=2)}")
    print(f"Part 2 - The Max Joltage is: {solve(input_text, keep=12)}")