import customtkinter as ctk

# Cores
cor0 = "#2C3E50"  # Azul Escuro para texto e rótulos (profissional e moderno)
cor1 = "#ECF0F1"  # Cinza Claro para fundo e texto (limpo e legível)
cor2 = "#3498DB"  # Azul para botões (calmo e moderno)
cor3 = "#E5E8E8"  # Cinza Claro para fundo da janela
cor4 = "#16A085"  # Verde Água para detalhes (fresco e estiloso)
cor5 = "#95A5A6"  # Cinza para texto secundário

janela = ctk.CTk()
janela.title('Calculadora de IMC')
janela.geometry('440x520')
janela.configure(bg=cor3)

# dividindo as telas
# quadro superior
quadro_superior = ctk.CTkFrame(janela, width=400, height=90, corner_radius=15)
quadro_superior.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

# configurando quadro superior
nome_app = ctk.CTkLabel(quadro_superior, text='Calculadora de IMC', 
                                        text_color=cor4, 
                                        anchor='center', 
                                        font=('Helvetica', 30, 'bold'))

nome_app.place(x=0, y=25, relwidth=1)

# quadro inferior
quadro_superior = ctk.CTkFrame(janela, width=400, height=350, corner_radius=15)
quadro_superior.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)


janela.mainloop()