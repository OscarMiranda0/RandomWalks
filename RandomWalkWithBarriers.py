import random
import csv


def random_walk_barriers(iterations,barrier_radius, left_prob, down_prob):
    end_x_positions = []
    end_y_positions = []
    x_position = 0
    y_position = 0
    for j in range(iterations):

        for i in range(1001):
            if i == 1000:
                if x_position == 0:                            #this is to ensure that our particle ends up on one side of the box, not the middle
                    if random.random() <= left_prob:
                        x_position -= 1
                        end_x_positions.append(x_position)
                        end_y_positions.append(y_position)
                        x_position = 0
                        y_position = 0
                    else:
                        x_position += 1
                        end_x_positions.append(x_position)
                        end_y_positions.append(y_position)
                        x_position = 0
                        y_position = 0
                else:
                    end_x_positions.append(x_position)
                    end_y_positions.append(y_position)
                    x_position = 0
                    y_position = 0
            else:
                if x_position == (barrier_radius):
                    x_position -= 1
                if x_position == -(barrier_radius):
                    x_position += 1
                if y_position == (barrier_radius):
                    y_position -= 1
                if y_position == -(barrier_radius):
                    y_position += 1
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
    four_right_zero_left = 0
    three_right_one_left = 0
    two_right_two_left = 0
    one_right_three_left = 0
    zero_right_four_left = 0
    for i in range(int(iterations/4)):
        if end_x_positions[(4*i)] > 0 and end_x_positions[(4*i)+1] > 0 and end_x_positions[(4*i)+2] > 0 and end_x_positions[(4*i)+3] > 0:
            four_right_zero_left += 1
        elif end_x_positions[(4 * i)] < 0 and end_x_positions[(4 * i) + 1] > 0 and end_x_positions[(4 * i) + 2] > 0 and end_x_positions[(4 * i) + 3] > 0:
            three_right_one_left += 1
        elif end_x_positions[(4 * i)] > 0 and end_x_positions[(4 * i) + 1] < 0 and end_x_positions[(4 * i) + 2] > 0 and end_x_positions[(4 * i) + 3] > 0:
            three_right_one_left += 1
        elif end_x_positions[(4 * i)] > 0 and end_x_positions[(4 * i) + 1] > 0 and end_x_positions[(4 * i) + 2] < 0 and end_x_positions[(4 * i) + 3] > 0:
            three_right_one_left += 1
        elif end_x_positions[(4 * i)] > 0 and end_x_positions[(4 * i) + 1] > 0 and end_x_positions[(4 * i) + 2] > 0 and end_x_positions[(4 * i) + 3] < 0:
            three_right_one_left += 1
        elif end_x_positions[(4 * i)] < 0 and end_x_positions[(4 * i) + 1] < 0 and end_x_positions[(4 * i) + 2] > 0 and end_x_positions[(4 * i) + 3] > 0:
            two_right_two_left += 1
        elif end_x_positions[(4 * i)] < 0 and end_x_positions[(4 * i) + 1] > 0 and end_x_positions[(4 * i) + 2] > 0 and end_x_positions[(4 * i) + 3] < 0:
            two_right_two_left += 1
        elif end_x_positions[(4 * i)] < 0 and end_x_positions[(4 * i) + 1] > 0 and end_x_positions[(4 * i) + 2] < 0 and end_x_positions[(4 * i) + 3] > 0:
            two_right_two_left += 1
        elif end_x_positions[(4 * i)] > 0 and end_x_positions[(4 * i) + 1] < 0 and end_x_positions[(4 * i) + 2] > 0 and end_x_positions[(4 * i) + 3] < 0:
            two_right_two_left += 1
        elif end_x_positions[(4 * i)] > 0 and end_x_positions[(4 * i) + 1] > 0 and end_x_positions[(4 * i) + 2] < 0 and end_x_positions[(4 * i) + 3] < 0:
            two_right_two_left += 1
        elif end_x_positions[(4 * i)] > 0 and end_x_positions[(4 * i) + 1] < 0 and end_x_positions[(4 * i) + 2] < 0 and end_x_positions[(4 * i) + 3] > 0:
            two_right_two_left += 1
        elif end_x_positions[(4 * i)] > 0 and end_x_positions[(4 * i) + 1] < 0 and end_x_positions[(4 * i) + 2] < 0 and end_x_positions[(4 * i) + 3] < 0:
            one_right_three_left += 1
        elif end_x_positions[(4 * i)] < 0 and end_x_positions[(4 * i) + 1] > 0 and end_x_positions[(4 * i) + 2] < 0 and end_x_positions[(4 * i) + 3] < 0:
            one_right_three_left += 1
        elif end_x_positions[(4 * i)] < 0 and end_x_positions[(4 * i) + 1] < 0 and end_x_positions[(4 * i) + 2] > 0 and end_x_positions[(4 * i) + 3] < 0:
            one_right_three_left += 1
        elif end_x_positions[(4 * i)] < 0 and end_x_positions[(4 * i) + 1] < 0 and end_x_positions[(4 * i) + 2] < 0 and end_x_positions[(4 * i) + 3] > 0:
            one_right_three_left += 1
        else:
            zero_right_four_left += 1
    print(four_right_zero_left)
    print(zero_right_four_left)
    print(three_right_one_left)
    print(one_right_three_left)
    print(two_right_two_left)




    left_count = 0
    right_count = 0
    #for i in end_x_positions:                       #delete this later
    #    if i > 0:
    #        right_count += 1
    #    else:
    #        left_count += 1
    #print(left_count)
    #print(right_count)


    # Write data to file
    with open('BarrierWalk.csv','w',newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        data_x = [end_x_positions]
        data_y = [end_y_positions]
        a.writerows(data_x)
        a.writerows(data_y)
random_walk_barriers(40000,5,0.500, 0.500)