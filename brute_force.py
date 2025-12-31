from caesar import caesar_decrypt
from wordfreq import zipf_frequency


def score_with_wordfreq(text):
    words = text.lower().split()
    score_fr = 0
    score_en = 0

    for w in words:
        score_fr += zipf_frequency(w, "fr")
        score_en += zipf_frequency(w, "en")

    return score_fr, score_en


def break_caesar(ciphertext):
    best_score = -1
    best_result = {
        "key": None,
        "text": "",
        "score": 0,
        "language": ""
    }

    for key in range(26):
        decrypted = caesar_decrypt(ciphertext, key)

        score_fr, score_en = score_with_wordfreq(decrypted)
        total_score = max(score_fr, score_en)

        print(key, decrypted, "FR:", score_fr, "EN:", score_en)

        if total_score > best_score:
            best_score = total_score
            best_result["key"] = key
            best_result["text"] = decrypted
            best_result["score"] = total_score
            best_result["language"] = "Français" if score_fr > score_en else "Anglais"

    return best_result
