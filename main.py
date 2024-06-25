import tkinter as tk
from tkinter import messagebox

def open_second_interface():
    first_interface.withdraw()  # Esconde a primeira interface
    second_interface.deiconify()  # Mostra a segunda interface

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

# Primeira interface
first_interface = tk.Tk()
first_interface.title("Bem-vindo")
first_interface.geometry("800x500")

# Carregar a imagem da logo
logo = tk.PhotoImage(file="image/logo.png")

# Adicionar a logo
logo_label = tk.Label(first_interface, image=logo)
logo_label.pack(pady=10)

label_welcome = tk.Label(first_interface, text="Bem-vindo!", font=("Helvetica", 16))
label_welcome.pack(pady=20)

btn_next = tk.Button(first_interface, text="Entrar", command=open_second_interface)
btn_next.pack(pady=10)

# Segunda interface
second_interface = tk.Toplevel()
second_interface.title("Dados do Usuário")
second_interface.geometry("600x400")
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
