def cek_angka(a, b, c):
   if a != b and a != c and b != c:
    if a + b == c or a + c == b or b + c == a:
       return True
   return False
  
print(cek_angka(1, 2, 3))
print(cek_angka(5, 8, 9))

      