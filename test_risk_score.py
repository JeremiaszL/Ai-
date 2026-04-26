import pytest
from risk_score import calculate_risk_score, get_risk_category

# --- TESTY LOGIKI OBLICZEŃ ---

def test_risk_logic():
    """Podstawowy test poprawności wzoru."""
    assert calculate_risk_score(50, 200, 150) == 15.5

def test_negative_values():
    """Test walidacji wartości ujemnych."""
    with pytest.raises(ValueError):
        calculate_risk_score(-10, 200, 150)

def test_zero_heart_rate():
    """Test walidacji tętna równego zero."""
    with pytest.raises(ValueError):
        calculate_risk_score(50, 200, 0)

def test_edge_case_low_risk():
    """Test dla osoby młodej z wysokim tętnem."""
    result = calculate_risk_score(20, 100, 220)
    assert result < 10.0

# --- MOJE DODATKOWE TESTY (EDGE CASES) ---

def test_heart_rate_near_zero():
    """Edge Case: Bardzo niskie tętno (1 bpm), co powinno podbić ryzyko."""
    # (50 * 0.2) + (200 * 0.05) - (1 * 0.03) = 19.97
    assert calculate_risk_score(50, 200, 1) == 19.97

def test_boundary_age_zero():
    """Edge Case: Wiek 0 (noworodek)."""
    # (0 * 0.2) + (200 * 0.05) - (150 * 0.03) = 10 - 4.5 = 5.5
    assert calculate_risk_score(0, 200, 150) == 5.5

# --- TESTY KATEGORYZACJI (PARAMETRYZOWANE) ---

@pytest.mark.parametrize("score, expected_category", [
    (9.99, "Niskie"),
    (10.0, "Średnie"),
    (19.99, "Średnie"),
    (20.0, "Wysokie"),
    (25.4, "Wysokie"),
])
def test_risk_categories(score, expected_category):
    """Sprawdza poprawność przypisywania kategorii dla progów punktowych."""
    assert get_risk_category(score) == expected_category
