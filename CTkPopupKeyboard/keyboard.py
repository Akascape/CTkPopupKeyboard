'''
On-screen Popup Keyboard for customtkinter
Author: Akash Bora
'''

from tkinter import *
from customtkinter import *
import sys

class PopupKeyboard(CTkToplevel):
    
    def __init__(self, attach, x=None, y=None, key_color=None,
                 text_color=None, hover_color=None, fg_color=None,
                 keywidth: int = 5, keyheight: int = 2, command=None,
                 alpha: float = 0.85, corner=20, **kwargs):
        
        super().__init__(takefocus=0)
        
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
            if not text_color:
                text_color = "black"
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
        self.keywidth = keywidth
        self.keyheight = keyheight
        self.keycolor = self._apply_appearance_mode(ThemeManager.theme["CTkFrame"]["top_fg_color"]) if key_color is None else key_color
        self.textcolor = self._apply_appearance_mode(ThemeManager.theme["CTkLabel"]["text_color"]) if text_color is None else text_color
        self.hovercolor = self._apply_appearance_mode(ThemeManager.theme["CTkButton"]["hover_color"]) if hover_color is None else hover_color
        self.command = command
        self.resizable(width=False, height=False)
        self.transient(self.master)

        self.row1_1 = CTkFrame(self.frame)
        self.row2_1 = CTkFrame(self.frame)
        self.row3_1 = CTkFrame(self.frame)
        self.row4_1 = CTkFrame(self.frame)
        self.row5_1 = CTkFrame(self.frame)

        self.row1_2 = CTkFrame(self.frame)
        self.row2_2 = CTkFrame(self.frame)
        self.row3_2 = CTkFrame(self.frame)
        self.row4_2 = CTkFrame(self.frame)
        self.row5_2 = CTkFrame(self.frame)
        
        self.row1_1.grid(row=1, column=0, pady=(5,0))
        self.row2_1.grid(row=2, column=0, padx=5)
        self.row3_1.grid(row=3, column=0, padx=5)
        self.row4_1.grid(row=4, column=0)
        self.row5_1.grid(row=5, column=0, pady=(0,5))
    
        self._init_keys(**kwargs)
        
        # hide/show PopupKeyboard
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
            'row1' : ['1','2','3','4','5','6','7','8','9','0','◀'],
            'row2' : ['Tab','q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','\ '],
            'row3' : ['⋀','a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',';','Enter'],
            'row4' : ['z', 'x', 'c', 'v', 'b', 'n', 'm',',','.','?'],
            'row5' : ['[',']','+',' space ','-','~',"'"]
            }
        
        self.keys2 = {
            'row1' : ['!','@','#','$','%','^','&','*','(',')','◀'],
            'row2' : ['Tab','Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P','|'],
            'row3' : ['⋁','A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',':','Enter'],
            'row4' : ['Z', 'X', 'C', 'V', 'B', 'N', 'M','<','>','/'],
            'row5' : ['{','}','=',' space ','_','`','"']
            }
        
        for row in self.keys.keys(): 
            if row == 'row1':            
                i = 1                     
                for k in self.keys[row]:
                    Button(self.row1_1,
                           text=k,
                           width=self.keywidth,
                           height=self.keyheight,
                           bg=self.keycolor,
                           fg=self.textcolor,
                           highlightthickness=0,
                           borderwidth=1,
                           activebackground=self.hovercolor,
                           command=lambda k=k: self._attach_key_press(k), **kwargs).grid(row=0,column=i)
                    i += 1
                i = 1
                for k in self.keys2[row]:
                    Button(self.row1_2,
                           text=k,
                           width=self.keywidth,
                           height=self.keyheight,
                           bg=self.keycolor,
                           fg=self.textcolor,
                           highlightthickness=0,
                           borderwidth=1,
                           activebackground=self.hovercolor,
                           command=lambda k=k: self._attach_key_press(k), **kwargs).grid(row=0,column=i)
                    i += 1
            elif row == 'row2':
                i = 2
                for k in self.keys[row]:
                    Button(self.row2_1,
                           text=k,
                           width=self.keywidth,
                           height=self.keyheight,
                           bg=self.keycolor,
                           fg=self.textcolor,
                           highlightthickness=0,
                           borderwidth=1,
                           activebackground=self.hovercolor,
                           command=lambda k=k: self._attach_key_press(k), **kwargs).grid(row=0,column=i)
                    i += 1
                i = 2
                for k in self.keys2[row]:
                    Button(self.row2_2,
                           text=k,
                           width=self.keywidth,
                           height=self.keyheight,
                           bg=self.keycolor,
                           fg=self.textcolor,
                           highlightthickness=0,
                           borderwidth=1,
                           activebackground=self.hovercolor,
                           command=lambda k=k: self._attach_key_press(k), **kwargs).grid(row=0,column=i)
                    i += 1
            elif row == 'row3':
                i = 2
                for k in self.keys[row]:
                    Button(self.row3_1,
                           text=k,
                           width=self.keywidth,
                           height=self.keyheight,
                           bg=self.keycolor,
                           fg=self.textcolor,
                           highlightthickness=0,
                           borderwidth=1,
                           activebackground=self.hovercolor,
                           command=lambda k=k: self._attach_key_press(k), **kwargs).grid(row=0,column=i)
                    i += 1
                i = 2
                for k in self.keys2[row]:
                    Button(self.row3_2,
                           text=k,
                           width=self.keywidth,
                           height=self.keyheight,
                           bg=self.keycolor,
                           fg=self.textcolor,
                           highlightthickness=0,
                           borderwidth=1,
                           activebackground=self.hovercolor,
                           command=lambda k=k: self._attach_key_press(k), **kwargs).grid(row=0,column=i)
                    i += 1
            elif row == 'row4':
                i = 2
                for k in self.keys[row]:
                    Button(self.row4_1,
                           text=k,
                           width=self.keywidth,
                           height=self.keyheight,
                           bg=self.keycolor,
                           fg=self.textcolor,
                           highlightthickness=0,
                           borderwidth=1,
                           activebackground=self.hovercolor,
                           command=lambda k=k: self._attach_key_press(k), **kwargs).grid(row=0,column=i)
                    i += 1
                i = 2
                for k in self.keys2[row]:
                    Button(self.row4_2,
                           text=k,
                           width=self.keywidth,
                           height=self.keyheight,
                           bg=self.keycolor,
                           fg=self.textcolor,
                           highlightthickness=0,
                           borderwidth=1,
                           activebackground=self.hovercolor,
                           command=lambda k=k: self._attach_key_press(k), **kwargs).grid(row=0,column=i)
                    i += 1
            else:
                i = 3
                for k in self.keys[row]:
                    if k == ' space ':
                        Button(self.row5_1,
                               text=k,
                               width=self.keywidth * 3,
                               height=self.keyheight,
                               bg=self.keycolor,
                               fg=self.textcolor,
                               highlightthickness=0,
                               borderwidth=1,
                               activebackground=self.hovercolor,
                               command=lambda k=k: self._attach_key_press(k), **kwargs).grid(row=0,column=i)
                    else:
                        Button(self.row5_1,
                               text=k,
                               width=self.keywidth,
                               height=self.keyheight,
                               bg=self.keycolor,
                               fg=self.textcolor,
                               highlightthickness=0,
                               borderwidth=1,
                               activebackground=self.hovercolor,
                               command=lambda k=k: self._attach_key_press(k), **kwargs).grid(row=0,column=i)
                    i += 1
                i = 3
                for k in self.keys2[row]:
                    if k == ' space ':
                        Button(self.row5_2,
                               text=k,
                               width=self.keywidth * 3,
                               height=self.keyheight,
                               bg=self.keycolor,
                               fg=self.textcolor,
                               highlightthickness=0,
                               borderwidth=1,
                               activebackground=self.hovercolor,
                               command=lambda k=k: self._attach_key_press(k), **kwargs).grid(row=0,column=i)
                    else:
                        Button(self.row5_2,
                               text=k,
                               width=self.keywidth,
                               height=self.keyheight,
                               bg=self.keycolor,
                               fg=self.textcolor,
                               highlightthickness=0,
                               borderwidth=1,
                               activebackground=self.hovercolor,
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
        if k == 'Enter':
            if self.command: self.command()
            self.withdraw()
            
        elif k == '⋁' or k =='⋀':
            if self.up:
                self.up = False
                self.row1_2.grid_forget()
                self.row2_2.grid_forget()
                self.row3_2.grid_forget()
                self.row4_2.grid_forget()
                self.row5_2.grid_forget()

                self.row1_1.grid(row=1, column=0, pady=(5,0))
                self.row2_1.grid(row=2, column=0, padx=5)
                self.row3_1.grid(row=3, column=0, padx=5)
                self.row4_1.grid(row=4, column=0)
                self.row5_1.grid(row=5, column=0, pady=(0,5))
            else:
                self.up = True
                self.row1_1.grid_forget()
                self.row2_1.grid_forget()
                self.row3_1.grid_forget()
                self.row4_1.grid_forget()
                self.row5_1.grid_forget()

                self.row1_2.grid(row=1, column=0, pady=(5,0))
                self.row2_2.grid(row=2, column=0, padx=5)
                self.row3_2.grid(row=3, column=0, padx=5)
                self.row4_2.grid(row=4, column=0)
                self.row5_2.grid(row=5, column=0, pady=(0,5))
            self.focus_set()
            self.update()
        elif k == ' space ':
            self.attach.insert(END, ' ')
        elif k == '◀':
            try:
                text = self.attach.get(0.0, END)
                self.attach.delete(0.0, END)
                self.attach.insert(0.0, text[:-2])
            except TypeError:
                text = self.attach.get()
                self.attach.delete(0, END)
                self.attach.insert(0, text[:-1])

        elif k == 'Tab':
            self.attach.insert(END, '    ')
        else:
            self.attach.insert(INSERT, k)

