with open("input_file.csv", "r") as file,open("output_file.csv","w") as outfile:
    for line in file:
        print(line.strip())
        outfile.write(line)