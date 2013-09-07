import wx
import os

class bucky(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Git GUI', size =(500,500))
        panel = wx.Panel(self)
        gitAddB = wx.Button(panel, label = "add", pos = (0,0), size =(60,60))
        gitCommitB = wx.Button(panel, label="commit", pos = (60,0), size=(70,60))
        gitPushB=wx.Button(panel, label="push", pos = (130,0), size=(60,60))
        gitCloneB=wx.Button(panel, label="clone", pos=(190, 0), size=(60,60))
        self.Bind(wx.EVT_BUTTON, self.clone, gitCloneB)
        


    def clone(self, event):
        print "hello clone"
        box=wx.TextEntryDialog(None, "What is the address of the repo you want to clone?", "Git GUI", "")
        box.ShowModal()
        repo = box.GetValue()
        print repo
        secondBox=wx.DirDialog(None)
        secondBox.ShowModal()
        path = secondBox.GetPath()
        print path
        os.system("mkdir /Users/colin/Desktop/helloworld")
        #os.system("git clone " + repo)
        #use os.system(mkdir) with the git clone command so that we navigate to the directory THEN clone the file

if __name__ =='__main__':
    app=wx.PySimpleApp()
    frame = bucky(parent = None, id = -1)
    frame.Show()
    app.MainLoop()
