from src.engine.settings import *
from src.shaders.shader import Shader


class Window:
    def __init__(self):
        self.isRunning = True
        self.win = None

    def event_handler(self):
        if not glfw.init():
            print("Ошибка инициализации GLFW")
            self.isRunning = False
            return

        self.win = glfw.create_window(WIDTH, HEIGHT, "Minecraft", None, None)
        if not self.win:
            print("Ошибка создания окна")
            self.isRunning = False
            glfw.terminate()
            return

        glfw.make_context_current(self.win)

    def setup_buffers(self):
        # Вершины треугольника
        vertices = np.array([
            0.0, 0.5, 0.0,  # Верхняя вершина
            -0.5, -0.5, 0.0,  # Левый угол
            0.5, -0.5, 0.0  # Правый угол
        ], dtype=np.float32)

        # Создаём VAO и VBO
        VAO = glGenVertexArrays(1)
        VBO = glGenBuffers(1)

        glBindVertexArray(VAO)

        # Создание буфера для вершин
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        # Указываем, как интерпретировать данные
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * vertices.itemsize, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

        return VAO

    def update(self, shader_program, VAO):
        while not glfw.window_should_close(self.win):
            glfw.poll_events()
            self.render(shader_program, VAO)
            glfw.swap_buffers(self.win)  # Обновление экрана

        self.isRunning = False

    def render(self, shader_program, VAO):
        glClearColor(1.0, 1.0, 1.0, 1.0)  # Белый фон
        glClear(GL_COLOR_BUFFER_BIT)

        # Используем шейдерную программу
        glUseProgram(shader_program)

        # Отображаем треугольник
        glBindVertexArray(VAO)
        glDrawArrays(GL_TRIANGLES, 0, 3)  # Рисуем треугольник
        glBindVertexArray(0)

    def run(self):
        while self.isRunning:
            self.event_handler()
            if self.isRunning:
                self.update(shader_program, VAO)
