from cryptography.fernet import Fernet

class GerenciadorSeguranca:
    def __init__(self):
        # Em um app real, a chave seria gerada a partir da senha mestra
        # Aqui, vamos gerar uma fixa para fins didáticos
        self.chave = b'uV8-p-R_G7S9Wp8Z2b6N-7-M8z2Z8w9X0Y1Z2A3B4C5=' 
        self.fernet = Fernet(self.chave)

    def criptografar(self, texto_puro):
        return self.fernet.encrypt(texto_puro.encode()).decode()

    def descriptografar(self, texto_cripto):
        return self.fernet.decrypt(texto_cripto.encode()).decode()