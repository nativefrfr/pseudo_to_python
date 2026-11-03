import sys
import pseudo_to_python.lines as lines
import os

filepath = sys.argv[1]
newfilename = sys.argv[2]
newfile = ""
def loadfile():
    global wholefile,all_lines
    with open(filepath, encoding="utf-8") as f:
        wholefile = f.read()
        #print(wholefile)
        all_lines = wholefile.split("\n")

def translate_word(psword,pyword,line):
    newline = line
    if type(psword) == list:
        for word in psword:
            newline = newline.replace(word,pyword)
    else:
        newline = newline.replace(psword,pyword)
    return newline



def translate_line(line):
    result = ""
    newline = translate_word(lines.PSPRINT,lines.PYPRINT,line)
    newline = translate_word(lines.PSINPUT,lines.PYINPUT,newline)
    newline = translate_word(lines.PSEQUALTO,lines.PYEQUALTO,newline)
    newline = translate_word(lines.PSEQUALS,lines.PYEQUALS,newline)
    newline = translate_word(lines.PSENDIF,lines.PYENDIF,newline)
    newline = translate_word(lines.PSENDWHILE,lines.PYENDWHILE,newline)
    newline = translate_word(lines.PSENDFOR,lines.PYENDFOR,newline)
    newline = translate_word(lines.PSELSEIF,lines.PYELSEIF,newline)
    newline = translate_word(lines.PSFOR,lines.PYFOR,newline)
    newline = translate_word(lines.PSIF,lines.PYIF,newline)
    newline = translate_word(lines.PSWHILE,lines.PYWHILE,newline)
    newline = translate_word(lines.PSELSE,lines.PYELSE,newline)
    newline = translate_word(lines.PSREPEAT,lines.PYREPEAT,newline)
    newline = translate_word(lines.PSTHEN,lines.PYTHEN,newline)
    newline = translate_word(lines.PSCOMMENT,lines.PYCOMMENT,newline)
    newline = translate_word(lines.PSGREATEQUAL,lines.PYGREATEQUAL,newline)
    newline = translate_word(lines.PSLESSEQUAL,lines.PYLESSEQUAL,newline)
    newline = translate_word(lines.PSNOTQUAL,lines.PYNOTQUAL,newline)
    newline = translate_word(lines.PSPLUSEQUAL,lines.PYPLUSEQUAL,newline)
    newline = translate_word(lines.PSMINUSEQUAL,lines.PYMINUSEQUAL,newline)
    newline = translate_word(lines.PSAND,lines.PYAND,newline)
    newline = translate_word(lines.PSOR,lines.PYOR,newline)
    newline = translate_word(lines.PSTRUE,lines.PYTRUE,newline)
    newline = translate_word(lines.PSFALSE,lines.PYFALSE,newline)
    newline = translate_word(lines.PSSTR,lines.PYSTR,newline)
    newline = translate_word(lines.PSINT,lines.PYINT,newline)

    omgquote = True
    for i in newline:
        if i == "\"":
            if omgquote:
                result += "(\""
                    
            else:
                result += "\")"
            omgquote = not omgquote
        else:
            result += i
    return result

def convert(all_lines):
    global newfile
    for line in all_lines:
        newfile += translate_line(line) + "\n"


def main():
    pass

def parsedatafromfile():
    global length,lineamt
    length = len(wholefile)
    lineamt = wholefile.count('\n')

def writefinish():
    os.makedirs("converted", exist_ok=True)
    with open(f"converted/{newfilename}","w",encoding="utf-8") as f:
        f.write(newfile)

if __name__ == "__main__":
    main()
loadfile()
parsedatafromfile()
print(f"length: {length}")
print(f"lineamt: {lineamt}")

convert(all_lines)
writefinish()