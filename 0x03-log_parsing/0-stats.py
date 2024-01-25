#!/usr/bin/python3
""" Module for storing the function that reads stdin line by line and computes
    metrics
"""
import sys


def print_metrics(total_size, status_count):
    """Print metrics after every 10 lines or keyboard interruption"""
    print("File size: {}".format(total_size))
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print("{}: {}".format(code, status_count[code]))


def main():
    """Main function that reads stdin line by line and computes metrics"""
    # read stdin line by line
    # check format of each line
    # <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    counter = 0
    total_size = 0
    status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            splited_line = line.split(" ")

            if len(splited_line) != 9:
                continue

            ip = splited_line[0]
            status_code = int(splited_line[7])
            file_size = int(splited_line[8])
            total_size += file_size
            status_count[status_code] += 1
            counter += 1

            if counter == 10:
                print_metrics(total_size, status_count)
                counter = 0

    except KeyboardInterrupt:
        print_metrics(total_size, status_count)


if __name__ == "__main__":
    main()
