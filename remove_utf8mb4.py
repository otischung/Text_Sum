import codecs


def remove_4byte_utf8(input_file, output_file):
    with codecs.open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove 4-byte UTF-8 characters
    cleaned_content = ''.join(char for char in content if len(char.encode('utf-8')) < 4)

    with codecs.open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

    print("4-byte UTF-8 characters have been removed. Output written to", output_file)


# Example usage
input_file = 'news.md'
output_file = 'news_mod.md'
remove_4byte_utf8(input_file, output_file)
