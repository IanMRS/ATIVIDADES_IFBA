import tkinter as tk
from tkinter import messagebox
from random import randint

class RifaApp:
    def __init__(self, root):
        self.participantes = []
        self.numeros_escolhidos = set()
        self.initUI(root)

    def initUI(self, root):
        root.title('Sorteio de Rifa')
        root.geometry('400x200')

        self.lbl_nome = tk.Label(root, text='Nome:')
        self.txt_nome = tk.Entry(root)

        self.lbl_numeros = tk.Label(root, text='Números (separados por vírgula):')
        self.txt_numeros = tk.Entry(root)

        self.btn_adicionar = tk.Button(root, text='Adicionar à Rifa', command=self.adicionar_participante)
        self.btn_sortear = tk.Button(root, text='Realizar Sorteio', command=self.realizar_sorteio)
        self.btn_mostrar_numeros = tk.Button(root, text='Números Selecionados', command=self.mostrar_numeros_selecionados)

        self.lbl_resultado = tk.Label(root, text='')

        self.text_browser_numeros = tk.Text(root)

        self.lbl_nome.pack()
        self.txt_nome.pack()
        self.lbl_numeros.pack()
        self.txt_numeros.pack()
        self.btn_adicionar.pack()
        self.btn_sortear.pack()
        self.btn_mostrar_numeros.pack()
        self.lbl_resultado.pack()
        self.text_browser_numeros.pack()

    def adicionar_participante(self):
        nome = self.txt_nome.get().strip()
        numeros_str = self.txt_numeros.get().strip()

        if nome and numeros_str:
            numeros = [int(num) for num in numeros_str.split(',')]

            if any(num in self.numeros_escolhidos for num in numeros):
                messagebox.showwarning('Erro', 'Um ou mais números já foram escolhidos por outro participante.')
                return

            self.numeros_escolhidos.update(numeros)

            participante = {'nome': nome, 'numeros': numeros}
            self.participantes.append(participante)
            messagebox.showinfo('Sucesso', 'Participante adicionado à rifa.')
        else:
            messagebox.showwarning('Erro', 'Por favor, insira nome e números válidos.')

        self.txt_nome.delete(0, tk.END)
        self.txt_numeros.delete(0, tk.END)

    def realizar_sorteio(self):
        if not self.participantes:
            messagebox.showwarning('Erro', 'A rifa está vazia. Adicione participantes antes de realizar o sorteio.')
            return

        numero_ganhador = randint(1, 100)
        ganhadores = [participante['nome'] for participante in self.participantes if numero_ganhador in participante['numeros']]

        if ganhadores:
            ganhadores_str = ', '.join(ganhadores)
            mensagem = f'O número sorteado foi {numero_ganhador}. Parabéns ao ganhador(a): {ganhadores_str}!'
        else:
            mensagem = f'O número sorteado foi {numero_ganhador}. Não houve ganhadores desta vez.'

        self.lbl_resultado.config(text=mensagem)

    def mostrar_numeros_selecionados(self):
        numeros_selecionados_str = ', '.join(map(str, sorted(self.numeros_escolhidos)))
        self.text_browser_numeros.delete(1.0, tk.END)
        self.text_browser_numeros.insert(tk.END, f'Números Selecionados: {numeros_selecionados_str}')

if __name__ == '__main__':
    root = tk.Tk()
    app = RifaApp(root)
    root.mainloop()
