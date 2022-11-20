# Converts a Transformation matrix to a quaternion
#input: .log file with the transformation matrix
#output: .posegraph file with the quaternion and coordinates
#Author: Balachandra Bhat
#Date: 20/11/2022


import numpy as np
import scipy as sp
import os
import sys
import logging


def main():
    
        # Read the file
        file = open(sys.argv[1], "r")
        lines = file.readlines()
        file.close()
    
        # Create a new file
        new_file = open(sys.argv[1] + ".posegraph", "w")
    
        # Read the transformation matrix
        for line in lines:
            iters = 0    # Number of iterations of loop
            num = line.split(" ")[0]
            if type(num) == int:
                index = 0
                pass

            elif  type(num) == int:
                Tmat = np.array([float(x) for x in line.split(" ")[:]]).reshape(4, 4)
                break
    
        # Convert to quaternion
        qut = sp.spatial.transform.Rotation.from_matrix(Tmat[:3, :3]).as_quat()
    
        # Write the quaternion and coordinates to the new file
        new_file.write("qut " + " ".join([str(x) for x in qut]) + "


#read matrix from txt file
def read_matrix(file):
    matrix = []
    for line in file:
        matrix.append([float(x) for x in line.split()])
    return matrix
