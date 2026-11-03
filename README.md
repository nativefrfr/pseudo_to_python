# Pseudocode to Python

Reads a pseudocode file and writes out the equivalent Python.

## Running

```
python convert.py examples/example.pseudo outputfile.py
```

## Files

| File                    | Job                                              |
|-------------------------|--------------------------------------------------|
| `convert.py`            | main file to convert pseudo to python.           |
| `examples/`             | example files to test                            |
| `lines.py`              | the list of lines it compares and replaces with  |
| `converted/`            | where the convered files end up afer run         |
| `generate_chain.py/`    | used to make lines.py into the big chunk in `convert.py` without typing allat        |

## How it works

the script reads the file line by line, replacing any words that are inside of `lines.py`. then writes it to `converted/`:

## Issues
if the pseudocode program does not have "quotation marks" around strings (e.g in prints,inputs) it will not put (brackets) around it. causing prints to fail

inputs do not account for if the progam expects an integer later on.
for example
```
a ← USERINPUT"enter number 1-10"
IF a > 3 THEN
    OUTPUT "number is greater than three"
ELSE THEN
    OUTPUT "number is less than three"
```

will come out as 

```python
a = input("enter number 1-10")
if a > 3:
    print("number is greater than three")
else:
    print("number is less than three")
```

which will always print ```"number is less than three"``` because a is a string with no mathmatical value

## extra notes

- this is for the AQA version of pseudo code so other ways may not be supported
- `lines.py` doesnt contain everything, it contains just what i remembered when typing this
- I honestly made this because i was bored and had nothing else to do, originally i was gonna make my own language but thats way too hard in python and im not even that good. Im just a 15 year old trying stuff out. I did not use ai for this project either, just me, my brain, and w3schools if i forgot something
- you might have to do some cleaning up. like adding ```str()``` and ```int()``` in places. do not use this on big projects it will not get it right

[<img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="Buy me a coffee!" />](https://buymeacoffee.com/nativefr)
