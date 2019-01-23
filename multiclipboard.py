#Here’s what the program does:
#The command line argument for the keyword is checked.
#If the argument is save, then the clipboard contents are saved to the keyword.
#If the argument is list, then all the keywords are copied to the clipboard.
#Otherwise, the text for the keyword is copied to the clipboard.

#Usage:     py.exe multiclipboard.pyw save <keyword> - Saves clipboard to keyword.
   #        py.exe multiclipboard.pyw <keyword> - Loads keyword to clipboard.
   #        py.exe multiclipboard.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

#open the shelve file

mcbshelve = shelve.open('multiclipboard')

#save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower()=='save':
    mcbshelve[sys.argv[2]] = pyperclip.paste() #paste the keyword() which is the second argument to shelve file

elif(len(sys.argv)) ==2 :
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelve.keys())))
    elif sys.argv[1] in mcbshelve:
        pyperclip.copy(mcbshelve[sys.argv[1]])


#close the shelve file
mcbshelve.close()
