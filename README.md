# GDDKIA-Parser
Pobierz historyczne zdjęcia z kamer (Generalna Dyrekcja Dróg Krajowych i Autostrad)

## Informacja

* skrypt prototype.py jest prototypem działania skryptu. Z jego możliwością można pobrać dane z kamer z *całego miesiąca* 
* skrypt *NIE* jest działającym rozwiązaniem.
* nie zachęcam do używania skryptu, może on obciążać serwery GDDKIA

## TODO
* pobieranie kamer od użytkownika linku do kamery
* pobieranie zdjęć bazując na aktualnej dacie
* "mądrzejsze" parsowanie zdjęć, są to klatki co 5 minut +- pare sekund, należy wykrywać w jakim czasie zdjęcia dla
danej kamery są dodawane
* refaktoryzacja całkowita kodu (najlepiej napisać od zera)
* implementacja algorytmu wykrywania tablic rejestracyjnych  