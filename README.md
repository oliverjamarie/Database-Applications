# Database-Applications

If the headers or lists aren't anchors, their documentation has not yet been written.   

GUI uses **wxPython** framework

# Files
* <a href = "#Main.py"> Main.py </a>
* <a href = "#Gui.py"> Gui.py </a>
* Connection.py
* Query_Resp.py
* Credentials.json

# <a name="Main.py"> Main.py </a> 
Main.py is used for testing and use case referencing mysql implementations.

## Global Variables

Variable | Description
-------- | -----------
data {} | Used to reference locally stored credentials from the **Credentials.json** file for the database ***LEGACY***
views [] | Used to reference the views from the database ***LEGACY***
tables [] | Used to reference the tables from the database ***LEGACY***
connect **Connection** | Connection object
mydb **mysql.connector.connection** | Reference to *connect.db* 
cursor **mysql.connector.cursor** | Refeence to *mydb.cursor()* 

## Functions

Function | Description
-------- | -----------
**void** init() | Populates *views* and *tables* ***LEGACY***
**void** dispTables() | Prints all tables from *tables* list
**void** dispTable(str) | Prints the data stored in the specified table
**void** dispViews() | Prints all the views from *views* list
**void** dispView(str) | Prints all the data stored in the specified view
**str** getUsers() | Returns an array of all the users in a database
**dict** getCredentials() | Opens and reads **Credentials.json** file to return a dictionary of the some of the users of the database ***LEGACY***

--------------
# <a name = "Gui.py"> Gui.py </a>
Handles the UI aspects of the application.  
Classes :  
* <a href="App"> App </a>
* <a href="LoginFrame"> Login Frame </a>
* QueryFrame
* QueryOutputFrame

## Classes
### <a name="App"> App(wx.App) </a>
Used to initialise the application
#### Functions
***bool*** OnInit() | Starts application
<br> <br>
### <a name="LoginFrame"> LoginFrame(wx.Frame) </a>
Used to allow a user to login to the database.  If the takes the inputs from __inputName__ and __inputPassword__ to attempt connecting to the database  
<br>
#### Frame Style:
* __wx.MAXIMIZE_BOX__ (user can minmize window)
* __wx.CLOSE_BOX__ (user can close the window)
#### Sizer:
  * Name: **sizer**  
  * Type: __wx.BoxSizer__  
#### Text Inputs:  
* __inputName__:
  * Purpose: Input field for the username
  * Sizer: sizer
* __inputPassword__ :
  * Purpose: Input field for the password
  * Style: __TE_PASSWORD__ (hides the input)
  * Sizer: sizer
* __loginBTN__:
  * Purpose: Attempts to login into database
  * Binded to: __loginBTNListener()__
  * Sizer: sizer
#### Static Texts:
* __LoginPrompt__ :
  * Purpose: 
    * Tells the user to log in
    * If the log in fails, it's used to tell the user that it failed


