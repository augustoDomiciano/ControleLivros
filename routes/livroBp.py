# Importando o Blueprint
from flask import Blueprint, render_template
#adiciona isso
from ..extensions import db
from ..models.livro import Livro

#Instanciar o blueprint
livroBp = Blueprint('livroBp', __name__)

@livroBp.route('/livro')
def livro_list():
#    return "Teste"
    #adiciona isso
    #db.create_all()
    livros_query = Livro.query.all()
    return render_template('livro_list.html', livros=livros_query)