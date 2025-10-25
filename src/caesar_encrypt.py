# main.py
ALPHABET_SIZE = 26
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.islower():
            result += chr((ord(char) - ord('a') + shift) % ALPHABET_SIZE + ord('a'))
        elif char.isupper():
            result += chr((ord(char) - ord('A') + shift) % ALPHABET_SIZE + ord('A'))
        else:
            result += char
    return result
def crack_caesar(file_in, file_out):
    with open(file_in, "r") as f:
        secret_text = f.read()
    for shift in range(ALPHABET_SIZE):
        decrypted = caesar_encrypt(secret_text, -shift)
        if " " in decrypted:
            with open(file_out, "w") as f_out:
                f_out.write(decrypted)
            print(f"Decrypted with shift={shift}:")
            print(decrypted)
            break

if __name__ == "__main__":
    original_text = "hello world"
    encrypted_text = caesar_encrypt(original_text, 3)
    print(f"Original: {original_text}")
    print(f"Encrypted: {encrypted_text}") # Expected: "khoor zruog"