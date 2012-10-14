level = __import__("level00")
print level.dungeon_name
print level.map






from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

cammov = []


def DrawGLScene():
    def make_square(x1, x2, y1, y2, z1, z2):
        glVertex3f( x1, y1, z1)
        glVertex3f( x1, y2, z1)
        glVertex3f( x2, y2, z2)
        glVertex3f( x2, y1, z2)
        

    glMatrixMode(GL_PROJECTION)
    while cammov:
        cammov.pop()()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #glTranslatef(-50,-8.0,-140.0)		# Move Right And Into The Screen
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.7, 0.7)
    map = level.map
    for i in range(22):
        for j in range(22):
            east = map[3*i+1][3*j+0]
            west = map[3*i+1][3*j+2]
            north = map[3*i+0][3*j+1]
            south = map[3*i+2][3*j+1]

            delta = 0.1
            y1, y2 = 0, 10
            x1 = (j+0)*10 + delta
            x2 = (j+1)*10 - delta
            z1 = (22-i)*10 - delta
            z2 = (21-i)*10 + delta
            z1 = (i+0)*10 + delta
            z2 = (i+1)*10 - delta

            if east!=" ":
                glNormal(1.0, 0.0, 0.0)
                make_square(x1, x1, y1, y2, z1, z2)
            if west!=" ":
                glNormal(-1.0, 0.0, 0.0)
                make_square(x2, x2, y1, y2, z1, z2)
            if north!=" ":
                glNormal(0.0, 0.0, 1.0)
                make_square(x1, x2, y1, y2, z1, z1)
            if south!=" ":
                glNormal(0.0, 0.0, -1.0)
                make_square(x1, x2, y1, y2, z2, z2)

    glEnd()
    glutSwapBuffers()

def keyPressed(key, x, y):
    if key == ESCAPE:
        glutDestroyWindow(window)
        sys.exit()
    elif key == '5':
        cammov.append(lambda: glTranslate(0,1,0))
        glutPostRedisplay()
    elif key == '4':
        cammov.append(lambda: glRotate(-1,0,1,0))
        glutPostRedisplay()
    elif key == '6':
        cammov.append(lambda: glRotate(1,0,1,0))
        glutPostRedisplay()
    elif key == '8':
        cammov.append(lambda: glRotate(-1,1,0,0))
        glutPostRedisplay()
    elif key == '2':
        cammov.append(lambda: glRotate(1,1,0,0))
        glutPostRedisplay()
    


def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)

    amb = 0.05
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (amb, amb, amb, 1))

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [300.0, 5.0, 300.0, 1.0])
    #glLightfv(GL_LIGHT0, GL_POSITION, [00.0, 5.0, 00.0, 1.0])
    glLightfv(GL_LIGHT0, GL_POSITION, [125.0, 5.0, 125.0, 1.0])
    glLightfv(GL_LIGHT0, GL_POSITION, [5.0, 5.0, 215.0, 1.0])
    glLight(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.03)


    glMatrixMode(GL_MODELVIEW)


def ReSizeGLScene(Width, Height):
    if Height == 0:
        Height = 1

    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 600.0)

    #gluLookAt(150., 300., 280.,
    #      100., 0., 100.,
    #      0., 1., 0.)


    gluLookAt(15., 5., 215.,
          5., 5., 210.,
          0., 1., 0.)


    glMatrixMode(GL_MODELVIEW)


def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Jeff Molofee's GL Code Tutorial ... NeHe '99")
    glutDisplayFunc(DrawGLScene)
    # glutFullScreen()
    #glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(640, 480)



	
# Print message to console, and kick off the main to get it rolling.
print "Hit ESC key to quit."

if __name__ == '__main__':
    try:
        GLU_VERSION_1_2
    except:
        print "Need GLU 1.2 to run this demo"
        sys.exit(1)
    main()
    glutMainLoop()
    	
