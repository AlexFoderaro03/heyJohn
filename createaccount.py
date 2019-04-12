from termcolor import colored
print()
print()
print()
name = str(input(colored("What's your name? ", "green")))
file1 = open("yourname.txt", "w")
file1.write(name)
file1.close()