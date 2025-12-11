def solve(coordinates: list) -> int:
    """
    Solve the Day 9 puzzle.
    
    Args:
        coordinates: The list of coordinates
    """
    max_area = 0
    input_length = len(coordinates)
    for i in range(input_length): # Get first set of coordinates
        for j in range(i + 1, input_length): # Get second set of coordinates
            x1, y1 = coordinates[i] # first corner of first coordinate
            x2, y2 = coordinates[j] # second corner (opposite corner) of second coordinate
            # +1 as tiles are inclusive
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1

            area = width * height

            max_area = max(max_area, area)
    return max_area

def get_coordinates(input_text: str):
    # Store all the coordinates
    coordinates = []
    for line in input_text.strip().split('\n'):
        x, y = map(int, line.split(','))
        coordinates.append((x, y))
    return coordinates


if __name__ == "__main__":
    # Read input from file
    with open(".\\day_9\\input_day_9.txt", "r") as f:
        input_text = f.read()
    coordinates = get_coordinates(input_text)
    print(f"Part 1: {solve(coordinates)}")
