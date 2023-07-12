#!/usr/bin/python3

import sys

# Initialize variables
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    # Read input line by line
    for line in sys.stdin:
        line_count += 1

        # Extract relevant information from the input line
        parts = line.split(" ")
        if len(parts) < 7:
            continue

        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Compute total file size
        total_file_size += file_size

        # Count status codes
        if status_code in status_codes:
            status_codes[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print("File size:", total_file_size)
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print(code, ":", count)
            print()

except KeyboardInterrupt:
    pass

# Print final statistics
print("Total file size:", total_file_size)
for code, count in sorted(status_codes.items()):
    if count > 0:
        print(code, ":", count)
