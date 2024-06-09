################## QUIZZ GAMEE
def new_game():
    jawab = []
    jawab_benar = 0
    nomor_soal = 1

    for key in pertanyaan:
        print("------------------")
        print(key)
        for i in jawaban[nomor_soal-1]:
            print(i)
        tebakan = input(" Enter (A, B, C, D): ")
        tebakan=tebakan.upper()
        jawab.append(tebakan)

        jawab_benar += check_answer(pertanyaan.get(key),tebakan)
        nomor_soal += 1

    display_score(jawab_benar,jawab)

# ------------------
def check_answer(jawaban,tebakan):
    if  jawaban == tebakan:
        print("benarr")
        return 1
    else:
        print("salahh")
        return 0
# ------------------
def display_score(jawab_benar,jawab):
    print("-------------------")
    print("------Hasil--------")
    print("-------------------")

    # print("Jawaban : ", end="")
    for i in pertanyaan:
        print(pertanyaan.get(i),end=" ")
    print()

    print("Jawab   : ", end="")
    for i in jawab:
        print(i,end=" ")
    print()

    score = int((jawab_benar/len(pertanyaan))*100)
    print("your score is "+str(score)+"%")
# ------------------
def play_again():
    response = input(" Do you want to play again? Y / N : ")
    response = response.upper()

    if response == "Y":
        return True
    else:
        return False
# ------------------

pertanyaan = {
    "Ultah micuq adalah ? ": "C",
    "Tanggal tunangan ? ": "D",
    "Mas Kawin ? ": "B",
    "makanan favorit ticuq ? ":"D"
}

jawaban = [
    ["A. 22 Mei 1996","B. 23 Mei 1996","C. 24 Mei 1996","D. 25 Mei 1996"],
    ["A. 28 Agustues 2022","B. 29 Agustues 2022","C. 30 Agustues 2022","D. 27 Agustues 2022"],
    ["A. Emas 5 gram","B. Emas 10 gram","C. Emas 15 gram","D. Emas 5 kilogram"],
    ["A. Tahu Khepell","B. Djamure Krispiye","C. Tungkule Kecape","D. semua benar"]
]

new_game()

while play_again() :
    new_game()

print("BYEE!!!")