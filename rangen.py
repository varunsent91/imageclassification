
import numpy as np
import math
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


arr = pd.read_csv("image.deep.fea",delim_whitespace=True, header = None)
rows = 50

g = nx.Graph()

largest = {}

count  = 0 
for vec1 in range(1,rows):
	v = arr.iloc[vec1,1:]


	mag = math.sqrt(sum(i**2 for i in v))

	v = v/mag

	for vec2 in range(1,rows): 
		v2 = arr.iloc[vec2,1:]
		
		mag2 = math.sqrt(sum(i**2 for i in v2))
		v2 = v2/mag2
		count +=1 
		if np.dot(v, v2) > 0.8 and np.dot(v,v2) != 1.0:
			 
			g.add_edge(arr.iloc[vec1,0],arr.iloc[vec2,0],weight=str(np.dot(v,v2)))
			if arr.iloc[vec1,0] in largest:
				largest[arr.iloc[vec1,0]] += 1
			else:
				largest[arr.iloc[vec1,0]] = 1

key, value = max(largest.iteritems(), key=lambda x:x[1])
print key,value

nx.draw(g)
plt.draw()
plt.show()
