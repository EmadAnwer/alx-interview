#!/usr/bin/python3
"""
0-validate_utf8 module
"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding."""

    def byte_sequence_count(byte):
        """retun numbers of bytes and validate the byte"""

        binary_represenstaion = bin(byte)[2:]
        if len(binary_represenstaion) > 8:
            return -1

        if len(binary_represenstaion) < 8:
            return 0

        if binary_represenstaion[:2] == "10":
            return 1

        sequence_count = len(binary_represenstaion[:5].split("0")[0])
        if sequence_count == 5:
            return -1

        return sequence_count

    i = 0

    while i < len(data):
        sequence_count = byte_sequence_count(data[i])
        if sequence_count == -1:
            return False

        if sequence_count == 0:
            i += 1
            continue

        if sequence_count == 1:
            return False

        i += 1

        if i + sequence_count > len(data):
            return False

        j = 0
        while j < sequence_count:
            if byte_sequence_count(data[i + j]) != 1:
                return False

            j += 1

        i += sequence_count + 1

    return True
