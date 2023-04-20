def check_jquery_fingerprint(content):
    jquery_fingerprint = "return (typeof $ !== 'undefined' && typeof $.fn !== 'undefined' && typeof $.fn.jquery !== 'undefined')"
    return jquery_fingerprint in content

def check_jquery_version_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    if check_jquery_fingerprint(content):
        print("jQuery fingerprint found in the crawled result.")
    else:
        print("jQuery fingerprint not found in the crawled result.")

if __name__ == '__main__':
    file_path = '../crawler/output.txt'
    check_jquery_version_in_file(file_path)