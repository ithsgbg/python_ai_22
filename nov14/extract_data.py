ITERATIONS = 10000


def main():
    with open('./nov14/Pet_Supplies.json', 'r') as in_file:
        with open(f'./nov14/Pet_Supplies_{ITERATIONS}.json', 'w') as out_file:
            for _ in range(ITERATIONS):
                out_file.write(in_file.readline())



if __name__ == '__main__':
    main()
