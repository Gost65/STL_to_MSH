# Pierre LESBATS
# Cardiff University/ School of engineering
# ENI TARBES/ LGP

# # Analyzer Python script.

# The goal of this script is to count the number of nodes, elements edges in MSH file

"""
Import the libraries
"""

import meshio



'''
Analyze function
'''

def analyse(mesh_file):
    print("")
    pat = mesh_file.split()[2]
    name= pat.split('/')[2]
    print('--Informations for', name, ':')
    mesh = meshio.read(mesh_file)
    point_coordinates = mesh.points

    faces = 0
    for cell_type, value in mesh.cells:
        print("  {}: {}".format(cell_type, value.shape[0]))
        faces = faces + value.shape[0]

    vertices = len(point_coordinates)
    print(" Info:", vertices, 'nodes')  # or nodes
    print(" Info:", faces, 'elements')  # or elements
    '''
    #Euler's formula:
    v=vertices
    e=edges
    f=faces
    v-e+f=2
    '''
    edges = vertices + faces - 2
    print("")
    print(" Info:", edges, 'edges')
    return edges

'''
Add your path
'''

path = "C:/Users/folder_mesh/"
file = "my_file.msh"


'''
Analyze your file
'''
analyse(path+file)
