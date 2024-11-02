from .user import Usuario
from .post import Publicacion

class RedInstagram:
    def __init__(self):
        self.usuarios = {}
        self.publicaciones = []

    def registrar_usuario(self, username, password):
        if username in self.usuarios:
            raise Exception("El nombre de usuario ya está en uso.")
        self.usuarios[username] = Usuario(username, password)

    def iniciar_sesion(self, username, password):
        user = self.usuarios.get(username)
        if user and user.contraseña == password:
            return user
        raise Exception("Credenciales incorrectas.")

    def agregar_publicacion(self, publicacion):
        self.publicaciones.append(publicacion)

    def obtener_publicaciones(self):
        return self.publicaciones






