# STL_to_MSH
This python script was made to mesh STL files.

The code uses GMSH library
The input is a folder of STL file and the output is a folder of MSH file.
You can ajust the parameters. The script uses multiprocessing.
You can custom the multiprocessing with your number of CPUs.

The code is structured as follow:

 1) Class
The first part of the code is a class to define the parameters of gmsh.
If you want to add more parameters, please add them inside the class and define them later on the mesh function.


 2) Report function
We create a report in txt format in which the stl files with problems are reported. 


 3) Mesher function
The input is a stl file. Inside the function you can change the path of the stl folder, the path for the result and the path for the report.
Then you find a ‘try’ to mesh. You have to call and define the mesh parameters. After you have all the step to mesh the file. After the ‘try’ you find the exception that return the report.


 4) Check
A little and very simple function to count te stl inside a folder.


 5) if main
Inside the main you define a path for the checker and the list.
For the multiprocessing we put in a list all the stl file. Using os.scandir and a for loop. 
After we define the number of CPU we want for the multiprocessing. And we create the pool.


 How to use the code ?
Go on mesher function and change the paths. Change also the path on the main for the multiprocessing
```python

'''
Mesh function
'''
def mesher(the_stl):
    # --PATH-- #

    # Put your own path:
    folder_stl = "C:/Users/folder_stl/"
    folder_msh = "C:/Users/folder_mesh/"
    folder_report = "C:/Users/report.txt"

'''
MAIN
'''
if __name__ == '__main__':

    # --PATH-- #

    path_stl = 'C:/Users/folder_stl'

```


# Analyzer
This python script was made to analyze MSH files.

The code uses meshio.
The input is a MSH file and the output are the number of nodes, edges and kind of mesh of the file.
How to use it? Go on add your path section and change the path and the file name.
```python
'''
Add your path
'''

path = "C:/Users/folder_mesh/"
file = "myfile.msh"

```

# References
 C. Geuzaine and J.-F. Remacle. Gmsh: a three-dimensional finite element mesh generator with built-in pre- and post-processing facilities. International Journal for Numerical Methods in Engineering 79(11), pp. 1309-1331, 2009.
 
 https://github.com/nschloe/meshio
