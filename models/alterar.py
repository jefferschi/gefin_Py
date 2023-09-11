# arquivo sobre como alterar somente os campos que de fato sofreram alteração pelo usuário nas entradas
# dos inputs. 

"""
Se você está usando uma interface gráfica Tkinter em Python e os dados fornecidos pelo usuário são 
armazenados em variáveis ​​para cada campo, então é uma abordagem comum criar um dicionário onde as chaves 
são os nomes dos campos na tabela e os valores são as variáveis ​​correspondentes que armazenamos os novos 
valores fornecidos pelo usuário.

Aqui está um exemplo de como você pode criar um dicionário para armazenar essas variáveis ​​e, em seguida, 
usar esse dicionário para gerar a declaração SQL de atualização dinamicamente:
"""

import sqlite3
import tkinter as tk

# Função para atualizar os dados no banco de dados
def atualizar_dados():
    id_usuario = 1  # ID do usuário que deseja atualizar
    
    # Dicionário para mapear nomes de campo para variáveis Tkinter
    campos_variaveis = {
        'nome': nome_var.get(),
        'idade': idade_var.get(),
        # Adicione mais campos e variáveis conforme necessário
    }

    # Conectar-se ao banco de dados
    conn = sqlite3.connect('seu_banco_de_dados.db')
    cursor = conn.cursor()

    # Montar a declaração SQL dinamicamente
    sql = "UPDATE pessoas SET "
    valores_atualizados = []

    for campo, novo_valor in campos_variaveis.items():
        if novo_valor is not None:
            sql += f"{campo} = ?, "
            valores_atualizados.append(novo_valor)

    # Remover a vírgula extra no final da string SQL
    sql = sql.rstrip(', ')

    # Adicionar a cláusula WHERE para identificar o registro específico
    sql += " WHERE id = ?"
    valores_atualizados.append(id_usuario)

    # Executar a atualização
    cursor.execute(sql, valores_atualizados)
    conn.commit()

    # Fechar a conexão com o banco de dados
    conn.close()

# Criar a janela Tkinter
root = tk.Tk()
root.title("Atualizar Dados")

# Variáveis Tkinter para os campos
nome_var = tk.StringVar()
idade_var = tk.IntVar()

# Entradas Tkinter para os campos
tk.Label(root, text="Nome:").pack()
tk.Entry(root, textvariable=nome_var).pack()

tk.Label(root, text="Idade:").pack()
tk.Entry(root, textvariable=idade_var).pack()

# Botão para atualizar os dados
tk.Button(root, text="Atualizar Dados", command=atualizar_dados).pack()

root.mainloop()


"""
Neste exemplo, criamos variáveis ​​Tkinter ( nome_vare idade_var) para armazenar os valores fornecidos 
pelo usuário para os campos "nome" e "idade". Essas variáveis ​​são então mapeadas para os campos no 
dicionário campos_variaveis. O restante do código é semelhante ao exemplo anterior, onde construímos 
dinamicamente a declaração SQL de atualização e a executamos no banco de dados. Isso permite atualizar 
apenas os campos que o usuário modificou.
"""