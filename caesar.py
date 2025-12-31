def caesar_decrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base - key) % 26 + base)
        else:
            result += char

    return result
