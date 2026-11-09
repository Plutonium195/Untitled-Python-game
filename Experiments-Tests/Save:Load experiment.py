import pickle


a=1
b=2
c=3

def save():
    file_name = 'savefile'
    list_of_variable_names = ('a', 'b', 'c')

    with open(file_name,'wb') as file:
        pickle.dump(list_of_variable_names, file)  # Store all the names first
        for variable_name in list_of_variable_names:
            pickle.dump(eval(variable_name), file) # Store the objects themselves
            
""" Test the load part """
def load():
    file_name = 'savefile'
    g = globals()

    with open(file_name,'rb') as file:
        list_of_variable_names = pickle.load(file)  # Get the names of stored objects
        for variable_name in list_of_variable_names:
            g[variable_name] = pickle.load(file)    # Get the objects themselve
