'''
On-screen Popup Numpad for customtkinter
Author: Akash Bora
'''

from tkinter import *
from customtkinter import *
import sys

class PopupNumpad(CTkToplevel):
    
    def __init__(self, attach, x=None, y=None, keycolor=None,
                 fg_color=None, keyheight: int = 50, keywidth: int = 50,
                 alpha: float = 0.85, corner=20, point=True, **kwargs):
        
        super().__init__(takefocus=1)
        
        self.focus()
        self.corner = corner
        self.disable = True
        
        if sys.platform.startswith("win"):
            self.overrideredirect(True)
            self.transparent_color = self._apply_appearance_mode(self._fg_color)
            self.attributes("-transparentcolor", self.transparent_color)
        elif sys.platform.startswith("darwin"):
            self.overrideredirect(True)
            self.bind('<Configure>', lambda e: self.withdraw() if not self.disable else None, add="+")
            self.transparent_color = 'systemTransparent'
            self.attributes("-transparent", True)
        else:
            self.attributes("-type", "splash")
            self.transparent_color = '#000001'
            self.corner = 0
            self.withdraw()
            
        self.disable = False  
        self.fg_color = ThemeManager.theme["CTkFrame"]["fg_color"] if fg_color is None else fg_color
        self.frame = CTkFrame(self, bg_color=self.transparent_color, fg_color=self.fg_color, corner_radius=self.corner, border_width=2)
        self.frame.pack(expand=True, fill="both")
        self.attach = attach
        self.keycolor = ThemeManager.theme["CTkFrame"]["fg_color"] if keycolor is None else keycolor
        self.keywidth = keywidth
        self.keyheight = keyheight
        self.point = point
        
        self.resizable(width=False, height=False)
        self.transient(self.master)

        self.frame_color = ThemeManager.theme["CTkFrame"]["fg_color"]
        self.row1 = CTkFrame(self.frame, fg_color=self.frame_color)
        self.row2 = CTkFrame(self.frame, fg_color=self.frame_color)
        self.row3 = CTkFrame(self.frame, fg_color=self.frame_color)
        self.row4 = CTkFrame(self.frame, fg_color=self.frame_color)
        
        self.row1.grid(row=1, column=0, pady=(10,0))
        self.row2.grid(row=2, column=0, padx=10)
        self.row3.grid(row=3, column=0, padx=10)
        self.row4.grid(row=4, column=0, pady=(0,10))
    
        self._init_keys(**kwargs)
    
        # hide/show PopupNumpad
        self.attach.bind('<Key>', lambda e: self.withdraw() if not self.disable else None, add="+")
        self.attach.bind('<Double-Button-1>', lambda e: self._iconify(), add="+")
        self.bind('<FocusOut>', lambda e: self.withdraw() if not self.disable else None, add="+")
        
        self.update_idletasks()
        self.x = x
        self.y = y
        self._iconify()
        self.attributes('-alpha', alpha)
        
    def _init_keys(self, **kwargs):
        self.keys = {
            'row1' : ['7','8','9'],
            'row2' : ['4','5','6'],
            'row3' : ['1','2','3'],
            'row4' : ['.','0','◀']
            }
        
        for row in self.keys.keys(): 
            if row == 'row1':            
                i = 1                     
                for k in self.keys[row]:
                    CTkButton(self.row1,
                              text=k,
                              width=self.keywidth,
                              height=self.keyheight,
                              fg_color=self.keycolor,
                              command=lambda k=k: self._attach_key_press(k), **kwargs).grid(row=0,column=i)
                    i += 1
            elif row == 'row2':
                i = 2
                for k in self.keys[row]:
                    CTkButton(self.row2,
                              text=k,
                              width=self.keywidth,
                              height=self.keyheight,
                              fg_color=self.keycolor,
                              command=lambda k=k: self._attach_key_press(k), **kwargs).grid(row=0,column=i)
                    i += 1
                i = 2
            elif row == 'row3':
                i = 2
                for k in self.keys[row]:
                    CTkButton(self.row3,
                              text=k,
                              width=self.keywidth,
                              height=self.keyheight,
                              fg_color=self.keycolor,
                              command=lambda k=k: self._attach_key_press(k), **kwargs).grid(row=0,column=i)
                    i += 1

            elif row == 'row4':
                i = 2
                for k in self.keys[row]:
                    CTkButton(self.row4,
                              text=k,
                              width=self.keywidth,
                              height=self.keyheight,
                              fg_color=self.keycolor,
                              command=lambda k=k: self._attach_key_press(k), **kwargs).grid(row=0,column=i)
                    i += 1
            
            self.up = False
            self.hide = False
            
    def destroy_popup(self):
        self.destroy()
        self.disable = True
        
    def _iconify(self):
        if self.disable: return
        if self.hide:
            self.deiconify()
            self.focus()
            self.hide = False
            self.x_pos =  self.attach.winfo_rootx() if self.x is None else self.x
            self.y_pos = self.attach.winfo_rooty() + self.attach.winfo_reqheight() + 5 if self.y is None else self.y
            self.geometry('{}x{}+{}+{}'.format(self.frame.winfo_reqwidth(),
                                               self.frame.winfo_reqheight(),
                                               self.x_pos,self.y_pos))
        else:
            self.withdraw()
            self.hide = True
        
    def _attach_key_press(self, k):
        if k == '◀':
            try:
                text = self.attach.get(0.0, END)
                self.attach.delete(0.0, END)
                self.attach.insert(0.0, text[:-2])
            except TypeError:
                text = self.attach.get()
                self.attach.delete(0, END)
                self.attach.insert(0, text[:-1])
            return
        if k == ".":
            if self.point:
                self.attach.insert(INSERT, k)
        else:
            self.attach.insert(INSERT, k)

