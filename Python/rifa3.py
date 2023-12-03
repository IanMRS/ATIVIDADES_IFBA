import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QTextBrowser
from random import randint

class RifaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.participantes = []
        self.numeros_escolhidos = set()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sorteio de Rifa')
        self.setGeometry(300, 300, 400, 200)

        self.lbl_nome = QLabel('Nome:', self)
        self.txt_nome = QLineEdit(self)

        self.lbl_numeros = QLabel('Números (separados por vírgula):', self)
        self.txt_numeros = QLineEdit(self)

        self.btn_adicionar = QPushButton('Adicionar à Rifa', self)
        self.btn_adicionar.clicked.connect(self.adicionar_participante)

        self.btn_sortear = QPushButton('Realizar Sorteio', self)
        self.btn_sortear.clicked.connect(self.realizar_sorteio)

        self.btn_mostrar_numeros = QPushButton('Números Selecionados', self)
        self.btn_mostrar_numeros.clicked.connect(self.mostrar_numeros_selecionados)

        self.lbl_resultado = QLabel('', self)

        self.text_browser_numeros = QTextBrowser(self)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_nome)
        layout.addWidget(self.txt_nome)
        layout.addWidget(self.lbl_numeros)
        layout.addWidget(self.txt_numeros)
        layout.addWidget(self.btn_adicionar)
        layout.addWidget(self.btn_sortear)
        layout.addWidget(self.btn_mostrar_numeros)
        layout.addWidget(self.lbl_resultado)
        layout.addWidget(self.text_browser_numeros)

        self.setLayout(layout)

    def adicionar_participante(self):
        nome = self.txt_nome.text().strip()
        numeros_str = self.txt_numeros.text().strip()

        if nome and numeros_str:
            numeros = [int(num) for num in numeros_str.split(',')]

            # Verifica se algum número já foi escolhido por outro participante
            if any(num in self.numeros_escolhidos for num in numeros):
                QMessageBox.warning(self, 'Erro', 'Um ou mais números já foram escolhidos por outro participante.')
                return

            # Adiciona os números escolhidos ao conjunto global
            self.numeros_escolhidos.update(numeros)

            participante = {'nome': nome, 'numeros': numeros}
            self.participantes.append(participante)
            QMessageBox.information(self, 'Sucesso', 'Participante adicionado à rifa.')
        else:
            QMessageBox.warning(self, 'Erro', 'Por favor, insira nome e números válidos.')

        self.txt_nome.clear()
        self.txt_numeros.clear()

    def realizar_sorteio(self):
        if not self.participantes:
            QMessageBox.warning(self, 'Erro', 'A rifa está vazia. Adicione participantes antes de realizar o sorteio.')
            return

        numero_ganhador = randint(1, 100)
        ganhadores = []

        for participante in self.participantes:
            if numero_ganhador in participante['numeros']:
                ganhadores.append(participante['nome'])

        if ganhadores:
            ganhadores_str = ', '.join(ganhadores)
            mensagem = f'O número sorteado foi {numero_ganhador}. Parabéns ao ganhador(a): {ganhadores_str}!'
        else:
            mensagem = f'O número sorteado foi {numero_ganhador}. Não houve ganhadores desta vez.'

        self.lbl_resultado.setText(mensagem)

    def mostrar_numeros_selecionados(self):
        numeros_selecionados_str = ', '.join(map(str, sorted(self.numeros_escolhidos)))
        self.text_browser_numeros.setPlainText(f'Números Selecionados: {numeros_selecionados_str}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    rifa_app = RifaApp()
    rifa_app.show()
    sys.exit(app.exec_())
