# Army class, keeps track of army name, let location and action
# be an attribute of Army. Maybe use string function to display army
# and location

army_info = []
# dictionary with city key, army array value
city_dict = {}

class Army:
    '''
    Stores attributes Army Name, Location, and Target Army/Location if any within a single object
    '''
    def __init__(self, name, location, action, target=None):
        
        self.target_army = None
        self.target_loc = None
        
        self.name = name
        # if dead, self.location = "[dead]"
        self.location = location

        # action can be hold, attack, support
        self.action = action.lower().capitalize()

        if self.action == 'Move':
            self.target_loc = target
        elif self.action == 'Support':
            self.target_army = target

        self.supporters = 0
        self.attacked = None
        
    
    def __str__(self):
        if self.action == 'Move':
            return f"{self.name} {self.target_loc}"
        else:
            return f"{self.name} {self.location}"
        
    
    def set_dead(self):
        '''
        Sets location/target location attributes to dead
        '''
        self.location = "[dead]"
        self.target_loc = "[dead]"

def diplomacy_read(s):
    '''
    read list of strings
    s a list of strings
    returns an Army object
    '''
    
    data = [str(i).strip() for i in s.split()]
    
    # -------
    # Preconditions
    # -------
   
    
    # checks that each line of data has between 3 - 4 entries
    assert 3 <= len(data) <= 4
    
    # checks that the first entry in line is a single character
    assert len(data[0]) == 1
    
    # checks that the first entry in line is capitalized
    assert 65 <= ord(data[0]) <= 90
    
    # checks that city entry has an uppercase first letter
    assert 65 <= ord(data[1][0]) <= 90
    
    # checks that action entry is either hold, support, or move
    assert data[2].lower() in ["move", "support", "hold"]
    
    if data[2].lower() == "support":
        # if action is support, the next entry should be an army
        # indicated by a single uppercase letter
        
        # checks that the last entry in line is a single character
        assert len(data[3]) == 1
        
        # checks that the last entry in line is capitalized
        assert 65 <= ord(data[3]) <= 90
        
    elif data[2].lower() == "move":
        # if action is move, the next entry should be a city
        
        # checks that city entry has an uppercase first letter
        assert 65 <= ord(data[1][0]) <= 90
    
    temp_army = Army(*data)
    
    assert type(temp_army) == Army
    
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
                support_arr.append(army.supporters)

            max_support = max(support_arr)
            
            if support_arr.count(max_support) > 1:
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
    Takes army object, returns number of armies that support given army object
    """
    support = 0
    for a in army_info:
        if a.target_army == army.name and a.name != army.name:

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
    
    # -------
    # Preconditions
    # -------
    
    # check that r can be read
    assert callable(r.read)
    
    # check that w can be written 
    assert callable(w.write)
    
    army_info.clear()
    # dictionary with city key, army array value
    city_dict.clear()
    for line in r:
        diplomacy_read(line)
        
    for army in army_info:
        army.supporters = diplomacy_check_support(army)
        
    diplomacy_eval()
    diplomacy_print(w)