#  English letter typing program 
import wx, time 
from random import randint
from datetime import timedelta
import typingGUI
    
#  打字計時一分鐘
class Typing():
    def onTimerTick(self, e):
        global startTime
        passTime = int(61-(time.time() - startTime))  # 倒時計時
        frame.staticTextTime.SetLabel(str(timedelta(seconds= passTime)))
        if passTime <= 0 :
            frame.timer.Stop()

#  尚待努力，用選擇子功能名稱來控制不同的相對功能,以精簡程式碼
#        miid = event.GetId() 
#        print(miid)

#  本位列子選單功能
    def ontypeHome(self, event):        
        self.typeInitial()  # 打字起始設定
        self.homeQuestion()  # 產生本位列打字題目
        frame.typeHeadMessage.SetLabel('本位列一分鐘') # 顯示標題
        self.setQuestion()  # 顯示要打的字母題目
    
#  上一列子選單功能
    def ontypeUpper(self, event):        
        self.typeInitial()
        self.upperQuestion()
        frame.typeHeadMessage.SetLabel('上一列一分鐘')
        self.setQuestion()

# 下一列子選單功能
    def ontypeLower(self, event):        
        self.typeInitial()
        self.lowerQuestion()
        frame.typeHeadMessage.SetLabel('下一列一分鐘')
        self.setQuestion()

#  全盤鍵子選單功能
    def ontypeWhole(self, event):
        self.typeInitial()
        self.wholeQuestion()
        frame.typeHeadMessage.SetLabel('全部字母一分鐘')
        self.setQuestion()

#  產生本位列五百個字母    
    def homeQuestion(self):
        global question
        question = []
        questionLetter = [97,115,100,102,103,104,106,107,108] #本位列字母小寫ASCII碼
        for i in range(500):
            rndNum = randint(97, 122)
            if rndNum in questionLetter:
                question.append(rndNum) 

#  產生上一列五百個字母
    def upperQuestion(self):
        global question
        question = []
        questionLetter = [113, 119, 101, 114, 116,
                          121, 117, 105, 111, 112]  # 上一列字母小寫ASCII碼
        for i in range(500):
            rndNum = randint(97, 122)
            if rndNum in questionLetter:
                question.append(rndNum) 

#  產生下一列五百個字母
    def lowerQuestion(self):
        global question
        question = []
        questionLetter = [122, 120, 99, 118, 98, 110, 109]  # 下一列字母小寫ASCII碼
        for i in range(500):
            rndNum = randint(97, 122)
            if rndNum in questionLetter:
                question.append(rndNum) 

#  產生全鍵盤五百個字母
    def wholeQuestion(self):
        global question
        question = []
        for i in range(500):
            rndNum = randint(97, 122)  # 全部小寫英字母ASCII碼
            question.append(rndNum) 

#  打字起始設定   
    def typeInitial(self):    
        global right, startTime, questionIdx  
        self.refresh()  # 起始鍵盤指示畫面
        frame.keyin.Enable()  # 啓動48行的輸入字母欄位
        frame.keyin.SetValue('')  # 輸入字母欄位清空
        frame.keyin.SetFocus()  # 游標移到輸入字母欄位
        frame.endTime.SetLabel('')  
        frame.score.SetLabel('')
        startTime = time.time()
        frame.timer.Start(700)  # 跳秒區間設定
        right = 0
        questionIdx = 0

#  起始鍵盤指示畫面    
    def refresh(self):
        for i in range(97,123):
            rndLetter = chr(i)
            labelLetter = '  '+ rndLetter +'  ' # 一個鍵的字母放中間
            Xposition = position[rndLetter][0]  # 鍵在螢幕位置,參205行
            Yposition = position[rndLetter][1]
            # 顯示鍵的鍵顏色,參213行
            wx.StaticText(parent=frame.panelType, label=labelLetter,
                          pos=(Xposition,Yposition)).SetBackgroundColour(color[rndLetter])

#  指示要輸入的字母在鍵盤位置,背景改為灰色       
    def setQuestion(self):
        global rndLetter, Xposition,Yposition
        rndLetter = chr(question[questionIdx])  # 取一個要輸入的字母
        frame.typeQuestion.SetLabel(rndLetter)  # 顯示題目,參48行
        labelLetter = '  '+ rndLetter +'  '
        Xposition = position[rndLetter][0]
        Yposition = position[rndLetter][1]
        wx.StaticText(parent=frame.panelType, label=labelLetter,
                      pos=(Xposition,Yposition)).SetBackgroundColour("gray")

#  輸入字母後的計數   
    def onCharEvent(self, event):
        global right, questionIdx
        keycode = event.GetKeyCode()  # 取得按鍵內碼
        answer = chr(keycode).lower()  # 轉成小寫字母內碼
        if answer == rndLetter:
            right += 1
            rightType = "打對"+str(right)+"鍵"
            frame.score.SetLabel(rightType)
            labelLetter = '  '+ rndLetter +'  '  # 改色變灰色鍵為原來顏色
            wx.StaticText(parent=frame.panelType, label=labelLetter, pos=(Xposition,Yposition)).SetBackgroundColour(color[rndLetter])
            event.Skip()  # 繼續打字輸入事件
            frame.messageInput.SetLabel(' ')  # 輸入處清空
            questionIdx += 1
            self.setQuestion()  # 到173行顯示要打的字母
        else: 
            frame.messageInput.SetLabel(answer)  # 打錯時出現紅色字母
        if time.time()-startTime >= 60:
            frame.endTime.SetLabel('時間到')
            frame.typeQuestion.SetLabel('')
            frame.keyin.SetValue('')
            frame.keyin.Disable()
    
#  Run the program
if __name__ == "__main__":
    global position, color

#  含字母的鍵位置參數
    position ={'q' : [100, 300], 'w' : [200, 300], 'e' : [300, 300], 'r' : [400, 300],
               't' : [500, 300], 'y' : [600, 300], 'u' : [700, 300], 'i' : [800, 300],
               'o' : [900, 300], 'p' : [1000, 300], 'a' : [150, 370], 's' : [250, 370],
               'd' : [350, 370], 'f' : [450, 370], 'g' : [550, 370], 'h' : [650, 370],
               'j' : [750, 370], 'k' : [850, 370], 'l' : [950, 370], 'z' : [200, 440], 
               'x' : [300, 440], 'c' : [400, 440], 'v' : [500, 440], 'b' : [600, 440],
               'n' : [700, 440], 'm' : [800, 440]}

#  含字母的鍵顏色參數
    color ={'q' : "plum", 'w' : "plum", 'e' : "plum", 'r' : "plum",
               't' : "plum", 'y' : "plum", 'u' : "plum", 'i' : "plum",
               'o' : "plum", 'p' : "plum", 'a' :"green", 's' :"green",
               'd' : "green", 'f' : "purple", 'g' : "green", 'h' : "green",
               'j' : "purple", 'k' : "green", 'l' : "green", 'z' : "coral", 
               'x' : "coral", 'c' : "coral", 'v' : "coral", 'b' : "coral",
               'n' : "coral", 'm' : "coral"}

    app = wx.App()
    typing = Typing()
    frame = typingGUI.GUI(typing)
    frame.Show() # 顯示息含功能選擇表的螢幕訊息    
    typing.refresh()  # 顯示鍵盤    
    app.MainLoop()
