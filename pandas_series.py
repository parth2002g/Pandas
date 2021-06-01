import pandas as pd

a = [1,5,6,3]

myvar = pd.Series(a, index = ["a","b","c","d"])

li = {"x":2, "y":4, "z":7}

myvar2 = pd.Series(li, index = ["x","y"])

print(myvar)

print(myvar[0])

print(myvar["c"])

print(myvar2)
