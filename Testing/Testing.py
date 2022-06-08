import time
import math

start_time = time.time()
# start


reps = 10000000 #10m
rep = 0

foo1 = 987654321.123456789
foo2 = math.pi

result = 0
while rep < reps:
    result = foo1 / foo2 * rep
    rep += 1

# end
end_time = time.time()

time_spent = end_time - start_time

print(int(time_spent * 1000), "ms")