from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
 
app = Flask(__name__)
#router routes for home page 

@app.route("/")
def home():
    return render_template('index.html')

#router routes for ceesar cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['InputPlainText']
    key = int(request.form['InputKeyText'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text} <br/> Key: {key} <br/> encrypt text: {encrypted_text}"

@app.route("/decrypt", methods = ['POST'])
def caesar_decrypt():
    text = request.form['InputCipherText']
    key = int(request.form['InputKeyText'])
    Caesar = CaesarCipher()
    decrypted_text =  Caesar.decrypt_text(text, key)
    return f"text: {text} <br/> Key: {key} <br/> decrypted text: {decrypted_text}"


@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['InputPlainText']
    key = request.form['InputKeyText']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.encrypt_text(text, key)
    return f"text: {text} <br/> Key: {key} <br/> encrypt text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['InputCipherText']
    key = request.form['InputKeyText']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.decrypt_text(text, key)
    return f"text: {text} <br/> Key: {key} <br/> decrypted text: {decrypted_text}"


@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['InputPlainText']
    key = int(request.form['InputKeyText'])
    RailFence = RailFenceCipher()
    encrypted_text = RailFence.rail_fence_encrypt(text, key)
    return f"text: {text} <br/> Key: {key} <br/> Encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['InputCipherText']
    key = int(request.form['InputKeyText'])
    RailFence = RailFenceCipher()
    decrypted_text = RailFence.rail_fence_decrypt(text, key)
    return f"text: {text} <br/> Key: {key} <br/> Decrypted text: {decrypted_text}"


@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['InputPlainText']
    key = request.form['InputKeyText']
    playfair_cipher = PlayFairCipher()
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(text, matrix)
    return f"Text: {text} <br/> Key: {key} <br/> Encrypted Text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['InputCipherText']
    key = request.form['InputKeyText']
    playfair_cipher = PlayFairCipher()
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(text, matrix)
    return f"Text: {text} <br/> Key: {key} <br/> Decrypted Text: {decrypted_text}"
#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5050, debug = True)