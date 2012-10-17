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
from direct.interval.IntervalGlobal import Sequence, Parallel

from pd import makeSquare, makeCube

from btimport import *

def white(s):
    return Vec4(s, s, s, 1)


class config(object):
    start_level = "level00"

    camera_angle = 110
    camera_angle = 90
    camera_angle = 170
    camera_angle_out = 60

    flash_time = 0.3
    move_time = 0.2

    smoke_color = white(0.1)
    smoke_exp_density = 1.0



def pos2vec(pos):
    return Point3(pos[0]*2, pos[1]*2, 0)

def render_level(map):
    from direct.showbase.Loader import Loader
    tex=Loader("foo").loadTexture("BrickOldSharp0215_2_thumbhuge.jpg")

    nor=Loader("foo").loadTexture("BrickOldSharp0215_2_thumbhuge-n.jpg")
    ts = TextureStage('ts')
    ts.setMode(TextureStage.MNormal)

    myMaterial = Material()
    myMaterial.setShininess(0.0)
    myMaterial.setAmbient(Vec4(0,0,0,1))
    myMaterial.setEmission(Vec4(0.0,0.0,0.0,1))
    myMaterial.setDiffuse(Vec4(0.2,0.2,0.2,1))
    myMaterial.setSpecular(Vec4(0.5,0.5,0.5,1))

    level_node = NodePath("level")
    for i in range(0,22,1):
        x = i * 2.0
        for j in range(0,22,1):
            y = j * 2.0

            hideset = set()
            cell = map[i][j]
            if cell.north == OPEN: hideset.add(2)
            if cell.west == OPEN: hideset.add(3)
            if cell.south == OPEN: hideset.add(0)
            if cell.east == OPEN: hideset.add(1)

            xcube = makeCube(inverse=True, hide=hideset)
            cube = NodePath(xcube)
            cube.setTexture(tex)
            cube.setTexture(ts,nor)
            cube.reparentTo(level_node)
            cube.setPos(x, y, 0 )
            #cube.setMaterial(myMaterial)
    return level_node


class App(ShowBase):
    def __init__(self):

        ShowBase.__init__(self)
        self.disableMouse()
        self.camLens.setNear(0.01)
        self.camLens.setFar(100)
        self.camLens.setFov(config.camera_angle)
        self.setBackgroundColor(Vec4(0, 0, 0, 0))
        

        self.level = load_level(config.start_level)
        self.dir = Direction()
        self.pos = Vector([0, 0])

        level_node = render_level(self.level)
        level_node.reparentTo(self.render)

        self.accept("escape", exit)
        self.accept("arrow_up", self.forward)
        self.accept("arrow_down", self.reverse)
        self.accept("arrow_down", self.backwards)
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

        print self.eventMgr

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
        pos = pos2vec(self.pos)
        dir = pos2vec(self.dir.forward_vec)
        
        if self.follow:
            self.camera.setPos(pos)
            #self.camera.setPos(Point3(pos-dir*0.5))
            self.camera.setPos(Point3(pos))
            self.camera.lookAt(Point3(pos+dir))
            self.camLens.setFov(config.camera_angle)
        self.light.setPos(Point3(pos))


    def set_camera_out(self):
        self.camera.setPos(21, -40, 30)
        self.camera.lookAt(21, 20, 0)
        self.camLens.setFov(config.camera_angle_out)
        self.follow = False

    def set_camera_in(self):
        self.follow = True
        self.set_camera()

    def moved(self):
        x, y = self.pos[0], self.pos[1]
        cell = self.level[x][y]
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
            self.teleport(Vector(cell.teleport))
            

    def forward(self):
        x, y = self.pos[0], self.pos[1]
        cell = self.level[x][y]
        if self.level[x][y].walls[self.dir.dir]!=WALL:
            self.pos = self.pos + self.dir.forward_vec
            Sequence(
                Parallel(
                    self.camera.posInterval(config.move_time, pos2vec(self.pos)),
                    self.light.posInterval(config.move_time, pos2vec(self.pos))
                    ),
                Func(self.moved)
                ).start()

    def reverse(self):
        self.dir.reverse()
        self.set_camera()
        
    def backwards(self):
        self.dir.reverse()
        if self.level[self.pos[0]][self.pos[1]].walls[self.dir.dir]!=WALL:
            self.pos = self.pos + self.dir.forward_vec

            Sequence(
                Parallel(
                    self.camera.posInterval(config.move_time, pos2vec(self.pos)),
                    self.light.posInterval(config.move_time, pos2vec(self.pos))
                    ),
                Func(self.moved)
                ).start()

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
            smoke.setColor(config.smoke_color)
            smoke.setExpDensity(config.smoke_exp_density)
            render.setFog(smoke)

 
    # Define a procedure to move the camera.
    def teleport(self, newpos):
        self.newpos = newpos

        amb1 = white(1.0)
        amb2 = white(0.0)
        dt = config.flash_time / 2.0
        from direct.interval.LerpInterval import LerpFunctionInterval
        from direct.interval.FunctionInterval import Func
        Sequence(
            LerpFunctionInterval(self.slight.setColor, dt, amb1, amb2),
            Func(self.set_newpos, newpos),
            LerpFunctionInterval(self.slight.setColor, dt, amb2, amb1)
            ).start()

    def set_newpos(self, newpos):
        self.pos = newpos
        self.set_camera()

        

app=App()
app.run()





