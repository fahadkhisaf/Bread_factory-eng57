# define the tests before we code the functions
from bread_factory import *
# test 1
print("When make dough is called with 'water' and 'flour' it should return 'dough'")

print(make_dough('water','flour') == 'dough')
print('got', make_dough('water','flour'))

# test 2 - make_dough()
print("When make dough is called with 'water' and 'cement' it should return 'not dough'")
make_dough('water','cement') == 'not dough'
print('got', make_dough('water','cement'))