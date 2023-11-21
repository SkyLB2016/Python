#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()

# https://mail.263.net/att2e/servlet/AttachServlet?emailIdentity=0063fdacf30b5a97@005a@e0bebefd212a3703&folderId=1&tfid=null&preType=null&usr=libin@linlongyun.com&sid=M2wyaTNiMmkwbjZANWw1aTNu&fid=0&random=6687&fileName=%E5%BE%AE%E5%8D%9A-2.png&sts=1678355605358&chr=cn&downFileName=0&loginPlatform=partner&mobile=partner
# https://mail.263.net/wm2e/FileDownloadPreServlet.do?emailIdentity=0064004af80c58fb@0052@2d0387f3a80669c1&folderId=1&usr=libin@linlongyun.com&sid=MmwzaTRiMmk2bjdANWw1aTNu&fid=0&fileName=10%E6%9C%88%E4%BB%BDgame1.pptx&sts=1678355766371&chr=cn&downFileName=0&loginPlatform=partner&mobile=partner