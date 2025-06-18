"""Test"""
def main ():
    """Test"""
original_list = [2, 8, 9, 48, 8, 22, -12, 2]
a = set(original_list)
new_list = []
for number in a:
    if number > 5:
        new_list.append(number + 2)
print(new_list)
main()
