from models import Pessoas, Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome='Iago', idade = 21)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    todas_as_pessoas = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Iago').first()
    print(pessoa)
    print(pessoa.idade)
    print(todas_as_pessoas)


def altera_pessoas():
    pessoa = Pessoas.query.filter_b(nome='Iago').first()
    pessoa.idade = 22
    pessoa.save()


def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Iago').first()
    pessoa.delete()

def insere_usuario():
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuario():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == "__main__":
    insere_usuario('Iago0002', '123')
    consulta_todos_usuario()
    insere_pessoas()
    consulta_pessoas()
    altera_pessoas()
