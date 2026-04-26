def calculate_risk_score(age: int, cholesterol: int, max_heart_rate: int) -> float:
    """
    Oblicza wskaźnik ryzyka na podstawie wieku, cholesterolu i tętna.
    Wzór: (wiek * 0.2) + (cholesterol * 0.05) - (tętno * 0.03)
    """
    if age < 0 or cholesterol < 0 or max_heart_rate <= 0:
        raise ValueError('All parameters must be positive.')

    score = age * 0.2 + cholesterol * 0.05 - max_heart_rate * 0.03
    return round(score, 2)

def get_risk_category(score: float) -> str:
    """
    Klasyfikuje wynik punktowy do odpowiedniej grupy ryzyka.
    """
    if score < 10:
        return "Niskie"
    elif 10 <= score < 20:
        return "Średnie"
    else:
        return "Wysokie"

if __name__ == "__main__":
    # Przykład użycia konsolowego
    try:
        a, c, h = 50, 200, 150
        s = calculate_risk_score(a, c, h)
        print(f"Wynik dla ({a}, {c}, {h}): {s} -> Kategoria: {get_risk_category(s)}")
    except Exception as e:
        print(f"Błąd: {e}")
