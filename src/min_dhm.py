def min_to_day_hour_minute(minutes):
    min_per_day = 24 * 60 # 1440
    d = minutes // min_per_day
    h = (minutes - (d * min_per_day)) // 60
    m = minutes - (d * min_per_day + h * 60)
    return (d, h, m) # tuple

def min_to_day_hour_minute_dic(minutes):
    min_per_day = 24 * 60 # 1440
    d = minutes // min_per_day
    h = (minutes - (d * min_per_day)) // 60
    m = minutes - (d * min_per_day + h * 60)
    return {'day': d, 'hour': h, 'minute': m}

if __name__ == "__main__":
    print(min_to_day_hour_minute(2441))
    d, h, m = min_to_day_hour_minute(2441)
    print(d, h, m)
    total_min = d * (24 * 60) + h * 60 + m
    print(total_min)
    # print(min_to_day_hour_minute_dic(2441))
    d = min_to_day_hour_minute_dic(2441)
    print(d['day'], d['hour'], d['minute'])