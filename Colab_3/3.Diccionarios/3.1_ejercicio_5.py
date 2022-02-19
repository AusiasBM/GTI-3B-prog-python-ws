

# Escribe una función que reciba el siguiente diccionario y cuente la cantidad de items que tienen True el campo success:

dic = {
    1 : {'id': 1, 
    'success': True, 
    'name': 'Lary'
    }, 
    2 : {'id': 2, 
    'success': False, 
    'name': 'Rabi'
    }, 
    3 : {'id': 3, 
    'success': True, 
    'name': 'Alex'
    }
}

def countSuccesTrue(dic):
    countTrue = 0    
    for item in dic:
        if dic[item]['success']:
            countTrue += 1

    return countTrue

print (countSuccesTrue(dic))