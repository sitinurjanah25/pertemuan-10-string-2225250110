
teks = " belajar    python  untuk           pendidikan       "

print("Teks asli:", teks)

teks = teks.strip()

while "  " in teks:
    teks = teks.replace("  ", " ")

print("Teks bersih:", teks)
print("Teks capitalize:", teks.capitalize())
