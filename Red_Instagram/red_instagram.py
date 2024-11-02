from .user import User
from .post import Post

class RedInstagram:
    def __init__(self):
        self.user = {}
        self.post = []

    def registrar_usuario(self, username, password):
        if username in self.user:
            raise Exception("El nombre de usuario ya está en uso.")
        self.user[username] = Usuario(username, password)

    def iniciar_sesion(self, username, password):
        user = self.user.get(username)
        if user and user.contraseña == password:
            return user
        raise Exception("Credenciales incorrectas.")

    def agregar_publicacion(self, publicacion):
        self.post.append(publicacion)

    def obtener_publicaciones(self):
        return self.post






