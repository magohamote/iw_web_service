import csv


def parse_csv(file):
    with open(file, 'rb') as csv_file:
        bottle_reader = csv.reader(csv_file, delimiter=',')
        sniffer = csv.Sniffer
        print(sniffer.has_header(bottle_reader))
        for row in bottle_reader:
            print(row)
