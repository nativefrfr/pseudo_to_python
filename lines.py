#lines
PSPRINT = "OUTPUT"
PYPRINT = "print"

PSINPUT = ["USERINPUT","INPUT"]
PYINPUT = "input()" #if pseudo has no text afterwards
#PYINPUT = "input" #if pseudo has text afterwards in quotes

#operands

PSEQUALTO = "="
PYEQUALTO = "=="

PSEQUALS = ["<--","←"," <-"]
PYEQUALS = "="

#loops and stuff

PSENDIF = "ENDIF"
PYENDIF = ""

PSENDWHILE = "ENDWHILE"
PYENDWHILE = ""

PSENDFOR = "ENDWHILE"
PYENDFOR = ""

PSELSEIF = ["ELSEIF","ELSE IF"]
PYELSEIF = "elif"

PSFOR = "FOR"
PYFOR = "for"

PSIF = "IF"
PYIF = "if"

PSWHILE = "WHILE"
PYWHILE = "while"

PSELSE = "ELSE"
PYELSE = "else:"

PSREPEAT = "REPEAT"
PYREPEAT = "while not"

PSTHEN = ["THEN","DO"]
PYTHEN = ":"

#comments

PSCOMMENT = "//"
PYCOMMENT = "#"

#error handling these are not correct. its to fix errors like >== and !==

PSGREATEQUAL = ">=="
PYGREATEQUAL = ">="

PSLESSEQUAL = "<=="
PYLESSEQUAL = "<="

PSNOTQUAL = "!=="
PYNOTQUAL = "!="

PSPLUSEQUAL = "+=="
PYPLUSEQUAL = "+="

PSMINUSEQUAL = "-=="
PYMINUSEQUAL = "-="

#AND OR

PSAND = "AND"
PYAND = "and"

PSOR = "OR"
PYOR = "or"

#fix lowercase true/false

PSTRUE = "true"
PYTRUE = "True"

PSFALSE = "false"
PYFALSE = "False"


# fix indent?

# PSINDENT = "    "
# PYINDENT = "    "

#casting

PSSTR = "INT_TO_STRING"
PYSTR = "str" #this will need brackets manually added

PSINT = "STRING_TO_INT"
PYINT = "int" #this MAY need brackets manually added