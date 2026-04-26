import pandas as pd
import logging

def load_data(path: str) -> pd.DataFrame:
    """Ładuje dane z obsługą błędów ścieżki i formatu."""
    try:
        df = pd.read_csv(path)
        if df.empty:
            logging.warning("Załadowany plik jest pusty.")
            return pd.DataFrame()
        return df
    except Exception as e:
        logging.error(f"Nie udało się załadować danych: {e}")
        return pd.DataFrame()

def basic_report(df: pd.DataFrame) -> dict:
    """Rozbudowany raport z walidacją wejścia."""
    # Moja poprawka: Walidacja czy wejście jest poprawnym DataFrame
    if not isinstance(df, pd.DataFrame) or df.empty:
        return {"error": "Nieprawidłowy lub pusty obiekt DataFrame"}

    report = {
        'rows': len(df),
        'columns': len(df.columns),
        'missing_values': int(df.isna().sum().sum()),
        'duplicates': int(df.duplicated().sum()), # Nowość: duplikaty
        'memory_usage_kb': round(df.memory_usage(deep=True).sum() / 1024, 2) # Nowość: pamięć
    }
    
    # Rozbudowa o statystyki wieku, jeśli kolumna istnieje
    if 'age' in df.columns:
        report['age_stats'] = {
            'mean': round(df['age'].mean(), 1),
            'min': int(df['age'].min()),
            'max': int(df['age'].max())
        }

    if 'target' in df.columns:
        report['target_distribution'] = df['target'].value_counts().to_dict()
        
    return report

if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/plotly/datasets/master/heart.csv'
    data = load_data(url)
    
    report = basic_report(data)
    
    # Wyświetlenie raportu w czytelny sposób
    import pprint
    pprint.pprint(report)
