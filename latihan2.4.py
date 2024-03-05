def cek_digit_belakang(a, b, c):
 
    k1 = a % 10
    k2 = b % 10
    k3 = c % 10

    if k1 == k2 or k1 == k3 or k2 == k3:
        return True
    else:
        return False

try:
    a = int(input("Masukkan a: "))  
    b = int(input("Masukkan b: "))  
    c = int(input("Masukkan c: "))
except:
 print("Format yang anda masukkan salah!")

print(cek_digit_belakang(a, b, c))

 