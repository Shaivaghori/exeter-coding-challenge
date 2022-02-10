import csv
from email import header
from csv import writer

f=open('french_dictionary.csv')
csvread=csv.reader(f)

eng_fren=[]
for row in csvread:
	eng_fren.append(row)

freq=[]

shakes=open('t8.shakespeare.txt')
content=shakes.read()

for i in range(0,999):
	c=[]
	if content.find(eng_fren[i][0]):
		c.append(content.count(eng_fren[i][0]))
		freq.append(c)
		first_capi=eng_fren[i][0].capitalize()
		second_capi=eng_fren[i][1].capitalize()
		whole_first_capi=eng_fren[i][0].upper()
		whole_second_capi=eng_fren[i][1].upper()

		content=content.replace(eng_fren[i][0],eng_fren[i][1])
		content=content.replace(first_capi,second_capi)
		content=content.replace(whole_first_capi,whole_second_capi)

fout=open("t8.shakespeare.translated.txt","w")
fout.write(content)
fout.close()

shakes.close()

f.close()
no=0
with open('french_dictionary.csv','r') as csvinput:
	with open('frequency.csv', 'w') as csvoutput:
		writer = csv.writer(csvoutput)
		for row in csv.reader(csvinput):
			if no<=999:
				writer.writerow(row+freq[no])
				no=no+1
			else:
				break

			