# -*- coding:utf-8 -*-
'''分割窗口
'''
import wx


class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title="分割窗口", size=(400, 300))
        self.Center()
        self.splitter = wx.SplitterWindow(self, -1)
        self.leftpanel = wx.Panel(self.splitter)
        self.rightpanel = wx.Panel(self.splitter)

        self.splitter.SplitVertically(self.leftpanel, self.rightpanel, 100)

        self.splitter.SetMinimumPaneSize(80)
        list2 = ['苹果', "橘子", "香蕉"]
        lb2 = wx.ListBox(self.leftpanel, -1, choices=list2, style=wx.LB_SINGLE)

        self.Bind(wx.EVT_LISTBOX, self.on_listbox, lb2)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(lb2, 1, flag=wx.ALL | wx.EXPAND, border=5)
        self.leftpanel.SetSizer(vbox1)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        self.content = wx.StaticText(self.rightpanel, label='右侧面板')
        vbox2.Add(self.content, 1, flag=wx.ALL | wx.EXPAND, border=5)
        self.rightpanel.SetSizer(vbox2)

    def on_listbox(self, event):
        s = '选择{0}'.format(event.GetString())  # 也是通过事件来获取字符串
        self.content.SetLabel(s)



class App(wx.App):
  ''' 自定以一个应用程序类
  '''
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):  # App在退出时自动调用这个OnExit方法
        print("应用程序退出")
        return 0


if __name__ == '__main__':
    app = App()  # 创建自定义对象App
    app.MainLoop()  # 进入事件主循环
