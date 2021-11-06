def separing(num):
    a = []
    if num // 10 == 0:
        return [num]
    a.extend(separing(num // 10))
    a.append(num % 10)
    return a


def max_formed(num):
    listed = separing(num)
    p = -1
    for i in range(len(listed)-1, 0, -1):
        if listed[i] > listed[i - 1]:
            p = i - 1
            break

    if p == -1:
        return p
    right = listed[p:]
    left = listed[:p]
    pivot = right.pop(0)
    s_right = right.copy()
    s_right.sort()
    x = None
    for num in s_right:
        if num > pivot:
            x = num
            break
    right.pop(right.index(x))
    right.append(pivot)
    right.sort()

    result = int(''.join([str(integer) for integer in left + [x] + right]))
    return result


print(max_formed(978564321))
print(max_formed(513))
print(max_formed(2017))
print(max_formed(9))
print(max_formed(111))
print(max_formed(531))
