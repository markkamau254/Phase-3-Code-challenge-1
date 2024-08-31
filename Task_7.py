def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

print(sort_by_age([('Alice', 25), ('Bob', 20), ('Charlie', 30)]))