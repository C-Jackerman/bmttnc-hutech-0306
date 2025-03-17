import math

class TranspositionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        text = text.replace(" ", "")
        ciphertext = [''] * self.key

        for col in range(self.key):
            pointer = col
            while pointer < len(text):
                ciphertext[col] += text[pointer]
                pointer += self.key

        return ''.join(ciphertext)

    def decrypt(self, text):
        num_cols = math.ceil(len(text) / self.key)
        num_rows = self.key
        num_shaded_boxes = (num_cols * num_rows) - len(text)

        plaintext = [''] * num_cols
        col, row = 0, 0

        for symbol in text:
            plaintext[col] += symbol
            col += 1  

            if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1

        return ''.join(plaintext)
