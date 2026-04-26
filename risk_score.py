import pytest
from risk_score import calculate_risk_score

def test_risk_logic():
    # Dane: wiek=50, chol=200, hr=150 -> (10 + 10 - 4.5) = 15.5
    assert calculate_risk_score(50, 200, 150) == 15.5

def test_negative_values():
    with pytest.raises(ValueError):
        calculate_risk_score(-10, 200, 150)

def test_zero_heart_rate():
    with pytest.raises(ValueError):
        calculate_risk_score(50, 200, 0)

# Mój Edge Case: Bardzo wysokie tętno przy niskim wieku/cholesterolu (wynik ujemny)
def test_edge_case_low_risk():
    result = calculate_risk_score(20, 100, 220)
    assert result < 10.0
