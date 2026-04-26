import pandas as pd
import logging
from typing import Optional, Dict, Any

# Konfiguracja logowania dla lepszej diagnostyki
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def load_data(path: str) -> pd.DataFrame:
    """
    Ładuje dane z pliku CSV. 
    Używa FileNotFoundError i pd.errors.EmptyDataError dla precyzyjnej obsługi błędów.
    """
    try:
        df = pd.read_csv(path)
        logging.info(f"Pomyślnie załadowano dane z: {path}")
        return df
    except FileNotFoundError:
        logging.error(f"Nie znaleziono pliku pod ścieżką: {path}")
    except pd.errors.EmptyDataError:
        logging.error("Plik CSV jest pusty.")
    except Exception as e:
        logging.error(f"Nieoczekiwany błąd podczas ładowania: {e}")
    
    return pd.DataFrame()

def basic_report(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Generuje raport o strukturze DataFrame.
    Dodano walidację typów i bardziej opisowe nazwy kluczy.
    """
    if not isinstance(df, pd.DataFrame) or df.empty:
        return {"status": "error", "message": "Brak danych do analizy"}

    report = {
        'metadata': {
            'rows_count': len(df),
            'cols_count': len(df.columns),
            'total_missing': int(df.isna().sum().sum()),
        },
        'schema': {
            'columns': list(df.columns),
            'dtypes': df.dtypes.astype(str).to_dict()
        }
    }
    
    # Analiza kolumny docelowej (target)
    if 'target' in df.columns:
        report['analysis'] = {
            'target_distribution': df['target'].value_counts(normalize=True).round(4).to_dict()
        }
        
    return report

# Heart Data Analyzer 🩺
Proste narzędzie do wstępnej analizy zbiorów danych kardiologicznych.

### Funkcjonalności:
- **Bezpieczne ładowanie plików**: Odporność na brak plików i błędny format CSV.
- **Raportowanie**: Szybki podgląd wymiarów danych, brakujących wartości i rozkładu klas.

### Wymagania:
- `pandas`
- `python 3.8+`

### Przykład użycia:
```python
df = load_data("heart.csv")
report = basic_report(df)
print(f"Liczba wierszy: {report['metadata']['rows_count']}")
