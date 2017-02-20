raw = "sample_input1_raw.txt"
form = "sample_input1.txt"


if __name__ == "__main__":
    lines = []
    with open(raw, "r") as readF:
        lines = [line.rstrip('\n') for line in readF]
    readF.close()
    with open(form, "w") as writeF:
        for line in lines:
            if len(line) > 0:
                words = line.split(' ')
                for idx in range(0, len(words)):
                    word = words[idx]
                    for idx2 in range(0, len(word)):
                        writeF.write(str(word[idx2]) + " ")
                    writeF.write("space ")
                writeF.write("enter ")
    writeF.close()