name = input("Whats your name ")
def format_name():
    name2 = name.title().strip()
    return name2

# input = "    SaMiR     "
# expected output = "Samir"
#
print('Input')
print(name)
print('Expected output: Samir')
print("Actual Output: ")
print(format_name())
print('The output is correct!')
