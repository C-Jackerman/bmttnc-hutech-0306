import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_MainWindow  # Đảm bảo đường dẫn đúng
import requests

class PlayfairApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.enPlay.clicked.connect(self.call_api_encrypt)
        self.ui.dePlay.clicked.connect(self.call_api_decrypt)
        
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.ui.plainTextEdit.toPlainText(),
            "key": self.ui.plainTextEdit_2.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit_3.setPlainText(data["encrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted successfully")
                msg.exec_()
            else:
                QMessageBox.warning(self, "Error", "Failed to encrypt text")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "API Error", str(e))
    
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text": self.ui.plainTextEdit_3.toPlainText(),
            "key": self.ui.plainTextEdit_2.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit.setPlainText(data["decrypted_message"])
                
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
    window = PlayfairApp()
    window.show()
    sys.exit(app.exec_())
