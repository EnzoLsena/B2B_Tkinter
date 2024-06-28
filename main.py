import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Definindo CPF e senha para autenticação
CPF_CORRETO = "045.629.455-40"
SENHA_CORRETA = "123456"

def format_cpf(cpf):
    """Formata a entrada do CPF para o formato ###.###.###-##"""
    cpf = cpf.replace(".", "").replace("-", "")[:11]  # Remove pontos e traços e limita a 11 dígitos
    formatted_cpf = ""
    if len(cpf) > 3:
        formatted_cpf += cpf[:3] + "."
    if len(cpf) > 6:
        formatted_cpf += cpf[3:6] + "."
    if len(cpf) > 9:
        formatted_cpf += cpf[6:9] + "-"
    formatted_cpf += cpf[9:]
    return formatted_cpf

def on_cpf_change(var, index, mode):
    entry_cpf.set(format_cpf(entry_cpf.get()))

def open_second_interface():
    cpf = entry_cpf.get()
    senha = entry_senha.get()
    
    # Verifica se o CPF e a senha inseridos estão corretos
    if cpf == CPF_CORRETO and senha == SENHA_CORRETA:
        first_interface.withdraw()  # Esconde a primeira interface
        second_interface.deiconify()  # Mostra a segunda interface
    else:
        messagebox.showerror("Erro", "CPF ou senha incorretos. Tente novamente.")

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)

def save_data():
    name = entry_name.get()
    age = entry_age.get()
    if name and age:
        # Aqui você pode adicionar o código para salvar no banco de dados
        print(f"Nome: {name}, Idade: {age}")
        messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")

# Primeira interface (formulário de login)
first_interface = tk.Tk()
first_interface.title("Login")
first_interface.geometry("300x250")

# Carregar a imagem da logo
logo = tk.PhotoImage(file="image/logo.png")

# Adicionar a logo
logo_label = tk.Label(first_interface, image=logo)
logo_label.pack(pady=10)

label_cpf = tk.Label(first_interface, text="CPF:")
label_cpf.pack(pady=5)

# Usando StringVar para controlar a entrada do CPF
entry_cpf = tk.StringVar()
entry_cpf.trace_add("write", on_cpf_change)

cpf_entry = ttk.Entry(first_interface, textvariable=entry_cpf)
cpf_entry.pack(pady=5)

label_senha = tk.Label(first_interface, text="Senha:")
label_senha.pack(pady=5)
entry_senha = tk.Entry(first_interface, show="*")
entry_senha.pack(pady=5)

btn_login = tk.Button(first_interface, text="Entrar", command=open_second_interface)
btn_login.pack(pady=20)

# Segunda interface
second_interface = tk.Toplevel()
second_interface.title("Dados do Usuário")
second_interface.geometry("300x200")
second_interface.withdraw()  # Começa escondida

label_name = tk.Label(second_interface, text="Nome:")
label_name.pack(pady=5)
entry_name = tk.Entry(second_interface)
entry_name.pack(pady=5)

label_age = tk.Label(second_interface, text="Idade:")
label_age.pack(pady=5)
entry_age = tk.Entry(second_interface)
entry_age.pack(pady=5)

frame_buttons = tk.Frame(second_interface)
frame_buttons.pack(pady=20)

btn_clear = tk.Button(frame_buttons, text="Limpar", command=clear_fields)
btn_clear.grid(row=0, column=0, padx=10)

btn_save = tk.Button(frame_buttons, text="Salvar", command=save_data)
btn_save.grid(row=0, column=1, padx=10)

first_interface.mainloop()
