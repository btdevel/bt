from math import pi, sin, cos

from direct.showbase.DirectObject import DirectObject
from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from panda3d.core import lookAt
from panda3d.core import GeomVertexFormat, GeomVertexData
from panda3d.core import Geom, GeomTriangles, GeomVertexWriter
from panda3d.core import Texture, GeomNode, NodePath
from panda3d.core import PerspectiveLens
from panda3d.core import CardMaker
from panda3d.core import Light, Spotlight, PointLight, AmbientLight
from panda3d.core import TextNode
from panda3d.core import Vec3, Vec4, Point3
import sys, os
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence

from pd import makeSquare, makeCube

def make_level(render):
    cube = NodePath(makeCube(inverse=True, hide=set([5])))
    for i in range(0,10):
        for j in range(0,10):
            c = render.attachNewNode("c")
            c.setPos((i-5)*3, (j-5)*3, -10 )
            cube.instanceTo(c)


OPEN = 0
DOOR = 1
SDOOR = 2
WALL = 3



def make_map():
    class cell(object):
        pass

    level = __import__("level00")
    print level.dungeon_name
    print level.map

    map = level.map
    map.reverse()
    import sys
    sys.modules.pop(level.__name__)


    char_map = {" ": OPEN, "D": DOOR, "S": SDOOR, "|": WALL, "-": WALL}


    cells = [[cell() for i in range(22)] for j in range(22)]
    for i in range(22):
        for j in range(22):
            cell = cells[i][j]
            cell.walls = {}
            cell.east  = char_map[map[3*j+1][3*i+2]]
            cell.west  = char_map[map[3*j+1][3*i+0]]
            cell.north = char_map[map[3*j+2][3*i+1]]
            cell.south = char_map[map[3*j+0][3*i+1]]
            cell.walls[Direction.NORTH] = cell.north
            cell.walls[Direction.EAST] = cell.east
            cell.walls[Direction.WEST] = cell.west
            cell.walls[Direction.SOUTH] = cell.south

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
            

def make_level(render):
    map = make_map()

    for i in range(0,22,1):
        x = i * 2.0
        for j in range(0,22,1):
            y = j * 2.0

            hideset = set()
            hideset.add(5)
            cell = map[i][j]
            if cell.north == OPEN: hideset.add(2)
            if cell.west == OPEN: hideset.add(3)
            if cell.south == OPEN: hideset.add(0)
            if cell.east == OPEN: hideset.add(1)

            cube = NodePath(makeCube(inverse=True, hide=hideset))
            cube.reparentTo(render)
            cube.setPos(x, y, 0 )
            #cube.setTwoSided(True)

            #cube = NodePath(makeCube(inverse=False, hide=hideset))
            #cube.reparentTo(render) 
            #cube.setPos(x, y, 0 )
            #cube.setTwoSided(True)


from movement import Direction, Vector
class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.disableMouse()
        self.camera.setPos(10, -80, 70)
        self.camera.lookAt(10, 20, 0)
        self.camLens.setFov(90.0)
	self.win.setClearColor(Vec4(0,0,0,0))

	make_level(self.render)

        self.accept("escape", exit)
        self.accept("arrow_up", self.forward)
        self.accept("arrow_down", self.reverse)
        self.accept("arrow_left", self.turn_left)
        self.accept("arrow_right", self.turn_right)

        self.accept("1", self.set_camera)
        self.accept("2", self.set_camera_out)
        self.accept("3", self.spin_camera_left)
        self.accept("4", self.spin_camera_right)
		
        slight = PointLight('slight')
        slight.setColor(Vec4(1, 1, 1, 1))
        slnp = render.attachNewNode(slight)
	render.setLight(slnp)
	slnp.setPos(self.camera, 0, 0, 20)

	alight = AmbientLight('alight')
	alight.setColor((0.2, 0.2, 0.2, 1))
	alnp = render.attachNewNode(alight)
	render.setLight(alnp)

        title = OnscreenText(text="Bard's Tale I",
                             style=1, fg=(1,1,1,1),
                             pos=(0.7,0.92), scale = .07)

        self.dir = Direction()
        self.pos = Vector([0, 0])
        self.map = make_map()
        self.set_camera()


    def spin_camera_right(self, degrees=360):
        s = self.dir.dir * 90.0
        self.camera.hprInterval(1, Point3(s, 0, 0), 
                                startHpr=Point3(s+degrees, 0, 0)).start()
    def spin_camera_left(self, degrees=360):
        s = self.dir.dir * 90.0
        self.camera.hprInterval(1, Point3(s, 0, 0), 
                                startHpr=Point3(s-degrees, 0, 0)).start()

    def set_camera(self):
        print self.pos, self.dir
        def pos2vec(pos):
            return Point3(pos[0]*2, pos[1]*2, 0)
        pos = pos2vec(self.pos)
        dir = pos2vec(self.dir.forward_vec)
        
        print pos
        self.camera.setPos(pos)
        print pos+dir
        self.camera.setPos(Point3(pos-dir*0.5))
        self.camera.lookAt(Point3(pos+dir))


    def set_camera_out(self):
        self.camera.setPos(10, -80, 70)
        self.camera.lookAt(10, 20, 0)

    def forward(self):
        if self.map[self.pos[0]][self.pos[1]].walls[self.dir.dir]!=WALL:
            self.pos = self.pos + self.dir.forward_vec
            self.set_camera()

    def reverse(self):
        self.dir.reverse()
        self.set_camera()

    def turn_left(self):
        self.dir.left()
        self.set_camera()

    def turn_right(self):
        self.dir.right()
        self.set_camera()


app=App()
app.run()





