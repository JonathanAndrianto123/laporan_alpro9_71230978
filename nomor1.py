def perbandingan_file(f1, f2) :
    with open(f1, "r") as file1, open(f2, "r") as file2:
        for i, (line1, line2) in enumerate(zip(file1, file2), start = 1) :
            if not line1 and not line2 :
                break
            if line1!= line2:
                print(f"Perbedaan ada pada baris {i}:")
                print(f"file 1: {line1.strip()}")
                print(f"file 2: {line2.strip()}")

file1 = input("masukkan nama file pertama = ")
file2 = input("masukkan nama file kedua = ")
perbandingan_file(file1, file2)