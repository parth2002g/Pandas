import pandas as pd

data = {
	"Names": ["Parth", "Joshua", "Ronak"],
	"Roll No": [7, 8, 9]	
}

myvar = pd.DataFrame(data)

myvar2 = pd.DataFrame(data, index = ['a', 'b', 'c'])

print(myvar)

#To locate row
print(myvar.loc[[0,1]])

print(myvar2.loc[["a","b"]])