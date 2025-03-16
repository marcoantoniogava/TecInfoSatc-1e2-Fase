#importando a biblioteca tkinter e a função de caixas de mensagem
import tkinter as tk
from tkinter import messagebox

#função pra configurar a janela principal e adicionar os elementos nela
def configurar_janela():
    #configurando o título, tamanho e cor de fundo da janela principal
    janela.title("PetShopping - Janela Principal")#define o título da janela
    janela.geometry("1920x1080")#define o tamanho da janela
    janela.configure(bg="#f5f5dc")#define a cor de fundo como bege

    #criando o título da página inicial
    global titulo#torna o título acessível em outras funções
    titulo = tk.Label(janela, text="Bem-vindo à Janela Principal do PetShopping!", font=("Arial", 48, "bold"), bg="#f5f5dc", fg="#333")#cria o título com fonte grande
    titulo.pack(pady=50)#posiciona o título na janela com espaçamento vertical

    #definindo estilo padrão dos botões
    estilo_botao = {#dicionário com configurações do estilo dos botões
        "width": 25,#largura do botão
        "height": 3,#altura do botão
        "font": ("Arial", 18, "bold"),#fonte do texto no botão
        "bg": "#4CAF50",#cor verde no botão
        "fg": "white",#cor branca no texto
        "relief": "flat",#botão sem borda
        "bd": 2,#espessura da borda (inativa)
        "highlightthickness": 0,#desativa o realce ao redor
        "activebackground": "#45a049",#cor verde mais clara quando o botão é clicado
        "activeforeground": "white",#mantém o texto branco ao clicar
    }

    #criando botões pra cada seção e colocando eles na janela
    global botao_clientes, botao_pets, botao_produtos, botao_servicos#torna os botões globais pra serem manipulados depois
    botao_clientes = tk.Button(janela, text="Clientes", command=abrir_clientes, **estilo_botao)#cria o botão da seção "Clientes"
    botao_clientes.pack(pady=10)#posiciona o botão com um pequeno espaçamento

    botao_pets = tk.Button(janela, text="Pets", command=abrir_pets, **estilo_botao)#cria o botão da seção "Pets"
    botao_pets.pack(pady=10)#posiciona o botão com espaçamento

    botao_produtos = tk.Button(janela, text="Produtos", command=abrir_produtos, **estilo_botao)#cria o botão da seção "Produtos"
    botao_produtos.pack(pady=10)#posiciona o botão com espaçamento

    botao_servicos = tk.Button(janela, text="Serviços", command=abrir_servicos, **estilo_botao)#cria o botão da seção "Serviços"
    botao_servicos.pack(pady=10)#posiciona o botão com espaçamento

    #adicionando efeitos de hover nos botões pra trocar a cor quando passa o mouse
    for botao in [botao_clientes, botao_pets, botao_produtos, botao_servicos]:#percorre todos os botões
        botao.bind("<Enter>", lambda evento, b=botao: b.config(bg="#45a049"))#muda a cor pra verde claro ao passar o mouse
        botao.bind("<Leave>", lambda evento, b=botao: b.config(bg="#4CAF50"))#volta pra cor verde original ao sair com o mouse

#função pra esconder os elementos da página inicial
def ocultar_pagina_inicial():
    titulo.pack_forget()#esconde o título
    botao_clientes.pack_forget()#esconde o botão de clientes
    botao_pets.pack_forget()#esconde o botão de pets
    botao_produtos.pack_forget()#esconde o botão de produtos
    botao_servicos.pack_forget()#esconde o botão de serviços

#função pra mostrar os elementos da página inicial de novo
def mostrar_pagina_inicial():
    titulo.pack(pady=50)#mostra o título com espaçamento
    botao_clientes.pack(pady=10)#mostra o botão de clientes
    botao_pets.pack(pady=10)#mostra o botão de pets
    botao_produtos.pack(pady=10)#mostra o botão de produtos
    botao_servicos.pack(pady=10)#mostra o botão de serviços

#função genérica pra criar páginas de gerenciamento (CRUD)
def criar_pagina_crud(titulo_texto):
    ocultar_pagina_inicial()#esconde os elementos da página inicial

    #criando o título da nova página
    titulo_label = tk.Label(janela, text=titulo_texto, font=("Arial", 48, "bold"), bg="#f5f5dc", fg="#333")#título grande da nova página
    titulo_label.pack(pady=30)#posiciona o título com espaçamento

    #criando um container (frame) pros botões CRUD
    frame_crud = tk.Frame(janela, bg="#f5f5dc")#frame com cor de fundo bege
    frame_crud.pack(pady=10)#posiciona o frame com espaçamento

    #função pra criar os botões CRUD com uma ação específica
    def criar_botao_crud(nome, acao):
        botao = tk.Button(frame_crud, text=nome, command=lambda: messagebox.showinfo(nome, f"{acao}..."), **estilo_botao)#botão que exibe uma mensagem de ação
        botao.bind("<Enter>", lambda evento: botao.config(bg="#45a049"))#muda a cor no hover
        botao.bind("<Leave>", lambda evento: botao.config(bg="#4CAF50"))#volta à cor original
        return botao#retorna o botão criado

    #criando os botões de cadastrar, visualizar, atualizar e deletar
    botoes = [#lista com os botões CRUD
        criar_botao_crud("Cadastrar", "Cadastrando"),#botão cadastrar
        criar_botao_crud("Visualizar", "Visualizando"),#botão visualizar
        criar_botao_crud("Atualizar", "Atualizando"),#botão atualizar
        criar_botao_crud("Deletar", "Deletando")#botão deletar
    ]

    #posicionando os botões no frame
    for idx, botao in enumerate(botoes):#percorre os botões com índice
        botao.grid(row=0, column=idx, padx=10)#posiciona os botões em uma linha com espaçamento horizontal

    #criando botão pra voltar pra página inicial
    botao_voltar = tk.Button(janela, text="Voltar", command=lambda: voltar_pagina(titulo_label, frame_crud, botao_voltar), **estilo_botao)#botão pra voltar
    botao_voltar.pack(pady=50)#posiciona com espaçamento
    botao_voltar.bind("<Enter>", lambda evento: botao_voltar.config(bg="#45a049"))#muda a cor no hover
    botao_voltar.bind("<Leave>", lambda evento: botao_voltar.config(bg="#4CAF50"))#volta à cor original

#funções pra abrir as seções específicas
def abrir_clientes():
    criar_pagina_crud("Gerenciamento de Clientes")#chama a página de clientes

def abrir_pets():
    criar_pagina_crud("Gerenciamento de Pets")#chama a página de pets

def abrir_produtos():
    criar_pagina_crud("Gerenciamento de Produtos")#chama a página de produtos

def abrir_servicos():
    criar_pagina_crud("Gerenciamento de Serviços")#chama a página de serviços

#função pra voltar pra página inicial, escondendo os widgets da página atual
def voltar_pagina(*widgets):#aceita múltiplos widgets como argumento
    for widget in widgets:#percorre os widgets fornecidos
        widget.pack_forget()#esconde widgets que usam pack
        widget.grid_forget() if isinstance(widget, tk.Frame) else None#esconde widgets que usam grid
    mostrar_pagina_inicial()#mostra os elementos da página inicial

#inicializando a aplicação
janela = tk.Tk()#cria a janela principal
estilo_botao = {#define o estilo dos botões fora da função pra reutilizar
    "width": 25,#largura
    "height": 3,#altura
    "font": ("Arial", 18, "bold"),#fonte
    "bg": "#4CAF50",#cor verde
    "fg": "white",#texto branco
    "relief": "flat",#sem borda
    "bd": 2,#borda inativa
    "highlightthickness": 0,#sem destaque
    "activebackground": "#45a049",#verde hover
    "activeforeground": "white",#texto branco hover
}
configurar_janela()#configura a janela principal
janela.mainloop()#inicia o loop da interface gráfica
