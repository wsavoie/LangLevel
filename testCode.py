# import pyperclip


# text=pyperclip.paste()
# print(text)



# def getClipboard():
#     return pyperclip.paste()


import sys
addonName='MM'
sys.path.insert(1, r'C:\Users\WS\AppData\Roaming\Anki2\addons21\{0}'.format(addonName))
from morph import morphemes
from morph import morphemizer
# from morph import readability
import wx

def CreatePopupMenu():
        """Override from wx.TaskBarIcon. Creates the right-click menu."""
        menu = wx.Menu()
        menu.AppendCheckItem(self.TBMENU_PAUSE, _("Pause all"))
        menu.Check(self.TBMENU_PAUSE, self.is_paused)
        menu.Append(self.TBMENU_RESTORE, _("Restore"))
        menu.Append(self.TBMENU_CLOSE, _("Close"))
        return menu 

CreatePopupMenu()

win.setWindowIcon(QIcon('logo.png'))


# class TaskBarIcon(wx.TaskBarIcon):

#     def __init__(self, parent, MainFrame, workingdir):
#         wx.TaskBarIcon.__init__(self)
#         self.parentApp = parent
#         self.MainFrame = MainFrame
#         self.wx_id = wx.NewId()

#         if ON_WINDOWS:
#             icon_file = os.path.join(
#                             os.path.abspath(workingdir),
#                             'chronolapse.ico'
#                         )
#         else:
#             icon_file = os.path.join(
#                             os.path.abspath(workingdir),
#                             'chronolapse_24.ico'
#                         )
#         self.SetIcon(wx.Icon(icon_file, wx.BITMAP_TYPE_ICO), 'Chronolapse')
#         self.CreateMenu()

#     def toggle_window_visibility(self, event):
#         if self.MainFrame.IsIconized() or not self.MainFrame.IsShown():
#             self.set_window_visible_on(event)
#         else:
#             self.set_window_visible_off(event)

#     def set_window_visible_off(self, event):
#         self.MainFrame.Show(False)
#         self.set_icon_action_text(True)

#     def set_window_visible_on(self, event):
#         self.MainFrame.Iconize(False)
#         self.MainFrame.Show(True)
#         self.MainFrame.Raise()
#         self.set_icon_action_text(False)

#     def set_icon_action_text(self, minimized=True):
#         if minimized:
#             self.menu.FindItemById(self.wx_id).SetText("Restore")
#         else:
#             self.menu.FindItemById(self.wx_id).SetText("Minimize")

#     def iconized(self, event):
#         # bound on non-windows only
#         if self.MainFrame.IsIconized():
#             logging.debug("Main Frame Is Iconized")
#             self.set_icon_action_text(True)
#             self.MainFrame.Show(False)
#         else:
#             logging.debug("Main Frame Is Not Iconized")
#             self.set_icon_action_text(False)
#             self.MainFrame.Show(True)
#             self.MainFrame.Raise()

#     def CreateMenu(self):
#         self.Bind(wx.EVT_TASKBAR_RIGHT_UP, self.ShowMenu)
#         self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.toggle_window_visibility)
#         self.Bind(wx.EVT_MENU, self.toggle_window_visibility, id=self.wx_id)
#         self.Bind(wx.EVT_MENU, self.MainFrame.iconClose, id=wx.ID_EXIT)
#         if ON_WINDOWS:
#             self.MainFrame.Bind(wx.EVT_ICONIZE, self.set_window_visible_off)
#         else:
#             self.MainFrame.Bind(wx.EVT_ICONIZE, self.iconized)
#         self.menu=wx.Menu()
#         self.menu.Append(self.wx_id, "Minimize","...")
#         self.menu.AppendSeparator()
#         self.menu.Append(wx.ID_EXIT, "Close Chronolapse")

#     def ShowMenu(self,event):
#         self.PopupMenu(self.menu)
# ##        if self.MainFrame.IsShown() and not self.MainFrame.IsIconized():
# ##            self.menu.FindItemById(self.wx_id).SetText("Minimize")
# ##        else:
# ##            self.menu.FindItemById(self.wx_id).SetText("Restore")


# class TaskBarFrame(wx.Frame):
#     def __init__(self, parent, MainFrame, id, title, workingdir):
#         wx.Frame.__init__(self, parent, -1, title, size = (1, 1),
#             style=wx.FRAME_NO_TASKBAR|wx.NO_FULL_REPAINT_ON_RESIZE)
#         self.tbicon = TaskBarIcon(self, MainFrame, workingdir)
#         self.Show(True)
#         self.MainFrame = MainFrame

#     def kill(self, event):
#         event.Skip()
#         self.tbicon.RemoveIcon()
#         self.tbicon.Destroy()
#         self.Close()

#     def toggle_window_visibility(self, event):
#         self.tbicon.toggle_window_visibility(event)

#     def set_icon_action_text(self, minimized):
#         self.tbicon.set_icon_action_text(minimized)


# app = wx.App(0)
#     chronoframe = ChronoFrame(None, -1, "")
#     app.SetTopWindow(chronoframe)
#     chronoframe.doShow()
#     app.MainLoop()