nums = [2, 7, 11, 5]
target = 9

# eredmeny tomb, ide rakjuk majd a ket szam poziciojat, egyelore ures tomb most:
result_array = []

# ez egy szemafor logikai valtozo, majd ezzel vezereljuk a kulso ciklusbol valo kilepest:
exit_from_main_loop = False

# kiirjuk a kiindulasi adatokat a legelejen:
print(f"nums: {nums}")
print(f"target: {target}")
print("")

# a kulso ciklusban vegigmegyunk a nums tombon, az utolso elem kihagyasaval: nums[:-1]
# az enumerate fuggvenyt egy tombon meghiva, a tomb egy adott elemeirol ket elemet ad vissza,
# az elso visszaadott ertek a tomb elemenek sorszama a tombon belul, a masodik pedig
# maga a tomb eleme
for number1_index, number1 in enumerate(nums[:-1]):
    print(f"DEBUG: number1_index: {number1_index}, number1: {number1}")

    # a belso ciklusban pedig a kulso ciklusban meghatarozott elem utan megmaradt tomb elemeken megyunk vegig:
    # nums[number1_index+1:]
    for number2_index, number2 in enumerate(nums[number1_index+1:]):
        print(f" DEBUG: number2_index: {number2_index}, number2: {number2}")

        # miutan igy rendelkezesunkre all a ket osszeadando szam
        # megcsinaljuk az osszeadasi vizsgálatot:
        if number1 + number2 == target:
            # ha az elvart eredmenyt kapjuk:
            # az eredmeny tombbe berakjuk az osszeadas elso elemenek indexet, amit a kulso ciklus allitott be:
            result_array.append(number1_index)

            # majd az eredmeny tombbe berakjuk az osszeadas masodik elemenek indexet, amit a kulso ciklus allitott be
            # itt trukkozni kell az index kiszamolasaval, mert a masodik ciklusban levo tomb mar csak egy resz tombje
            # az eredeti tombnek.
            # Ezert a kulso ciklus es a belso ciklus indexeibol lehet kiszamolni, hogy mi a masodik szam indexe
            # eredeti tombben
            result_array.append(number1_index + 1 + number2_index)

            # mivel a feladat szerint csak egy megoldast kell keresnunk
            # az elso megoldas utan abba is hagyhatjuk a keresest.
            # A kulso ciklusbol egy logikai valtozo "igen" -re allitasaval lepunk ki
            # ezt a megoldast hivjak "szemafor" "semaphor" -nak is,
            # beallitjuk a szemafort, es kesobb a kulso hurokban kiertekeljuk
            exit_from_main_loop = True

            # a belso ciklusbol viszont ezzel egyszeruen kilephetunk:
            break

    # itt ertekeljuk ki a szemafort, ha erteke true, akkor egy break-el kilepunk a kulso ciklusbol is:
    if exit_from_main_loop:
        break

# itt a legvegen kiiratjuk az eredmeny tombot:
print("")
print(f"output {result_array}")

