#Calululate  number of lines in the files and  number of words in each line
def file_oper(file_name):
    with open(file_name) as f:
        lines_count = 0
        file_words = 0
        for line in f:
            line_words  = len(line.split())
            print("number of wods in line :{}".format(line_words))
            lines_count += 1
            file_words += line_words
    print("number of lines in the file is : {}".format(lines_count))
    print("number of words in the file is {}".format(file_words))
file_name = "assets_report.txt"
file_oper(file_name)