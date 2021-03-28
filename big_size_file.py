#!/home/andrei/.pyenv/shims/python3
import os, pprint
from sys import argv, exc_info

trace = 1
dirname, extname = os.curdir, '.py'
if len(argv) > 1: dirname = argv[1]
if len(argv) > 2: extname = argv[2]
if len(argv) > 3: trace   = int(argv[3])

def try_print(arg):
    try:
        print(arg)
    except UnicodeDecodeError:
        print(arg.encode())                #Кодирует строку в байты(принем. строку)

visited = set()
allsizes = []
for (thisDir, subHere, filesHere) in os.walk(dirname):
    if trace: try_print(thisDir)
    thisDir = os.path.normpath(thisDir)    #нормализует путь, убирая избыточные делители и ссылки
    fixname = os.path.normcase(thisDir)    #нормализует регистор пути(в нижний)
    if fixname in visited:
        if trace: try_print('skipping ' + thisDir)
    else:
        visited.add(fixname)
        for filename in filesHere:
            if filename.endswith(extname):  #заканчивается ли строка указанныим постфиксом
                if trace > 1: try_print('+++' + filename)
                fullname = os.path.join(thisDir, filename)
                try:
                    bytesize = os.path.getsize(fullname)
                    linesize = sum(+1 for line in open(fullname, 'rb'))
                except Exception:
                    print('error', exc_info()[0])
                else:
                    allsizes.append((bytesize, linesize, fullname))

for (title, key) in [('bytes', 0), ('lines', 1)]:
    print('\nBy %s...' % title)
    allsizes.sort(key=lambda x: x[key])
    pprint.pprint(allsizes[:3])
    pprint.pprint(allsizes[-3:])
    print(argv)
