def sortfile(input,output):
    with open(input, 'r') as file:
        contents = file.readlines()
        contents = [line.strip() for line in contents]
        contents.sort(key = len)
        with open(output, 'w') as file:
            for line in contents:
                file.write(line+'\n')
sortfile('LAB-6-Z.txt','LAB-6-ZO.txt')