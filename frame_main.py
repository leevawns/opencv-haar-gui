# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep 12 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class mainframe
###########################################################################

class mainframe ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"FACE RECOGNIZER", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 500,500 ), wx.DefaultSize )

		self.m_menubar = wx.MenuBar( 0 )
		self.m_menu_file = wx.Menu()
		self.m_menuItem_exit = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Exit"+ u"\t" + u"F1", u"exit program", wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menuItem_exit )

		self.m_menubar.Append( self.m_menu_file, u"File" )

		self.m_menu_about = wx.Menu()
		self.m_menuItem_about = wx.MenuItem( self.m_menu_about, wx.ID_ANY, u"about", u"about program", wx.ITEM_NORMAL )
		self.m_menu_about.Append( self.m_menuItem_about )

		self.m_menubar.Append( self.m_menu_about, u"About" )

		self.SetMenuBar( self.m_menubar )

		self.m_statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		bSizer = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"FACE DETECT AND RECOGNIZER PROGRAM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer4.Add( self.m_staticText2, 1, wx.ALL, 5 )


		bSizer.Add( bSizer4, 1, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_run = wx.Button( self, wx.ID_ANY, u"RUN", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button_run.SetBitmapFocus( wx.NullBitmap )
		self.m_button_run.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_button_run.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_button_run.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer3.Add( self.m_button_run, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button_train_dataset = wx.Button( self, wx.ID_ANY, u"TRAIN DATASET", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_train_dataset.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer3.Add( self.m_button_train_dataset, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button_create_dataset = wx.Button( self, wx.ID_ANY, u"CREATE DATASET", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_create_dataset.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer3.Add( self.m_button_create_dataset, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer.Add( bSizer3, 1, wx.EXPAND, 5 )

		self.m_staticline24 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer.Add( self.m_staticline24, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.mainframeOnClose )
		self.Bind( wx.EVT_MENU, self.m_menuItem_exitOnMenuSelection, id = self.m_menuItem_exit.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem_aboutOnMenuSelection, id = self.m_menuItem_about.GetId() )
		self.m_button_run.Bind( wx.EVT_BUTTON, self.m_button_runOnButtonClick )
		self.m_button_train_dataset.Bind( wx.EVT_BUTTON, self.m_button_train_datasetOnButtonClick )
		self.m_button_create_dataset.Bind( wx.EVT_BUTTON, self.m_button_create_datasetOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def mainframeOnClose( self, event ):
		event.Skip()

	def m_menuItem_exitOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItem_aboutOnMenuSelection( self, event ):
		event.Skip()

	def m_button_runOnButtonClick( self, event ):
		event.Skip()

	def m_button_train_datasetOnButtonClick( self, event ):
		event.Skip()

	def m_button_create_datasetOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog_type_name
###########################################################################

class MyDialog_type_name ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Type Name:", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText.Wrap( -1 )

		bSizer.Add( self.m_staticText, 0, wx.ALL, 5 )

		self.m_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer.Add( self.m_textCtrl, 0, wx.ALL, 5 )

		m_sdbSizer = wx.StdDialogButtonSizer()
		self.m_sdbSizerOK = wx.Button( self, wx.ID_OK )
		m_sdbSizer.AddButton( self.m_sdbSizerOK )
		self.m_sdbSizerCancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer.AddButton( self.m_sdbSizerCancel )
		m_sdbSizer.Realize();

		bSizer.Add( m_sdbSizer, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer )
		self.Layout()
		bSizer.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizerCancel.Bind( wx.EVT_BUTTON, self.m_sdbSizerOnCancelButtonClick )
		self.m_sdbSizerOK.Bind( wx.EVT_BUTTON, self.m_sdbSizerOnOKButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_sdbSizerOnCancelButtonClick( self, event ):
		event.Skip()

	def m_sdbSizerOnOKButtonClick( self, event ):
		event.Skip()


