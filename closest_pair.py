import os
import csv
import matplotlib.pyplot as plt

cwd_path = os.getcwd()
file_path = 'files'


def read_file(file_name):
    """
    Reads csv file from given folder
    :param file_name: (str) the name of csv file
    :return:
    """
    data_points = []
    with open(os.path.join(cwd_path, file_path, file_name), 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # skip header
        next(csv_reader)

        # read each row
        for row in csv_reader:
            data_points.append([float(number) for number in row])

    return data_points






def draw_data(data_points, closest_pair=[]):
    """
    Function creates new figure and draw data points into scatter plot.
    :param data_points: (list of lists): each sublist is 1x2 list with x and y coordinate of a point.
    :param closest_pair: (tuple of ints): indices of the closest pair of points, default = empty list
    :return:
    """

    plt.scatter(
        x=[point[0] for point in data_points],
        y=[point[1] for point in data_points],
        color=['blue' if point not in closest_pair else 'red' for point in data_points]
    )
    plt.show()
    
def closest_pair_BF(array):
    min_dist = math.dist(array[0], array[1])
    point_1 = array[0]
    point_2 = array[1]
    num_points = len(array)

    if num_points == 2:
        return point_1, point_2, min_dist
    for i in range(num_points - 1):
        for j in range(i + 1, num_points):
            if i != 0 and j != 1:
                dist = math.dist(array[i], array[j])
                if dist < min_dist:
                    min_dist = dist
                    point_1, point_2 = array[i], array[j]
    return point_1, point_2, min_dist

def closest_split_pair(x_wise, y_wise, min_dist, points):
    num_points = len(x_wise)
    midpointX = x_wise[num_points // 2][0]

    subarrayY = list()
    for item in y_wise:
        if (midpointX - min_dist) <= item[0] <= (midpointX + min_dist):
            subarrayY.append(item)

def closest_pair(x_wise, y_wise):
    num_points = len(x_wise)
    sterdny_idx = num_points // 2

    if num_points <= 3:
        point1, point2, min_dist = closest_pair_BF(x_wise)
        return point1, point2, min_dist

    left_x = x_wise[:sterdny_idx]
    right_x = x_wise[sterdny_idx:]

    mid_point = x_wise[sterdny_idx][0]
    left_y = list()
    right_y = list()

    for point in y_wise:
        if point[0] <= sterdny_idx:
            left_y.append(point)
        else:
            right_y.append(point)

    (p1, q1, m1) = closest_pair(left_x, left_y)
    (p2, q2, m2) = closest_pair(right_x, right_y)

    if m1 <= m2:
        min_dist = m1
        points = (p1, q1)
    else:
        min_dist = m2
        points = (p2, q2)

def main(file_name):
    # read data points
    data_points = read_file(file_name)

    # draw points
    draw_data(data_points)


if __name__ == '__main__':
    my_file = 'points.csv'
    main(my_file)
