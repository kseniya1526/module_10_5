from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf - 8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start1 = datetime.now()
    for filename in filenames:
        read_info(filename)
    end1 = datetime.now()
    print(f'{end1 - start1} (линейный)')

    start2 = datetime.now()
    with multiprocessing.Pool(processes= 4) as pool:
        pool.map(read_info, filenames)
    end2 = datetime.now()
    print(f'{end2 - start2} (многопроцессный)')




