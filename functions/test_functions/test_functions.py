import pytest

from functions.functions import QuadraticFunction, SquareAreaFunction
from functions.utils import get_random_circle_area


@pytest.fixture
def requests_patch(mocker):
    return mocker.patch('functions.utils.requests.get')


class TestQuadraticFunction:
    def test_answer_correct(self):
        # Arrange
        quadratic = QuadraticFunction(2, 5, 2)
        # Act
        quadratic.solve()
        # Assert
        assert quadratic.answer == [-0.5, -2.0]

    def test_answer_one_solution(self):
        quadratic = QuadraticFunction(2, 4, 2)

        quadratic.solve()

        assert quadratic.answer == [-1.0]

    def test_answer_exception(self):
        quadratic = QuadraticFunction(5, 2, 5)

        with pytest.raises(ValueError) as ex:
            quadratic.solve()

        assert str(ex.value) == str(ValueError('x can not be found'))


class TestRandomCircleArea:
    def test_answer_correct(self, mocker, requests_patch):
        requests_patch.return_value.content = 2

        area_patch = mocker.patch('functions.utils.CircleAreaFunction')
        area_patch.return_value.answer = [6]

        answer = get_random_circle_area()

        requests_patch.assert_called_once_with(
            url='https://www.random.org/integers/',
            params={
                'num': 1,
                'min': 1,
                'max': 10,
                'col': 1,
                'base': 10,
                'format': 'plain',
                'rnd': 'new',
            }
        )
        assert answer == (2, 6)

    def test_test_requests_except(self, requests_patch):
        requests_patch.side_effect = ConnectionError

        answer = get_random_circle_area()

        assert answer == ('Error', 'Error')


class TestSquareAreaFunction:
    def test_answer_correct(self):
        square = SquareAreaFunction(4, 5)

        square.solve()

        assert square.answer == [20]

    def test_answer_correct_other(self):
        square = SquareAreaFunction(2, 7)

        square.solve()

        assert square.answer == [14]

    def test_a_is_zero(self):
        with pytest.raises(ValueError) as ex:
            SquareAreaFunction(0, 2)

        assert str(ex.value) == str(ValueError(['a should be greater than zero']))

    def test_b_is_zero(self):
        with pytest.raises(ValueError) as ex:
            SquareAreaFunction(2, 0)

        assert str(ex.value) == str(ValueError(['b should be greater than zero']))

    def test_a_lower_zero(self):
        with pytest.raises(ValueError) as ex:
            SquareAreaFunction(-1, 2)

        assert str(ex.value) == str(ValueError(['a should be greater than zero']))

    def test_b_lower_zero(self):
        with pytest.raises(ValueError) as ex:
            SquareAreaFunction(2, -1)

        assert str(ex.value) == str(ValueError(['b should be greater than zero']))
