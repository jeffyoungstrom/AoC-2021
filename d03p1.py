def get_data(filename):
    values = []
    with open(filename) as f:
        for line in f:
            values.append(line.rstrip())
    return values


def d03p1(values):
    """
    :param values: array of strings representing binary numbers
    :return: product of gamma and epsilon
    gamma is the digits of the binary number made up of the most common bits
    epsilon is the least common bits
    """
    active = [0 for i in range(len(values[0]))]
    print(f'{"-".join(map(str, active))}')

    for value in values:
        bits = [*value]
        i = 0
        for bit in bits:
            if bit == '1':
                active[i] += 1
            i += 1

    gamma_bits = ""
    epsilon_bits = ""
    for count in active:
        if count > len(values) / 2:
            gamma_bits += "1"
            epsilon_bits += "0"
        elif count < len(values) / 2:
            gamma_bits += "0"
            epsilon_bits += "1"
        else:
            print("Equal number of active and inactive bits. Undefined.")
            gamma_bits += "1"
            epsilon_bits += "0"

    gamma = int(gamma_bits, 2)
    epsilon = int(epsilon_bits, 2)

    print(f'gamma: {gamma} epsilon: {epsilon}')
    return gamma * epsilon


if __name__ == '__main__':
    data = get_data('d03p1_input.txt')
    # data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111',
    #         '11100', '10000', '11001', '00010', '01010']
    print(f'd03p1: power consumption {d03p1(data)}')
