import webbrowser
import sys

urlStart = 'https://asitis.com/2/'
urlEnd = '.html'
rangeStart = int(sys.argv[1])
rangeEnd = int(sys.argv[2])
complete = ''
for i in range(rangeStart, rangeEnd):
    webbrowser.open(urlStart+str(i)+urlEnd)
