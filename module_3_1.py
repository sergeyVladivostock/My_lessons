calls = 0
j = ["Hello", "Cat", "Dog", "House"]


def count_calls():
    global calls
    calls = calls + 1
    return calls

def string_info(string):
    string = (len(string),string.upper(),string)
    count_calls()
    return string



def is_contains(string,list_to_search):
    count_calls()
    top = False
    for i in list_to_search:
        if string.lower() == i.lower():
            top = True
            break
    return top

count_calls()


print(string_info('Poffendui'))
print(is_contains("Hello",j))
print(calls)

