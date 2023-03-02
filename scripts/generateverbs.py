import requests
from bs4 import BeautifulSoup
from os import path
from os import remove
import time
import threading

def write_to_file(form_index, filename, links,verb):
   file_exists = path.exists(filename)
   offset = 2
   if not file_exists:
      f = open(filename, 'w', encoding='utf-8')
      f.write(f'{verb},')

      f.write(f'{links[offset + (6 * form_index)].text},')
      f.write(f'{links[offset + 2 + (6 * form_index)].text},')
      f.write(f'{links[offset + 3 + (6 * form_index)].text},')
      f.write(f'{links[offset + 5 + (6 * form_index)].text}')

   else:
      f = open(filename, 'a', encoding='utf-8')
      f.write('\n')
      f.write(f'{verb},')

      f.write(f'{links[offset + (6 * form_index)].text},')
      f.write(f'{links[offset + 2 + (6 * form_index)].text},')
      f.write(f'{links[offset + 3 + (6 * form_index)].text},')
      f.write(f'{links[offset + 5 + (6 * form_index)].text}')

   f.close()

def get_verbs():
        fname = "../data/vocab_lists/verbos2.txt"
        data = ""

        try:
            with open(fname, "r", encoding="utf-8") as f:
                data = f.read()
        except Exception as e:
            raise ValueError(f"Unable to read file {fname}") from e
        
        return data.splitlines()

def generate_verbs():
    if path.exists("../data/indi_presente.txt"):
        remove("../data/indi_presente.txt")
    if path.exists("../data/indi_preimp.txt"):
        remove("../data/indi_preimp.txt")
    if path.exists("../data/indi_preperf.txt"):
        remove("../data/indi_preperf.txt")
    if path.exists("../data/indi_futpret.txt"):
        remove("../data/indi_futpret.txt")
    if path.exists("../data/sub_preimp.txt"):
        remove("../data/sub_preimp.txt")
    if path.exists("../data/sub_futuro.txt"):
        remove("../data/sub_futuro.txt")
    
        
    verbs = get_verbs()

    for line in verbs:
        verb = line.split('=')
        r = requests.get(f'https://www.conjugacao.com.br/{verb[0]}')
        soup = BeautifulSoup(r.text.encode('utf-8'), 'html.parser')
        links = soup.findAll('span', class_='f')
        verb = soup.find('h1', class_='nmt')
        print(verb)
        verb = verb.text[6:].lower()

        t1 = threading.Thread(target=write_to_file, args=(0,"../data/indi_presente.txt",links,verb,))
        t2 = threading.Thread(target=write_to_file, args=(1,"../data/indi_preimp.txt",links,verb,))
        t3 = threading.Thread(target=write_to_file, args=(2,"../data/indi_preperf.txt",links,verb,))
        t4 = threading.Thread(target=write_to_file, args=(5,"../data/indi_futpret.txt",links,verb,))
        t5 = threading.Thread(target=write_to_file, args=(7,"../data/sub_preimp.txt",links,verb,))
        t6 = threading.Thread(target=write_to_file, args=(8,"../data/sub_futuro.txt",links,verb,))

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()

    start = time.time()

    # write_to_file(0,"../data/presente.txt",links,verb)

    # write_to_file(1,"../data/pretimp.txt",links,verb)

    # write_to_file(2,"../data/preperf.txt",links,verb)

    # write_to_file(5,"../data/futpret.txt",links,verb)

    # write_to_file(8,"../data/futuro.txt",links,verb)

    t1 = threading.Thread(target=write_to_file, args=(0,"../data/presente.txt",links,verb,))
    t2 = threading.Thread(target=write_to_file, args=(1,"../data/pretimp.txt",links,verb,))
    t3 = threading.Thread(target=write_to_file, args=(2,"../data/preperf.txt",links,verb,))
    t4 = threading.Thread(target=write_to_file, args=(5,"../data/futpret.txt",links,verb,))
    t5 = threading.Thread(target=write_to_file, args=(8,"../data/futuro.txt",links,verb,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    result = time.time() - start
    print(result)

if __name__ == '__main__':
    generate_verbs()
   

# write_to_file(20,26)

# write_to_file(26,32)