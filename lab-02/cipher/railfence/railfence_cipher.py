class RailFenceCipher:
    def __init__(self, num_rails):
        self.num_rails = int(num_rails)  # Lưu số đường ray

    def encrypt_text(self, plain_text):
        rails = [[] for _ in range(self.num_rails)]
        rail_index = 0
        direction = 1 
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == self.num_rails - 1:
                direction = -1
            rail_index += direction
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def decrypt_text(self, cipher_text):
        rail_lengths = [0] * self.num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1  
            if rail_index == 0:
                direction = 1
            elif rail_index == self.num_rails - 1:
                direction = -1
            rail_index += direction

        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(cipher_text[start:start + length])
            start += length

        plain_text = ""
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index][0]
            rails[rail_index] = rails[rail_index][1:]
            if rail_index == 0:
                direction = 1
            elif rail_index == self.num_rails - 1:
                direction = -1
            rail_index += direction
            
        return plain_text
