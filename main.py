from brute_force import break_caesar

def main():
    ciphertext =input("Message chiffré :")
    print("\n--- Cryptanalyse automatique (FR / EN) ---\n")

    result = break_caesar(ciphertext)

    print("Clé détectée :", result["key"])
    print("Langue détectée :", result["language"])
    print("Score :", result["score"])
    print("\nTexte clair probable :\n")
    print(result["text"])

if __name__ == "__main__":
    main()
