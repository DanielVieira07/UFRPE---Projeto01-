# Readme.md



README - Sistema de Gerenciamento de Plantas com Notificações Automáticas
Descrição do Projeto
O Sistema de Gerenciamento de Plantas com Notificações Automáticas é uma aplicação desktop desenvolvida em Python com o objetivo de ajudar usuários a gerenciar seus cuidados com plantas. O sistema permite que o usuário cadastre plantas, adicione anotações de cuidados específicos e agende notificações para lembrá-lo dos cuidados necessários. A aplicação utiliza Tkinter para a interface gráfica, SQLite como banco de dados local e threading para permitir notificações em tempo real sem interferir na interação do usuário.

Funcionalidades Principais
Cadastro de Usuário: Usuários podem se cadastrar com um login único, email e senha.
Cadastro de Plantas: Cada usuário pode cadastrar suas próprias plantas e relacioná-las com seu perfil.
Anotações e Lembretes: Usuários podem inserir anotações sobre suas plantas e definir horários para notificações de lembretes.
Notificações em Tempo Real: Uma thread paralela é usada para verificar, a cada minuto, se o horário atual coincide com algum lembrete agendado. Se houver uma correspondência, uma notificação é exibida usando messagebox do Tkinter.

projeto01-UFRPE---Aplicativo-Bot-nico-
Projeto desenvolvido para a diciplina de projeto interdisciplinar para Sistema de Informação na Universidade Federal Rural de Pernambuco - UFRPE. no curso de bacharelado de Sistema da Informação.

Um aplicativo Botânico desenvolvido durante os horarios da disciplina e fora dela, utilizando a linguaguem python com a IDE pycharm com o sistema de interface com a biblioteca Tkinter e para armazenar os dados foi usado a outra biblioteca Sqlite3.

Requisitos

python 3.12.1
sqlite3 
tkinter 

acesse: https://docs.python.org/pt-br/3/tutorial/ (para obter mais informacoes sobre os requisitos utilizados e como baixa-los, em python e tkinter)
