# from flask import Flask, request, jsonify
# from cipher.caesar import CaesarCipher
# app = Flask(__name__)

# caesar_cipher = CaesarCipher()

# @app.route("/api/caesar/encrypt", methods = ["POST"])

# def caesar_encrypt():
#     data = request.json
#     plain_text = data['plain_text']
#     key = int(data['key'])
#     encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
#     return jsonify({'encrypted_message': encrypted_text})

# @app.route("/api/caesar/decrypt", methods  = ["POST"])
# def caesar_decrypt():
#     data = request.json
#     cipher_text = data['cipher_text']
#     key = int(data['key'])
#     decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
#     return jsonify({'decrypted_message': decrypted_text})

# if __name__ == "__main__":
#     app.run(host = "0.0.0.0", port = 5000, debug = True)

# ////////////////////////////////////////////////////////
# from flask import Flask, request, jsonify
# from cipher.vigenere.vigenere_cipher import VigenereCipher

# app = Flask(__name__)

# vigenere_cipher = VigenereCipher()

# @app.route("/api/vigenere/encrypt", methods=["POST"])
# def vigenere_encrypt():
#     data = request.json
#     plain_text = data['plain_text']
#     key = data['key']
#     encrypted_text = vigenere_cipher.encrypt_text(plain_text, key)
#     return jsonify({'encrypted_message': encrypted_text})

# @app.route("/api/vigenere/decrypt", methods=["POST"])
# def vigenere_decrypt():
#     data = request.json
#     cipher_text = data['cipher_text']
#     key = data['key']
#     decrypted_text = vigenere_cipher.decrypt_text(cipher_text, key)
#     return jsonify({'decrypted_message': decrypted_text})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)

#///////////////////////////////////////////////////
from flask import Flask, request, jsonify
from cipher.railfence.railfence_cipher import RailFenceCipher

app = Flask(__name__)

@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    rails = int(data['rails'])
    cipher = RailFenceCipher(rails)
    encrypted_text = cipher.encrypt_text(plain_text)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    rails = int(data['rails'])
    cipher = RailFenceCipher(rails)
    decrypted_text = cipher.decrypt_text(cipher_text)
    return jsonify({'decrypted_message': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
