from csv import writer as w


def csv_writerow(filename: str, data, mode: str = 'w'):
    with open(filename, mode) as f:
        w(f, delimiter=';').writerow(data)
    