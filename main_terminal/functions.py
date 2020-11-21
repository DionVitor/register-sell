def lines():
    print('-' * 35)

def body_of_menu(num_lines=30, * strings):
    print('-' * num_lines)
    list = []

    for c in range(0, len(strings)):
        print(f'{c + 1} - {strings[c]}')
        list.append(f'{c + 1}')
    print('-' * num_lines)

    return list

def append_in_data(file, cont):
    archive = open(file, 'a')
    archive.write(f'{cont}\n')
    archive.close()


def lines_in_archive(file):
    archive = open(file)
    total = 0
    for line in archive:
        total += 1
    archive.close()
    return total
