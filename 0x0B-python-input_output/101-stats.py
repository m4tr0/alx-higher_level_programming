#!/usr/bin/python3

import sys

# Initialize variables
total_file_size = 0
status_codes = {}

try:
    line_count = 0

    # Read input line by line
    for line in sys.stdin:
        line_count += 1

        # Extract relevant information from the input line
        parts = line.split(" ")
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Compute total file size
        total_file_size += file_size

        # Count status codes
        if status_code not in status_codes:
            status_codes[status_code] = 1
        else:
            status_codes[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print("File size:", total_file_size)
            for code in sorted(status_codes):
                print(code, ":", status_codes[code])
            print()

except KeyboardInterrupt:
    pass

# Print final statistics
print("Total file size:", total_file_size)
for code in sorted(status_codes):
    print(code, ":", status_codes[code])
