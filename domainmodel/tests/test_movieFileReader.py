import pytest
import csv

from CS235FlixSkeleton.domainmodel.movie import Movie, Director, Actor, Genre

from CS235FlixSkeleton.datafilereaders.movie_file_csv_reader import MovieFileCSVReader

@pytest.fixture
def movieFileCSVReader():
    return MovieFileCSVReader()

def test_dataset_of_movies():
    path = r"C:\Users\Jack\PycharmProjects\COMPSCI235 assignment 1\CS235FlixSkeleton\datafiles\Data1000Movies.csv"
    test = MovieFileCSVReader(path)
    movie_list = test.dataset_of_movies
    print(len(movie_list))

def test_dataset_of_actors():
    path = r"C:\Users\Jack\PycharmProjects\COMPSCI235 assignment 1\CS235FlixSkeleton\datafiles\Data1000Movies.csv"
    test = MovieFileCSVReader(path)
    actor_list = test.dataset_of_actors
    print(len(actor_list))

def test_dataset_of_directors():
    path = r"C:\Users\Jack\PycharmProjects\COMPSCI235 assignment 1\CS235FlixSkeleton\datafiles\Data1000Movies.csv"
    test = MovieFileCSVReader(path)
    director_set = test.dataset_of_directors
    print(len(director_set))

def test_dataset_of_genres():
    path = r"C:\Users\Jack\PycharmProjects\COMPSCI235 assignment 1\CS235FlixSkeleton\datafiles\Data1000Movies.csv"
    test = MovieFileCSVReader(path)

    print(len(test.dataset_of_genres))

def test_codeRunnerTest():
    filename = r"C:\Users\Jack\PycharmProjects\COMPSCI235 assignment 1\CS235FlixSkeleton\datafiles\Data1000Movies.csv"
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
    print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
    print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
    print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')
