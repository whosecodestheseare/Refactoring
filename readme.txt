__________________ THE FOLLOWING IS THE FIX FOR WHERE I WAS STUCK __________________ 


IMPORT NUMPY COULD NOT BE RESOLVED FROM SOURCE PYLANCE (REPORT MISSING MODULE SOURCE)

objective is to use numpy with vscode editor

go to the folder where you want to place your project

right click (in windows 11) -> show more options -> open with code

and this will open that folder with vscode. Confirm that PYTHONAPPS is located in left explorer.

Now create your python/numpy  file/script. 

Create your python/numpy code eg.

import numpy as np

# create a 2d array
my_array = np.array([[1,2,3,],[4,5,6,],[7,8,9]])

#print the array
print(my_array)

#get the shape of the array
print(my_array.shape)

#get the datatype of the array
print(my_array.dtype)

#perform some basic arithmetic on the array
result = my_array + 2
print(result)

#calculate the mean of the array
mean = np.mean(my_array)
print(mean)


# THIS IS THE BIT I WAS STUCK ON!!

To install numpy in vscode: 

Click Terminal -> New Terminal -> 

Once the terminal is open you can choose between powershell and cmd in the sixth icon from the right, (click on the + sign and you see Powershell, Bash, CMD etc)

NOW CREATE A VIRTUAL ENVIRONMENT FOR YOUR PROJECT

C:\Users\THINKPAD\...     Downloads\python -m venv "u s e r e n v" (myenv)

Teacher Example:

C\\Users\codingbind\Desktop\pythonapps>python -m venv myenv  >PRESS ENTER

This will create a myenv folder on the left.

As a consequence you should a popup notification will state the following:

"We noticed a ne environment has been created. Do youo want to select it for the workspace folder?

Click Yes. 

once you click yes, vscode will recognise your virtual environment, you will see a few scripts

There will be a script called activate. 

Activate our virtual environment. Write the following command.

Write the name of your virtual environment folder

* Don't forget to hit the forward slash and not the backslash

C:\Users\codebind\Desktop\pythonapps>myenv\Scripts\activate


On the left under "myenv" (or whatever you file is called) you should see (in a dropdown menu

______________
activate      |
activate.bat  |
activate.ps1  |
deactivate.bat|
pip.exe       |
pip3.10.exe   |
pip3.exe      |
python_d.exe  |
python.exe    |
pyenv.cfg     |
______________

If you run without .bat 

you will see that your environment has been activated. Notice (in teerminal)

(myenv) C:|users\codebind\...etc

^
|  notice the parentheses (myenv) before the command. 

This means your environment has been activated. 

You can therefore install any package and it shall be relevant to this environment only.


pip install numpy


It should look like this (in terminal):  


C:\Users\codebind\Desktop\pythonapps\pip install numpy
Collecting numpy
   Using cached numpy...
installing collected packages: numpy
Successfully installed numpy-1.24.2
...

VIDEO CONTINUES FROM 4:44 to 08:23 in case furthr troubleshooting is required.




ProgrammingKnowledge2 https://www.youtube.com/watch?v=qGoR6H6HYfY