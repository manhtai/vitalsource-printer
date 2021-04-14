# Print a book from VitalSource Bookshelf to PDF

This script simulates mouse click in the next page button and takes screenshot
of current page in the opened book.

This script depends on pyautogui for automating mouse clicks and screenshots.
pyautogui uses the Pillow module for screenshots. OS X uses the "screencapture"
command. Linux uses the "scrot" command, which you may need to install.

## Usage

```bash
pip install -r requirements.txt
python app.py top_left right_bottom next_button total_page
# Ex: python app.py 153,78 892,990 941,537 785
```
