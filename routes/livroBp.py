# Importando o Blueprint
from flask import Blueprint, render_template, redirect, request, url_for
#adiciona isso
from ..extensions import db
from ..models.livro import Livro
from datetime import date, datetime

#Instanciar o blueprint
livroBp = Blueprint('livroBp', __name__)

@livroBp.route('/livro')
def livro_list():
#    return "Teste"
    #adiciona isso
    #db.create_all()
    livros_query = Livro.query.all()
    return render_template('livro_list.html', livros=livros_query)

@livroBp.route('/livro/create')
def create_livro():
    return render_template('livro_create.html')

@livroBp.route('/livro/add', methods=["POST"])
def add_livro():

    sNome = request.form["nome"]
    sGenero = request.form["genero"]
    dEntrada = datetime.strptime(request.form["entrada"], '%Y-%m-%d')
    dSaida = datetime.strptime(request.form["saida"], '%Y-%m-%d')

    livro = Livro(nome=sNome, genero=sGenero, entrada=dEntrada, saida=dSaida)
    db.session.add(livro)
    db.session.commit()

    return redirect(url_for("livroBp.livro_list"))

@livroBp.route('/livro/update/<livro_id>')
def update_livro(livro_id=0):
    livro_query = Livro.query.filter_by(id = livro_id).first()
    return render_template('livro_update.html', livro=livro_query)

@livroBp.route('/livro/upd', methods=["POST"])
def upd_livro():

    iLivro = request.form["id"]
    sNome = request.form["nome"]
    sGenero = request.form["genero"]
    dEntrada = datetime.strptime(request.form["entrada"], '%Y-%m-%d')
    dSaida = datetime.strptime(request.form["saida"], '%Y-%m-%d')

    livro = Livro.query.filter_by(id = iLivro).first()
    livro.nome = sNome
    livro.tipo = sGenero
    livro.inicio = dEntrada
    livro.fim = dSaida
    db.session.add(livro)
    db.session.commit()

    return redirect(url_for("livroBp.livro_list"))

@livroBp.route('/livro/delete/<livro_id>')
def delete_livro(livro_id=0):
    livro_query = Livro.query.filter_by(id = livro_id).first()
    return render_template('livro_delete.html', livro=livro_query)

@livroBp.route('/livro/dlt', methods=["POST"])
def dlt_livro():

    iLivro = request.form["id"]
    livro = Livro.query.filter_by(id = iLivro).first()
    db.session.delete(livro)
    db.session.commit()

    return redirect(url_for("livroBp.livro_list"))