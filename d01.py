def get_data(filename):
    values = []
    with open('d01p1_input.txt') as f:
        for line  in f:
            values.append(int(line))
    return values


def d01p1():
    """ Count how often depth reading increases in sample """
    count = 0
    previous = -1
    increases = 0
    with open('d01p1_input.txt') as f:
        for line in f:
            count += 1
            current = int(line)
            if previous < 0:
                print(f'{current} (N/A)')
                previous = current
                continue
            if current > previous:
                print(f'{current} (increased)')
                increases += 1
            else:
                print(f'{current} (decreased (or same))')
            previous = current
    return increases


def d01p2(v):
    """ Count how often three-sample sliding window increases in data """

    i = 0
    window = 3
    increases = 0
    while i + window < len(v):
        current = v[i] + v[i+1] + v[i+2]
        following = v[i+1] + v[i+2] + v[i+3]
        if following > current:
            print(f'({v[i]} + {v[i+1]} + {v[i+2]} = {current}) vs '
                  f'({v[i+1]} + {v[i+2]} + {v[i+3]} = {following})'
                  ' (increased)')
            increases += 1
        else:
            print(f'({v[i]} + {v[i+1]} + {v[i+2]} = {current}) vs '
                  f'({v[i+1]} + {v[i+2]} + {v[i+3]} = {following})'
                  ' (decreased (or same))')
        i += 1

    return increases


if __name__ == '__main__':
    #    print(f'd01p1: Depth increased {d01p1()} times')
    data = get_data('d01p1_input.txt')
    #    data = [199,200,208,210,200,207,240,269,260,263]
    print(f'd01p2: 3-sample sliding window increased {d01p2(data)}')
