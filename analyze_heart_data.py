import pandas as pd
import logging

def load_data(path: str) -> pd.DataFrame:
    """Ładuje dane z CSV z podstawową obsługą błędów."""
    try:
        return pd.read_csv(path)
    except Exception as e:
        logging.error(f"Błąd ładowania danych: {e}")
        return pd.DataFrame()

def basic_report(df: pd.DataFrame) -> dict:
    """Generuje rozszerzony raport o strukturze danych."""
    if df.empty:
        return {"error": "Pusty DataFrame"}

    report = {
        'rows': len(df),
        'columns': len(df.columns),
        'missing_values': int(df.isna().sum().sum()),
        'column_names': list(df.columns)
    }
    
    if 'target' in df.columns:
        report['target_distribution'] = df['target'].value_counts(normalize=True).to_dict()
        
    return report
