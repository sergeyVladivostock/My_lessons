calls = 0
j = ["Hello", "Cat", "Dog", "House"]

string = input("Введите текст: ").lower()
def count_calls():
    global calls
    calls = calls + 1
    return calls

def string_info():

    global string
    string = (len(string),string.upper(),string)
    count_calls()
    return string



def is_contains():
    global string
    list_to_search = j
    if list_to_search.count(string):
        print(True)
    else:
        print(False)


print(string_info())
print(is_contains())
print(calls)

