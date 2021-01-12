from pip._vendor import requests

from functions.functions import CircleAreaFunction


def get_random_circle_area():
    url = 'https://www.random.org/integers/'
    params = {
        'num': 1,
        'min': 1,
        'max': 10,
        'col': 1,
        'base': 10,
        'format': 'plain',
        'rnd': 'new',
    }
    try:
        response = requests.get(url=url, params=params)
    except ConnectionError:
        return 'Error', 'Error'

    radius = int(response.content)
    circle_function = CircleAreaFunction(radius)
    circle_function.solve()
    answer = circle_function.answer[0]
    return radius, answer
