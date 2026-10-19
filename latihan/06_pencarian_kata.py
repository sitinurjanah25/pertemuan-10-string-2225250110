
teks = "Python untuk data. Python untuk pendidikan."

teks = teks.lower()
kata = "python"

print("Teks:", teks)
print("Apakah kata ditemukan?", kata in teks)
print("Jumlah kemunculan:", teks.count(kata))
print("Posisi pertama:", teks.find(kata))
