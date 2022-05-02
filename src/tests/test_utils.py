import pytest
from src.utils import randomWord
from src.utils import validateWord
from src.utils import comparationWords


def test_randomWord():
    """
    Verifica que la palabra si sea del rango esperado y que sea de tipo String
    """
    word = randomWord(5)
    assert isinstance(word, str)
    assert len(word) == 5


def test_randomWord_badLength():
    """
    Manda un true en caso de que el número no este dentro del rango esperado
    """
    with pytest.raises(ValueError):
        _ = randomWord(11)
    with pytest.raises(ValueError):
        randomWord(3)
    assert True


def test_validateWord_BadequalsLenght():
    """
    Verifica que la palabra random y la del usuario sean de la misma longitud
    """
    _ = validateWord("beach", randomWord(6))
    assert True


def test_validateWord():
    """
    Verifica que la palabra exista en el diccionario
    """
    _ = validateWord("prñad", randomWord(5))
    assert True


def test_comparationWord_equals():
    """
    En la primera verificacion ve que las dos listas sean iguales, todas siendo
    mandada a la función.
    En la segunda se ve que si esten las letras en la palabra, pero no en la
    posicion correcta.
    En la tercera se ve que haya algunas que no están dentro de la palabra,
    las que si están y en la posición correcta, y las que si están en la
    palabra pero no en la posición correcta.
    """
    test_1 = comparationWords("black", "black")
    equal = [2, 2, 2, 2, 2]
    test_2 = comparationWords("kcalb", "black")
    equal_2 = [1, 1, 2, 1, 1]
    test_3 = comparationWords("pluca", "black")
    equal_3 = [0, 2, 0, 2, 1]
    assert equal == test_1
    assert equal_2 == test_2
    assert equal_3 == test_3
