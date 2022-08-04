one_to_nine = ["um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
ten_to_nineteen = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
tens = ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
hundreds = ["cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

f = open("../data/numbers.csv", "w")
f.write("zero,")

# Write 1-9 to file
for number in one_to_nine:
    f.write(number + ",")

# Write 10-19 to file
for number in ten_to_nineteen:
    f.write(number + ",")

# Write 20-99 to file 
for ten in tens:
    f.write(ten + ",")
    for number in one_to_nine:
        f.write(ten + " e " + number + ",")

# 100 is unique
f.write("cem,")

# Write 101-999 to file
for hundred in hundreds:
    if hundred != "cento":
        f.write(hundred + ",")
    for number in one_to_nine:
        f.write(hundred + " e " + number + ",")
    for number in ten_to_nineteen:
        f.write(hundred + " e " + number + ",")
    for ten in tens:
        f.write(hundred + " e " + ten + ",")
        for number in one_to_nine:
            f.write(hundred + " e " + ten + " e " + number + ",")

#1000
f.write("mil,")

# Write 1001-1099 to file
for number in one_to_nine:
    f.write("mil" + " e " + number + ",")
for number in ten_to_nineteen:
    f.write("mil" + " e " + number + ",")
for ten in tens:
    f.write("mil" + " e " + ten + ",")
    for number in one_to_nine:
        f.write("mil" + " e " + ten + " e " + number + ",")

#1100
f.write("mil e cem,")

# Write 1101-1999 to file
for hundred in hundreds:
    if hundred != "cento":
        f.write("mil " + "e " + hundred + ",")
    for number in one_to_nine:
        f.write("mil " + hundred + " e " + number + ",")
    for number in ten_to_nineteen:
        f.write("mil " + hundred + " e " + number + ",")
    for ten in tens:
        f.write("mil " + hundred + " e " + ten + ",")
        for number in one_to_nine:
            f.write("mil " + hundred + " e " + ten + " e " + number + ",")

# Write 2000-9999 to file
for i in range(1, len(one_to_nine)):
    f.write(one_to_nine[i] + " mil,")
    for number in one_to_nine:
        f.write(one_to_nine[i] + " mil" + " e " + number + ",")
    for number in ten_to_nineteen:
        f.write(one_to_nine[i] + " mil" + " e " + number + ",")
    for ten in tens:
        f.write(one_to_nine[i] + " mil" + " e " + ten + ",")
        for number in one_to_nine:
            f.write(one_to_nine[i] + " mil" + " e " + ten + " e " + number + ",")

    f.write(one_to_nine[i] + " mil e cem,")

    for hundred in hundreds:
        if hundred != "cento":
            f.write(one_to_nine[i] + " mil " + "e " + hundred + ",")
        for number in one_to_nine:
            f.write(one_to_nine[i] + " mil " + hundred + " e " + number + ",")
        for number in ten_to_nineteen:
            f.write(one_to_nine[i] + " mil " + hundred + " e " + number + ",")
        for ten in tens:
            f.write(one_to_nine[i] + " mil " + hundred + " e " + ten + ",")
            for number in one_to_nine:
                f.write(one_to_nine[i] + " mil " + hundred + " e " + ten + " e " + number + ",")

#10000
f.write("dez mil")  
f.close()