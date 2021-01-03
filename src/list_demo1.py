def demo_basic_operation():
    flowers = ["calla", "lily", "jasmine"]
    print(flowers)
    flowers = flowers + ["forget me not", "sunflower", "ivy", "gypso"]
    print(flowers)
    del flowers[1]
    print(flowers)
    flowers.remove("jasmine")
    print(flowers)
    sorted_flowers = sorted(flowers)
    print(sorted_flowers)
    print(flowers)
    flowers.sort()
    print(flowers)
    flowers.append("carnation")
    print(flowers)


def demo():
    flowers = ['calla', 'lily', 'jasmine', 'forget me not', 'sunflower', 'ivy', 'gypso']
    # slice
    print(flowers[1:4])  # [inclusive:exclusive]
    print(flowers[-1])
    print(flowers[-1:-4:-1])
    print(flowers[:3])
    print(flowers[2:])


demo()
