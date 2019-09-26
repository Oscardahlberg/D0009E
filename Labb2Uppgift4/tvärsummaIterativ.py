def tvarsumman2(heltal):
    siffror = 1
    while heltal > 10:
        heltal = heltal / 10
        siffror += 1
    tvarsumman = 0
    while siffror > 0:
        tvarsumman += int(heltal % 10)
        heltal = heltal * 10
        siffror -= 1
    return tvarsumman


print(tvarsumman2(1019))
