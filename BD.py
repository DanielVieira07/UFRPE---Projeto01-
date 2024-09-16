import sqlite3
import re
from datetime import *


class BancoDeDados:
    def __init__(self, banco_usuarios='Usuarios.db', banco_plantas_usuario='PlantasDoUsuario.db',
<<<<<<< HEAD
                 banco_detalhes_plantas='DetalhesDasPlantas.db', banco_anotacao_notificacao='anotacao.db'):
        self.banco_usuarios = sqlite3.connect(banco_usuarios)
        self.banco_plantas_usuario = sqlite3.connect(banco_plantas_usuario)
        self.banco_detalhes_plantas = sqlite3.connect(banco_detalhes_plantas)
        self.banco_anotacao_notificacao = sqlite3.connect(banco_anotacao_notificacao)

    def criar_tabelas(self):
        # Tabela para receber o horario e anotacoes
        with self.banco_anotacao_notificacao as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS anotacoes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            usuario_id INTEGER,
                            horario TEXT,
                            anotacao TEXT, 
                            FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
                        )
                    ''')
        self.banco_anotacao_notificacao.commit()

<<<<<<< HEAD

=======
=======
>>>>>>> d97cb22c3aaa3d9ccc3cea31dc29e7ca6f50de01
                 banco_detalhes_plantas='DetalhesDasPlantas.db', banco_anotacoes_notficacao='AnotacoesAndNotficacao.BD'):
        self.banco_usuarios = sqlite3.connect(banco_usuarios)
        self.banco_plantas_usuario = sqlite3.connect(banco_plantas_usuario)
        self.banco_detalhes_plantas = sqlite3.connect(banco_detalhes_plantas)
        self.banco_anotacoes_notificacao = sqlite3.connect(banco_anotacoes_notficacao)

    def criar_tabelas(self):
>>>>>>> e1401d62b8ccfc96b30cac16381755cc073e1099
        with self.banco_usuarios as conexao:
            # Criando a tabela no Banco de dados para armazenar as informações do usuário
            cursor = conexao.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    login TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    senha TEXT NOT NULL,
                    idade INTEGER NOT NULL
                )
            ''')
        self.banco_usuarios.commit()

        with self.banco_plantas_usuario as conexao:
            # Tabela para armazenar qual planta o usuário possui
            cursor = conexao.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS plantas_do_usuario (
                    id_planta INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_popular TEXT,
                    usuario_id INTEGER,
                    FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
                    FOREIGN KEY(nome_popular) REFERENCES plantas(nome_popular)
                )
            ''')
        self.banco_plantas_usuario.commit()

        with self.banco_detalhes_plantas as conexao:
            # Plantas existentes no BD
            cursor = conexao.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS plantas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_popular TEXT UNIQUE,
                    nome_cientifico TEXT,
                    familia TEXT,
                    genero TEXT,
                    cuidados TEXT,
                    pragas TEXT,
                    sol TEXT,
                    tipo_solos TEXT
                )
            ''')

            cursor.execute('''
                INSERT OR IGNORE INTO plantas (nome_popular, nome_cientifico, familia, genero, cuidados, pragas, sol, 
                tipo_solos)
                VALUES ('Samambaia', 'Nephrolepis Exaltata', 'Nefrolepidáceas', 'Neuroleptics',
                        'Mantenha úmido, mas sem acúmulo de água',
                        'Fertilização uma vez a cada 4 semanas durante o período de crescimento.',
                        'Sol parcial, Tolerância à Luz Solar: Sol pleno, Sombra total',
                        'Argila, Areia')
            ''')
        self.banco_detalhes_plantas.commit()

<<<<<<< HEAD
    def inserir_anotacao_horario(self, usuario_id, horario, anotacao):
        # inserir anotacao e receber horario para notificacao
        with self.banco_anotacao_notificacao as conexao:
            cursor = conexao.cursor()
            cursor.execute('INSERT INTO anotacoes (usuario_id, horario, anotacao) VALUES (?, ?, ?)',
                           (usuario_id, horario, anotacao))
        self.banco_anotacao_notificacao.commit()
=======
        # Tabela para receber o horario e anotacoes
        with self.banco_anotacoes_notificacao as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                    CREATE TABLE IF NOT EXISTS anotacoes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario_id INTEGER,
                        horario TEXT,
                        anotacoes TEXT,
                        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
                    )
                ''')
        self.banco_plantas_usuario.commit()
>>>>>>> e1401d62b8ccfc96b30cac16381755cc073e1099

    def inserir_usuario(self, login, email, senha, idade):
        # Recebe os dados do usuário para serem armazenados no BD
        with self.banco_usuarios as conexao:
            cursor = conexao.cursor()
            cursor.execute('INSERT INTO usuarios (login, email, senha, idade) VALUES (?, ?, ?, ?)',
                           (login, email, senha, idade))
        self.banco_usuarios.commit()

    def inserir_planta(self, nome_popular, usuario_id):
        # Cadastrar qual planta o usuário possui
        with self.banco_plantas_usuario as conexao:
            cursor = conexao.cursor()
            cursor.execute('INSERT INTO plantas_do_usuario (nome_popular, usuario_id) VALUES (?, ?)',
                           (nome_popular, usuario_id))
        self.banco_plantas_usuario.commit()

    def verificacao_planta(self, nome_popular, usuario_id):
        # verificacao se a planta ja foi cadastrada
        with self.banco_plantas_usuario as conexao:
            cursor = conexao.cursor()
            cursor.execute('SELECT * FROM plantas_do_usuario WHERE nome_popular=? AND usuario_id=?',
                           (nome_popular, usuario_id))
            return cursor.fetchone()

    def verificar_usuario(self, login, senha):
        # Verificar se o usuário consta no Banco de Dados
        with self.banco_usuarios as conexao:
            cursor = conexao.cursor()
            cursor.execute('SELECT * FROM usuarios WHERE login=? AND senha=?', (login, senha))
            return cursor.fetchone()

    def buscar_informacoes_planta(self, nome_popular):
        # Buscar informações sobre a planta no banco de dados
        with self.banco_detalhes_plantas as conexao:
            cursor = conexao.cursor()
            cursor.execute('SELECT * FROM plantas WHERE nome_popular=?', (nome_popular,))
            return cursor.fetchone()

    def excluir_usuario(self, usuario_id):
        # deletar o usuário do banco de dados pelo ID.
        with self.banco_usuarios as conexao:
            cursor = conexao.cursor()
            cursor.execute('DELETE FROM usuarios WHERE id = ?', (usuario_id,))
            conexao.commit()

    @staticmethod
    def verificar_email(email):
        # Verificar se o email está no formato correto
        padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(padrao_email, email) is not None


if __name__ == "__main__":
    banco = BancoDeDados()

<<<<<<< HEAD

=======
>>>>>>> e1401d62b8ccfc96b30cac16381755cc073e1099
