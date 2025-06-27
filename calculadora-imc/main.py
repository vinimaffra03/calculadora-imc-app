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
# quadro superior ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
quadro_superior = ctk.CTkFrame(janela, width=400, height=90, corner_radius=15)
quadro_superior.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

# configurando quadro superior #####################################
nome_app = ctk.CTkLabel(quadro_superior, text='Calculadora de IMC', 
                                        text_color=cor4, 
                                        anchor='center', 
                                        font=('Helvetica', 30, 'bold'))

nome_app.place(x=0, y=25, relwidth=1)

# quadro inferior ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
quadro_inferior = ctk.CTkFrame(janela, width=400, height=350, corner_radius=15)
quadro_inferior.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)

# configurando quadro inferior #####################################
# Label PESO >>>>>>
l_peso = ctk.CTkLabel(quadro_inferior, text='Digite seu peso (Kg) :', 
                                        text_color=cor0, 
                                        font=('Helvetica', 15))

l_peso.grid(row=0, column=0, sticky='nw', padx=20, pady=15)

# Entry PESO <<<<<<<
e_peso = ctk.CTkEntry(quadro_inferior, width=180, 
                                        font=('Helvetica', 16), 
                                        justify='center', 
                                        corner_radius=12)

e_peso.grid(row=0, column=1, sticky='nsew', padx=20, pady=15)

# Label ALTURA >>>>>>
l_altura = ctk.CTkLabel(quadro_inferior, text='Digite sua altura (m) :', 
                                        text_color=cor0, 
                                        font=('Helvetica', 15))

l_altura.grid(row=1, column=0, sticky='nw', padx=20, pady=15)

# Entry ALTURA <<<<<<<
e_altura = ctk.CTkEntry(quadro_inferior, width=180, font=('Helvetica', 16), 
                                        justify='center', 
                                        corner_radius=12)

e_altura.grid(row=1, column=1, sticky='nsew', padx=20, pady=15)

# Label RESULTADO >>>>>>
l_resultado = ctk.CTkLabel(quadro_inferior, text='---', 
                                            width=5,
                                            height=1,
                                            text_color=cor0, 
                                            font=('Helvetica', 32, 'bold'),
                                            anchor='center',
                                            corner_radius=12)

l_resultado.grid(row=1, column=0, columnspan=2, padx=15, pady=30)

# Label TEXTO RESULTADO >>>>>>
l_texto_resultado = ctk.CTkLabel(quadro_inferior, text='Resultado do calculo', 
                                            text_color=cor0, 
                                            font=('Helvetica', 16),
                                            anchor='center')

l_texto_resultado.grid(row=1, column=0, columnspan=2, padx=15, pady=30)


janela.mainloop()