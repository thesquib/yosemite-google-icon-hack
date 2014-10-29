yosemite-google-drive-fix.sh
=========================
This script is a quick hack to fix the Google Drive menu bar icon when using the dark theme in Yosemite. It is a reversible operation, just run the script again.


google_hangouts_fix.py
=========================
The current versions of the Google Hangouts extension is not compatible with the
dark menu bar on Mac OS X Yosemite. This is *not* for the Google Hangouts App, only for the extension.

This simple script works with the current version of the Google Hangouts extension, and inverts the 
presence images so they are visible in the menu bar. 

To reverse, just run again. 

Assumptions:
Mac OS X Yosemite
Google Chrome with Google Hangouts extension
You know what you are doing (I wrote this for myself)
python is installed with python PIL or Pillow, i.e:
 brew install pillow
