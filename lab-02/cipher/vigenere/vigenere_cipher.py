from cipher.caesar.alphabet import ALPHABET

class VigenereCipher:
    def __init__(self):
        self.alphabet = ALPHABET
        self.alphabet_len = len(ALPHABET)

    def repeat_key(self, key: str, text_length: int) -> str:
        key = key.upper()
        return (key * (text_length // len(key))) + key[:text_length % len(key)]

    def encrypt_text(self, text: str, key: str) -> str:
        text = text.upper()
        key = self.repeat_key(key, len(text))
        encrypted_text = []

        for i, letter in enumerate(text):
            if letter in self.alphabet:
                text_index = self.alphabet.index(letter)
                key_index = self.alphabet.index(key[i])
                encrypted_index = (text_index + key_index) % self.alphabet_len
                encrypted_text.append(self.alphabet[encrypted_index])
            else:
                encrypted_text.append(letter)  # Giữ nguyên ký tự không phải chữ cái

        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: str) -> str:
        text = text.upper()
        key = self.repeat_key(key, len(text))
        decrypted_text = []

        for i, letter in enumerate(text):
            if letter in self.alphabet:
                text_index = self.alphabet.index(letter)
                key_index = self.alphabet.index(key[i])
                decrypted_index = (text_index - key_index) % self.alphabet_len
                decrypted_text.append(self.alphabet[decrypted_index])
            else:
                decrypted_text.append(letter)

        return "".join(decrypted_text)
