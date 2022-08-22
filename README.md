# Print a book from VitalSource Bookshelf to PDF

This script simulates mouse click in the next page button and takes screenshot
of current page in the opened book.

This script depends on pyautogui for automating mouse clicks and screenshots.
pyautogui uses the Pillow module for screenshots. OS X uses the "screencapture"
command. Linux uses the "scrot" command, which you may need to install.

## Usage

```bash
pip install -r requirements.txt
python vitalsource-printer.py top_left right_bottom next_button total_page
# Ex: python vitalsource-printer.py 153,78 892,990 941,537 785
```

## Finding Cursor Coordinates

To find the coordinates you will need to supply as inputs for the
script, you may use "position()" function of the pyautogui module.

```bash
python
>>> import pyautogui
>>> pyautogui.position() # while cursor is on desired location
```

## GUI app (For macOS & Windows)

https://github.com/plainlab/plainprinter
