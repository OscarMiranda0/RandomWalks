import random
import csv


def Two_Dim_random_walk(iterations, left_prob, down_prob):
    end_x_positions = []
    end_y_positions = []
    x_position = 0
    y_position = 0
    for steps in range(iterations):
        for steps in range(101):
            if i == 100:
                end_x_positions.append(x_position)
                end_y_positions.append(y_position)
                x_position = 0
                y_position = 0
            else:
                if random.random() <= left_prob:
                    x_position -= 1
                    if random.random() <= down_prob:
                        y_position -= 1
                    else:
                        y_position += 1
                else:
                    x_position += 1
                    if random.random() <= down_prob:
                        y_position -= 1
                    else:
                        y_position += 1

    print(end_x_positions)
    print(end_y_positions)

    # Write data to file
    with open('TwoDimRandomWalkerData.csv','w',newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        data_x = [end_x_positions]
        data_y = [end_y_positions]
        a.writerows(data_x)
        a.writerows(data_y)
Two_Dim_random_walk(5000,0.550, 0.550)