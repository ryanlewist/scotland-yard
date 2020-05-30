import numpy as np


# Normalize the main board-matrix
def normalize_board(board_matrix):
    normal_board = np.zeros([200, 200], dtype=int)
    for outer_index, j in enumerate(board_matrix):
        for innder_index, v in enumerate(j):
            if v != 0:
                normal_board[outer_index][innder_index] = 1
    return normal_board


def matrix_as_list(matrix):
    matrix_list = []
    for row in matrix:
        matrix_list.append(list(np.array(row).reshape(-1, )))
    return matrix_list


def create_distance_matrix(normalized_board, power=16):
    # Calculate higher orders of the matrix to create a new matrix
    # with the minimal distance between nodes
    b = np.zeros([200, 200], dtype=int)
    for n in range(1, power):
        for outer_index, j in enumerate(np.linalg.matrix_power(normalized_board, n)):
            for inner_index, v in enumerate(j):
                if (v != 0) and (b[outer_index][inner_index] == 0) and (outer_index != inner_index):
                    b[outer_index][inner_index] = n
                    b[inner_index][outer_index] = n
    b_list = matrix_as_list(b)
    return b_list


def format_board_clean(board):
    clean_board = {}

    for station in range(1, len(board.matrix)):
        taxi_list = []
        bus_list = []
        underground_list = []
        river_list = []
        for routes in board.routes_from(station):
            if routes['ticket'] == 'taxi':
                taxi_list.append(routes['station'])
            if routes['ticket'] == 'bus':
                bus_list.append(routes['station'])
            if routes['ticket'] == 'underground':
                underground_list.append(routes['station'])
            if routes['ticket'] == 'black':
                river_list.append(routes['station'])
        clean_board.update({station: {'taxi': taxi_list,
                                      'bus': bus_list,
                                      'underground': underground_list,
                                      'river': river_list}})
    return clean_board


def clean_board_to_matrix(clean_board):
    matrix = []
    zero_array = [0] * (len(clean_board) + 1)
    matrix.append(zero_array)
    for index, routes in enumerate(clean_board.values()):
        station_matrix = zero_array.copy()
        for key, values in routes.items():
            if key == 'taxi':
                for value in values:
                    if station_matrix[value] == 0:
                        station_matrix[value] = 1
                    elif station_matrix[value] == 2:  # already a bus
                        station_matrix[value] = 3
            if key == 'bus':
                for value in values:
                    if station_matrix[value] == 0:
                        station_matrix[value] = 2
                    elif station_matrix[value] == 1:  # already a taxi
                        station_matrix[value] = 3
                    elif station_matrix[value] == 4:  # already an underground
                        station_matrix[value] = 6
            if key == 'underground':
                for value in values:
                    if station_matrix[value] == 0:
                        station_matrix[value] = 4
                    elif station_matrix[value] == 2:  # already a bus
                        station_matrix[value] = 6
            if key == 'river':
                for value in values:
                    station_matrix[value] = 10
        matrix.append(station_matrix)
    return matrix
