# Mude  a  função  “on_mouse_press(x,y,button)”  para  identificar  qual  o 
# vértice  mais  próximo  do  click.  Adicione  uma  função 
# “on_mouse_drag(x,y,dx,dy,button)”,  quando  o  botão  está  pressionado 
# mova a posição do vértice mais próxima. 

import numpy as np
from glumpy import app, gloo, gl, glm

vertex = """
    attribute vec2 position;
    attribute vec4 color;
    varying vec4 vColor;
    void main()
    {
        gl_Position = vec4(position, 0.0, 1.0);
        gl_PointSize = 25.0;
        vColor = color;
    }
"""

fragment = """
varying vec4 vColor;
    void main()
    {
        gl_FragColor = vColor;
    }
"""
vertices = np.array([(-0.5, -0.5), (0.5, -0.5), (-0.5, 0.5)], dtype=np.float32)
cores = np.array([(1, 0, 0, 1),
                  (0, 1, 0, 1),
                  (0, 0, 1, 1)])
selected_vertex = None

def setup():
    colors = np.array([[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]], dtype=np.float32)
    program['color'] = colors
    global draw_mode
    draw_mode = gl.GL_TRIANGLES

def find_closest_vertex(x, y):
    global vertices
    distances = np.sum((vertices - np.array([x, y]))**2, axis=1)
    return np.argmin(distances)

window = app.Window(width=720, height=480, color=(1, 1, 1, 1))

@window.event
def on_init():
    gl.glEnable(gl.GL_BLEND)
    gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

@window.event
def on_mouse_drag(x, y, dx, dy, button):
    global vertices, selected_vertex
    width, height = window.width, window.height
    x = (x / width) * 2 - 1
    y = 1 - (y / height) * 2

    selected_vertex = find_closest_vertex(x, y)
    vertices[selected_vertex] = [x, y]
    program['position'] = vertices

@window.event
def on_draw(dt):
    window.clear()
    program.draw(draw_mode)

program = gloo.Program(vertex, fragment, count=3)
setup()
app.run()