import random

print("================================")
print("       GAME TEBAK ANGKA")
print("================================")
print("Aku sudah memilih angka dari 1 sampai 25.")
print("Kamu punya 5 kesempatan untuk menebak!")
print()

angka_rahasia = random.randint(1, 25)
kesempatan = 5

while kesempatan > 0:
    try:
        tebakan = int(input("Masukkan tebakanmu: "))

        if tebakan <= 1 and tebakan >= 25:
            print("Masukkan angka antara 1 sampai 25!")
            continue

        if tebakan == angka_rahasia:
            print("WAAAHHHH KAMUUU HEBAATTTT!!!!")
            print("Selamat!! Tebakanmu benar!")
            break
        elif tebakan < angka_rahasia:
            print("Tebakanmu terlalu kecil!")
        else:
            print("Tebakanmu terlalu besar!")

        kesempatan -= 1

        if kesempatan > 0:
            print(f"Sisa kesempatan: {kesempatan}")
            print()
        else:
            print("Kesempatanmu habis!")
            print(f"Angka yang benar adalah {angka_rahasia}.")

    except ValueError:
        print("Input tidak valid! Masukkan angka saja yaaa.")