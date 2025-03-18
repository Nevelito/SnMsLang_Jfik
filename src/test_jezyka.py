import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grammar.SnMsLangLexer import SnMsLangLexer
from grammar.SnMsLangParser import SnMsLangParser
from antlr4 import *

def test_przypisanie():
    input_stream = InputStream('x = 5 + 3;')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.statement()
    print("✔️ Test przypisania zmiennej przeszedł pomyślnie")

def test_wypisz():
    input_stream = InputStream('wypisz(x);')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.printStmt()
    print("✔️ Test wypisania zmiennej przeszedł pomyślnie")

def test_wczytaj():
    input_stream = InputStream('wczytaj(x);')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.readStmt()
    print("✔️ Test wczytania zmiennej przeszedł pomyślnie")

def test_jezeli():
    input_stream = InputStream('jezeli (x > 3) { wypisz(x); } inaczej { wypisz(0); }')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.ifStmt()
    print("✔️ Test warunku jezeli przeszedł pomyślnie")

def test_dopoki():
    input_stream = InputStream('dopoki (x < 5) { x = x + 1; }')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.whileStmt()
    print("✔️ Test petli dopoki przeszedł pomyślnie")

def test_funkcja():
    input_stream = InputStream('funkcja dodaj(liczba x, liczba y) { zwroc x + y; }')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.funcDecl()
    print("✔️ Test funkcji przeszedł pomyślnie")

def test_przekazania_zmiennych_bez_typow():
    input_stream = InputStream('funkcja dodaj(x, y) { zwroc x + y; }')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.funcDecl()
    print("✔️ Test przekazania zmiennych bez typow do funkcji przeszedł pomyślnie")

def test_zmienna():
    input_stream = InputStream('liczba x;')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.varDecl()
    print("✔️ Test zmiennej przeszedł pomyślnie")

def test_tablica():
    input_stream = InputStream('liczba x[5];')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.varDecl()
    print("✔️ Test tablicy przeszedł pomyślnie")

def test_klasa():
    input_stream = InputStream('klasa MojaKlasa { liczba x; funkcja dodaj(liczba x, liczba y) { zwroc x + y; } }')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.classDecl()
    print("✔️ Test klasy przeszedł pomyślnie")

def test_struktura():
    input_stream = InputStream('struktura MojaStruktura { liczba x; zmiennoprzecinkowa y; }')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.structDecl()
    print("✔️ Test struktury przeszedł pomyślnie")

def test_wyrazenie_tablicowe():
    input_stream = InputStream('x[1, 2, 3];')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.expr()
    print("✔️ Test wyrazenia tablicowego przeszedł pomyślnie")

def test_dzialania_arytmetyczne():
    input_stream = InputStream('5 + 3 * (2 - 1);')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.expr()
    print("✔️ Test działań arytmetycznych przeszedł pomyślnie")

def test_porownania():
    input_stream = InputStream('x > 3 && y < 5;')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.expr()
    print("✔️ Test porównywania przeszedł pomyślnie")

def test_logiczne():
    input_stream = InputStream('x && y || z;')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.expr()
    print("✔️ Test wyrazenia logicznego przeszedł pomyślnie")

def test_dynamiczne_typowanie():
    input_stream = InputStream('x = 5; x = "test";')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.statement()
    print("✔️ Test dynamicznego typowania przeszedł pomyślnie")

def test_generatory():
    input_stream = InputStream('funkcja liczby_od(n) { dopoki (n > 0) { yield n; n = n - 1; } }')
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    parser.funcDecl()
    print("✔️ Test generatorów przeszedł pomyślnie")

def test_bledy_leksykalne():
    input_stream = InputStream('x = 5 @ 3;')  # Nedozwolony znak @
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    try:
        parser.statement()
        print("❌ Test błędów leksykalnych nie wykrył błędu!")
    except Exception as e:
        print(f"✔️ Test błędów leksykalnych przeszedł pomyślnie: {e}")

def test_bledy_skladniowe():
    input_stream = InputStream('jezeli x > 5 { wypisz(x);')  # Brak nawiasu zamykającego }
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    try:
        parser.ifStmt()
        print("❌ Test błędów składniowych nie wykrył błędu!")
    except Exception as e:
        print(f"✔️ Test błędów składniowych przeszedł pomyślnie: {e}")

def test_bledy_skladniowe2():
    input_stream = InputStream('funkcja dodaj(liczba x) { zwroc x + }')  # Nieoczekiwany +
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    try:
        parser.funcDecl()
        print("❌ Test błędów składniowych nie wykrył błędu!")
    except Exception as e:
        print(f"✔️ Test błędów składniowych przeszedł pomyślnie: {e}")

def test_bledy_skladniowe3():
    input_stream = InputStream('funkcja dodaj(liczba x, liczba y) { zwroc x + y')  # Brak zamykającego nawiasu }
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    try:
        parser.funcDecl()
        print("❌ Test błędów składniowych nie wykrył błędu!")
    except Exception as e:
        print(f"✔️ Test błędów składniowych przeszedł pomyślnie: {e}")

def test_bledy_skladniowe4():
    input_stream = InputStream('klasa MojaKlasa { liczba x; funkcja dodaj(liczba x, liczba y) { zwroc x + y;')  # Brak zamykającego nawiasu
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    try:
        parser.classDecl()
        print("❌ Test błędów składniowych nie wykrył błędu!")
    except Exception as e:
        print(f"✔️ Test błędów składniowych przeszedł pomyślnie: {e}")

def test_bledy_skladniowe5():
    input_stream = InputStream('struktura MojaStruktura { liczba x; zmiennoprzecinkowa y')  # Brak zamykającego nawiasu
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    try:
        parser.structDecl()
        print("❌ Test błędów składniowych nie wykrył błędu!")
    except Exception as e:
        print(f"✔️ Test błędów składniowych przeszedł pomyślnie: {e}")

def test_bledy_skladniowe6():
    input_stream = InputStream('liczba x[5, 6,];')  # Niespodziewany dodatkowy przecinek
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    try:
        parser.varDecl()
        print("❌ Test błędów składniowych nie wykrył błędu!")
    except Exception as e:
        print(f"✔️ Test błędów składniowych przeszedł pomyślnie: {e}")

def main():
    test_przypisanie()
    test_wypisz()
    test_wczytaj()
    test_jezeli()
    test_dopoki()
    test_funkcja()
    test_przekazania_zmiennych_bez_typow()
    test_zmienna()
    test_tablica()
    test_klasa()
    test_struktura()
    test_wyrazenie_tablicowe()
    test_dzialania_arytmetyczne()
    test_porownania()
    test_logiczne()
    test_dynamiczne_typowanie()
    test_generatory()
    test_bledy_leksykalne()

if __name__ == '__main__':
    main()
