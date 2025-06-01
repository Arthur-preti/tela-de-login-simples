import customtkinter as ctk

def validarlogin():
    entryuser = entry.get()
    entrypassword = entrysenha.get()
    if entryuser == 'arthur' and entrypassword == 'boa':
        result.configure(text='login autorizado!', text_color='green')
    else:
        result.configure(text= 'senha ou usuário incorreto!', text_color = 'red')


ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title('login')
app.geometry('300x300')

user = ctk.CTkLabel(app, text='usuário')
user.pack(pady=10)

entry = ctk.CTkEntry(app, placeholder_text='digite seu usuário')
entry.pack(pady=10)

senha = ctk.CTkLabel(app, text='senha')
senha.pack(pady=10)

entrysenha = ctk.CTkEntry(app, placeholder_text='digite seu usuário')
entrysenha.pack(pady=10)

botao = ctk.CTkButton(app, text='login', command=validarlogin)
botao.pack(pady=10)

result = ctk.CTkLabel(app, text='')
result.pack(pady=10)

app.mainloop()