from sys import flags
import wx
from wx.core import MAXIMIZE_BOX, PasswordEntryDialog, TE_PASSWORD
from Connection import Connection


class QueryFrame(wx.Frame):
	def __init__(self, parent, title, connection:Connection):
		super(QueryFrame,self).__init__(parent, title=title)

		self.panel = wx.Panel(self)
		self.superSizer = wx.BoxSizer(wx.VERTICAL)

		self.connect = connection
		dbInfo = wx.StaticText(self.panel, label ="Logged into " + self.connect.name)
		self.superSizer.Add(dbInfo, 0, wx.ALL | wx.CENTER,5)

		self.changeUserBTN = wx.Button(self.panel, label='Change User')
		self.changeUserBTN.Bind(wx.EVT_BUTTON, self.changeUserLISTEN)
		self.superSizer.Add(self.changeUserBTN,0,wx.ALL | wx.CENTER,5)

		self.queryIN = wx.TextCtrl(self.panel)
		self.superSizer.Add(self.queryIN,0, wx.ALL | wx.CENTER | wx.EXPAND , 5 )

		self.executeQueryBTN = wx.Button(self.panel, label = "Execute Command")
		self.executeQueryBTN.Bind(wx.EVT_BUTTON, self.executeQueryLISTEN)
		self.superSizer.Add(self.executeQueryBTN,0,wx.ALL | wx.CENTER,5)

		

		self.panel.SetSizer(self.superSizer)
		self.Centre()

	def changeUserLISTEN(self, event):
		self.Hide()

		login = LoginFrame()
		login.Show()

	def executeQueryLISTEN(self,event):
		cmd = self.queryIN.GetValue()

		if not cmd:
			print('Empty Query')
		else:
			print (cmd)
			result = self.connect.execute(cmd)
			print(result)
		

class LoginFrame (wx.Frame):
	def __init__(self, parent=None, title="Log In"):
		super(LoginFrame,self).__init__(parent, title=title, style= wx.MAXIMIZE_BOX | wx.CLOSE_BOX)
		self.panel = wx.Panel(self)
		self.sizer = wx.BoxSizer(wx.VERTICAL)


		self.inputName= wx.TextCtrl(self.panel, pos=(5, 5))
		self.sizer.Add(self.inputName,0, wx.ALL | wx.EXPAND, 5)

		self.inputPassword = wx.TextCtrl(self.panel, pos=(155,5), style=TE_PASSWORD)
		self.sizer.Add(self.inputPassword,0, wx.ALL | wx.EXPAND, 5)

		self.my_btn = wx.Button(self.panel, label='Login', pos=(5, 55))
		self.my_btn.Bind(wx.EVT_BUTTON,self.btnListener)
		self.sizer.Add(self.my_btn,0, wx.ALL | wx.CENTER, 5)

		self.LoginPrompt = wx.StaticText(self.panel, label="Please Login")
		self.sizer.Add(self.LoginPrompt,0, wx.ALL | wx.CENTER, 5)

		self.panel.SetSizer(self.sizer)

		# Makes sure the login prompt spawns in the middle of the screen 
		self.Centre()

	def btnListener(self, event):
		name = self.inputName.GetValue()
		password = self.inputPassword.GetValue()
		if not name:
			print('No input')
		else:
			try:
				self.connection = Connection(userName= name, psswrd= password)
				print ('SUCCESS')
				self.LoginPrompt.SetLabel("Successfully Logged In")

				self.Hide()
				
				nextFrame = QueryFrame(parent = None, title="Database", connection = self.connection)
				nextFrame.Show()
			except Exception as e:
				self.LoginPrompt.SetLabelText("Failed to Login")
				print(e)
				print("Failed to connect to the database")
				self.Show()

class App(wx.App):
	def OnInit(self):
		self.frame = LoginFrame(parent=None, title="Login")
		self.frame.Show()

		return True

app = App()
app.MainLoop()