import wx
class GUI(wx.Frame):
 
    def __init__(self,typing):
        wx.Frame.__init__(self, parent=None, title="輕鬆學拼音", size=(1500,800), style = wx.DEFAULT_FRAME_STYLE)
        fontSize = wx.Font(28, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.NORMAL) # 設定字型大小
        
#  配置主選單元件
        menubar = wx.MenuBar()
        typeMenu = wx.Menu()
    
#  鍵盤快手元件子選單       
        menubar.Append(typeMenu, '&鍵盤快手')
        typeItem1 = wx.MenuItem(typeMenu, wx.ID_ANY, u"本位列 ", wx.EmptyString, wx.ITEM_NORMAL )
        typeMenu.Append(typeItem1)
        typeItem2 = wx.MenuItem(typeMenu, wx.ID_ANY, u"上一列", wx.EmptyString, wx.ITEM_NORMAL )
        typeMenu.Append(typeItem2)
        typeItem3 = wx.MenuItem(typeMenu, wx.ID_ANY, u"下一列", wx.EmptyString, wx.ITEM_NORMAL )
        typeMenu.Append(typeItem3)
        typeItem4 = wx.MenuItem(typeMenu, wx.ID_ANY, u"全部字母", wx.EmptyString, wx.ITEM_NORMAL )
        typeMenu.Append(typeItem4)

#  不指示位置的打字功能,尚未完成 
    #    typeItem5 = wx.MenuItem(typeMenu, wx.ID_ANY, u"不指示位置", wx.EmptyString, wx.ITEM_NORMAL )
    #    typeMenu.Append(typeItem5)

#  子選單連結事件        
        self.Bind(wx.EVT_MENU, typing.ontypeHome, typeItem1)
        self.Bind(wx.EVT_MENU, typing.ontypeUpper, typeItem2)
        self.Bind(wx.EVT_MENU, typing.ontypeLower, typeItem3)
        self.Bind(wx.EVT_MENU, typing.ontypeWhole, typeItem4)
        # self.Bind(wx.EVT_MENU, self.ontypeNoind, typeItem5)
        
#  啓動menuBar
        self.SetMenuBar(menubar) 

#  使用者全螢幕介面安排   
        self.panelType = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size(1500,800 ), wx.TAB_TRAVERSAL)
        self.panelType.SetFont(fontSize)
        self.typeMessage = wx.StaticText(parent=self.panelType, label='鍵盤快手--', pos=(10,10))
        self.typeHeadMessage = wx.StaticText(parent=self.panelType, label='', pos=(200,10))
        self.typeHeadMessage.SetForegroundColour('Blue')     
        self.typeQuestion = wx.StaticText(parent=self.panelType, label='', pos=(555,80))
        self.typeQuestion.SetForegroundColour('Blue')
        self.keyin = wx.TextCtrl(self.panelType, value="",pos=(550,120),size=(26,50))
        self.messageInput = wx.StaticText(parent=self.panelType, label='', pos=(552,123))
        self.messageInput.SetForegroundColour('RED')
        self.endTime = wx.StaticText(parent=self.panelType, label='', pos=(600,180))
        self.endTime.SetBackgroundColour('red')
        self.score = wx.StaticText(parent=self.panelType, label='', pos=(750,180))
        self.staticTextTime = wx.StaticText(parent=self.panelType, pos=(1000,200), label='')  
        self.staticTextTime.SetFont(wx.Font(22, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.NORMAL))
        self.messageWarn = wx.StaticText(parent=self.panelType, label='左手食指按ｆ鍵,右手食指按ｊ鍵,隨時歸位', pos=(200,550))
        self.messageWarn.SetFont(wx.Font(22, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.NORMAL))
        to_bmp_imageShow = wx.Image("type.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()  
        self.bitmapShow = wx.StaticBitmap(self.panelType,-1, to_bmp_imageShow, (800, 510))  
        image_width = to_bmp_imageShow.GetWidth()  
        image_height = to_bmp_imageShow.GetHeight() 
        self.timer = wx.Timer(self)         #放一個計時器timer
    
#  計時器與打字輸入的連結事件    
        self.Bind(wx.EVT_TIMER, typing.onTimerTick, self.timer)
        self.keyin.Bind(wx.EVT_CHAR, typing.onCharEvent) # 按任意鍵的連結
        
        def setTypeHeadMessage(self, title):
            self.typeHeadMessage.SetLabel(title)