#Jonathan Veltri
#CS 175
#AverageFromInput

def handle_IoError():
    print("SystemExit: File not found: numbers.txt - exiting")
    exit()

def handle_valueError():
    print(f"Bad Data: {badData} - skipping")

def main():
    sum = 0
    count = 0

    try:
        file = open("numbers.txt", 'r')
    except IOError:
        handle_IoError()

    for line in file:
        try:
            number = float(line.strip())
            sum += number
            count += 1
            print(f'I read in {count} number(s). Current number is:    {number:.2f}  Total is:    {sum}')
        except ValueError:
            number = str(line.strip())
            global badData
            badData = number
            handle_valueError()

    average = sum / count
    print(f"Average: {average:.1f}")

    file.close()

if __name__ == '__main__':
    main()