# Abbas Salim
# 2026396
import csv

def main():
    input_file = input()

    word_counts = {}

    try:
        with open(input_file, newline='') as file:
            reader = csv.reader(file)

            for row in reader:
                for word in row:
                    cleaned_word = word.strip()

                    word_lower = cleaned_word.lower()

                    if word_lower not in word_counts:
                        word_counts[word_lower] = 1
                    else:
                        word_counts[word_lower] += 1

        for word in word_counts:
            original_case_word = next((w for w in word_counts if w.lower() == word), None)
            count = word_counts[word]
            print(original_case_word, count)

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

if __name__ == '__main__':
    main()
