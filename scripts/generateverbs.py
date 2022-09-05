import requests
from bs4 import BeautifulSoup
from os import path

def write_to_file(start, end, filename, links,verb):
   file_exists = path.exists(filename)
   if not file_exists:
      f = open(filename, 'w')
      f.write(f'{verb},')

      for i in range(start, end):
         if i == end-1:
            f.write(links[i].text) 
         else:
            f.write(f'{links[i].text},') 
   else:
      f = open(filename, 'a')
      f.write('\n')
      f.write(f'{verb},')

      for i in range(start, end):
         if i == end-1:
            f.write(links[i].text) 
         else:
            f.write(f'{links[i].text},') 

   f.close()

def get_verbs():
        fname = "verbs.txt"
        data = ""

        try:
            with open(fname, "r", encoding="utf-8") as f:
                data = f.read()
        except Exception as e:
            raise ValueError(f"Unable to read file {fname}") from e
        
        return data.splitlines()

verbs = get_verbs()

for verb in verbs:
   r = requests.get(f'https://www.conjugacao.com.br/{verb}')
   soup = BeautifulSoup(r.text.encode('utf-8'), 'html.parser')
   links = soup.findAll('span', class_='f')
   verb = soup.find('h1', class_='nmt')
   verb = verb.text[6:].lower()

   write_to_file(2,8,"test.txt",links,verb)

   write_to_file(8,14,"pretimp.txt",links,verb)

# write_to_file(14,20)

# write_to_file(20,26)
