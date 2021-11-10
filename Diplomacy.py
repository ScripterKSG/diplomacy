# Army class, keeps track of army name, let location and action
# be an attribute of Army. Maybe use string function to display army
# and location

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
    
    def __str__(self):
        return f"{self.name} {self.location}"

"""
TODO:
- 2 more run ins and outs
"""

def diplomacy_read(s, army_info, **army_dict):
    '''
    read list of strings
    s a list of strings
    returns an Army object
    '''
    data = [str(i) for i in s.split()]
    temp_army = Army(*data)
    army_info.append(temp_army)
    """
    if temp_army.target_loc:
        try: 
            army_dict[temp_army.target_loc].append(temp_army)
        except:
            army_dict[temp_army.target_loc] = [temp_army]
    else:
        try: 
            army_dict[temp_army.location].append(temp_army)
        except:
            army_dict[temp_army.location] = [temp_army]
    """

    return temp_army


    # insert code to put data in an Army class object
    # put Army object into armyInfo

def diplomacy_print(w, army_info):
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

    """
    iter through army info
    for army in army info
        if
    """
    pass

def diplomacy_solve(r, w):
    '''
    r a reader
    w a writer
    reads all input from the file and executes Diplomacy
    '''
    army_info = []

    army_dict = {}
    for line in r:
        # put army info into army_info array
        diplomacy_read(line, army_info)

    diplomacy_print(w, army_info)