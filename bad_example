def average_age(records):
    # BŁĄD 2: Zakładałem naiwnie, że lista nigdy nie będzie pusta.
    # Jakby była, to na końcu dzieliłbym przez zero. Zabezpieczam to od razu.
    if not records:
        return 0

    total = 0
    valid_records_count = 0

    for record in records:
        # BŁĄD 3: Zbyt ufnie podszedłem do danych. Sprawdzam, czy klucz 'age' w ogóle istnieje,
        # żeby nie dostać w twarz błędem KeyError.
        if 'age' in record:
            try:
                # BŁĄD 4: Nie wziąłem pod uwagę, że ktoś wpisze tekst. 
                # Próbuję to na siłę przerobić na liczbę (float).
                age = float(record['age'])
                total += age
                # Dodaję 1 do licznika tylko wtedy, gdy udało się poprawnie odczytać wiek
                valid_records_count += 1
            except (ValueError, TypeError):
                # Jak się nie da przerobić na liczbę (np. ktoś wpisał "nieznany"), 
                # to łapię błąd i po prostu ignoruję ten wpis (idę dalej).
                continue

    # BŁĄD 5 (O TYM ZAPOMNIAŁEM NAJBARDZIEJ!): 
    # Co jeśli nikt na liście nie podał poprawnego wieku, albo wywaliłem wszystkich przez złe dane?
    # Mój licznik wynosiłby 0 i znowu dzieliłbym przez zero (ZeroDivisionError).
    # Dodaję tego ifa, żeby upewnić się, że mam przez co dzielić.
    if valid_records_count == 0:
        return 0

    # BŁĄD 1 (Mój główny błąd): Zjadłem "s" i dzieliłem przez len(record) zamiast liczby osób.
    # Teraz dzielę sumę przez mój nowy licznik poprawnych, zliczonych osób.
    return total / valid_records_count

 

 

if __name__ == '__main__':
    # Wrzuciłem tu wszystkie dziwne przypadki, żeby udowodnić, że mój kod teraz to przetrwa
    sample = [
        {'name': 'Anna', 'age': 21},
        {'name': 'Piotr', 'age': 23},
        {'name': 'Maria', 'age': 25},
        {'name': 'Krzysztof'},               # Brak wieku (ominie)
        {'name': 'Zofia', 'age': '20'},      # Wiek jako tekst (przekonwertuje)
        {'name': 'Jan', 'age': 'nieznany'},  # Zły tekst (ominie)
    ]

    # Odpalam i patrzę jak działa!
    print(average_age(sample))
