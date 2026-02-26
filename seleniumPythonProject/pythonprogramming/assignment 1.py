import sys

def numStudents(A, B, C, D, E, F, G):
    # n(A∩B∩C) = G - A - B - C + D + E + F
    result = G - A - B - C + D + E + F
    return result

def main():
    # Reading from stdin to handle multiple test cases
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            # Parsing the 7 space-separated integers
            data = list(map(int, line.split()))
            if len(data) == 7:
                A, B, C, D, E, F, G = data
                print(numStudents(A, B, C, D, E, F, G))
        except ValueError:
            break

if __name__ == "__main__":
    main()