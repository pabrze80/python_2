mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
# Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

total_sales = (int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales))

total_sales = str(total_sales)

print(" Całkowity przychód z tygodnia wynosi : " , total_sales)

print("/--------------------------------------------------------------/")

# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# and try them out here

my_string = "jan nowak"
print(my_string.swapcase())


print("pętla while /--------------------------------------------------------------/")

my_string = "jan nowak"
i = 1
while i < 6:
    print(my_string.swapcase(), i)
    i += 1

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
wers = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(wers, "\n")

print("Wers ma długość {} znaki.".format(len(verse)))
print("The first occurence of the word 'and' occurs at the {}th index.".format(verse.find('and')))
print("The last occurence of the word 'you' occurs at the {}th index.".format(verse.rfind('you')))
print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))
wers = int(len(wers))
print("Wers ma długość {} znaków.".format(wers))
