t = '$3.55'
p = float(t[1:])
print(p)

import string
import random
print(random.choice(string.digits))
a = 3
print(a%2)
l = [1,2,3,4,5,6,7,8]
print([x*2 for x in l if x%2])
print(list(map(lambda x: x + 1, filter(lambda x: x - 1, [-3, 0, 1]))))
print(max([('Alice', 5), ('Bob', 3), ('Charlie', 4), ('Diana', 2)], key=lambda x: x[0]))
s = 2
for i in range(5):
    s = s ** i

d = {1: 1, 2: 2, 3: 3}
di = d.copy()
for i in di.keys():
    print(i)
    if i < 4:
        d[i + 3] = i + 3
print(d)

def test_l(driver):
    driver.get("http://selenium2.ru")
    [print(l) for l in driver.get_log("browser")]