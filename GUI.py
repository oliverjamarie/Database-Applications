from sys import flags
import wx
import wx.grid
from wx.core import MAXIMIZE_BOX, Panel, PasswordEntryDialog, Sleep, TE_PASSWORD
from Connection import Connection
from Query_Resp import Query_Resp

class QueryOutputFrame(wx.Frame):
	def __init__(self,query_resp:Query_Resp, parent = None, title = "Query Output"):
		super(QueryOutputFrame,self).__init__(parent, title= title)
		
		self.mainSizer = wx.BoxSizer(wx.VERTICAL)

		self.grid = wx.grid.Grid(self, -1)
		
		results = query_resp.respl

		width = len(results[0])
		height = len(results)

		#creates a grid of width times height
		self.grid.CreateGrid(height,width)

		self.grid.SetRowSize(0, 120)
		self.grid.SetColSize(0,120)

		for i in range(0, height-1):
			for j in range (0, width-1):
				msg = '{}'.format(results[i][j])
				print ('{}\t{}\t{}\t'.format(i,j,msg))
				self.grid.SetCellValue(j,i,msg)
		self.mainSizer.Add(self.grid,0, wx.ALL| wx.CENTER, 5)
		
		self.Show()




class QueryFrame(wx.Frame):
	def __init__(self, parent, title, connection:Connection):
		super(QueryFrame,self).__init__(parent, title=title)

		self.panel = wx.Panel(self)
		self.mainSizer = wx.BoxSizer(wx.VERTICAL)

		self.connect = connection
		dbInfo = wx.StaticText(self.panel, label ="Logged into " + self.connect.name)
		self.mainSizer.Add(dbInfo, 0, wx.ALL | wx.CENTER,5)

		self.changeUserBTN = wx.Button(self.panel, label='Change User')
		self.changeUserBTN.Bind(wx.EVT_BUTTON, self.changeUserLISTEN)
		self.mainSizer.Add(self.changeUserBTN,0,wx.ALL | wx.CENTER,5)

		self.queryIN = wx.TextCtrl(self.panel)
		self.mainSizer.Add(self.queryIN,0, wx.ALL | wx.CENTER | wx.EXPAND , 5 )

		self.executeQueryBTN = wx.Button(self.panel, label = "Execute Command")
		self.executeQueryBTN.Bind(wx.EVT_BUTTON, self.executeQueryLISTEN)
		self.mainSizer.Add(self.executeQueryBTN,0,wx.ALL | wx.CENTER,5)

		permTypeStr = 'User Permission Types: \n'
		
		for i in self.connect.privilegeTypes:
			permTypeStr += i + '\n'

		self.permTypeTxt = wx.StaticText(self.panel, label = permTypeStr)
		self.mainSizer.Add(self.permTypeTxt, 0, wx.ALL | wx.CENTER)
		permStr = 'User Permissions:\n'

		for i in self.connect.privileges:
			permStr += i + '\n'

		self.permTxt = wx.StaticText(self.panel, label = permStr)
		self.mainSizer.Add(self.permTxt,0, wx.ALL | wx.CENTER,5)

		self.panel.SetSizer(self.mainSizer)
		self.Centre()
		

	def changeUserLISTEN(self, event):
		self.Destroy()

		login = LoginFrame()
		login.Show()

	def executeQueryLISTEN(self,event):
		cmd = self.queryIN.GetValue()

		if not cmd:
			print('Empty Query')
		else:
			result = self.connect.execute(cmd)
			QueryOutputFrame(result)
		

class LoginFrame (wx.Frame):
	def __init__(self, parent=None, title="Log In"):
		super(LoginFrame,self).__init__(parent, title=title, style= wx.MAXIMIZE_BOX | wx.CLOSE_BOX)
		self.panel = wx.Panel(self)
		self.sizer = wx.BoxSizer(wx.VERTICAL)


		self.inputName= wx.TextCtrl(self.panel, pos=(5, 5))
		self.sizer.Add(self.inputName,0, wx.ALL | wx.EXPAND, 5)

		self.inputPassword = wx.TextCtrl(self.panel, pos=(155,5), style=TE_PASSWORD)
		self.sizer.Add(self.inputPassword,0, wx.ALL | wx.EXPAND, 5)

		self.loginBTN = wx.Button(self.panel, label='Login', pos=(5, 55))
		self.loginBTN.Bind(wx.EVT_BUTTON,self.loginBTNListener)
		self.sizer.Add(self.loginBTN,0, wx.ALL | wx.CENTER, 5)

		self.LoginPrompt = wx.StaticText(self.panel, label="Please Login")
		self.sizer.Add(self.LoginPrompt,0, wx.ALL | wx.CENTER, 5)

		self.panel.SetSizer(self.sizer)

		# Makes sure the login prompt spawns in the middle of the screen 
		self.Centre()

	def loginBTNListener(self, event):
		name = self.inputName.GetValue()
		password = self.inputPassword.GetValue()
		if not name:
			print('No input')
		else:
			try:
				self.connection = Connection(userName= name, psswrd= password)
				print ('SUCCESS')
				self.LoginPrompt.SetLabel("Successfully Logged In")

				#self.Hide()
				
				nextFrame = QueryFrame(parent = None, title="Database", connection = self.connection)
				nextFrame.Show()

			except Exception as e:
				self.LoginPrompt.SetLabelText("Failed to Login")
				print(e)
				print("Failed to connect to the database")
				self.Show()

class App(wx.App):
	def OnInit(self):
		#self.frame = LoginFrame(parent=None, title="Login")

		#self.frame = QueryOutputFrame()

		self.frame = QueryFrame(None,'Query',  Connection(user_index=3))

		self.frame.Show()

		return True

app = App()
app.MainLoop()