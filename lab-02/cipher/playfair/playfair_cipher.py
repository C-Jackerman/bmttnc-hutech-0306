class PlayFairCipher:
    def __init__(self, key):
        self.key = self._generate_key_square(key)

    def _generate_key_square(self, key):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key = "".join(dict.fromkeys(key.upper().replace("J", "I") + alphabet))
        return [list(key[i:i+5]) for i in range(0, 25, 5)]

    def _find_position(self, letter):
        for row in range(5):
            for col in range(5):
                if self.key[row][col] == letter:
                    return row, col
        return None

    def _process_text(self, text):
        text = text.upper().replace("J", "I")
        processed_text = ""
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i+1] if i+1 < len(text) else "X"
            if a == b:
                processed_text += a + "X"
                i += 1
            else:
                processed_text += a + b
                i += 2
        if len(processed_text) % 2 != 0:
            processed_text += "X"
        return processed_text

    def encrypt(self, plain_text):
        text = self._process_text(plain_text)
        cipher_text = ""
        for i in range(0, len(text), 2):
            row1, col1 = self._find_position(text[i])
            row2, col2 = self._find_position(text[i+1])
            if row1 == row2:
                cipher_text += self.key[row1][(col1+1) % 5] + self.key[row2][(col2+1) % 5]
            elif col1 == col2:
                cipher_text += self.key[(row1+1) % 5][col1] + self.key[(row2+1) % 5][col2]
            else:
                cipher_text += self.key[row1][col2] + self.key[row2][col1]
        return cipher_text

    def decrypt(self, cipher_text):
        plain_text = ""
        for i in range(0, len(cipher_text), 2):
            row1, col1 = self._find_position(cipher_text[i])
            row2, col2 = self._find_position(cipher_text[i+1])
            if row1 == row2:
                plain_text += self.key[row1][(col1-1) % 5] + self.key[row2][(col2-1) % 5]
            elif col1 == col2:
                plain_text += self.key[(row1-1) % 5][col1] + self.key[(row2-1) % 5][col2]
            else:
                plain_text += self.key[row1][col2] + self.key[row2][col1]
        return plain_text
