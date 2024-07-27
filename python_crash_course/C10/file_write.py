from pathlib import Path

path = Path('programming.txt') # if not txt, will create a new one
path.write_text("I love programming.")

contents = "I love creating new games.\nI also love working with data.\n"
path.write_text(contents) # this will override the txt