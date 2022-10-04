import requests
from bs4 import BeautifulSoup
from os import path
from os import remove

def write_to_file(form_index, filename, links,verb):
   file_exists = path.exists(filename)
   offset = 2
   if not file_exists:
      f = open(filename, 'w')
      f.write(f'{verb},')

      f.write(f'{links[offset + (6 * form_index)].text},')
      f.write(f'{links[offset + 2 + (6 * form_index)].text},')
      f.write(f'{links[offset + 3 + (6 * form_index)].text},')
      f.write(f'{links[offset + 5 + (6 * form_index)].text}')

   else:
      f = open(filename, 'a')
      f.write('\n')
      f.write(f'{verb},')

      f.write(f'{links[offset + (6 * form_index)].text},')
      f.write(f'{links[offset + 2 + (6 * form_index)].text},')
      f.write(f'{links[offset + 3 + (6 * form_index)].text},')
      f.write(f'{links[offset + 5 + (6 * form_index)].text}')

   f.close()

def get_verbs():
        fname = "../data/verbs.txt"
        data = ""

        try:
            with open(fname, "r", encoding="utf-8") as f:
                data = f.read()
        except Exception as e:
            raise ValueError(f"Unable to read file {fname}") from e
        
        return data.splitlines()

if path.exists("../data/presente.txt"):
    remove("../data/presente.txt")
if path.exists("../data/pretimp.txt"):
    remove("../data/pretimp.txt")
if path.exists("../data/preperf.txt"):
    remove("../data/preperf.txt")
if path.exists("../data/futpret.txt"):
    remove("../data/futpret.txt")
if path.exists("../data/futuro.txt"):
    remove("../data/futuro.txt")
    
verbs = get_verbs()

for verb in verbs:
   r = requests.get(f'https://www.conjugacao.com.br/{verb}')
   soup = BeautifulSoup(r.text.encode('utf-8'), 'html.parser')
   links = soup.findAll('span', class_='f')
   verb = soup.find('h1', class_='nmt')
   verb = verb.text[6:].lower()

   write_to_file(0,"../data/presente.txt",links,verb)

   write_to_file(1,"../data/pretimp.txt",links,verb)

   write_to_file(2,"../data/preperf.txt",links,verb)

   write_to_file(5,"../data/futpret.txt",links,verb)

   write_to_file(8,"../data/futuro.txt",links,verb)
   

# write_to_file(20,26)

# write_to_file(26,32)


