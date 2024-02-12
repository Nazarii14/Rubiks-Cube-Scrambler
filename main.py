from scrambler import get_random_scramble
from concurrent.futures import ProcessPoolExecutor
import time

number = 1_000_000
output_file = 'scrambles_1e6_0.txt'


def generate_and_write_scrambles(args):
    file, start_index, number = args
    with open(file, 'a') as f:
        for i in range(start_index, start_index + number):
            scramble = get_random_scramble()
            f.write(' '.join(scramble) + "\n")


if __name__ == '__main__':
    start = time.time()

    with ProcessPoolExecutor() as executor:
        processes = 4
        scrambles_per_process = number // processes

        args_list = [(output_file, i * scrambles_per_process, scrambles_per_process) for i in range(processes)]
        executor.map(generate_and_write_scrambles, args_list)

    end = time.time()
    duration = end - start
    print(f"Time: {duration}s")
