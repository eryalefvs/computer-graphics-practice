import numpy as np
from glumpy import app, gloo, gl

vertex = """
    attribute vec2 position;
    uniform float point_size;
    void main()
    {
        gl_Position = vec4(position, 0.0, 1.0);
        gl_PointSize = point_size;
    }
"""

fragment = """
    void main()
    {
        gl_FragColor = vec4(1, 0, 0, 1);
    }
"""

# Definição dos vértices
vertices = np.array([
    (-0.5, -0.5), (0.5, -0.5), (-0.5, 0.5),
    (0.5, 0.5), (-0.75, 0.75), (0.75, 0.75)
], dtype=np.float32)

window = app.Window(width=720, height=480, color=(1, 1, 1, 1))

program = gloo.Program(vertex, fragment, count=len(vertices))
program["position"] = vertices
program["point_size"] = 10.0

# Modos de desenho (começando com pontos)
draw_modes = [gl.GL_POINTS, gl.GL_LINES, gl.GL_TRIANGLES]
draw_mode_index = 0

@window.event
def on_draw(dt):
    window.clear()
    program.draw(draw_modes[draw_mode_index])

@window.event
def on_key_press(symbol, modifiers):
    global draw_mode_index
    if symbol == app.window.key.SPACE:  # Alterna entre os modos com espaço
        draw_mode_index = (draw_mode_index + 1) % len(draw_modes)
    elif symbol == app.window.key.UP:  # Aumenta o tamanho dos pontos
        program["point_size"] += 2.0
    elif symbol == app.window.key.DOWN:  # Diminui o tamanho dos pontos
        program["point_size"] = max(1.0, program["point_size"] - 2.0)

app.run()
