message = "Hello Python Crash Course reader!"
print(message)

name = "ada lovelace"
print(name.title()) #Ada Lovelace
print(name.upper()) #ADA LOVELACE
print(name.lower()) #ada lovelace

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name) #ada lovelace
print(f"Hello, {full_name.title()}!") #Hello, Ada Lovelace!

print("Languages:\n\tPython\n\tC\n\tJavaScript")
# Languages:
#         Python
#         C
#         JavaScript

fa = 'python '
print(fa.rstrip()) #python, fa itself still has whitespace

fa = ' python cool '
print(fa.lstrip()) #'python cool '
print(fa.rstrip) #' python cool'
print(fa.strip()) #'python cool'

mm = "https://python_notes.txt"
print(mm.removeprefix("https://")) #python_notes.txt
print(mm.removesuffix(".txt"))

#ex2.9
print(5+3) #8
print(9-1) #8
print(16/2) #8.0
print(2**3) #8

#ex2.10
fav = 6
message = f"my favorite number is {fav}."
print(message) #my favorite number is 6.