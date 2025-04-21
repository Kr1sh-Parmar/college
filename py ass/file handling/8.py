def clean_articles(input_file, output_file):
    articles = ['a', 'an', 'the']

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            words = line.strip().split()
            filtered_words = [word for word in words if word.lower() not in articles]
            new_line = ' '.join(filtered_words)
            outfile.write(new_line + '\n')

# i.e
if __name__ == "__main__":
    clean_articles("input.txt", "output.txt")
    print("Articles removed. Check output.txt!")
