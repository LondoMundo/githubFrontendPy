import wx
import os

class bucky(wx.Frame):
    
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Git GUI', size =(500,500))
        panel = wx.Panel(self)
        gitAddB = wx.Button(panel, label = "add", pos = (0,0), size =(60,60))
        gitAddAllB=wx.Button(panel, label = "add all", pos=(0,60), size=(60,60))
        self.Bind(wx.EVT_BUTTON, self.addAll, gitAddAllB)
        
        gitCommitB = wx.Button(panel, label="commit", pos = (60,0), size=(70,60))
        self.Bind(wx.EVT_BUTTON, self.commit, gitCommitB)
        
        gitPushB=wx.Button(panel, label="push", pos = (130,0), size=(60,60))
        self.Bind(wx.EVT_BUTTON, self.push, gitPushB)
        
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
        #os.system("mkdir /Users/colin/Desktop/helloworld")
        os.system("git clone " + repo+ " " + path)
        #use os.system(mkdir) with the git clone command so that we navigate to the directory THEN clone the file

    def addAll(self, event):
        specify = wx.DirDialog(None)
        specify.ShowModal()
        repo = specify.GetPath()
        os.system("cd " + repo + " && git add *")
#the function below this isn't done
    def commit(self, event):
        commitMessage = wx.TextEntryDialog(None, "Enter your commit message", "Git GUI", "Default")
        commitMessage.ShowModal()
        message = commitMessage.GetValue()
        print message
        os.system
        #do the same thing that i did in addAll cd to the directory, then run git commit -m message
        #otherwise it wont work, you can't pass a directory as an argument for git verbs, I guess.

    def push(self, event):
        #write a function that allows for the user to specify an alias of a directory(i.e. /Users/colin/python/stuff: stuff)
        os.system("cd ")
        pushMessage = wx.MessageDialog(None, "", "Pushed to server", wx.OK)
        pushMessage.ShowModal()
        pushMessage.Destroy()

if __name__ =='__main__':
    app=wx.PySimpleApp()
    frame = bucky(parent = None, id = -1)
    frame.Show()
    app.MainLoop()
