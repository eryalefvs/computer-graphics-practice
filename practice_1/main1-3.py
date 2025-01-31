# Crie uma função on_init no contexto da janela. A função “on_init” deve 
# habilitar a renderização em blend usando as duas funções do glossário. 
# Faça  com  que  as  cores  dos  triângulos  mudem  suavemente  entre  os 
# vértices. Para isso você vai precisar adicionar uma característica de cor 
# variante no vertex e a mesma característica em fragment. Além disso em 
# setup, precisamos de um vetor de array com 6 cores (uma para cada 
# vértice)  e  precisamos  passar  essa  característica  através  do  dicionário 
# program[‘color’]. 

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
    vertices = np.array([(-0.5, -0.5), (0.5, -0.5), (-0.5, 0.5),
                         (0.5, 0.5), (-0.75, 0.75), (0.75, 0.75)], dtype=np.float32)
    program['position'] = vertices

    cores = np.array([(1, 0, 0, 1),
                      (0, 1, 0, 1),
                      (0, 0, 1, 1),
                      (0, 1, 0, 1),
                      (0, 0, 1, 1),
                      (1, 0, 0, 1)])
    program['color'] = cores

    global draw_mode
    #draw_mode = gl.GL_LINES
    #draw_mode = gl.GL_POINTS
    draw_mode = gl.GL_TRIANGLES

    def on_init():
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

window = app.Window(width=720, height=480, color=(1, 1, 1, 1))

@window.event
def on_draw(dt):
    window.clear()
    program.draw(draw_mode)

program = gloo.Program(vertex, fragment, count=6)
setup()
app.run()