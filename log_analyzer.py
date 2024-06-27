import re


def collect_404_errors(log_file_path):
    pattern = re.compile(r".* 404 .*")
    with open(log_file_path, "r") as file:
        lines = file.readlines()
    error_lines = [line.strip() for line in lines if pattern.match(line)]
    return error_lines


def main():
    log_file_path = "sample_log_file.txt"
    error_lines = collect_404_errors(log_file_path)
    for line in error_lines:
        print(line)


if __name__ == "__main__":
    main()
