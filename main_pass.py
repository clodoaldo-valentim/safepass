import sys
import random
import string
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QListWidget, QLabel, QMessageBox)
from crypto_manager import GerenciadorSeguranca

class SafePassApp(QWidget):
    def __init__(self):
        super().__init__()
        self.seguranca = GerenciadorSeguranca()
        self.setWindowTitle("SafePass - Gestor de Senhas")
        self.setFixedSize(400, 500)

        self.layout = QVBoxLayout()

        # Inputs
        self.in_site = QLineEdit(); self.in_site.setPlaceholderText("Site/Serviço (ex: Netflix)")
        self.in_senha = QLineEdit(); self.in_senha.setPlaceholderText("Senha")
        
        # Botões de Ação
        layout_btns = QHBoxLayout()
        btn_gerar = QPushButton("Gerar Senha Forte")
        btn_gerar.clicked.connect(self.gerar_senha_aleatoria)
        btn_salvar = QPushButton("Guardar")
        btn_salvar.setStyleSheet("background-color: #2ecc71; color: white;")
        btn_salvar.clicked.connect(self.guardar_senha)
        
        layout_btns.addWidget(btn_gerar)
        layout_btns.addWidget(btn_salvar)

        # Lista de Senhas (Visualizamos o site, a senha fica oculta)
        self.lista_senhas = QListWidget()
        self.lista_senhas.itemDoubleClicked.connect(self.revelar_senha)

        self.layout.addWidget(QLabel("🔒 Novo Registo:"))
        self.layout.addWidget(self.in_site)
        self.layout.addWidget(self.in_senha)
        self.layout.addLayout(layout_btns)
        self.layout.addWidget(QLabel("📋 Clique duplo para copiar a senha:"))
        self.layout.addWidget(self.lista_senhas)
        
        self.setLayout(self.layout)
        self.senhas_memoria = {} # Simulando o banco de dados para este exemplo rápido

    def gerar_senha_aleatoria(self):
        caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
        senha = "".join(random.choice(caracteres) for _ in range(12))
        self.in_senha.setText(senha)

    def guardar_senha(self):
        site = self.in_site.text()
        senha = self.in_senha.text()
        if site and senha:
            # CRIPTOGRAFIA EM AÇÃO
            senha_secreta = self.seguranca.criptografar(senha)
            self.senhas_memoria[site] = senha_secreta
            self.lista_senhas.addItem(f"{site} (Protegido)")
            self.in_site.clear(); self.in_senha.clear()

    def revelar_senha(self, item):
        site = item.text().replace(" (Protegido)", "")
        senha_cripto = self.senhas_memoria[site]
        # DESCRIPTOGRAFIA EM AÇÃO
        senha_real = self.seguranca.descriptografar(senha_cripto)
        
        # Copia para o Clipboard (Área de transferência)
        QApplication.clipboard().setText(senha_real)
        QMessageBox.information(self, "Sucesso", f"A senha para {site} foi copiada!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SafePassApp()
    window.show()
    sys.exit(app.exec())