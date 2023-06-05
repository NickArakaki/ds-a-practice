import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    print(val)
    print(num / val)
    if num / val == val:
        return True
    return False

print(is_smart_number(1)) # true
print(is_smart_number(2)) # false
print(is_smart_number(7)) # false
print(is_smart_number(169)) # true
