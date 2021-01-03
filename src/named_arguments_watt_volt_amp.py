# watt = amp * volt

def watt(amp, volt):
    return amp * volt

def solve(watt=None, amp=None, volt=None):
    if watt is None:
        return amp * volt
    elif amp is None:
        return watt / volt
    elif volt is None:
        return watt / amp
    else:
        return None

if __name__ == "__main__":
    w=watt(.25, 5)
    print(f'w = {w}')

    w2=watt(amp=.25, volt=5) # keyword/named arguments/parameters
    print(f'w2 = {w2}')

    w3=watt(volt=5, amp=.25) # keyword/named arguments/parameters
    print(f'w3 = {w3}')

    w4=solve(volt=5, amp=.25)
    print(f'w4 = {w4}')

    a=solve(watt=1.25, volt=5)
    print(f'a = {a}')

    v=solve(watt=1.25, amp=.25)
    print(f'v = {v}')
