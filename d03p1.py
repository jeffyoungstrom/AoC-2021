def get_data(filename):
    values = []
    with open(filename) as f:
        for line in f:
            values.append(line.rstrip())
    return values


class Diagnostic:
    def __init__(self, report_data):
        self.report_data = report_data
        self.report_bits = len(self.report_data[0])
        self.data_count = len(self.report_data)
        self.data_most_min = len(self.report_data) / 2
        self.bit_frequency = self.get_bit_frequency()

    def get_bit_frequency(self):
        active = [0 for i in range(self.report_bits)]

        for value in self.report_data:
            bits = [*value]
            i = 0
            for bit in bits:
                if bit == '1':
                    active[i] += 1
                i += 1
        return active

    def get_power_consumption(self):
        """
        puzzle 1
        :return: product of gamma and epsilon
        gamma is the digits of the binary number made up of the most common bits
        epsilon is the least common bits
        """
        gamma_bits = ""
        epsilon_bits = ""
        for count in self.bit_frequency:
            if count > self.data_most_min:
                gamma_bits += "1"
                epsilon_bits += "0"
            elif count < self.data_most_min:
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


    def get_most_common_value(self, i, default):
        if self.bit_frequency[i] > self.data_most_min:
            return "1"
        elif self.bit_frequency[i] < self.data_most_min:
            return "0"
        else:
            return default


def get_life_support_rating(report_data):
    return get_rating(report_data, oxygen_generator_check) * get_rating(report_data, co2_scrubber_check)


def oxygen_generator_check(d, i):
    """
    :param d: Diagnostic
    :param i: index in bit string
    :return: most frequent value at index or "1"
    """
    if d.bit_frequency[i] > d.data_most_min:
        return "1"
    elif d.bit_frequency[i] < d.data_most_min:
        return "0"
    else:
        return "1"


def co2_scrubber_check(d, i):
    """
    :param d: Diagnostic
    :param i: index in bit string
    :return: least frequent value at index or "0"
    """
    if d.bit_frequency[i] > d.data_most_min:
        return "0"
    elif d.bit_frequency[i] < d.data_most_min:
        return "1"
    else:
        return "0"


def get_rating(values, value_function):
    """
    :param values: data values
    :param value_function: function to identify desired value of given bit
    :return: decimal value of unique data entry
    """
    remaining_values = Diagnostic(values)
    for position in range(remaining_values.report_bits):
        pass_data = []
        position_check_value = value_function(remaining_values, position)
        print(f'checking remaining {remaining_values.data_count} items')
        for value in remaining_values.report_data:
            value_bits = [*value]
            if value_bits[position] == position_check_value:
                pass_data.append(value)
        # see if we're done
        if len(pass_data) == 1:
            # found it
            return int(pass_data[0], 2)
        else:
            # keep looking
            remaining_values = Diagnostic(pass_data)
    # didn't narrow down to 1. show what we've got and bail
    print(f'still have {remaining_values.data_count} items after looking through everything')
    for value in remaining_values.report_data:
        print(f'    {value}')
    raise ValueError('failed to find unique value')


if __name__ == '__main__':
    data = get_data('d03p1_input.txt')
    # data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111',
    #         '11100', '10000', '11001', '00010', '01010']
    report = Diagnostic(data)
    print(f'd03p1: power consumption {report.get_power_consumption()}')
    print(f'd03p1: life support rating {get_life_support_rating(data)}')
