import sqlite3
import threading
from tkinter import *
from tkinter import messagebox
import time

from BD import BancoDeDados


class App:
    def __init__(self):
        self.interface = None
        self.BD = BancoDeDados()  # Inicializa a conexão com o banco de dados

        # Inicializando a tela inicial, onde ficará o menu de Login e Cadastro
        self.interface = Tk()
        self.interface.title('BEN')
<<<<<<< HEAD
        self.interface.geometry('600x700')  # Aumentando a geometria da tela
=======
        self.interface.geometry('400x500')
>>>>>>> e1401d62b8ccfc96b30cac16381755cc073e1099
        self.interface.config(bg='#80b874')  # Cor de fundo
        self.interface.iconphoto(False, PhotoImage(file='logo.png'))
        self.interface.resizable(width=False, height=False)

        # Criação dos botões de Login e Cadastro
<<<<<<< HEAD
        self.botao_login = Button(self.interface, width=10, text='Login', bg='#4CAF50', fg='white', relief='raised',
                                  command=self.login)
        self.botao_login.place(x=250, y=500)
        self.botao_cadastro = Button(self.interface, width=10, text='Cadastro', bg='#4CAF50', fg='white', relief='flat',
                                     command=self.cadastrar)
        self.botao_cadastro.place(x=250, y=550)

        # Caixa de Entrada para receber login e senha
        self.Entrada_Login = Entry(self.interface, width=30, font='Arial 12')
        self.Entrada_Login.place(x=150, y=350)
        self.Label_Login = Label(self.interface, width=0, height=0, text='Login: ', font='Arial 12 bold', fg='#141414',
                                 bg='#d1e7cf')
        self.Label_Login.place(x=70, y=350)

        self.Entrada_Senha = Entry(self.interface, show='*', width=30, font='Arial 12')
        self.Entrada_Senha.place(x=150, y=400)
        self.Label_Senha = Label(self.interface, width=0, height=0, text='Senha: ', font='Arial 12 bold', fg='#141414',
                                 bg='#d1e7cf')
        self.Label_Senha.place(x=70, y=400)

        # Label para exibir mensagens de status
        self.Label_Status = Label(self.interface, width=50, height=2, text='', font='Arial 10 bold', fg='#ff0000',
                                  bg='#80b874')
        self.Label_Status.place(x=100, y=600)

=======
        self.botao_login = Button(self.interface, width=10, text='Login', relief='raised', command=self.login)
        self.botao_login.place(x=150, y=350)
        self.botao_cadastro = Button(self.interface, width=10, text='Cadastro', relief='flat', command=self.cadastrar)
        self.botao_cadastro.place(x=150, y=400)

        # Caixa de Entrada para receber login e senha
        self.Entrada_Login = Entry(self.interface, width=30, font='Arial 10')
        self.Entrada_Login.place(x=100, y=250)
        self.Label_Login = Label(self.interface, width=0, height=0, text='Login: ', font='Arial 10 bold', fg='#141414')
        self.Label_Login.place(x=25, y=250)

        self.Entrada_Senha = Entry(self.interface, show='*', width=30, font='Arial 10')
        self.Entrada_Senha.place(x=100, y=300)
        self.Label_Senha = Label(self.interface, width=0, height=0, text='Senha: ', font='Arial 10 bold', fg='#141414')
        self.Label_Senha.place(x=25, y=300)

        # Label para exibir mensagens de status
        self.Label_Status = Label(self.interface, width=40, height=2, text='', font='Arial 10 bold', fg='#ff0000',
                                  bg='#80b874')
        self.Label_Status.place(x=50, y=450)
>>>>>>> e1401d62b8ccfc96b30cac16381755cc073e1099
        self.interface.mainloop()

    def login(self):
        # Função para logar na conta
        login = self.Entrada_Login.get()
        senha = self.Entrada_Senha.get()

        # Verifica no banco de dados se a senha e login estão corretos
        logar = self.BD.verificar_usuario(login, senha)
        if logar:
            self.Label_Status.config(text='Login Bem-Sucedido!', fg='#00ff00')
            self.interface.destroy()
            self.abrir_janela_principal(logar[0], login)
        else:
            self.Label_Status.config(text='Usuário ou Senha Incorreto!', fg='#ff0000')

    def cadastrar(self):
        # Criando uma janela para cadastro
        self.janela_cadastro = Tk()
        self.janela_cadastro.title('Cadastro')
<<<<<<< HEAD
        self.janela_cadastro.geometry('600x700')  # Aumentando a geometria da tela
=======
        self.janela_cadastro.geometry('400x500')
>>>>>>> e1401d62b8ccfc96b30cac16381755cc073e1099
        self.janela_cadastro.config(bg='#80b874')  # Cor de fundo
        self.janela_cadastro.resizable(width=False, height=False)

        # Entradas para cadastro de login, senha, email e idade
<<<<<<< HEAD
        self.tela_cadastro = Label(self.janela_cadastro, text='Cadastro:', font='Arial 20 bold', fg='#0a0909',
                                   bg='#d1e7cf')
        self.tela_cadastro.place(x=200, y=20)

        self.Label_Login = Label(self.janela_cadastro, text='Login:', font='Arial 12 bold', fg='#141414', bg='#d1e7cf')
        self.Label_Login.place(x=50, y=100)
        self.Cadastrar_Login = Entry(self.janela_cadastro, width=40, font='Arial 12')
        self.Cadastrar_Login.place(x=200, y=100)

        self.Label_Senha = Label(self.janela_cadastro, text='Senha:', font='Arial 12 bold', fg='#141414', bg='#d1e7cf')
        self.Label_Senha.place(x=50, y=150)
        self.Cadastrar_Senha = Entry(self.janela_cadastro, show='*', width=40, font='Arial 12')
        self.Cadastrar_Senha.place(x=200, y=150)

        self.Label_confirmar_Senha = Label(self.janela_cadastro, text='Confir. Senha:', font='Arial 12 bold',
                                           fg='#141414', bg='#d1e7cf')
        self.Label_confirmar_Senha.place(x=50, y=200)
        self.confirmar_senha = Entry(self.janela_cadastro, show='*', width=40, font='Arial 12')
        self.confirmar_senha.place(x=200, y=200)

        self.Label_Email = Label(self.janela_cadastro, text='Email:', font='Arial 12 bold', fg='#141414', bg='#d1e7cf')
        self.Label_Email.place(x=50, y=250)
        self.Cadastrar_Email = Entry(self.janela_cadastro, width=40, font='Arial 12')
        self.Cadastrar_Email.place(x=200, y=250)

        self.Label_Idade = Label(self.janela_cadastro, text='Idade:', font='Arial 12 bold', fg='#141414', bg='#d1e7cf')
        self.Label_Idade.place(x=50, y=300)
        self.Cadastrar_Idade = Entry(self.janela_cadastro, width=40, font='Arial 12')
        self.Cadastrar_Idade.place(x=200, y=300)

        self.botao_confirmar_cadastro = Button(self.janela_cadastro, width=12, text='Cadastrar', bg='#4CAF50',
                                               fg='white', relief='flat', command=self.confirmar_cadastro)
        self.botao_confirmar_cadastro.place(x=250, y=400)

        # Label para exibir mensagens de status no cadastro
        self.Label_Status_Cadastro = Label(self.janela_cadastro, width=60, height=2, text='', font='Arial 12 bold',
                                           fg='#ff0000', bg='#80b874')
        self.Label_Status_Cadastro.place(x=100, y=500)
=======
        self.tela_cadastro = Label(self.janela_cadastro, text='Cadastro:', font='Arial 15 bold', fg='#0a0909',
                                   bg='#80b874')
        self.tela_cadastro.place(x=150, y=20)

        self.Label_Login = Label(self.janela_cadastro, text='Login:', font='Arial 10 bold', fg='#141414', bg='#80b874')
        self.Label_Login.place(x=25, y=80)
        self.Cadastrar_Login = Entry(self.janela_cadastro, width=30, font='Arial 10')
        self.Cadastrar_Login.place(x=150, y=80)

        self.Label_Senha = Label(self.janela_cadastro, text='Senha:', font='Arial 10 bold', fg='#141414', bg='#80b874')
        self.Label_Senha.place(x=25, y=130)
        self.Cadastrar_Senha = Entry(self.janela_cadastro, show='*', width=30, font='Arial 10')
        self.Cadastrar_Senha.place(x=150, y=130)

        self.Label_confirmar_Senha = Label(self.janela_cadastro, text='Confir. Senha:', font='Arial 10 bold',
                                           fg='#141414', bg='#80b874')
        self.Label_confirmar_Senha.place(x=25, y=180)
        self.confirmar_senha = Entry(self.janela_cadastro, show='*', width=30, font='Arial 10')
        self.confirmar_senha.place(x=150, y=180)

        self.Label_Email = Label(self.janela_cadastro, text='Email:', font='Arial 10 bold', fg='#141414', bg='#80b874')
        self.Label_Email.place(x=25, y=230)
        self.Cadastrar_Email = Entry(self.janela_cadastro, width=30, font='Arial 10')
        self.Cadastrar_Email.place(x=150, y=230)

        self.Label_Idade = Label(self.janela_cadastro, text='Idade:', font='Arial 10 bold', fg='#141414', bg='#80b874')
        self.Label_Idade.place(x=25, y=280)
        self.Cadastrar_Idade = Entry(self.janela_cadastro, width=30, font='Arial 10')
        self.Cadastrar_Idade.place(x=150, y=280)

        self.botao_confirmar_cadastro = Button(self.janela_cadastro, width=12, text='Cadastrar', relief='flat',
                                               command=self.confirmar_cadastro)
        self.botao_confirmar_cadastro.place(x=150, y=350)

        # Label para exibir mensagens de status no cadastro
        self.Label_Status_Cadastro = Label(self.janela_cadastro, width=40, height=2, text='', font='Arial 10 bold',
                                           fg='#ff0000', bg='#80b874')
        self.Label_Status_Cadastro.place(x=50, y=400)
>>>>>>> e1401d62b8ccfc96b30cac16381755cc073e1099

        self.janela_cadastro.mainloop()

    def confirmar_cadastro(self):
        # Função para confirmar o cadastro
        login = self.Cadastrar_Login.get()
        senha = self.Cadastrar_Senha.get()
        confirmar_senha = self.confirmar_senha.get()
        email = self.Cadastrar_Email.get()
        idade = self.Cadastrar_Idade.get()

        # Verifica se todos os campos foram preenchidos
        if not (login and senha and email and idade):
            self.Label_Status_Cadastro.config(text='Por favor, preencha todos os campos!', fg='#ff0000')
            return

        # Verifica se o email está no formato correto
        if not self.BD.verificar_email(email):
            self.Label_Status_Cadastro.config(text='Email inválido!', fg='#ff0000')
            return

        # Verifica se a senha esta correta.
        if confirmar_senha != senha:
            self.Label_Status_Cadastro.config(text='Senhas não compativeis!')
            return

        try:
            # Chama a função do banco de dados para cadastrar o usuário
            self.BD.inserir_usuario(login, email, senha, idade)
            self.Label_Status_Cadastro.config(text='Cadastro Bem-Sucedido!', fg='#00ff00')
            # cria uma thread para aguardar 2 segundos exibi a msg cadastro bem sucedido e depois fecha a janela
            threading.Timer(2.0, self.janela_cadastro.destroy).start()
        except sqlite3.IntegrityError as e:
            self.Label_Status_Cadastro.config(text=f'Erro: Login ou Email já Cadastrado{e}.', fg='#ff0000')

    def abrir_janela_principal(self, usuario_id, login):
        # Criando uma janela principal após login ou cadastro
        self.janela_principal = Tk()
        self.janela_principal.title('Bem-vindo ao BEN')
<<<<<<< HEAD
        self.janela_principal.geometry('600x850')  # Aumentando a geometria
        self.janela_principal.config(bg='#80b874')  # Cor de fundo
        self.janela_principal.resizable(width=False, height=False)

        # Seção para o perfil organizado
        perfil_frame = Frame(self.janela_principal, bg='#d1e7cf', padx=10, pady=10)
        perfil_frame.place(x=50, y=30, width=500, height=120)

        self.perfil_do_usuario = Label(perfil_frame, width=20, font='Arial 15 bold', text='Perfil do Usuário',
                                       fg='#0a0909', bg='#d1e7cf')
        self.perfil_do_usuario.grid(row=0, column=0, columnspan=2, pady=5)

        self.nome_usuario_label = Label(perfil_frame, width=15, font='Arial 12 bold', text='Nome:', fg='#141414',
                                        bg='#d1e7cf')
        self.nome_usuario_label.grid(row=1, column=0, sticky=W)

        self.nome_usuario = Label(perfil_frame, width=20, font='Arial 12', text=f'{login}', fg='#0a0909', bg='#d1e7cf')
        self.nome_usuario.grid(row=1, column=1, sticky=W)

        # Entradas para cadastrar planta
        planta_frame = Frame(self.janela_principal, bg='#d1e7cf', padx=10, pady=10)
        planta_frame.place(x=50, y=170, width=500, height=100)

        self.Label_Planta = Label(planta_frame, text='Nome da Planta:', font='Arial 12 bold', fg='#141414',
                                  bg='#d1e7cf')
        self.Label_Planta.grid(row=0, column=0, sticky=W, pady=5)

        self.Cadastrar_Planta = Entry(planta_frame, width=30, font='Arial 12')
        self.Cadastrar_Planta.grid(row=0, column=1, sticky=W)

        self.botao_confirmar_planta = Button(planta_frame, width=15, text='Cadastrar Planta', bg='#4CAF50', fg='white',
                                             relief='flat', command=lambda: self.confirmar_planta(usuario_id))
        self.botao_confirmar_planta.grid(row=1, column=0, pady=10)

        # Label para exibir mensagens de status no cadastro de plantas
        self.Label_Status_Planta = Label(planta_frame, width=25, height=2, text='', font='Arial 12 bold', fg='#ff0000',
                                         bg='#d1e7cf')
        self.Label_Status_Planta.grid(row=1, column=1, padx=10)

        # Botão para adicionar anotações e notificações
        self.botao_notificao_anotacoes = Button(self.janela_principal, width=20, text='Anotações e Notificações',
                                                bg='#4CAF50', fg='white',
                                                relief='flat', command=lambda: self.abrir_anotacoes(usuario_id))
        self.botao_notificao_anotacoes.place(x=180, y=300)

        # mostra as informacoes sobre a planta
        dicas_frame = Frame(self.janela_principal, bg='#d1e7cf', padx=10, pady=10)
        dicas_frame.place(x=50, y=350, width=500, height=250)  # Aumentei a altura

        self.label_dicas = Label(dicas_frame, text='Informações sobre Jardinagem:', font='Arial 12 bold', fg='#141414',
                                 bg='#d1e7cf')
        self.label_dicas.grid(row=0, column=0, sticky=W, pady=5)

        self.botao_dicas = Button(dicas_frame, width=25, text='Dicas de Jardinagem', bg='#4CAF50', fg='white',
                                  relief='flat', command=self.mostrar_dicas)
        self.botao_dicas.grid(row=1, column=0, pady=5)

        self.texto_dicas = Text(dicas_frame, width=60, height=10, font='Arial 12', wrap=WORD)  # Grid maior
        self.texto_dicas.grid(row=2, column=0, pady=5)

        # excluir conta caso o usuario q queira
        self.botao_excluir_conta = Button(self.janela_principal, width=12, text='Excluir Conta', bg='#f44336',
                                          fg='white', relief='flat', command=lambda: self.excluir_conta(usuario_id))
        self.botao_excluir_conta.place(x=470, y=30)

        # voltar para tela de login
        self.botao_voltar_login = Button(self.janela_principal, width=12, text='Voltar ao Login', bg='#4CAF50',
                                         fg='white',
                                         relief='flat', command=self.voltar_login)
        self.botao_voltar_login.place(x=470, y=70)

        self.janela_principal.mainloop()

    def voltar_login(self):
        # funcao de retorno para tela de login
        self.janela_principal.destroy()
        self.__init__()

=======
        self.janela_principal.geometry('400x500')
        self.janela_principal.config(bg='#80b874')  # Cor de fundo
        self.janela_principal.resizable(width=False, height=False)

        # Entradas para cadastrar planta
        self.perfil_do_usuario = Label(self.janela_principal, width=10, font='Arial 15 bold',
                                       text=f'Bem Vindo: ', fg='#0a0909')
        self.perfil_do_usuario.place(x=20, y=30)

        self.nome_usuario = Label(self.janela_principal, width=15, font='Arial 10 bold',
                                  text=f'{login}', fg='#0a0909')
        self.nome_usuario.place(x=160, y=33)

        self.Label_Planta = Label(self.janela_principal, text='Nome da Planta: ', font='Arial 10 bold', fg='#141414')
        self.Label_Planta.place(x=30, y=100)

        self.Cadastrar_Planta = Entry(self.janela_principal, width=30, font='Arial 10')
        self.Cadastrar_Planta.place(x=150, y=100)

        self.botao_confirmar_planta = Button(self.janela_principal, width=12, text='Cadastrar Planta', relief='flat',
                                             command=lambda: self.confirmar_planta(usuario_id))
        self.botao_confirmar_planta.place(x=150, y=150)

        # Label para exibir mensagens de status no cadastro de plantas
        self.Label_Status_Planta = Label(self.janela_principal, width=40, height=2, text='', font='Arial 10 bold',
                                         fg='#ff0000', bg='#80b874')
        self.Label_Status_Planta.place(x=30, y=200)

        # Botão para adicionar anotações e notificações
        self.botao_notificao_anotacoes = Button(self.janela_principal, width=20, text='Anotação e Notificação',
                                                relief='flat', command=lambda: self.abrir_anotacoes(usuario_id))
        self.botao_notificao_anotacoes.place(x=100, y=250)

        # Botão para mostrar dicas de jardinagem
        self.botao_dicas = Button(self.janela_principal, width=20, text='Dicas de Jardinagem', relief='flat',
                                  command=self.mostrar_dicas)
        self.botao_dicas.place(x=100, y=290)

        # Área para exibir informações sobre as plantas
        self.texto_dicas = Text(self.janela_principal, width=45, height=10, font='Arial 10')
        self.texto_dicas.place(x=25, y=330)

        # Botão para excluir conta do usuário
        self.botao_excluir_conta = Button(self.janela_principal, width=10, text='Excluir Conta', relief='flat',
                                          command=lambda: self.excluir_conta(usuario_id))
        self.botao_excluir_conta.place(x=10, y=290)

        self.janela_principal.mainloop()

>>>>>>> e1401d62b8ccfc96b30cac16381755cc073e1099
    def confirmar_planta(self, usuario_id):
        # Função para confirmar o cadastro da planta
        nome_planta = self.Cadastrar_Planta.get()

        if not nome_planta:
            self.Label_Status_Planta.config(text='Por favor, insira o nome da planta!', fg='#ff0000')
            return

        planta_existe = self.BD.verificacao_planta(nome_planta, usuario_id)
        if planta_existe:
            self.Label_Status_Planta.config(text='Planta já foi cadastrada!', fg='#ff0000')
            return

        try:
            self.BD.inserir_planta(nome_planta, usuario_id)
<<<<<<< HEAD
            self.Label_Status_Planta.config(text='Planta cadastrada com sucesso!', fg='#050505')
=======
            self.Label_Status_Planta.config(text='Planta cadastrada com sucesso!', fg='#00ff00')
>>>>>>> e1401d62b8ccfc96b30cac16381755cc073e1099
        except sqlite3.IntegrityError as e:
            self.Label_Status_Planta.config(text=f'Erro ao cadastrar a planta {e}.', fg='#ff0000')

    def mostrar_dicas(self):
        # Função para mostrar dicas de jardinagem com base na planta cadastrada
        nome_planta = self.Cadastrar_Planta.get()
        info_planta = self.BD.buscar_informacoes_planta(nome_planta)

        if info_planta:
            dicas = f"Nome Popular: {info_planta[1]}\nNome Científico: {info_planta[2]}\nFamília: {info_planta[3]}\nGênero: {info_planta[4]}\nCuidados: {info_planta[5]}\nPragas: {info_planta[6]}\nSol: {info_planta[7]}\nTipo de Solos: {info_planta[8]}"
            self.texto_dicas.delete(1.0, END)
            self.texto_dicas.insert(END, dicas)
        else:
            self.texto_dicas.delete(1.0, END)
            self.texto_dicas.insert(END, 'Planta não encontrada no banco de dados.')

    def excluir_conta(self, usuario_id):
        # excluir a conta do usuario.
        confirmar = messagebox.askyesno('Conta excluida', 'Tem certeza que deseja excluir?')
        if confirmar:
            self.BD.excluir_usuario(usuario_id)
            messagebox.showinfo('Conta Excluida', 'Sua conta foi excluida com sucesso.')
            self.janela_principal.destroy()
            self.interface.tk.tk()

    def abrir_anotacoes(self, usuario_id):
<<<<<<< HEAD
        # Criando uma janela para anotações e notificações
        self.janela_anotacoes = Tk()
        self.janela_anotacoes.title('Anotações e Notificações')
        self.janela_anotacoes.geometry('600x600')
        self.janela_anotacoes.config(bg='#80b874')  # Cor de fundo
        self.janela_anotacoes.resizable(width=False, height=False)

        anotacao_frame = Frame(self.janela_anotacoes, bg='#d1e7cf', padx=10, pady=10)
        anotacao_frame.place(x=50, y=50, width=500, height=400)

        self.label_horario = Label(anotacao_frame, text="Horário para regar (HH:MM):", bg='#d1e7cf',
                                   font="Arial 12 bold")
        self.label_horario.grid(row=0, column=0, sticky=W, pady=5)
        self.entrada_horario = Entry(anotacao_frame, width=10, font='Arial 12')
        self.entrada_horario.place(x=250, y=5)

        self.botao_salvar_anotacoes = Button(self.janela_anotacoes, text="Salvar",
                                             command=lambda: self.salvar_anotacoes(usuario_id))
        self.botao_salvar_anotacoes.place(x=50, y=250)

        self.botao_voltar = Button(self.janela_anotacoes, text="Voltar", command=self.janela_anotacoes.destroy)
        self.botao_voltar.place(x=50, y=350)

        # Botão para salvar horário
        self.botao_salvar_horario = Button(anotacao_frame, text="Salvar Horário", bg='#4CAF50', fg='white',
                                           relief='flat', command=lambda: self.salvar_anotacoes(usuario_id))
        self.botao_salvar_horario.place(x=350, y=5)

        self.label_anotacoes = Label(anotacao_frame, text="Escreva sua Anotação:", bg='#d1e7cf', font="Arial 12 bold")
        self.label_anotacoes.grid(row=1, column=0, sticky=W, pady=5)

        # Área de texto para escrever anotação
        self.texto_anotacao = Text(anotacao_frame, width=50, height=5, font='Arial 12')
        self.texto_anotacao.grid(row=2, column=0, columnspan=2, pady=5)

        # Lista para exibir anotações
        self.lista_anotacoes = Listbox(anotacao_frame, width=50, height=10)
        self.lista_anotacoes.grid(row=3, column=0, columnspan=2)
        scrollbar = Scrollbar(anotacao_frame)
        scrollbar.grid(row=3, column=2, sticky='ns')
        self.lista_anotacoes.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.lista_anotacoes.yview)


        self.janela_anotacoes.mainloop()

    def salvar_anotacoes(self, usuario_id):
        # Função para adicionar anotação
        horario = self.entrada_horario.get()
        anotacao = self.texto_anotacao.get(1.0, END).strip()

        # Insere a anotação no banco de dados
        self.BD.inserir_anotacao_horario(usuario_id, horario, anotacao)

        # Adiciona a anotação à lista de anotações exibida
        self.lista_anotacoes.insert(END, f"{horario}: {anotacao}")

        # Limpa os campos de entrada após salvar
        self.entrada_horario.delete(0, END)
        self.texto_anotacao.delete(1.0, END)

    def excluir_anotacao(self):
        # Função para excluir uma anotação selecionada
        selecionado = self.lista_anotacoes.curselection()
        if selecionado:
            self.lista_anotacoes.delete(selecionado)
=======
        self.janela_anotacoes = Tk()
        self.janela_anotacoes.title('Notificações e Anotações')
        self.janela_anotacoes.geometry('400x500')
        self.janela_anotacoes.config(bg='#80b874')
        self.janela_anotacoes.resizable(width=False, height=False)

        self.label_horario = Label(self.janela_anotacoes, text="Horário para regar (HH:MM):", bg='#80b874')
        self.label_horario.place(x=50, y=50)
        self.entrada_horario = Entry(self.janela_anotacoes, width=10)
        self.entrada_horario.place(x=200, y=50)

        self.label_anotacoes = Label(self.janela_anotacoes, text="Anotações:", bg='#80b874')
        self.label_anotacoes.place(x=50, y=100)
        self.entrada_anotacoes = Text(self.janela_anotacoes, width=40, height=10)
        self.entrada_anotacoes.place(x=50, y=130)

        self.botao_salvar_anotacoes = Button(self.janela_anotacoes, text="Salvar",
                                             command=lambda: self.salvar_anotacoes(usuario_id))
        self.botao_salvar_anotacoes.place(x=150, y=350)

        self.botao_voltar = Button(self.janela_anotacoes, text="Voltar", command=self.janela_anotacoes.destroy)
        self.botao_voltar.place(x=250, y=350)

        self.janela_anotacoes.mainloop()

        def salvar_anotacoes(usuario_id):
            pass
>>>>>>> e1401d62b8ccfc96b30cac16381755cc073e1099
