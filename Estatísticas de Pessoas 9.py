import tkinter as tk
from tkinter import ttk

# Função para calcular e exibir as porcentagens
def calcular():
    try:
        desktop = int(entry_desktop.get())
        notebook = int(entry_notebook.get())
        smartphone = int(entry_smartphone.get())
        tablet = int(entry_tablet.get())

        # Calcular total de pessoas
        total = desktop + notebook + smartphone + tablet
        label_total.config(text=f"Total de Pessoas Pesquisadas: {total}")

        # Verificar se o total é maior que zero para evitar divisão por zero
        if total > 0:
            # Calcular e exibir as porcentagens com barra de progresso
            porcentagens = [
                ("Desktop", desktop),
                ("Notebook", notebook),
                ("Smartphone", smartphone),
                ("Tablet", tablet),
            ]

            for i, (nome, quantidade) in enumerate(porcentagens):
                percent = (quantidade / total) * 100
                bars[i].config(value=percent)
                labels[i].config(text=f"{nome}: {percent:.2f}%")
        else:
            # Caso o total seja zero, limpar as barras e exibir mensagem
            for i in range(len(bars)):
                bars[i].config(value=0)
                labels[i].config(text=f"{porcentagens[i][0]}: 0%")
    
    except ValueError:
        label_total.config(text="Por favor, insira valores numéricos válidos.")

# Configurações da janela principal
root = tk.Tk()
root.title("Estatísticas de Preferência por Dispositivos")
root.geometry("600x500")
root.config(bg="#2C3E50")

# Título do aplicativo
title = tk.Label(root, text="Estatísticas de Preferência por Dispositivos", 
                 font=("Helvetica", 16, "bold"), bg="#2980B9", fg="white", pady=10)
title.pack(fill="x")

# Widgets de entrada de dados com cores e estilos
frame_inputs = tk.Frame(root, bg="#34495E", pady=10)
frame_inputs.pack(pady=10, padx=20, fill="x")

tk.Label(frame_inputs, text="Pessoas que gostam de Desktop:", bg="#34495E", fg="white", font=("Arial", 10)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_desktop = tk.Entry(frame_inputs, font=("Arial", 10), width=10)
entry_desktop.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Pessoas que gostam de Notebook:", bg="#34495E", fg="white", font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_notebook = tk.Entry(frame_inputs, font=("Arial", 10), width=10)
entry_notebook.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Pessoas que gostam de Smartphone:", bg="#34495E", fg="white", font=("Arial", 10)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_smartphone = tk.Entry(frame_inputs, font=("Arial", 10), width=10)
entry_smartphone.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Pessoas que gostam de Tablet:", bg="#34495E", fg="white", font=("Arial", 10)).grid(row=3, column=0, sticky="w", padx=5, pady=5)
entry_tablet = tk.Entry(frame_inputs, font=("Arial", 10), width=10)
entry_tablet.grid(row=3, column=1, padx=5, pady=5)

# Botão para calcular com estilo
btn_calcular = tk.Button(root, text="Calcular", command=calcular, 
                         bg="#1ABC9C", fg="white", font=("Arial", 12, "bold"), pady=5, relief="flat")
btn_calcular.pack(pady=10)

# Label para exibir o total de pessoas
label_total = tk.Label(root, text="Total de Pessoas Pesquisadas: 0", 
                       font=("Arial", 12, "bold"), bg="#2C3E50", fg="white")
label_total.pack(pady=5)

# Lista para barras de progresso e rótulos de porcentagem
bars = []
labels = []

# Criando barras e rótulos de porcentagem para cada dispositivo
colors = ["#3498DB", "#9B59B6", "#E74C3C", "#F1C40F"]
for i, nome in enumerate(["Desktop", "Notebook", "Smartphone", "Tablet"]):
    frame = tk.Frame(root, bg="#2C3E50")
    frame.pack(fill="x", pady=5, padx=20)

    label = tk.Label(frame, text=nome + ":", bg="#2C3E50", fg="white", font=("Arial", 10, "bold"))
    label.pack(side="left")

    style = ttk.Style()
    style.theme_use('clam')
    style.configure(f"{nome}.Horizontal.TProgressbar", 
                    troughcolor="#34495E", background=colors[i], thickness=20)

    progress = ttk.Progressbar(frame, orient="horizontal", length=300, 
                               mode="determinate", style=f"{nome}.Horizontal.TProgressbar")
    progress.pack(side="left", padx=10)

    percent_label = tk.Label(frame, text="0%", bg="#2C3E50", fg="white", font=("Arial", 10, "bold"))
    percent_label.pack(side="right")

    # Adicionar às listas para referência
    bars.append(progress)
    labels.append(percent_label)

# Executar o aplicativo
root.mainloop()
