from describe import describe

def test_describe():
    with open('test_data/films_described.txt', 'r') as expected:
        assert describe('test_data/films.csv').to_string() == expected.read()
