'''1 = [('Hola', 'Don Pepito'),('Hola', 'Don jose'),('Buenos', 'dias')]
print (tuplas_a_diccionario(1))
{[('Hola', 'Don Pepito'),('Hola', 'Don jose'),('Buenos', 'dias')]}'''

def tuples_to_dict(tuple_list):
    '''conversion from a collection of given tuples to a dictionary key.
    The folloring elements will be appended to a listlinked to a their keys
    tuple_list (list): collection of tuples
    outples (dict): input converted as per above description '''
    my_dict = {}
    for my_tuple in tuple_list:
       key, *value = my_tuple
       key = str(key)
       if key in my_dict:
         my_dict [key].extend (value)
       else:
          my_dict [key] = value
    return my_dict

1 = [('Hola', 'Don Pepito'),('Hola', 'Don jose'),('Buenos', 'dias')]
print (tuples_to_dict(1))
12 = [(True,1,2,3), (True,'1','2',3) (1, 'Don Pepito'),('Hola', 'Don jose'),('Buenos', 'dias')]
print (tuples_to_dict(12))