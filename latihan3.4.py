ctof = lambda c: (9/5) * c + 32
ctor = lambda c: 0.8 * c

c1 = 100
fahrenheit1 = ctof(c1)
print(f"C = {c1}. Output F = {fahrenheit1}.")

c2 = 80
reamur = ctor(c2)
print(f"C = {c2}. Output R = {reamur}.")

c3 = 0
fahrenheit2 = ctof(c3)
print(f"C = {c3}. Output F = {fahrenheit2}.")
