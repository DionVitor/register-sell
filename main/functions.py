def append_in_data(file, cont):
    with open(file, 'a') as archive:
        archive.write(f'{cont}\n')
        archive.close()


def lines_in_archive(file):
    archive = open(file)
    total = 0
    for line in archive:
        total += 1
    archive.close()
    return total
