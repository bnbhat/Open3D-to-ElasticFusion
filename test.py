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
        print("Reading file...")
        file = open('trajectory.txt', "r")
        lines = file.readlines()
        file.close()

        # Create a new file
        new_file = open('trajectory'+ ".posegraph", "w")

        
        # Get transformation matrix from file
        Tmat = np.zeros((4,4))

        iters = 0   # Number of iterations of loop
        for line in lines[:]:
            #print(line)
            if iters%5 == 0:  # Every 5th line is the metadata. Skip it
                #print('skipping line') 
                pass

            else:             # Read the transformation matrix 4 lines after the metadata
                i_iters = 0
                for x in line.split(" ")[:4]:
                    Tmat[iters%5-1 ,i_iters] = str(x)
                    if (iters%5-1 == 0 and i_iters == 3):     # Extract the translation tx,ty,tz
                        tx = float(x)
                        #print(iters%5-1)
                        #print(tx)
                    elif (iters%5-1 == 1 and i_iters == 3):
                        ty = float(x)
                        #print(ty)
                    elif (iters%5-1 == 2 and i_iters == 3):
                        tz = float(x)
                        #print(tz)
                    i_iters += 1

            iters+=1

            if iters%5 == 4:
                #print(Tmat)
                # Convert to quaternion
                quterion = sp.spatial.transform.Rotation.from_matrix(Tmat[:3, :3]).as_quat()
                #print(quterion)
                #print(tx,ty,tz)
                #print(iters%5-1)
                # Write the quaternion and coordinates to the new file
                new_file.write(timestamp+ "\t"+ str(tx) + "\t"+ str(ty) + "\t" + str(tz) + "\t" + str(quterion[0]) + "\t" + str(quterion[1]) + "\t" + str(quterion[2]) + "\t" + str(quterion[3]) + "\n")  
                


main()

print('done')