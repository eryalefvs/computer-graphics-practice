# Crie uma função que recebe o click do mouse
# “on_mouse_press(x,y,button)” e atualiza a posição do triângulo.

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
def setup():
    program['position'] = vertices
    program['color'] = cores
    global draw_mode
    #draw_mode = gl.GL_LINES
    #draw_mode = gl.GL_POINTS
    draw_mode = gl.GL_TRIANGLES

def update_triangle_position(x, y):
    global vertices, triangle_offset
    triangle_offset = np.array([x, y])
    half_size = 0.5
    vertices = np.array([[x - half_size, y - half_size],
                         [x + half_size, y - half_size],
                         [x, y + half_size]], dtype=np.float32)
    program['position'] = vertices

window = app.Window(width=720, height=480, color=(1, 1, 1, 1))

@window.event
def on_init():
    gl.glEnable(gl.GL_BLEND)
    gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

@window.event
def on_mouse_press(x, y, button):
    global selected_vertex
    width, height = window.width, window.height
    x = (x / width) * 2 - 1
    y = 1 - (y / height) * 2

    update_triangle_position(x, y)
@window.event
def on_draw(dt):
    window.clear()
    program.draw(draw_mode)

program = gloo.Program(vertex, fragment, count=3)
setup()
app.run()