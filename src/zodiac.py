def zodiac(buddhist_year):
    z = "มะเส็ง", "มะเมีย", "มะแม", "วอก", "ระกา", "จอ", "กุน", "ชวด", "ฉลู", "ขาล", "เถาะ", "มะโรง"  # tuple
    # print(z[0])
    return z[buddhist_year % 12]

print(zodiac(2559))
for i in range(2559, 2573):
    print(i, zodiac(i))
