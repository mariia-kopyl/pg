def calculate_statistics(text):
    num_lines = 0
    num_words = 0
    num_chars = 0

    # Your solution here

    return num_lines, num_words, num_chars


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python program.py input_file")
        sys.exit(1)
    
    input_file = sys.argv[1]

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()

        num_lines, num_words, num_chars = calculate_statistics(content)

        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_chars}")

    except FileNotFoundError:
        print("Input file does not exist")
    except Exception:
        print("An error occurred while processing the file")