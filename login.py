# import da biblioteca de ciação da gui
import tkinter as tk

def valida_senha():
    nome = usuario.get()
    psw = senha.get()
    if nome == 'padrão' and psw == '123a':
        print('Logado')
    else:
        print('Senha ou login incorretos')

# criando janela
janela = tk.Tk()
janela.geometry('300x350')
janela.title('Login caixa')

# Criando inputs de login
usuario = tk.Entry(janela)
usuario.pack(padx=50, pady=50)

senha = tk.Entry(janela)
senha.pack(padx=50, pady=50)

# Criando o botão de validação
botao = tk.Button(janela, text="login", command=valida_senha, bg='pink')
botao.pack(padx=50, pady=50)

# mantendo a jenela aberta

janela.mainloop()




