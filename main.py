from src.engine.settings import *
from src.engine.window import Window
from src.shaders.shader import Shader
def main():
    window = Window()
    window.event_handler()
    shader = Shader()

    # Настроим буферы для треугольника
    VAO = window.setup_buffers()

    # Основной цикл
    window.update(shader.shader_program, VAO)

if __name__ == "__main__":
    main()