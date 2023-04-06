from heifer_generator import HeiferGenerator
import sys

#a list of cow objects
cows = HeiferGenerator.get_cows()
def list_cows(cows): # displays the available cows form the list of Cow object
    cow_names =""
    for cow in cows:
        cow_names += f"{cow.get_name()} "
    return cow_names

def find_cow(name, cows):
    # interate through cows
    for cow in cows:
        if cow.name == name: # if there is this name in the list, so return the name, otherwise: None
            return cow
    return None

# Working with arguments
args = sys.argv

if args[1] == "-l":
    print(f"Cows available: {list_cows(cows)}") # return the list of cows

    #list out al the cows by calling all the cows
elif args[1] == "-n":
    # find the specific cow based o the name
    name_of_cow = args[2]
    message = " ".join(args[3:]) # return a string from a list of strings
    # #and print it out the massage
    preferred_cow = find_cow(name_of_cow, cows)
    if preferred_cow is None:
        print(f"Could not find {name_of_cow} cow!")
    else:
        print(message)
        print(preferred_cow.get_image())
else:
    # find the specific cow based o the name
    name_of_cow = "heifer"
    message = " ".join(args[1:])
    #Access the object cow
    preferred_cow = find_cow(name_of_cow, cows)
    print(message)
    print(preferred_cow.get_image())

#print(cows[0].name)
#print(cows[0].image) - not working