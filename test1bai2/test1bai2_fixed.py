#open file 
file_input = open('input.txt', 'r', encoding='utf-8')
#calling Counter collection from collection
from collections import Counter
wordcount = Counter(file_input.read().split())
#for item in wordcount.items(): print("{}\t{}".format(*item))
#open output file for writting
file_output = open ('output.txt', 'w', encoding='utf-8')
#wtite output into file
for item in wordcount.items(): 
	file_output.write("{} {} \n".format(*item))

# parse ra dictionary
a = dict(wordcount)
#open a new file to print new data
file_output_dic = open('outputdic.txt', 'w', encoding='utf-8')
#get keys/values in dictionary 
for k,v in a.items():

	file_output_dic.write(str(k) + '  ')

