import OpenGL.GL as GL
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtOpenGL import QOpenGLFunctions_4_1_Core


class EditorWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.gl = QOpenGLFunctions_4_1_Core()

    def initializeGL(self):
        self.gl.initializeOpenGLFunctions()
        self.gl.glClearColor(0.0, 0.0, 0.0, 1.0)

    def resizeGL(self, width, height):
        self.gl.glViewport(0, 0, width, height)

    def paintGL(self):
        self.gl.glClearColor(1.0, 1.0, 1.0, 1.0)
        self.gl.glClear(GL.GL_COLOR_BUFFER_BIT)
