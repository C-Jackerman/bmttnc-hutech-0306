import numpy as np

class PlayfairCipher:
    def __init__(self, key):
        self.key = key
        self.matrix = self._generate_matrix(key)

    def _generate_matrix(self, key):
        key = key.upper().replace("J", "I")
        key_set = []
        for char in key:
            if char not in key_set and char.isalpha():
                key_set.append(char)
        
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in key_set:
                key_set.append(char)
        
        return np.array(key_set).reshape(5, 5)

    def _find_position(self, letter):
        row, col = np.where(self.matrix == letter)
        return row[0], col[0]

    def encrypt(self, text):
        text = text.upper().replace("J", "I").replace(" ", "")
        pairs = []
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i+1] if i + 1 < len(text) else 'X'
            if a == b:
                pairs.append((a, 'X'))
                i += 1
            else:
                pairs.append((a, b))
                i += 2
        
        encrypted_text = ""
        for a, b in pairs:
            row1, col1 = self._find_position(a)
            row2, col2 = self._find_position(b)
            
            if row1 == row2:
                encrypted_text += self.matrix[row1, (col1 + 1) % 5]
                encrypted_text += self.matrix[row2, (col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += self.matrix[(row1 + 1) % 5, col1]
                encrypted_text += self.matrix[(row2 + 1) % 5, col2]
            else:
                encrypted_text += self.matrix[row1, col2]
                encrypted_text += self.matrix[row2, col1]
        
        return encrypted_text

    def decrypt(self, text):
        text = text.upper().replace(" ", "")
        decrypted_text = ""
        
        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]
            row1, col1 = self._find_position(a)
            row2, col2 = self._find_position(b)
            
            if row1 == row2:
                decrypted_text += self.matrix[row1, (col1 - 1) % 5]
                decrypted_text += self.matrix[row2, (col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += self.matrix[(row1 - 1) % 5, col1]
                decrypted_text += self.matrix[(row2 - 1) % 5, col2]
            else:
                decrypted_text += self.matrix[row1, col2]
                decrypted_text += self.matrix[row2, col1]
        
        return decrypted_text
