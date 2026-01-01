from caesar import caesar_decrypt
from wordfreq import zipf_frequency


def score_with_wordfreq(text):
    # Calcule un score pour le français et l’anglais

    words = text.lower().split()  # Sépare le texte en mots dans une list
    score_fr = 0                  
    score_en = 0                  

    for w in words:               
        score_fr += zipf_frequency(w, "fr")  # Fréquence du mot en français
        score_en += zipf_frequency(w, "en")  # Fréquence du mot en anglais

    return score_fr, score_en     


def break_caesar(ciphertext):

    best_score = -1               # Meilleur score trouvé
    best_result = {               # un enregistrement du Résultat final
        "key": None,
        "text": "",
        "language": ""
    }

    for key in range(26):         # Teste toutes les clés possibles
        decrypted = caesar_decrypt(ciphertext, key)  # Déchiffre le texte

        # Calcule les scores linguistiques
        score_fr, score_en = score_with_wordfreq(decrypted)
        total_score = max(score_fr, score_en)

        # Affiche les résultats intermédiaires
        print(key, decrypted, "FR:", score_fr, "EN:", score_en)

        # Garde le meilleur résultat
        if total_score > best_score:
            best_score = total_score
            best_result["key"] = key
            best_result["text"] = decrypted
            
            best_result["language"] = "Français" if score_fr > score_en else "Anglais"

    return best_result 