# Monopoly comparison
# Tim Vergenz, 3/10/2012
#
# Chris Evans and I had fairly desirable Monopoly setups, and
# we were wondering which was more advantageous...

from __future__ import division
from itertools import product

props = {
	37: ('Park Place', 'Chris', 1100),    # 3 houses
	39: ('Boardwalk', 'Chris', 1400),     # 3 houses
	1:  ('Mediterranean', 'Chris', 250),  # hotel
	3:  ('Baltic', 'Chris', 450),         # hotel
	6:  ('Oriental', 'Tim', 550),         # hotel
	7:  ('Vermont', 'Tim', 550),          # hotel
	9:  ('Connecticut', 'Tim', 600),      # hotel
	11: ('St. Charles', 'Tim', 750),      # hotel
	13: ('States', 'Tim', 750),           # hotel
	14: ('Virginia', 'Tim', 900),         # hotel
}

avg_income = { 'Chris':0, 'Tim':0 }

for person in ['Chris', 'Tim']:

	# for each possible starting position
	for pos in range(0,40):
	
		# for each possible die roll
		for d1,d2 in product( range(1,7), range(1,7) ):
			if (pos+d1+d2)%40 in props:
				prop = props[(pos+d1+d2)%40]
				if prop[1]!=person:
					avg_income[prop[1]] += 1/40 * 1/36 * prop[2]
					
print avg_income
			

