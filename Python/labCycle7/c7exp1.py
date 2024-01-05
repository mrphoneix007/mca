def read_file_into_list(file_path):
    lines_list = []
    with open(file_path, 'r') as file:
        for line in file:
            lines_list.append(line.strip()) 

    return lines_list
file_path = 'file.txt'
result = read_file_into_list(file_path)
print("Lines read from the file:")
for line in result:
    print(line)
print("\nList of lines:")
print(result)
