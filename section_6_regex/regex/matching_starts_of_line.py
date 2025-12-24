import re


text = """
I am going to take the gospel to England, it is a country with a long and complex history.
The weather END in England varies greatly throughout the year.
Some people say England has the best countryside in the world.
At the end of this sentence is a keywordEND. I choose to extend it.

France is known for its wine and cuisine.
Germany manufactures some of the best cars in Europe.
Italy has a rich cultural heritage and amazing food.
The Netherlands is famous for its windmills and tulips.

England stands out again at the start of this line.
This line ends with a specific marker: FINISH
Another random line of text to expand the block.
FinalLineEndMarkerXYZ

Scotland is part of the United Kingdom.
Wales is also part of the United Kingdom.
Northern Ireland completes the UK lineup. I am also going to take the gospel to these Kingdoms.

The last line ends right hereEND
"""

result = re.search(r"^England.{20}",text, re.DOTALL | re.MULTILINE) # ^ => matches the start of a string but with the flag re.MULTILINE, it matches the start of a line


print(f" Match 1: {result.group(0)}")


result = re.search(r".{12}END\s$",text, re.DOTALL | re.MULTILINE) # $ => matches the end of a string but with the flag re.MULTILINE, it matches the end of a line
print(f" Match 2: {result.group(0)}")