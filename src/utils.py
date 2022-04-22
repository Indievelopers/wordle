import requests


def randomWord(length: int) -> str:

    # Valida si la palabra esta en un rango de 5 a 10 letras
    if not (5 <= length <= 10):
        raise ValueError("La variable length debe ser un entero entre 5-10")
    # Manda a llamar la API 'requests' para que me mande una palabra de tipo String.
    r = requests.get(f'https://random-word-api.herokuapp.com/word?length={length}')
    # Valida el status code para cualquier error esperado
    if r.status_code != 200:
        print(r.text)
        r.raise_for_status()
    # Convierte el String en una variable de tipo lista y lo retorna
    return r.json()[0]


# if __name__ == "__main__":
#     print(randomWord(10))
