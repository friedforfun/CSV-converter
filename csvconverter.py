import os
import sys
import argparse
import csv


def parse_args():
    parser = argparse.ArgumentParser(description='CSV converter')
    args = parser.add_argument_group('main args')
    args.add_argument('--csv', '-c', help='csv file to convert', required=True)
    args.add_argument(
        '--delim', '-d', help='Delimeter to convert from', required=False, default=';')
    args.add_argument('--out', '-o', help='File output name',
                      required=False, default=None)
    return parser.parse_args()


def write_out_file(path, header, content):
    with open(path, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for line in content:
            writer.writerow(line)


def main(args):
    lines = []

    # full absolute path
    path = str(os.path.abspath(args.csv))

    # path to file directory
    file_dir = str(os.path.split(path)[0])

    # actual file name
    file_name = str(os.path.basename(path))

    with open(path, 'r') as f:
        csv_reader = csv.reader(f, delimiter=args.delim)
        header = next(csv_reader)

        for line in csv_reader:
            lines.append(line)

    if args.out is None:
        new_path = path.split('.csv')[0]+'_clean.csv'
    else:
        new_path = file_dir + args.out

    write_out_file(new_path, header, lines)


if __name__ == "__main__":
    sys.exit(main(parse_args()) or 0)
