
def cleaning(string):
    hotel = ["Resort"]

    for w in hotel:
        if w in str(string): 
            return "Algarve"
    else:
         return "Lisbon"

def greater_than(i):
        if i > 2015: 
            return i
        else:
            return "NaN"