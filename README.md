# CTkPopupKeyboard
**On-Screen Keyboard/Numpad widget for customtkinter app.**

## Features
- Custom keyboard and numpad styles 
- All keyboard characters available
- transparency effect
- double click popup 

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
