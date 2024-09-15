import sys
from pathlib import Path
import shutil
from ebookatty import MetadataFetcher
p = Path('.')

#pattern1 = list(p.glob('*'))
#print(pattern1)
#for plik in pattern1:
zmienna = sys.argv[1]
inkcensus = open(zmienna,"w")
omnium = []
for plik in p.glob('**/*'):
 try:
  print(plik.name)
  if ".mobi" or ".azw3" in str(plik.name):
     print(plik)
     ebook = MetadataFetcher(plik)
     author = ebook.get_metadata().get("author")
     title = ebook.get_metadata().get("title")
     print(author)
     print(title)
     sciezka = str(plik)
     lista = sciezka.split("/")
     dlugosc = len(lista) - 1
     counter = 0
     print("==================")
     while counter != dlugosc:
         if counter == 0:
           maincategory = str(lista[counter])
           if "sdr" not in maincategory and maincategory not in omnium:
             inkcensus.write("-----------------------------------"+"\n")
             inkcensus.write("Main Category: "+str(maincategory)+" "+"\n")
             omnium.append(maincategory)
           print("Main category: " + lista[counter])
         if counter > 0:
             subcategory = str(lista[counter])
             if "sdr" not in subcategory and subcategory not in omnium:
                inkcensus.write("-----------------------------------"+"\n")
                inkcensus.write("SubCategory: "+str(subcategory)+" "+"\n")
                omnium.append(subcategory)
             print("Subcategory of " + lista[counter -1] + ":" + lista[counter])
         counter =  counter + 1 
     print("=========================")
     inkcensus.write(str(author)+" "+str(title)+" "+"\n")
 except:
   pass
# dst = str(src).strip()
# shutil.move(src, dst)

#pattern2 = list(p.glob(' *'))

#for plik in pattern2:
# src = plik
# dst = str(src).strip()
# shutil.move(src, dst)





