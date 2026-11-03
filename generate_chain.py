import pseudo_to_python.lines as lines

for name in vars(lines):
    if name.startswith("PS"):
        pyname = "PY" + name[2:]
        if hasattr(lines, pyname):
            print(f"    newline = translate_word(lines.{name},lines.{pyname},newline)")
