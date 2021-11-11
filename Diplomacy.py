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
        self.attacked = None
        
    
    def __str__(self):
        if self.action == 'Move':
            return f"{self.name} {self.target_loc}"
        else:
            return f"{self.name} {self.location}"
        
    def set_dead(self):
        self.location = "[DEAD]"
        self.target_loc = "[DEAD]"

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

            support_arr = []

            for army in armies_in_city:
                num_supports = diplomacy_check_support(army)

                army.supporters = num_supports
                support_arr.append(num_supports)

            max_support = max(support_arr)
            
            multiple_max = False
            found_already = False
            
            # check if multiple armies have the same number of supports -- if true everyone dead :(
            for army in armies_in_city:
                if army.supporters == max_support:
                    if not found_already: 
                        found_already = True
                    else:
                        multiple_max = True
                
            if multiple_max:
                for army in armies_in_city:
                    army.set_dead()
            else:
                for army in armies_in_city:
                    if army.supporters != max_support:
                        army.set_dead()
    return None

#Helper function for eval
def diplomacy_check_support(army):
    """
    @params: army object
    returns number of armies that support input single army
    """
    support = 0
    for a in army_info:
        if a.target_army == army.name and a.name != army.name:
            if a.attacked is None:
                a.attacked = False
                for b in army_info:
                    if b.target_loc == a.location:
                        a.attacked = True
                        break
                
            if not a.attacked: 
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
        
    for city in city_dict:
        [print(army.name, sep="") for army in city_dict[city]]
    diplomacy_eval()
    diplomacy_print(w)