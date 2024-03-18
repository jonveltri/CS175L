#Jonathan Veltri
#CS 175
#AverageFromInput

def main():
    sum = 0
    count = 0

    file = open("numbers.txt", 'r')
    for line in (file):
        number = float(line.strip())
        sum += number
        count += 1
        print(f'I read in {count} number(s). Current number is:    {number:.2f}  Total is:    {sum}')
    average = sum / count
    print(f"Average: {average:.1f}")

if __name__ == '__main__':
    main()