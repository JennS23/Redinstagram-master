class Post:
    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto
        self.me_gusta = 0
        self.comentarios = []

    def dar_like(self):
        self.me_gusta += 1

    def agregar_comentario(self, comentario):
        self.comentarios.append(comentario)



