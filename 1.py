# SLICE STRINGS

strings = input()
# line1
print(len(strings))
# line2
print(strings[-3:])
# line3
strings_reverse = strings[::-1]
for i in range(0, len(strings), 2):
    print(strings_reverse[i], end="")
print()
# line4
print(strings[:-2])
# line5
print(strings[:5])
# line6
for i in range(0, len(strings), 2):
    print(strings[i], end="")
print()
# line7
for i in range(1, len(strings), 2):
    print(strings[i], end="")
print()
# line8
print(strings_reverse)
# line9
print(strings[-2])
