# Army class, keeps track of army name, let location and action
# be an attribute of Army. Maybe use string function to display army
# and location

army_info = []
# dictionary with city key, army array value
city_dict = {}

class Army:
    def __init__(self, name, location, action, target=None):
        
        self.target_army = None
        self.target_loc = None
        
        self.name = name
        # if dead, self.location = "[dead]"
        self.location = location

        # action can be hold, attack, support
        self.action = action

        if action == 'Move':
            self.target_loc = target
        elif action == 'Support':
            self.target_army = target

        self.supporters = 0
    
    def __str__(self):
        return f"{self.name} {self.location}"

"""
TODO:
- 2 more run ins and outs
"""

def diplomacy_read(s):
    '''
    read list of strings
    s a list of strings
    returns an Army object
    '''
    data = [str(i) for i in s.split()]
    temp_army = Army(*data)
    army_info.append(temp_army)

    if temp_army.target_loc:
        try: 
            city_dict[temp_army.target_loc].append(temp_army)
        except:
            city_dict[temp_army.target_loc] = [temp_army]
    else:
        try: 
            city_dict[temp_army.location].append(temp_army)
        except:
            city_dict[temp_army.location] = [temp_army]

    return temp_army

###TEST
def diplomacy_dict():
    return city_dict

def diplomacy_print(w):
    '''
    w a writer
    takes data from army_info and army name and their locations
    '''
    for army in army_info:
        w.write(str(army) + "\n")
    

def diplomacy_eval():
    '''
    evaluates all data from army_info and updates location attributes of the army objects
    '''
    for key in city_dict:
        armies_in_city = city_dict[key]
        if len(armies_in_city) > 1:
            for army in armies_in_city:
                army.supporters = diplomacy_check_support(army)
                # Work start again here to compare supporters

#Helper function for eval
def diplomacy_check_support(army):
    support = 0
    for a in army_info:
        if a.target_army == army.name and a.name != army.name:
            attacked = False
            for b in army_info:
                if b.target_loc == a.location:
                    attacked = True
                    break
            if not attacked:
                support += 1
    return support
        


def diplomacy_solve(r, w):
    '''
    r a reader
    w a writer
    reads all input from the file and executes Diplomacy
    '''
    army_info.clear()
    # dictionary with city key, army array value
    city_dict.clear()
    for line in r:
        # put army info into army_info array
        # put city: [army]
        diplomacy_read(line)

    diplomacy_print(w)