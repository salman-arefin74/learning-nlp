person = "salman"
print(f"my name is {person}")

d = {'a':123, 'b':456}
print(f"my number is {d['a']}")

mylist = [0,1,2]
print(f"my number is {mylist[0]}")

library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]
for author, topic, pages in library:
  print(f"{author} {topic} {pages}")

library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]
for author, topic, pages in library:
  print(f"{author:{10}} {topic:{30}} {pages:{10}}") #here 10,30, and 10 are minimum space

"""
Author     Topic                          Pages     
Twain      Rafting                               601
Feynman    Physics                                95
Hamilton   Mythology                             144
"""

library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]
for author, topic, pages in library:
  print(f"{author:{10}} {topic:{30}} {pages:>{10}}")

"""
Author     Topic                               Pages
Twain      Rafting                               601
Feynman    Physics                                95
Hamilton   Mythology                             144
"""

%%writefile test.txt
Hello, this is a quick text file.
This is the second line of the file.

# The above command only works in Jupyter Notebook, this is for creating a text file.

myfile = open('test.txt') # Open the text file
myfile.read() # Read the opened file. This only works once because the pointer then points to EOF
myfile.seek(0) # This resets the pointer

content = myfile.read()
print(content)

myfile.close() # Close the file. You should always do it. It will cause issues if you open an already opened file from another program.

mylines = myfile.readlines() # This reads every line as a seperate item.
for line in mylines:
  print(line)

myfile = open('test.txt', 'w+') # To open in write mode. This will override the existing one.





