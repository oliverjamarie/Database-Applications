# Database-Applications


# Files
* <a href = "#Main.py"> Main.py </a>
* Gui.py
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
# Gui.py
Handles the UI aspects of the application.  
Objects :  
* App
* Login Frame
* QueryFrame
* QueryOutputFrame
