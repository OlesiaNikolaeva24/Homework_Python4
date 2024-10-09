from fake_math import divide as simple_divide
from true_math import divide as complex_divide


result1 = simple_divide(69, 3)
result2 = simple_divide(3, 0)
result3 = complex_divide(49, 7)
result4 = complex_divide(15, 0)
result5 = simple_divide(100, 8)
result6 = simple_divide(0, 0)
result7 = simple_divide(5.5, 0.0)
result8 = complex_divide(0.0, 7.5)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
