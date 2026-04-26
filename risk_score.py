def calculate_risk_score(age, cholesterol, heart_rate):
    """
    Oblicza wskaźnik ryzyka na podstawie wieku, cholesterolu i tętna.
    
    Logika: (wiek * 0.2) + (cholesterol * 0.05) - (tętno * 0.03)
    """
    # Sprawdzenie typów danych (Type Safety)
    if not all(isinstance(x, (int, float)) for x in [age, cholesterol, heart_rate]):
        raise TypeError("Wszystkie argumenty muszą być liczbami (int lub float).")

    # Walidacja wartości logicznych
    if age < 0:
        raise ValueError("Wiek nie może być ujemny.")
    if cholesterol < 0:
        raise ValueError("Poziom cholesterolu nie może być ujemny.")
    if heart_rate <= 0:
        raise ValueError("Tętno musi być wartością dodatnią.")

    # Obliczenia
    score = (age * 0.2) + (cholesterol * 0.05) - (heart_rate * 0.03)
    
    return round(score, 2)
