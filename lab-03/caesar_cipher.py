import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):  # Sửa lỗi "def__init__" thành "def __init__"
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)  # Sửa lỗi "pushButtons" thành "pushButton"
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)
        
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.plainTextEdit.toPlainText(),  # Sửa "text()" thành "toPlainText()"
            "key": self.ui.textEdit_2.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit_2.setPlainText(data["encrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)  # Sửa "QMessageBox.information" thành "QMessageBox.Information"
                msg.setText("Encrypted successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))  # Sửa "e.message" thành "str(e)"
    
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.plainTextEdit_2.toPlainText(),  # Sửa "toText()" thành "toPlainText()"
            "key": self.ui.textEdit_2.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit.setPlainText(data["decrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)  # Sửa "QMessageBox.information" thành "QMessageBox.Information"
                msg.setText("Decrypted successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))  # Sửa "e.message" thành "str(e)"
            
if __name__ == "__main__":  # Sửa "if__name__" thành "if __name__"
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())