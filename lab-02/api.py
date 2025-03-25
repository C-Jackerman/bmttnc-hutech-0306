from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

# Initialize ciphers
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data.get('plain_text', '')
    key = data.get('key', 0)
    try:
        key = int(key)
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        return jsonify({'encrypted_message': encrypted_text})
    except ValueError:
        return jsonify({'error': 'Invalid key. Key must be an integer.'}), 400

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', 0)
    try:
        key = int(key)
        decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
        return jsonify({'decrypted_message': decrypted_text})
    except ValueError:
        return jsonify({'error': 'Invalid key. Key must be an integer.'}), 400

@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    encrypted_text = vigenere_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    decrypted_text = vigenere_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    data = request.json
    plain_text = data.get('plain_text', '')
    rails = data.get('rails', 0)
    try:
        rails = int(rails)
        cipher = RailFenceCipher(rails)
        encrypted_text = cipher.encrypt_text(plain_text)
        return jsonify({'encrypted_message': encrypted_text})
    except ValueError:
        return jsonify({'error': 'Invalid rails value. Must be an integer.'}), 400

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text', '')
    rails = data.get('rails', 0)
    try:
        rails = int(rails)
        cipher = RailFenceCipher(rails)
        decrypted_text = cipher.decrypt_text(cipher_text)
        return jsonify({'decrypted_message': decrypted_text})
    except ValueError:
        return jsonify({'error': 'Invalid rails value. Must be an integer.'}), 400

@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    data = request.json
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    cipher = PlayFairCipher(key)
    encrypted_text = cipher.encrypt(plain_text)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    cipher = PlayFairCipher(key)
    decrypted_text = cipher.decrypt(cipher_text)
    return jsonify({'decrypted_message': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
