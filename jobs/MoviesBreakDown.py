from mrjob.job import MRJob
from mrjob.step import MRStep

#sorting by movie count
class MoviesBreakDown(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_movies,
                   reducer=self.reducer_count_movies),
            MRStep(reducer=self.reducer_sorted_output)
        ]

    def mapper_get_movies(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, 1

    def reducer_count_movies(self, key, values):
        yield str(sum(values)).zfill(5), key

    def reducer_sorted_output(self, count, movies):
        for movie in movies:
            yield movie, count

if __name__=='__main__':
    MoviesBreakDown.run()