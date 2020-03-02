import urllib.request,urllib.parse,urllib.error

from bs4 import BeautifulSoup as soup
search_links ="https://www.esquire.com/mens-hairstyles/"
images_dic ={}
counter = 0

fhand = urllib.request.urlopen(search_links)
x = soup(fhand,'html.parser')
data = x.find_all("div",{"class":"full-item"})

for image in data:
	images_dic[counter]=image.img['src']
	counter=counter+1
print(images_dic)

for key,value in images_dic.items():
	key =str(key)
	
	string="https:" +value
	urllib.request.urlretrieve(string, key+".png")
	print("\nadded")
print("\n\n\nFinished Sucessfully\n\n\n")








