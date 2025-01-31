# Troque as primitivas renderizadas para Linhas e Triângulos. Quando fizer 
# isso, reduza o tamanho dos pontos. 

import numpy as np
from glumpy import app, gloo, gl, glm

vertex = """
    attribute vec2 position;
    void main()
    {
        gl_Position = vec4(position, 0.0, 1.0);
    }
"""

fragment = """
    void main()
    {
        gl_FragColor = vec4(1,0,0,1);
    }
"""

def setup():
    vertices = np.array([(-0.5, -0.5), (0.5, -0.5), (-0.5, 0.5),
                         (0.5, 0.5), (-0.75, 0.75), (0.75, 0.75)], dtype=np.float32)
    program['position'] = vertices
    global draw_mode
    #draw_mode = gl.GL_POINTS
    draw_mode = gl.GL_LINE
    draw_mode = gl.GL_TRIANGLES

window = app.Window(width=720, height=480, color=(1, 1, 1, 1))

@window.event
def on_draw(dt):
    window.clear()
    program.draw(draw_mode)

program = gloo.Program(vertex, fragment, count=6)
setup()
app.run()