import argparse
import utilities


endings = list(map(ord, ['ם', 'ף', 'ן', 'ך', 'ץ']))
first = ord('א')
last = ord('ת')


def translate(content):
    content = list(content)
    result = []
    for char in content:
        code = ord(char)
        if code in endings:
            result.append(code + 1)
        elif code >= first and code <= last:
            result.append(code)

    return ''.join(map(chr, result))


def replace(content):
    utilities.protect_file_from_delete(args.output_file)
    with open(args.output_file, "w", encoding=utilities.ENCODING) as f:
        f.write(content)


def main():
    content = utilities.read_utf8_encrypted_file(
        args.input_file)
    replace(translate(content))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    parser.add_argument("output_file", type=str)
    args = parser.parse_args()
    main()
