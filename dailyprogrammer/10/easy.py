#This is sort of a regex problem
#One tiny assumption is that mixing of space/dash/dot notation is allowed, as this s not mentioned in the problem

from re import *

print(bool(compile(r'((\([0-9]{3}\)|[0-9]{3})[ -.]?)?[0-9]{3}[ -.]?[0-9]{4}').match(input())))