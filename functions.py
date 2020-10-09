def body_of_menu(num_lines=30, * strings):
    print('-' * num_lines)
    list = []

    for c in range(0, len(strings)):
        print(f'{c + 1} - {strings[c]}')
        list.append(f'{c + 1}')
    print('-' * num_lines)

    return list

def write_in_data(file):
    open(file, 'w')
