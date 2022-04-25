import pytest
from src.utils import randomWord


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
