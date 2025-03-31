import pandas as pd

D = [34,89,56,78,88,35,81,32,55,84]
I = ['a','b','c','d','e','f','g','h','i','j']

s = pd.Series(data=D, index=I)
s[s > 80] = s[s > 80] + 3
