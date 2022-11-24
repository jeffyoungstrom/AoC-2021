def get_data(filename):
    values = []
    with open(filename) as f:
        for line in f:
            values.append(line)
    return values


class Submarine:
    """ has a 2-d location and a depth """
    def __init__(self):
        self.location = 0
        self.depth = 0

    def locate(self):
        """ report current location and depth """
        print(f'Location: {self.location} Depth: {self.depth}')
        product = self.location * self.depth
        print(f'Product for answer: {product}')
        return product

    def navigate(self, command):
        """ Take a command and do the thing.
            "forward <int>" add to location
            "down <int>" increase depth
            "up <int> "decrease depth
        """
        pair = command.split()
        direction = pair[0]
        distance = int(pair[1])

        if direction == 'forward':
            print(f'charge! {distance}')
            self.location += distance
        elif direction == 'down':
            print(f'dive! {distance}')
            self.depth += distance
        elif direction == 'up':
            print(f'rise! {distance}')
            self.depth -= distance


def d02p1(commands):
    """ navigate forward, down, and up from 0,0 """
    my_sub = Submarine()
    count = 0
    for c in commands:
        my_sub.navigate(c)
        my_sub.locate()
        count += 1
    print(f'Acted on {count} commands')
    return my_sub.locate()


if __name__ == '__main__':
    #    print(f'd01p1: Depth increased {d01p1()} times')
    data = get_data('d02p1_input.txt')
    # data = [ 'forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2', ]
    print(f'd02p1: move as directed {d02p1(data)}')
