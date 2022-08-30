from typing import Deque


def solve_puzzle(Board: list, Source: tuple, Destination: tuple):
    """Finds a solution to a 2-D puzzle using a breadth first search

    Parameters
    ----------
    Board : list
        A graph represented as an adjacency matrix
    Source : tuple
        The starting point on the board
    Destination : tuple
        The goal position
    """

    queue = Deque()
    queue.append(Source)
    visited = {}

    if is_valid(Source[0], Source[1], Board, visited):
        visited[Source] = 0
        if Source == Destination:
            return [Destination]
    else:
        return None

    while len(queue) > 0:
        r, c = queue.popleft()
        possible_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for move_row, move_col in possible_moves:
            row, col = r + move_row, c + move_col
            if is_valid(row, col, Board, visited):
                queue.append((row, col))
                visited[(row, col)] = visited[(r, c)] + 1
                if (row, col) == Destination:
                    return get_path(row, col, visited)

    return None


def is_valid(x: int, y: int, Board: list, visited: dict) -> bool:
    """Helper for solve_puzzle() to determine if a move is valid

    Parameters
    ----------
    x : int
        Row
    y : int
        Column
    Board : list
        A graph represented as an adjacency matrix
    visited : dict
        Coordinates that have been visited

    Returns
    -------
    bool
        True if the move is valid, otherwise False
    """

    exists = False
    valid = False

    if (x >= 0 and y >= 0) and (x < len(Board) and y < len(Board[0])):
        exists = True

    target = (x, y)
    if exists:
        if Board[x][y] != "#" and target not in visited:
            valid = True

    return valid and exists


def get_path(row: int, col: int, visited: dict) -> tuple:
    """Helper for solve_puzzle() to assemble the steps and moves into lists

    Parameters
    ----------
    row : int
        Row on the board
    col : int
        Column on the board
    visited : dict
        Coordinates that have been visited

    Returns
    -------
    tuple
        List of tuples containing coordinates traversed, and list of directions
    """

    steps = visited[(row, col)]
    steps -= 1
    path = [(row, col)]
    directions = []

    while steps >= 0:
        if (row - 1, col) in visited and visited[(row - 1, col)] == steps:
            path.append((row - 1, col))
            directions.append("D")
            row -= 1
        if (row + 1, col) in visited and visited[(row + 1, col)] == steps:
            path.append((row + 1, col))
            directions.append("U")
            row += 1
        if (row, col - 1) in visited and visited[(row, col - 1)] == steps:
            path.append((row, col - 1))
            directions.append("R")
            col -= 1
        if (row, col + 1) in visited and visited[(row, col + 1)] == steps:
            path.append((row, col + 1))
            directions.append("L")
            col += 1
        steps -= 1

    path.reverse()
    directions.reverse()
    return (path, directions)


# ------------------------------ Basic Testing --------------------------------#

if __name__ == "__main__":

    puzzle = [
        ["-", "-", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["#", "-", "#", "#", "-"],
        ["-", "#", "-", "-", "-"],
    ]

    source = (0, 2)
    destination = (2, 2)
    # source = (0, 0)
    # destination = (4, 4)
    result = solve_puzzle(puzzle, source, destination)
    print(result)
