from random import randint


def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield randint(begin, end)



def main_gen_random():
    numbers = gen_random(4, 0, 5)
    for el in numbers:
        print(el, end=' ')


if __name__ == '__main__':
    main_gen_random()
