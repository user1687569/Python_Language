# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

print(123)
print("Blockchain Lee")

a = 10
b = 10
print(a, id(a))
print(b, id(b))

print(a == b)
print(a is b)

scores = {'张三': 100, '李四': 98, '王五': 99}
for item in scores:
    print(item, scores[item])

t = tuple((123,))
print(t)
print(type(t))

print(set('Python'))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
