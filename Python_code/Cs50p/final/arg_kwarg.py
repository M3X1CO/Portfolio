
# args creates a tuple of lists?
"""
def f(*args, **kwargs):
    print("Positional: ", args)

f(100, 50, 25)

"""

# kwargs creates a dictionary with key valued pairs

def f(*args, **kwargs):
    print("Named", kwargs)

f(galleons=100, sickles=50, knuts=25)