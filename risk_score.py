import unittest

 

def calculate_risk_score(age: int, cholesterol: int, max_heart_rate: int) -> float:
    if age < 0 or cholesterol < 0 or max_heart_rate <= 0:
        raise ValueError('All parameters must be positive.')
    score = age * 0.2 + cholesterol * 0.05 - max_heart_rate * 0.03
    return round(score, 2)

 

class TestCalculateRiskScore(unittest.TestCase):
    # --- PROPOZYCJE TESTÓW OD AI ---

 

    def test_normal_values(self):
        # Sprawdzamy standardowe poprawne parametry
        # Obliczenia: 30*0.2 (6) + 200*0.05 (10) - 150*0.03 (4.5) = 11.5
        self.assertEqual(calculate_risk_score(30, 200, 150), 11.5)

 

    def test_high_risk_values(self):
        # Sprawdzamy wyższe wartości ryzyka
        # Obliczenia: 80*0.2 (16) + 300*0.05 (15) - 100*0.03 (3) = 28.0
        self.assertEqual(calculate_risk_score(80, 300, 100), 28.0)

 

    def test_invalid_age(self):
        # Sprawdzamy, czy ujemny wiek wywoła błąd
        with self.assertRaises(ValueError):
            calculate_risk_score(-10, 200, 150)

 

    def test_invalid_cholesterol(self):
        # Sprawdzamy, czy ujemny cholesterol wywoła błąd
        with self.assertRaises(ValueError):
            calculate_risk_score(30, -5, 150)

 

    def test_invalid_heart_rate_zero(self):
        # Sprawdzamy tętno równe 0 (powinno wywołać błąd wg warunku <= 0)
        with self.assertRaises(ValueError):
            calculate_risk_score(30, 200, 0)

    # --- TWÓJ WŁASNY TEST EDGE CASE (DODANY PONIŻEJ) ---
    def test_edge_case_boundaries(self):
        # Test na absolutnych granicach dopuszczonych przez instrukcję warunkową.
        # Wiek i cholesterol mogą być zerem (warunek to < 0), a tętno musi być > 0 (dajemy 1).
        # Obliczenia: 0*0.2 (0) + 0*0.05 (0) - 1*0.03 (-0.03) = -0.03
        self.assertEqual(calculate_risk_score(0, 0, 1), -0.03)

 

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)
