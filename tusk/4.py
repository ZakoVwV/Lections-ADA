with open ('tusk/python.txt', 'w') as file:
    text = """
Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions;
you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2),
but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.
"""
    file.write(text)
o_words = []
with open ('tusk/python.txt', 'r') as file:
    words = file.read().split()
    for i in words:
        if 'o' in i:
            o_words.append(i)
    print(o_words)
    