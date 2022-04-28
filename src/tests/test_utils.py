import pytest
from src.utils import randomWord
from src.utils import validateWord


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
