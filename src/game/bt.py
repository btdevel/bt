from math import pi, sin, cos

from direct.showbase.DirectObject import DirectObject
from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from panda3d.core import lookAt
from panda3d.core import GeomVertexFormat, GeomVertexData
from panda3d.core import Geom, GeomTriangles, GeomVertexWriter
from panda3d.core import Texture, TextureStage, GeomNode, NodePath
from panda3d.core import PerspectiveLens
from panda3d.core import CardMaker
from panda3d.core import Light, Spotlight, PointLight, AmbientLight
from panda3d.core import TextNode
from panda3d.core import Vec3, Vec4, Point3, Material
import sys, os
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence

from pd import makeSquare, makeCube


OPEN = 0
DOOR = 1
SDOOR = 2
WALL = 3

def pos2vec(pos):
    return Point3(pos[0]*2, pos[1]*2, 0)


def make_map():
    class cell(object):
        pass

    level = __import__("level11")
    #level = __import__("level02")
    print level.dungeon_name
    #print level.map

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
    #cells[0][1].teleport = (1, 10)
        

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
            

def make_level(render):
    map = make_map()

    from direct.showbase.Loader import Loader
    tex=Loader("foo").loadTexture("BrickOldSharp0216_2_thumbhuge.jpg")
    tex=Loader("foo").loadTexture("BrickOldDirty0108_5_thumbhuge.jpg")
    tex=Loader("foo").loadTexture("BrickOldSharp0215_2_thumbhuge.jpg")
    nor=Loader("foo").loadTexture("BrickOldSharp0215_2_thumbhuge-n.jpg")

    ts = TextureStage('ts')
    ts.setMode(TextureStage.MNormal)

    for i in range(0,22,1):
        x = i * 2.0
        for j in range(0,22,1):
            y = j * 2.0

            hideset = set()
            #hideset.add(5)
            cell = map[i][j]
            if cell.north == OPEN: hideset.add(2)
            if cell.west == OPEN: hideset.add(3)
            if cell.south == OPEN: hideset.add(0)
            if cell.east == OPEN: hideset.add(1)

            xcube = makeCube(inverse=True, hide=hideset)
            cube = NodePath(xcube)
            cube.setTexture(tex)
            cube.setTexture(ts,nor)
            cube.reparentTo(render)
            cube.setPos(x, y, 0 )

            myMaterial = Material()
            myMaterial.setShininess(0.0)
            myMaterial.setAmbient(Vec4(0,0,0,1))
            myMaterial.setEmission(Vec4(0.0,0.0,0.0,1))
            myMaterial.setDiffuse(Vec4(0.2,0.2,0.2,1))
            myMaterial.setSpecular(Vec4(0.5,0.5,0.5,1))
            cube.setMaterial(myMaterial)


from movement import Direction, Vector
class App(ShowBase):
    def __init__(self):

        ShowBase.__init__(self)
        self.disableMouse()
        self.camera.setPos(10, -80, 70)
        self.camera.lookAt(10, 20, 0)
        self.camLens.setFov(90.0)
        self.camLens.setNear(0.01)
        self.camLens.setFar(100)
        self.setBackgroundColor(Vec4(0, 0, 0, 0))
        

        make_level(self.render)

        self.accept("escape", exit)
        self.accept("arrow_up", self.forward)
        self.accept("arrow_down", self.reverse)
        self.accept("arrow_left", self.turn_left)
        self.accept("arrow_right", self.turn_right)

        self.accept("1", self.set_camera_in)
        self.accept("2", self.set_camera_out)
        self.accept("3", self.spin_camera_left)
        self.accept("4", self.spin_camera_right)

        self.accept("s", self.toggle_smoke)

        title = OnscreenText(text="Bard's Tale I",
                             style=1, fg=(1,1,1,1),
                             pos=(0.7,0.92), scale = .07)

        self.dir = Direction()
        self.pos = Vector([0, 0])
        self.map = make_map()

        slight = PointLight('slight')
        slight.setColor(Vec4(1, 1, 1, 1))
        slnp = render.attachNewNode(slight)
        slight.setAttenuation((1, 0, 0.02))
        render.setLight(slnp)
        self.slight = slight
        self.light = slnp

        alight = AmbientLight('alight')
        amb = 0.05
        alight.setColor((amb, amb, amb, 1))
        alnp = render.attachNewNode(alight)
        self.alight = alight
        render.setLight(alnp)

        text = TextNode("foo")
        text.setText("")
        text.setShadow(0.2,0.2)
        text.setShadowColor(0, 0, 0, 1)
        tn = NodePath(text)
        tn.setScale(0.1)
        tn.reparentTo(aspect2d)
        tn.setPos(-1, -1, 0)
        self.text = text

        #render.setShaderAuto()

        from panda3d.core import AntialiasAttrib
        self.render.setAntialias(AntialiasAttrib.MMultisample)

        self.follow = True
        self.set_camera()


    def spin_camera_right(self, degrees=360, time=1.0):
        s = self.dir.dir * 90.0
        self.camera.hprInterval(time, Point3(s, 0, 0), 
                                startHpr=Point3(s+degrees, 0, 0)).start()
    def spin_camera_left(self, degrees=360, time=1.0):
        s = self.dir.dir * 90.0
        self.camera.hprInterval(time, Point3(s, 0, 0), 
                                startHpr=Point3(s-degrees, 0, 0)).start()

    def set_camera(self):
        #print self.pos, self.dir
        pos = pos2vec(self.pos)
        dir = pos2vec(self.dir.forward_vec)
        
        #print pos
        #print pos+dir
        if self.follow:
            self.camera.setPos(pos)
            #self.camera.setPos(Point3(pos-dir*0.5))
            self.camera.setPos(Point3(pos))
            self.camera.lookAt(Point3(pos+dir))
            self.camLens.setFov(90.0)
            self.camLens.setFov(110.0)
            print "Foooo", pos
        print "Bar"
        self.light.setPos(Point3(pos))


    def set_camera_out(self):
        self.camera.setPos(21, -40, 30)
        self.camera.lookAt(21, 20, 0)
        self.camLens.setFov(60.0)
        self.follow = False

    def set_camera_in(self):
        self.follow = True
        self.set_camera()

    def moved(self):
        x, y = self.pos[0], self.pos[1]
        cell = self.map[x][y]
        msg = cell.msg
        if msg:
            print ">", x, y, msg
            self.text.setText(msg)
            self.text.setWordwrap(10)
        else:
            self.text.setText("")

        if cell.spinner:
            self.spin_camera_left(degrees=3*360, time=1.0)
        if cell.teleport:
            self.newpos = Vector(cell.teleport)
            self.taskMgr.add(self.flashTask, "FlashTask")
            

    def forward(self):
        x, y = self.pos[0], self.pos[1]
        cell = self.map[x][y]
        if self.map[x][y].walls[self.dir.dir]!=WALL:
            self.pos = self.pos + self.dir.forward_vec
            time = 0.1
            self.camera.posInterval(time, pos2vec(self.pos)).start()
            self.light.posInterval(time, pos2vec(self.pos)).start()
            self.moved()

    def reverse(self):
        self.dir.reverse()
        if self.map[self.pos[0]][self.pos[1]].walls[self.dir.dir]!=WALL:
            self.pos = self.pos + self.dir.forward_vec
            time = 0.3
            self.camera.posInterval(time, pos2vec(self.pos)).start()
            self.light.posInterval(time, pos2vec(self.pos)).start()
            self.moved()
        self.dir.reverse()

    def turn_left(self):
        self.dir.left()
        self.set_camera()
        self.spin_camera_left(degrees=90, time=0.2)

    def turn_right(self):
        self.dir.right()
        self.set_camera()
        self.spin_camera_right(degrees=90, time=0.2)

    def toggle_smoke(self):
        from panda3d.core import Fog
        if self.render.getFog():
            self.render.clearFog()
        else:
            smoke = Fog("smoke")
            smoke.setColor(0.3, 0.3, 0.3)
            smoke.setExpDensity(1)
            render.setFog(smoke)

 
    # Define a procedure to move the camera.
    def flashTask(self, task):
        amb1 = 1.0
        amb2 = 0.0
        dt = 0.15
        ret = task.cont
        if task.time<dt:
            amb = amb1 + (amb2-amb1) * task.time/dt
        elif task.time<2*dt:
            if self.newpos:
                print "FOOOO", self.pos, self.newpos
                self.pos = self.newpos
                self.newpos = None
                self.set_camera()

            amb = amb2 + (amb1-amb2) * (task.time-dt)/dt
        else:
            amb = amb1
            ret = None
        self.slight.setColor((amb, amb, amb, 1))
        return ret

app=App()
app.run()





