import random

R, C = 10, 10

north_wall = [[1 for _ in range(C)] for _ in range(R)]
east_wall = [[1 for _ in range(C)] for _ in range(R)]

visited = [[False for _ in range(C)] for _ in range(R)]
sol_visited = [[False for _ in range(C)] for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def valid(x, y):
    return 0 <= x < R and 0 <= y < C


def remove_wall(a, b):
    ax, ay = a
    bx, by = b

    if ax == bx:
        if ay > by:
            east_wall[bx][by] = 0
        else:
            east_wall[ax][ay] = 0
    else:
        if ax > bx:
            north_wall[bx][by] = 0
        else:
            north_wall[ax][ay] = 0


def generate_maze(sx, sy):
    stack = []
    stack.append((sx, sy))
    visited[sx][sy] = True

    while stack:
        x, y = stack[-1]

        neighbors = []

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if valid(nx, ny) and not visited[nx][ny]:
                neighbors.append((nx, ny))

        if neighbors:
            nx, ny = random.choice(neighbors)

            remove_wall((x, y), (nx, ny))

            visited[nx][ny] = True
            stack.append((nx, ny))
        else:
            stack.pop()


def print_maze():
    for i in range(R):

        for j in range(C):
            print("+", end="")
            if north_wall[i][j]:
                print("---", end="")
            else:
                print("   ", end="")
        print("+")

        for j in range(C):
            if east_wall[i][j]:
                print("|", end="")
            else:
                print(" ", end="")
            print("   ", end="")
        print("|")

    for _ in range(C):
        print("+---", end="")
    print("+")


def solve(x, y):

    if x == R - 1 and y == C - 1:
        return True

    sol_visited[x][y] = True

    # UP
    if x > 0 and not north_wall[x - 1][y] and not sol_visited[x - 1][y]:
        if solve(x - 1, y):
            return True

    # DOWN
    if x < R - 1 and not north_wall[x][y] and not sol_visited[x + 1][y]:
        if solve(x + 1, y):
            return True

    # LEFT
    if y > 0 and not east_wall[x][y - 1] and not sol_visited[x][y - 1]:
        if solve(x, y - 1):
            return True

    # RIGHT
    if y < C - 1 and not east_wall[x][y] and not sol_visited[x][y + 1]:
        if solve(x, y + 1):
            return True

    return False


generate_maze(0, 0)

print("\n=== GENERATED MAZE ===\n")
print_maze()

print("\n=== SOLVING MAZE ===\n")

if solve(0, 0):
    print("Path found!")
else:
    print("No path found!")