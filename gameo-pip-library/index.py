from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
global window_title
window = 0                                             # glut window number
width, height = 500, 400                               # window size
global project
#get name of the user's program
def programName(name):
    global project
    project = __import__(name)
def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
def draw():  
    global project                                          # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()  
    project.main()                                 # reset position
    glutSwapBuffers() 

#draw rectangle
def drawRect(x, y, width, height, r, g, b):

    glLoadIdentity()                                   # reset position
    refresh2d(width, height)
    glColor3f(r, g, b)                           # set color to blue
  
    glutSwapBuffers()                                  # important for double buffering


    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()  
#mainloop function  
def mainloop():
    glutMainLoop()     
# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("gameo project")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
                 