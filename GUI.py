from sys import flags
import wx
from wx.core import MAXIMIZE_BOX, PasswordEntryDialog, TE_PASSWORD
from Connection import Connection




class LoginFrame (wx.Frame):
	def __init__(self, parent, title):
		super(LoginFrame,self).__init__(parent, title=title, style= wx.MAXIMIZE_BOX | wx.CLOSE_BOX)
		self.panel = wx.Panel(self)
		self.sizer = wx.BoxSizer(wx.VERTICAL)


		self.inputName= wx.TextCtrl(self.panel, pos=(5, 5))
		self.sizer.Add(self.inputName,0, wx.ALL | wx.EXPAND, 5)

		self.inputPassword = wx.TextCtrl(self.panel, pos=(155,5), style=TE_PASSWORD)
		self.sizer.Add(self.inputPassword,0, wx.ALL | wx.EXPAND, 5)

		self.my_btn = wx.Button(self.panel, label='Press Me', pos=(5, 55))
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
			except:
				self.LoginPrompt.SetLabelText("Failed to Login")
				print("Failed to connect to the database")

class App(wx.App):
	def OnInit(self):
		self.frame = LoginFrame(parent=None, title="Login")
		self.frame.Show()

		return True

app = App()
app.MainLoop()