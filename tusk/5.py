with open ('tusk/5.txt', 'w') as file:
    text2 = """
.detacilpmoc naht retteb si xelpmoC
.xelpmoc naht retteb si elpmiS
.ticilpmi naht retteb si ticilpxE
.ylgu naht retteb si lufituaeB
"""
    file.write(text2)

with open ('tusk/5.txt', 'r') as file:
    
    print(file.read()[:: -1])
