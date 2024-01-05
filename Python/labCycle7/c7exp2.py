input_file_path = 'file_1.txt'
output_file_path = 'file_2.txt'

with open(input_file_path, 'r') as file_1:
    with open(output_file_path, 'w') as file_2:
        lines = file_1.readlines()
        for index, line in enumerate(lines):
            if index % 2 == 0:
                file_2.write(line)
with open(output_file_path, 'r') as file_2:
    output_content = file_2.read()
    print("Content of the output file:")
    print(output_content )
