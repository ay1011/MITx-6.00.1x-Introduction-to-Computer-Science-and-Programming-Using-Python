"""
def beads(num_of_beads,set_color):
    if num_of_beads ==0:
        return [[]]
    array = beads(num_of_beads - 1, set_color)
    array = [ [set_color[j]]+array[i]  for j in range(len(set_color)) for i in range(len(array)) ]
    return array
"""
def beads(num_of_beads,set_color):
    array = [[]]
    for k in range (num_of_beads):
        array = [ [set_color[j]]+array[i]  for j in range(len(set_color)) for i in range(len(array)) ]
    return array

num_of_beads = 2
set_color = ['r','g','b']
print beads(num_of_beads,set_color)
print len(beads(num_of_beads,set_color))
#for i in range(len(beads(num_of_beads,set_color))):
#    print beads(num_of_beads,set_color)[i]


