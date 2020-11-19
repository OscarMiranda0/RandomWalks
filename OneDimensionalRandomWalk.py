import random
import csv

def One_Dim_random_walk(iterations, left_prob):
    particle_end_positions = []
    particle_current_position = 0
    for dummy in range(iterations):
        for step in range(101): #there are 100 steps in each iteration of the random walk.
            if step == 100:
                particle_end_positions.append(particle_current_position)
                particle_current_position = 0 # this resets the particle's position to 0 for the next iteration.
            elif random.random() <= left_prob:
                particle_current_position -= 1
            else:
                particle_current_position += 1
    # The follow code is used to write data to a file for use in analyzing the resultiing data.
    # Comment this out if you would like to create a csv file with the end_positions
#    with open('OneDimRandomWalkerData.csv','w',newline='') as fp:
#        a = csv.writer(fp, delimiter=',')
#        data = [end_positions]
#        a.writerows(data)
    print(particle_end_positions)
One_Dim_random_walk(5000,0.55)

