cyphered_text = open("p59.txt", "r")
text = []
for line in cyphered_text:
    text = line.split(',')
text = [chr(int(x)) for x in text]

possible_keys = [chr(a) + chr(b) + chr(c) for a in range(97, 97+26) for b in range(97, 97+26) for c in range(97, 97+26)]

def decrypt(text, key):
    common_words = [' a ', ' the ']
    decrypted = []
    for i in range(0, len(text), 3):
        for j in range(3):
            if i + j >= len(text):
                break
            decrypted += [chr(ord(text[i + j]) ^ ord(key[j]))]

    decrypted_string = ''.join(decrypted)
    for word in common_words:
        if word in decrypted_string:
            print(''.join(decrypted_string))
            sum_ascii = 0
            for i in range(len(decrypted)):
                sum_ascii += ord(decrypted[i])
            print(sum_ascii)

for key in possible_keys:
    decrypt(text, key)
