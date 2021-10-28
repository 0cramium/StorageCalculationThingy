import math

blue = "\033[94m"
reset = "\033[0;0m"

print(
"██████╗░██╗░██████╗██╗░░██╗  ██████╗░███████╗██████╗░░█████╗░███████╗███╗░░██╗████████╗"
"██╔══██╗██║██╔════╝██║░██╔╝  ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝████╗░██║╚══██╔══╝"
"██║░░██║██║╚█████╗░█████═╝░  ██████╔╝█████╗░░██████╔╝██║░░╚═╝█████╗░░██╔██╗██║░░░██║░░░"
"██║░░██║██║░╚═══██╗██╔═██╗░  ██╔═══╝░██╔══╝░░██╔══██╗██║░░██╗██╔══╝░░██║╚████║░░░██║░░░"
"██████╔╝██║██████╔╝██║░╚██╗  ██║░░░░░███████╗██║░░██║╚█████╔╝███████╗██║░╚███║░░░██║░░░"
"╚═════╝░╚═╝╚═════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░")

#Grab the amount of the drive that's taken up.
gbsTaken = int(input("How many GBS are taken on your drive?\n: " + blue))
#Grab the total capacity of the drive.
drvCapacity = int(input(reset + "What is your drive's capacity?\n: " + blue))

#initiate calculation
def getPercent(gbsTaken, drvCapacity):
    #Divide the taken up space by the total size of the drive.
    quotient = gbsTaken / drvCapacity
    #Multiply the result by 100 to get the percentage.
    percent = quotient * 100
    #Return the result of the equation to the program.
    return percent

#Call the calculaton function and print the results to console.
drvValue = getPercent(gbsTaken, drvCapacity)

if drvValue <= 70:
    print(drvValue, reset + "Percent of your drive is taken up, your good to go.")
else:
    print(drvValue, reset + "Percent of your drive is taken up, free up some space.")