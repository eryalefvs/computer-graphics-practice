# Altere o último programa da prática 1 para exibir apenas um triângulo.
# Você pode escolher quais dos dois.

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

def setup():
    vertices = np.array([(-0.5, -0.5), (0.5, -0.5), (-0.5, 0.5)], dtype=np.float32)
    program['position'] = vertices

    cores = np.array([(1, 0, 0, 1),
                      (0, 1, 0, 1),
                      (0, 0, 1, 1)])
    program['color'] = cores

    global draw_mode
    #draw_mode = gl.GL_LINES
    #draw_mode = gl.GL_POINTS
    draw_mode = gl.GL_TRIANGLES


window = app.Window(width=720, height=480, color=(1, 1, 1, 1))

@window.event
def on_init():
    gl.glEnable(gl.GL_BLEND)
    gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
    
@window.event
def on_draw(dt):
    window.clear()
    program.draw(draw_mode)

program = gloo.Program(vertex, fragment, count=3)
setup()
app.run()