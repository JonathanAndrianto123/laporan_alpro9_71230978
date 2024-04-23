def soal(file_soal) :
    with open(file_soal, "r") as file:
        soal = file.readlines()

        for line in soal :
            q, a = line.strip().split("||")
            a = a.strip().lower().split()
            print(q)
            jawab = input("jawab : ")
            jawab = jawab.strip().lower().split()
            if jawab == a :
                print("BENAR")
            else :
                print("SALAH")

inp = input("nama file : ")
soal(inp)