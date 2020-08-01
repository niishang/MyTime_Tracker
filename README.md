# MyTime_Tracker
Time tracker App - PYG-28

# Time Tracking Program
Problem - Nana wants to know the amount he has earned based on the number of hours he spends working

# Algorithm for Time Tracking Program
Input start date
Input start time
Input end date
Input end time
Calculate the number of hours between start time and end time.
***how is program going to cater for minutes***
Calculate the amount per hour
Store the number of hours and the rate per hour in an excel or csv file

# Program Dependencies
we imported all from tkinter. The tkinter package which is the standard python interface to the Tk GUI toolkit. 
Tkinter us a module in the python standard library which serves as an interface to Tk a simple toolkit which provides GUI elements to build an interface such as buttons, menus, entry fields, display areas -all of these are called widgets. Each widget has a parent widget.
This provided the GUI for the time tracker application
We imported csv module which implements classes to read and write tabular data in CSV. to help us save the time tracking info to the csv file
We imported datetime module to give the date along with time in hours, minutess, seconds and milliseconds.

# Design
Input  - start date and time, end date and time
Process - calculate number of hours worked, calculate money earned
Output - number of hours worked, money earned

# Implementation process
imported all from tkinter package which is the standard python interface to the Tk GUI toolkit. 
tkinter is a module in the python standard library which serves as an interface to Tk a simple toolkit which provides GUI elements to build an interface such as buttons, menus, entry fields, display areas -all of these are called widgets. each widget has a parent widget.
This provided the GUI for the time tracker application.

imported csv module  which implements classes to read and write tabular data in CSV. to help us push the time tracking info to the csv file.

imported datetime module to give the date along with time in hours, minutess, seconds and milliseconds.

A class called Window is created with the widget Frame. A class is created because a class is a set of objects with the same property or attribute in common. The class serves as a blue print for individual objects with exact behaviour. The class Window is going to contain objects with the same property.

Frame is a class widget. A container widget that is placed inside the class Window. Frame is used to group related widgets together in the time tracker application's layout.

__init__() is a function that will always execute when the class Window is being initiated. It assigns values to object properties and other operations that are necessary to do when the object is being created. 

The self parameter is a reference to the current instance of  the class Window. It is used to access variables that belong to the class Window. 

The pack method is used to aarange the widgets in a singular column inside the class Window. 

The widget class Menu is used to create a pulldown menu and assign it to the variable menu.

config() is used to configure resources which are Open and Exit of the widget menu.

The Menu widget configured to be the menubar of the root window is used to create a Menubar.
A fileMenu object is created. 
The menu is a dropdown containing the commands Open and Exit. 
The fileMenu is added to the menubar using the add_cascade method.

datetime.now() is used to get the current time in day, month, year.

Entry rows are created for Task Start time, Task End time, Hours worked, Amount Earned $.

Entry() widget is used to accept single line strings from the user of the time tracker application. bd stands for size of the border

grid() puts the widgets in a 2 dimensional table.

The current time is inserted into the entry widget created for it. 

A submit button is created which when clicked, the number of hours worked and the amount earned is calculated and all the information is wriiten into the csv file.

The labels of the entry fields are wriiten in the first row of the csv file.

A function called calculate is created to calculate the hours worked and the amount earned.

To calculate the hours worked(the final time elapsed) the start time is subtracted from the end time.

The total hours is converted to seconds and rounded to 2 decimal places. This is inserted into the entry field created.

The total hours which has been converted to seconds is multiplied by $5 and rounded to 2 decimal places. This is inserted into the entry field.

Functions are created for exiting the application and for opening the csv file.

root.mainloop() is a method on the main window which executes when the time tracker application is run. It will loop forever aiting for events from the user until the user exits the time tracker app by closing the application.

The root window is created using root = Tk(). This is the main application window.  


# Team
This is PYG-28. Papa Nii, Phoebe and Naa are the members of this team
