# from flask import Flask, render_template, request, json
# from cipher.caesar import CaesarCipher
# from cipher.vigenere import VigenereCipher
# from cipher.railfence import RailFenceCipher
# from cipher.playfair import PlayFairCipher
 
# app = Flask(__name__)
# #router routes for home page 

# @app.route("/")
# def home():
#     return render_template('index.html')

# #router routes for ceesar cypher
# @app.route("/caesar")
# def caesar():
#     return render_template('caesar.html')

# @app.route("/encrypt", methods=['POST'])
# def caesar_encrypt():
#     text = request.form['InputPlainText']
#     key = int(request.form['InputKeyText'])
#     Caesar = CaesarCipher()
#     encrypted_text = Caesar.encrypt_text(text, key)
#     return f"text: {text} <br/> Key: {key} <br/> encrypt text: {encrypted_text}"

# @app.route("/decrypt", methods = ['POST'])
# def caesar_decrypt():
#     text = request.form['InputCipherText']
#     key = int(request.form['InputKeyText'])
#     Caesar = CaesarCipher()
#     decrypted_text =  Caesar.decrypt_text(text, key)
#     return f"text: {text} <br/> Key: {key} <br/> decrypted text: {decrypted_text}"


# @app.route("/vigenere")
# def vigenere():
#     return render_template('vigenere.html')

# @app.route("/vigenere/encrypt", methods=['POST'])
# def vigenere_encrypt():
#     text = request.form['InputPlainText']
#     key = request.form['InputKeyText']
#     Vigenere = VigenereCipher()
#     encrypted_text = Vigenere.encrypt_text(text, key)
#     return f"text: {text} <br/> Key: {key} <br/> encrypt text: {encrypted_text}"

# @app.route("/vigenere/decrypt", methods=['POST'])
# def vigenere_decrypt():
#     text = request.form['InputCipherText']
#     key = request.form['InputKeyText']
#     Vigenere = VigenereCipher()
#     decrypted_text = Vigenere.decrypt_text(text, key)
#     return f"text: {text} <br/> Key: {key} <br/> decrypted text: {decrypted_text}"


# @app.route("/railfence")
# def railfence():
#     return render_template('railfence.html')

# @app.route("/railfence/encrypt", methods=['POST'])
# def railfence_encrypt():
#     text = request.form['InputPlainText']
#     key = int(request.form['InputKeyText'])
#     RailFence = RailFenceCipher()
#     encrypted_text = RailFence.rail_fence_encrypt(text, key)
#     return f"text: {text} <br/> Key: {key} <br/> Encrypted text: {encrypted_text}"

# @app.route("/railfence/decrypt", methods=['POST'])
# def railfence_decrypt():
#     text = request.form['InputCipherText']
#     key = int(request.form['InputKeyText'])
#     RailFence = RailFenceCipher()
#     decrypted_text = RailFence.rail_fence_decrypt(text, key)
#     return f"text: {text} <br/> Key: {key} <br/> Decrypted text: {decrypted_text}"


# @app.route("/playfair")
# def playfair():
#     return render_template('playfair.html')

# @app.route("/playfair/encrypt", methods=['POST'])
# def playfair_encrypt():
#     text = request.form['InputPlainText']
#     key = request.form['InputKeyText']
#     playfair_cipher = PlayFairCipher()
#     matrix = playfair_cipher.create_playfair_matrix(key)
#     encrypted_text = playfair_cipher.playfair_encrypt(text, matrix)
#     return f"Text: {text} <br/> Key: {key} <br/> Encrypted Text: {encrypted_text}"

# @app.route("/playfair/decrypt", methods=['POST'])
# def playfair_decrypt():
#     text = request.form['InputCipherText']
#     key = request.form['InputKeyText']
#     playfair_cipher = PlayFairCipher()
#     matrix = playfair_cipher.create_playfair_matrix(key)
#     decrypted_text = playfair_cipher.playfair_decrypt(text, matrix)
#     return f"Text: {text} <br/> Key: {key} <br/> Decrypted Text: {decrypted_text}"
# #main function
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port = 5050, debug = True)

import subprocess
import os
from flask import Flask

app = Flask(__name__)

# Lấy đường dẫn tuyệt đối của thư mục lab-03/ui
LAB_03_UI_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lab-03"))

@app.route("/")
def home():
    return """<h1>Chọn phương thức mã hóa:</h1>
              <ul>
                  <li><a href='/caesar'>Caesar</a></li>
                  <li><a href='/vigenere'>Vigenere</a></li>
                  <li><a href='/railfence'>Rail Fence</a></li>
                  <li><a href='/playfair'>Playfair</a></li>
              </ul>"""

@app.route("/caesar")
def open_caesar():
    script_path = os.path.join(LAB_03_UI_PATH, "caesar_cipher.py")
    subprocess.Popen(["python", script_path], shell=True)
    return "🔑 Đã mở ứng dụng Caesar trên desktop!"

@app.route("/vigenere")
def open_vigenere():
    script_path = os.path.join(LAB_03_UI_PATH, "vingenere_cipher.py")
    subprocess.Popen(["python", script_path], shell=True)
    return "🔑 Đã mở ứng dụng Vigenere trên desktop!"

@app.route("/railfence")
def open_railfence():
    script_path = os.path.join(LAB_03_UI_PATH, "railfence_cipher.py")
    subprocess.Popen(["python", script_path], shell=True)
    return "🔑 Đã mở ứng dụng Rail Fence trên desktop!"

@app.route("/playfair")
def open_playfair():
    script_path = os.path.join(LAB_03_UI_PATH, "playfair_cipher.py")
    subprocess.Popen(["python", script_path], shell=True)
    return "🔑 Đã mở ứng dụng Playfair trên desktop!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

