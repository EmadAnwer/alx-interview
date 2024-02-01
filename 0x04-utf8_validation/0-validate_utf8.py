#!/usr/bin/python3
"""
0-validate_utf8 module
"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding."""

    def byte_sequence_count(byte):
        """return numbers of bytes and validate the byte"""

        binary_representation = bin(byte)[2:].rjust(8, '0') 
        if binary_representation[:2] == "10":
            return 1
        elif binary_representation[:3] == "110":
            return 2
        elif binary_representation[:4] == "1110":
            return 3
        elif binary_representation[:5] == "11110":
            return 4
        elif binary_representation[:1] == "0":
            return 0
        else:
            return -1

    i = 0

    while i < len(data):
        sequence_count = byte_sequence_count(data[i])
        if sequence_count == -1:
            return False

        i += 1
        if sequence_count == 0:
            continue

        if sequence_count == 1:
            return False

        if i + sequence_count - 1 > len(data):
            return False

        j = 0
        while j < sequence_count - 1:
            if byte_sequence_count(data[i + j]) != 1:
                return False

            j += 1

        i += sequence_count

    return True
