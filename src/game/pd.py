from math import pi, sin, cos

from direct.showbase.DirectObject import DirectObject
from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from panda3d.core import lookAt
from panda3d.core import GeomVertexFormat, GeomVertexData
from panda3d.core import Geom, GeomTriangles, GeomVertexWriter
from panda3d.core import Texture, GeomNode
from panda3d.core import PerspectiveLens
from panda3d.core import CardMaker
from panda3d.core import Light, Spotlight, PointLight
from panda3d.core import TextNode
from panda3d.core import Vec3, Vec4, Point3
import sys, os
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence


def makeSquare(face, rhs=True):
    format=GeomVertexFormat.getV3n3cpt2()
    vdata=GeomVertexData('square', format, Geom.UHDynamic)

    vertex=GeomVertexWriter(vdata, 'vertex')
    normal=GeomVertexWriter(vdata, 'normal')
    color=GeomVertexWriter(vdata, 'color')
    texcoord=GeomVertexWriter(vdata, 'texcoord')

    if not rhs:
        face = list(reversed(face))

	
    normalvec = (face[1]-face[0]).cross(face[2]-face[0])
    normalvec.normalize()

    f = 0.9 if rhs else 0.8
    f = 1.0
    for ver in face:
        vertex.addData3f(ver*f)
	normal.addData3f(normalvec)
	color.addData3f(ver*0.0+1.0)
	color.addData3f((ver+1.0+2.0)*0.25)

    if not normalvec.z:
        texcoord.addData2f(0.0, 0.0)
	texcoord.addData2f(1.0, 0.0)
	texcoord.addData2f(1.0, 1.0)
	texcoord.addData2f(0.0, 1.0)

    tri1=GeomTriangles(Geom.UHDynamic)
    tri2=GeomTriangles(Geom.UHDynamic)
    tri1.addVertices(0, 1, 2)
    tri2.addVertices(2, 3, 0)
    tri1.closePrimitive()
    tri2.closePrimitive()

    square=Geom(vdata)
    square.addPrimitive(tri1)
    square.addPrimitive(tri2)
	
    return square

def makeCube(inverse=False, hide={}):
    from panda3d.core import LVector3f as Vector3
    #      6----7
    #     /|   /|
    #    4----5 |
    #    | 2--|-3
    #    |/   |/
    #    0----1
    v = [Vector3(x, y, z) for z in [-1, 1] for y in [-1, 1] for x in [-1, 1]]
    faces = [
        (v[0], v[1], v[5], v[4]), # front
        (v[1], v[3], v[7], v[5]), # right
        (v[3], v[2], v[6], v[7]), # back
        (v[2], v[0], v[4], v[6]), # left
        (v[0], v[2], v[3], v[1]), # bottom
        (v[4], v[5], v[7], v[6]), # top
        ]
    squares = [makeSquare(face, rhs=not inverse) 
               for i, face in enumerate(faces) 
	       if i not in hide]
    cube=GeomNode('cube')
    for square in squares:
        cube.addGeom(square)
    return cube



