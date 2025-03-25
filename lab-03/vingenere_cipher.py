import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.vingenere import Ui_MainWindow  # Đảm bảo đường dẫn đúng
import requests

class VigenereApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.VinEn.clicked.connect(self.call_api_encrypt)
        self.ui.VinDe.clicked.connect(self.call_api_decrypt)
        
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
        payload = {
            "plain_text": self.ui.plainVin.toPlainText(),
            "key": self.ui.keyVin.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainDe.setPlainText(data["encrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted successfully")
                msg.exec_()
            else:
                QMessageBox.warning(self, "Error", "Failed to encrypt text")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "API Error", str(e))
    
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
        payload = {
            "cipher_text": self.ui.plainDe.toPlainText(),
            "key": self.ui.keyVin.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainVin.setPlainText(data["decrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted successfully")
                msg.exec_()
            else:
                QMessageBox.warning(self, "Error", "Failed to decrypt text")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "API Error", str(e))
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VigenereApp()
    window.show()
    sys.exit(app.exec_())
