file = open('./message_02.txt', 'r')

commands = file.readline()

print(commands)
file.close()

value = 0
final_value = ""
for command in commands:
    if command == '#':
        value += 1
    elif command == '@':
        value -= 1
    elif command == '*':
        value *= value
    elif command == '&':
        final_value += str(value)

print(final_value)
