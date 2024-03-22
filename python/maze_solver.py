class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y


def walk(
    maze: list[str],
    wall: str,
    current: Point,
    end: Point,
    seen: list[list[bool]],
    path: list[Point],
) -> bool:
    directions = [
        [0, -1],
        [1, 0],
        [0, 1],
        [-1, 0],
    ]
    # Base cases
    # 1. Off the map
    if (
        current.x >= len(maze[0])
        or current.x < 0
        or current.y >= len(maze)
        or current.y < 0
    ):
        return False

    # 2. On a wall
    if maze[current.y][current.x] == wall:
        return False

    # 3. End
    if current.x == end.x and current.y == end.y:
        path.append(current)
        return True

    # 4. Seen
    if seen[current.y][current.x]:
        return False

    # Recursive cases
    # Pre
    seen[current.y][current.x] = True
    path.append(current)

    # Recurse

    for direction in directions:
        x, y = direction
        new_point = Point(current.x + x, current.y + y)
        if walk(maze, wall, new_point, end, seen, path):
            return True

    # Post
    path.pop()
    return False


initial_maze: list[str] = ["### ", "# # ", "# # ", "    ", "# ##", "#   ", "# ##"]
maze_start = Point(1, 6)
maze_end: Point = Point(3, 0)


def solve(
    maze: list[str],
    wall: str,
    start: Point,
    end: Point,
) -> list[Point]:
    seen: list[list[bool]] = [[False] * len(maze[0]) for _ in range(len(maze))]
    path: list[Point] = []

    walk(maze, wall, start, end, seen, path)

    return path


result = solve(initial_maze, "#", maze_start, maze_end)

for values in result:
    print("x", values.x)
    print("y", values.y)
