def count_pairs(number_list, target):
    count = 0
    for i in range(len(number_list)):
        for j in range(i+1, len(number_list)):
            if number_list[i] + number_list[j] == target:
                count += 1
    return count


print(count_pairs([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 10))
print(count_pairs([1, 3, 6, 2, 2, 0, 4, 5], 5))
