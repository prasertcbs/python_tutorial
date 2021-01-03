def air_quality_if_version(aqi):
    quality=''
    if aqi >= 201:
        quality='มีผลกระทบต่อสุขภาพ'
    elif aqi >= 101:
        quality='เริ่มมีผลกระทบต่อสุขภาพ'
    elif aqi >= 51:
        quality='ปานกลาง'
    elif aqi >= 26:
        quality='ดี'
    else:
        quality='ดีมาก'
    return quality

def vlookup(aqi):
    tbl = [
        [0, 'ดีมาก', 'great'],
        [26, 'ดี', 'good'],
        [51, 'ปานกลาง', 'moderate'],
        [101, 'เริ่มมีผลกระทบต่อสุขภาพ', 'unhealthy'],
        [201, 'มีผลกระทบต่อสุขภาพ', 'very unhealthy']
    ]
    tmp = []
    for e in tbl:
        if aqi >= e[0]:
            tmp.append(e)
        else:
            break
    # print(tmp)
    # print('-' * 80)
    # print(tmp[-1][1])
    return tmp[-1][2]

def vlookup2(v, tbl, col):
    tmp = []
    for e in tbl:
        if v >= e[0]:
            tmp.append(e)
        else:
            break
    # print(tmp)
    # print('-' * 80)
    # print(tmp[-1][1])
    return tmp[-1][col]

if __name__ == "__main__":
    tbl = [
        [0, 'ดีมาก', 'great'],
        [26, 'ดี', 'good'],
        [51, 'ปานกลาง', 'moderate'],
        [101, 'เริ่มมีผลกระทบต่อสุขภาพ', 'unhealthy'],
        [201, 'มีผลกระทบต่อสุขภาพ', 'very unhealthy']
    ]
    aqi=210
    print(air_quality_if_version(aqi))
    print(vlookup(aqi))
    print(vlookup2(aqi, tbl, 2))