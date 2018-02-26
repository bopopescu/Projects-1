#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org

import  wx
def windows():
    app  = wx.App()
    window = wx.Frame(None,title = "第一个",size = (600,900))
    panel = wx.Panel(window)
    label = wx.StaticText(panel,label = "Hollo world" ,pos = (200,10))
    window.Show(True)
    app.MainLoop()

windows()