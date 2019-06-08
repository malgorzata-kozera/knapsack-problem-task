import numpy as np
import sys


def calculate(usb_size: int, memes: list):
    """
    function ​that calculates the best set of memes.
    Given a set of items, each with a size and a price,
    calculate and provide the number of each item to include in a USB stick
    so that the total weight is less than or equal to a given
    capacity of the USB stick and the total value is as large as possible.

    :param usb_size: a number describing the capacity of the USB stick in
    GiB(int)

    :param memes: a list of 3-element tuples, each with the name, size in MiB,
     and price in caps per meme: (list[tuple[str, int, int]])

    :return:
        tuple: USB stick. The return value with the first element being the
        total value of all memes on the USB stick, and the second being the set
        of names of the memes that should be copied onto the USB stick to
        maximize its value.

    """

    try:
        memes = sorted(memes, key=lambda memes: (memes[1], memes[0]))
        full_size = usb_size * 1024
        table = np.zeros((len(memes), full_size+1))

        for i in range(len(memes)):   # i = table row
            for j in range(full_size + 1):      # j = table column/capacity
                if j < memes[i][1]:
                    table[i][j] = table[i-1][j]
                else:
                    val1 = memes[i][2] + table[i-1][j-memes[i][1]]
                    val2 = table[i-1][j]
                    table[i][j] = max(val1, val2)

        chosen_memes = set()
        price = 0
        j = full_size
        for i in reversed(range(len(memes))):
            if i == 0 and table[i][j] != 0:
                chosen_memes.add(memes[i][0])
            if table[i][j] != table[i - 1][j]:
                chosen_memes.add(memes[i][0])
                price = price + memes[i][2]
                j -= memes[i][1]
        return price, chosen_memes

    except TypeError as e:
        print(e, file=sys.stderr)
        print('Enter a value with the correct type')
        exit()

    except IndexError as e:
        print(e, file=sys.stderr)
        print('Each tuple must contain exactly 3 elements.'
              ' Enter the correct number of values')
        exit()


if __name__ == '__main__':
    usb_size = 1
    memes = [
        ('rollsafe.jpg', 205, 6),
        ('sad_pepe_compilation.gif', 410, 10),
        ('yodeling_kid.avi', 605, 12)
    ]
    print(calculate(usb_size, memes))
