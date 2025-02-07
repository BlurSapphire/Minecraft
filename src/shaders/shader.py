from src.engine.settings import *


class Shader:
    def __init__(self):
        self.shader_program = self.create_shader()

    def create_shader(self):
        vertex_shader = """
        #version 330 core
        layout(location = 0) in vec3 position;
        void main() {
            gl_Position = vec4(position, 1.0);
        }
        """
        fragment_shader = """
        #version 330 core
        out vec4 FragColor;
        void main() {
            FragColor = vec4(1.0, 0.0, 0.0, 1.0);  // Красный цвет
        }
        """

        vertex_shader_obj = compileShader(vertex_shader, GL_VERTEX_SHADER)
        fragment_shader_obj = compileShader(fragment_shader, GL_FRAGMENT_SHADER)

        shader_program = compileProgram(vertex_shader_obj, fragment_shader_obj)
        return shader_program
