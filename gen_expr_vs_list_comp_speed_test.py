import time
gener_start_time = time.time() # time.time() returns the current time
print(sum(num for num in range(10000000)))
gener_duration = time.time() - gener_start_time

list_start_time = time.time()
print(sum([num for num in range(10000000)]))
list_duration = time.time() - list_start_time

print(f"sum((num for num in range(10000000))) took: {gener_duration}")
print(f"sum([num for num in range(10000000)]) took: {list_duration}")

gener_start_time = time.time()
print(sum(num for num in range(30000000)))
gener_duration = time.time() - gener_start_time

list_start_time = time.time()
print(sum([num for num in range(30000000)]))
list_duration = time.time() - list_start_time

print(f"sum((num for num in range(30000000))) took: {gener_duration}")
print(f"sum([num for num in range(30000000)]) took: {list_duration}")

# a generator expression is generally faster than a list comprehension, so unless we need to
# use all the data at once we should utilise a generator expression