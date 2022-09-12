def reverse_string(string):
    lyst = list(string)
    lyst_rev = [lyst[i] for i in range(len(string) - 1, -1, -1)]
    return "".join(lyst_rev)

string = int(input("Input your string: "))
print(string)
string = reverse_string(string)
print(string)
