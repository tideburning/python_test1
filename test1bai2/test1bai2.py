#open file 
file_input = open('input.txt', 'r', encoding='utf-8')
#calling Counter collection from collection
from collections import Counter
wordcount = Counter(file_input.read().split())
#for item in wordcount.items(): print("{}\t{}".format(*item))
#open output file for writting
file_output = open ('output.txt', 'w', encoding='utf-8')
#wtite output into file
for item in wordcount.items(): file_output.write("{} {} \n".format(*item))