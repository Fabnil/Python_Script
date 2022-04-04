import csv;
def CountNumberOfOccurrences(NameOfFile, Word, Delimiter = ',', SkipInitSpace = False;):
    with open(NameOfFile, 'r', encoding='UTF-8') as f:
        data = csv.reader(f, delimiter = Delimiter, skipinitialspace = SkipInitSpace)
        counter = 0
        for CurWord in data:
            if CurWord == Word:
                counter++;
    return counter;
