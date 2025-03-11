class RailFenceCipher:
    def __init__(self, rails: int):
        self.rails = rails

    def encrypt_text(self, text: str) -> str:
        if self.rails <= 1:
            return text

        rail_matrix = [''] * self.rails
        rail_index = 0
        step = 1

        for char in text:
            rail_matrix[rail_index] += char
            rail_index += step

            if rail_index == 0 or rail_index == self.rails - 1:
                step *= -1  # Đảo chiều di chuyển

        return ''.join(rail_matrix)

    def decrypt_text(self, cipher_text: str) -> str:
        if self.rails <= 1:
            return cipher_text

        rail_lengths = [0] * self.rails
        rail_index = 0
        step = 1

        # Xác định độ dài của từng đường ray
        for _ in cipher_text:
            rail_lengths[rail_index] += 1
            rail_index += step

            if rail_index == 0 or rail_index == self.rails - 1:
                step *= -1  # Đảo chiều di chuyển

        rail_chars = []
        index = 0

        # Cắt từng đoạn của ciphertext vào rail_chars
        for length in rail_lengths:
            rail_chars.append(list(cipher_text[index:index + length]))
            index += length

        # Giải mã từ đường ray
        rail_index = 0
        step = 1
        decrypted_text = []

        for _ in cipher_text:
            decrypted_text.append(rail_chars[rail_index].pop(0))
            rail_index += step

            if rail_index == 0 or rail_index == self.rails - 1:
                step *= -1  # Đảo chiều di chuyển

        return ''.join(decrypted_text)
