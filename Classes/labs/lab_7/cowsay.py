from heifer_generator import HeiferGenerator
import sys

#a list of cow objects
cows = HeiferGenerator.get_cows()
def list_cows(cows): # displays the available cows form the list of Cow object
    for i in range(0, len(cows)):
        print(cows[i].name, cows[i].image) #get name and image to print

def find_cow(name, cows):
    # interate through cows
    for i in cows:
        if cows[i].name == name: # if there is this name in the list, so return the name, otherwise: None
            return cows[i].name
        return None

# Working with arguments
args = sys.argv
args = (args[2:])
if args[1] == "-l":
    print(f"Cows available: {cows}") # SHOULD I USE LIST_COWS? how?
    #list out al the cows by calling all the cows
elif args[1] == "-n":
    # find the specific cow based o the name
    # #and print it out the massage
    find_cow()


#print(cows[0].name)
#print(cows[0].image) - not working