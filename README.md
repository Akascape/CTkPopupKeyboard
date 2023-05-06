# CTkPopupKeyboard
**On-Screen Keyboard/Numpad widget for customtkinter entries and textbox.**

## Features
- Customize keyboard and numpad styles 
- All keyboard characters available
- transparency effect
- double click popup window

![screenshot](https://user-images.githubusercontent.com/89206401/236622957-5e140b42-eeaa-41de-aeb3-a6d95d3023b1.png)

## Installation
### [<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Akascape/CTkPopupKeyboard?&color=white&label=Download%20Source%20Code&logo=Python&logoColor=yellow&style=for-the-badge"  width="400">](https://github.com/Akascape/CTkPopupKeyboard/archive/refs/heads/main.zip)

**Download the source code, paste the `ctkpopupkeyboard` folder in the directory where your program is present.**

## Example Program:
```python
from ctkpopupkeyboard import PopupKeyboard, PopupNumpad
import customtkinter

def show_popup():
    # Disable/Enable popup
    if switch.get()==1:
        keyboard.disable = False
        numpad.disable = False
    else:
        keyboard.disable = True
        numpad.disable = True
        
root = customtkinter.CTk()

text_box = customtkinter.CTkTextbox(root)
text_box.pack(fill="both", padx=10, pady=10)

# attach popup keyboard to text_box
keyboard = PopupKeyboard(text_box)

entry = customtkinter.CTkEntry(root, placeholder_text="Write Something...")
entry.pack(fill="both", padx=10, pady=10)

# attach popup keyboard to entry
numpad = PopupNumpad(entry)

switch = customtkinter.CTkSwitch(root, text="On-Screen Keyboard", command=show_popup)
switch.pack(pady=10)
switch.toggle()

root.mainloop()
```

## Arguments for PopupKeyboard/PopupNumpad
| Parameter | Description |
|-----------| ------------|
| **attach** | parent widget to which the keyboard will be attached  |
| x | **optional**, change the horizontal offset of the widget manually  |
| y | **optional**, change the vertical offset of the widget manually |
| keywidth | change the default width of the keys |
| keyheight | change the default height of the keys |
| **key_color** | change the fg_color of the buttons |
| text_color | change the text_color of the buttons |
| hover_color | change the hover_color of the buttons |
| **alpha** | change the transparency of the whole keyboard widget (range: 0-1) |
| **fg_color** | change the background frame color of the widget |
| corner | adjust roundness of the frame corners |
| relief | change the button style for keyboard, **only for PopupKeyboard:** (flat, raised, sunken, groove, ridge) |
| point | define if you want the point in numpad, **only for PopupNumpad:** boolean |
| _*Other Button Parameters_ | _All other parameters for ctkbutton/tkbutton can be passed in popupkeyboard_ |
