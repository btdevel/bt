class Vector(list):
    def __add__(self, other):
        assert isinstance(other, list)
        return Vector(map(int.__add__, self, other))
    def __radd__(self, other):
        assert isinstance(other, list)
        return Vector(map(int.__add__, self, other))
    def __mul__(self, other):
        assert isinstance(other, int)
        return Vector(map(lambda x: other * x, self))
    def __rmul__(self, other):
        assert isinstance(other, int)
        return Vector(map(lambda x: other * x, self))


_left = lambda dir: (dir + 1) % 4
_reverse = lambda dir: (dir + 2) % 4
_right = lambda dir: (dir + 3) % 4
class Direction():
    NORTH = 0
    WEST = 1
    SOUTH = 2
    EAST = 3
    vectors = map(Vector, [[0, 1], [-1, 0], [0, -1], [1, 0]])
    names = ["north", "west", "south", "east"]

    def __init__(self, dir=NORTH):
        self.dir = dir

    def __str__(self):
        return Direction.names[self.dir]

    def left(self):
        self.dir = _left(self.dir)

    def reverse(self):
        self.dir = _reverse(self.dir)

    def right(self):
        self.dir = _right(self.dir)

    @property
    def forward_vec(self):
        return Direction.vectors[self.dir]
    @property
    def left_vec(self):
        return Direction.vectors[_left(self.dir)]
    @property
    def right_vec(self):
        return Direction.vectors[_right(self.dir)]

