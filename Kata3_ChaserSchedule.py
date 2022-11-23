def ChaserSchedule(s, t):
    d = 0
    while t > 0:
        if t == 1:
            d = d + s*2
            t = t - 1
        elif t == 2:
            d = d + s
            t = t-1
        elif t > 2:
            if 2*s+(s-1)*(t-1)+(s-1) > t*s + s and t % 2 != 0:
                print('d: ', d)
                print('t: ', t)
                print('s: ', s)
                d = d + s*2
                s = s - 1
                d = d + s
                t = t - 2
            else:
                d = d + s
                t = t-1
                print('d: ', d)
                print('t: ', t)
    return d

def main():
    s = 48
    t = 684
    d = ChaserSchedule(s, t)
    print(d)

if __name__ == '__main__':
    main()