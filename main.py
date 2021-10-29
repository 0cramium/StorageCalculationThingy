import math
import time
import psutil

print(
"██████╗░██╗░██████╗██╗░░██╗  ██████╗░███████╗██████╗░░█████╗░███████╗███╗░░██╗████████╗\n"
"██╔══██╗██║██╔════╝██║░██╔╝  ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝████╗░██║╚══██╔══╝\n"
"██║░░██║██║╚█████╗░█████═╝░  ██████╔╝█████╗░░██████╔╝██║░░╚═╝█████╗░░██╔██╗██║░░░██║░░░\n"
"██║░░██║██║░╚═══██╗██╔═██╗░  ██╔═══╝░██╔══╝░░██╔══██╗██║░░██╗██╔══╝░░██║╚████║░░░██║░░░\n"
"██████╔╝██║██████╔╝██║░╚██╗  ██║░░░░░███████╗██║░░██║╚█████╔╝███████╗██║░╚███║░░░██║░░░\n"
"╚═════╝░╚═╝╚═════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░\n")

#Grab the amount of the drive that's taken up.
diskUsed = psutil.disk_usage("/").used
#Grab the total capacity of the drive.
diskCapacity = psutil.disk_usage("/").total

#initiate calculation
def getPercent(diskUsed, diskCapacity):
    #Divide the taken up space by the total size of the drive.
    quotient = diskUsed / diskCapacity
    #Multiply the result by 100 to get the percentage.
    percent = quotient * 100
    #Return the result of the equation to the program.
    return percent

#Call the calculaton function and print the results to console.
driveValue = getPercent(diskUsed, diskCapacity)

if driveValue <= 70:
    print(driveValue, "Percent of your drive is taken up, your good to go.")
else:
    print(driveValue, "Percent of your drive is taken up, free up some space.")

print("Program will close automatically in 15 seconds.")

time.sleep(15)
