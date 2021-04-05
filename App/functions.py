from typing import NewType, NoReturn


def append_in_data(file: str, cont: str) -> NoReturn:
    with open(file, 'a') as archive:
        archive.write(f'{cont}\n')
        archive.close()


def lines_in_archive(file: str) -> int:
    archive = open(file)
    total = 0
    for line in archive:
        total += 1
    archive.close()
    return total
