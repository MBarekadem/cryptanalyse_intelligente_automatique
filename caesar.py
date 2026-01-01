def caesar_decrypt(text, key):
    # Cette fonction déchiffre un texte avec le chiffrement de César
    

    result = ""  # Variable pour stocker le texte déchiffré

    for char in text:  # Parcourt chaque caractère du texte

        if char.isalpha():  
            # Choisit la base selon majuscule ou minuscule
            base = ord('a') if char.islower() else ord('A')
            # Applique le décalage inverse pour déchiffrer
            result += chr((ord(char) - base - key) % 26 + base)
        else:
            # Garde les espaces et symboles inchangés
            result += char

    return result  
