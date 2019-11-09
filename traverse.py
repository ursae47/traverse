# -*- coding: utf-8 -*-
##############################################################################
#                       
#                        Program name: traverse.py
#                        Created:      Sun Jan 7 2018 13:03
#                        author:       Stephen Flowers Chávez
#
##############################################################################
#library import
import math
import os

# clear screen and input values
os.system('cls')
distance=float(input("What's the value for 'distance' in miles?")) 
bearing=float(input("What's the value for 'bearing'in degrees?")) 

#changing to radians from degrees
radbearing=math.radians(bearing)
#compute difference in latitude
diffLat=distance*math.cos(radbearing)

#header info
print("\n")
print('Traverse Table Output:')
print('----------------------\n')
print('Distance: ', distance, ' miles')
print('Bearing: ', bearing, 'degrees\n')

#convert decimal degrees to degrees and minutes
if abs(diffLat)>=60:
    diffLatMinutes=diffLat % 60
    diffLat=diffLat/60

#print results
#   print("difflat/60", diffLat) - used for debugging
#   print("diffLatMinutes", diffLatMinutes) - used for debugging
    print('Difference in Latitude = {0:.0f}'.format(math.trunc(diffLat)), "degrees"," {0:.2f} ".format(round(diffLatMinutes,2)), "minutes")
    
else:
#       print("difflat", diffLat) - used for debugging
        print("Difference in Latitude = {0:.2f}".format(round(diffLat,2)), "minutes")
            
departure=distance*math.sin(radbearing)
print("Departure = {0:.2f}".format(round(departure,2)), "miles")
