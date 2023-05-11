# Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
x[1] = [15,8,9]
##########################
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
##########################
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'[0]] = 'Andres'
##########################
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
##########################
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(dict):
    for dictionary in dict:
        for key, value in dictionary.items():
            print(f"{key} - {value}")

iterateDictionary(students)
##########################
# Create a function iterateDictionary2(key_name, 
# some_list) that, given a list of dictionaries and 
# a key name, the function prints the value stored 
# in that key for each dictionary. 

def iterateDictionary2(key_name, dict):
    for dictionary in dict:
        print(dictionary[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
##########################

# Create a function printInfo(some_dict) that 
# given a dictionary whose values are all lists, 
# prints the name of each key along with the 
# size of its list, and then prints the associated 
# values within each key's list.

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dict):
    for key, value in dict.items():
        print(f"{len(value)} {key.upper()}" )
        for val in value:
            print(val)
printInfo(dojo)
