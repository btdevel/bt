OPEN = 0
DOOR = 1
SDOOR = 2
WALL = 3


def load_level(filename):
    class cell(object):
        pass

    level = __import__(filename)
    print level.dungeon_name

    map = list(reversed(level.map))

    char_map = {" ": OPEN, "D": DOOR, "S": SDOOR, "|": WALL, "-": WALL}

    cells = [[cell() for i in range(22)] for j in range(22)]
    for i in range(22):
        for j in range(22):
            cell = cells[i][j]
            cell.walls = {}
            cell.msg = None
            cell.spinner = False
            cell.teleport = None
            cell.east  = char_map[map[3*j+1][3*i+2]]
            cell.west  = char_map[map[3*j+1][3*i+0]]
            cell.north = char_map[map[3*j+2][3*i+1]]
            cell.south = char_map[map[3*j+0][3*i+1]]
            cell.walls[Direction.NORTH] = cell.north
            cell.walls[Direction.EAST] = cell.east
            cell.walls[Direction.WEST] = cell.west
            cell.walls[Direction.SOUTH] = cell.south

    for (y, x), msg in level.messages:
        cells[x][y].msg = msg

    for y, x in level.spinners:
        cells[x][y].spinner = True

    for (y, x), (yt, xt) in level.teleports:
        cells[x][y].teleport = (xt, yt)
        print (x, y), (xt, yt)
    cells[0][1].teleport = (1, 5)
        

    if level.dungeon_name == "Cellars":
        assert cells[0][0].east == OPEN
        assert cells[0][0].north == OPEN
        assert cells[0][0].south == WALL
        assert cells[0][0].west == WALL

        assert cells[0][1].east == OPEN
        assert cells[0][1].north == WALL
        assert cells[0][1].south == OPEN
        assert cells[0][1].west == WALL

        assert cells[1][0].east == WALL
        assert cells[1][0].north == OPEN
        assert cells[1][0].south == WALL
        assert cells[1][0].west == OPEN

        assert cells[1][1].east == OPEN
        assert cells[1][1].north == OPEN
        assert cells[1][1].south == OPEN
        assert cells[1][1].west == OPEN

        assert cells[2][5].east == WALL
        assert cells[2][5].north == WALL
        assert cells[2][5].south == OPEN
        assert cells[2][5].west == DOOR
    return cells
            



from movement import Direction, Vector
