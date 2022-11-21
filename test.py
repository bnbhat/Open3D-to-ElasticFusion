#Converts a Transformation matrix to a quaternion
#input: .log file with the transformation matrix
#output: .posegraph file with the quaternion and coordinates
#Author: Balachandra Bhat
#Date: 20/11/2022


import numpy as np
import scipy as sp
import os
import logging


def main():

        #timestamp
        timestamp = "0.0"  #timestamp is not available in the log file from Open3D
    
        # Read the file
        file = open('trajectory.txt', "r")
        lines = file.readlines()
        file.close()

        # Create a new file
        new_file = open('trajectory'+ ".posegraph", "w")
        
        for mat_line in range(0,len(lines),  5) :
            # Get transformation matrix from file
            Tmat = np.zeros((4,4))

            iters = 0   # Number of iterations of loop
            for line in lines[:5]:
                print(line)
                if iters%5 == 0:  # Every 5th line is the metadata. Skip it
                    print('skipping line') 

                else:             # Read the transformation matrix 4 lines after the metadata
                    i_iters = 0
                    for x in line.split(" ")[:]:
                        Tmat[iters%5-1 ,i_iters] = str(x)

                        if iters%5-1 == 0 and i_iters == 3:     # Extract the translation tx,ty,tz
                            tx = str(x)
                        elif iters%5-1 == 1 and i_iters == 3:
                            ty = str(x)
                        elif iters%5-1 == 2 and i_iters == 3:
                            tz = str(x)

                        i_iters += 1

                iters+=1

            #print(Tmat)

            # Convert to quaternion
            quterion = sp.spatial.transform.Rotation.from_matrix(Tmat[:3, :3]).as_quat()
            print(quterion)
            print(tx,ty,tz)
            print(type(tx))
            print(type(quterion[0]))

            # Write the quaternion and coordinates to the new file
            new_file.write(timestamp+ " "+ tx + " "+ ty + " " + tz + " " + str(quterion[0]) + " " + str(quterion[1]) + " " + str(quterion[2]) + " " + str(quterion[3]) + "\n") 


main()
'''
#read matrix from txt file
def read_matrix(file):
    matrix = []
    for line in file:
        matrix.append([float(x) for x in line.split()])
    return matrix
'''

#read a file from current directory pwd command
def read_file_pwd(file):
    pwd = os.getcwd()
    f = open(pwd + '/' + file, 'r')
    return f
def read_file(file):
    f = open(file, 'r')
    return f