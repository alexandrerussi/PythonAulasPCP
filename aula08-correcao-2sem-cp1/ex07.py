def even_count(lst):
    count = 0
    for x in lst:
        if x % 2 == 0:
            count += 1
    return count

print(even_count([1,2,3,4,6]))