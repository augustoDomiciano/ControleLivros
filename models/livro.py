from ..extensions import db

class Livro(db.Model):
    __tablename__ = "livros"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    genero = db.Column(db.String(50))
    entrada = db.Column(db.Date)
    saida = db.Column(db.Date)

    def __repr__(self):
        return "<Livro(nome={}, genero={}, entrada={}, saida{}, )>".format(self.nome, self.genero, self.entrada, self.saida)