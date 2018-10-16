tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm\\a\\cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies \t%s
\t          \t%s
\t* Catnip\t* Grass
''' %("10 salmons","5 tuna")

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat