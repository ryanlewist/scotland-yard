import yaml


# The board is a huge matrix where there is a route from point X to point Y when the matrix at
# the position (X, Y) is non-zero. The number determines the way one can go there:
# 1...taxi, 2...bus, 4...underground and 10...ship
# So for example, if one can go from X to Y with bus and taxi, the relevant position in the matrix
# will be 1 + 2 = 3.


class Board:

    # Load the board- and distance-matrix from a yaml-file.
    def __init__(self):
        with open('yml/board-matrix.yml') as f:
            self.matrix = yaml.load(f, Loader=yaml.FullLoader)
        with open('yml/distance-table.yml') as f:
            self.distance_matrix = yaml.load(f, Loader=yaml.FullLoader)

    # Returns an array of all possible routes one can move to from station [station_number].
    def routes_from(self, station_number):
        result = []
        for index, number in enumerate(self.matrix[station_number]):
            if number == 0:
                continue
            if number == 1:
                result.append({'station': index, 'ticket': 'taxi'})
            elif number == 2:
                result.append({'station': index, 'ticket': 'bus'})
            elif number == 3:
                result.append({'station': index, 'ticket': 'taxi'})
                result.append({'station': index, 'ticket': 'bus'})
            elif number == 4:
                result.append({'station': index, 'ticket': 'underground'})
            elif number == 6:
                result.append({'station': index, 'ticket': 'bus'})
                result.append({'station': index, 'ticket': 'underground'})
            elif number == 10:
                result.append({'station': index, 'ticket': 'black'})
        return result

    # Returns distance between two stations
    def distance(self, station1, station2):
        return self.distance_matrix[station1][station2]
