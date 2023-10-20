#global var



#functions

def print_dict():
    me = {
        'name': 'jessie',
        'last': 'guerrero',
        'hobbies': ['playing', 'loving', 'coding']
    }

    print(me)

#read
    print(me['name'])

#add
    me['age'] = 30

#modify
    me['age'] = 25
    print(me)

#calll the functions
print_dict()