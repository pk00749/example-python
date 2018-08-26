#! /usr/bin/env python
#-*- encoding: utf-8 -*-
#author pythontab.com

#引入wx模块
import wx

#定义一个wx 的class
class sayHello(wx.App):

    def OnInit(self):
        frame = wx.Frame(parent=None,title="Hello wxPython")
        frame.Show()
        return True


app = sayHello()
#主循环
app.MainLoop()