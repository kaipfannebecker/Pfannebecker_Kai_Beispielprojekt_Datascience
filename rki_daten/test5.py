import requests
import gc
import lzma
import urllib.request
import pandas as pd
import json
from ast import literal_eval
import os


# nötig: log generieren und in abschnitten einlesen

#only_item_cells = strainer("div", attrs={"class": "item-cell"})
#page_soup = soup(page_html, 'html.parser', parse_only=only_item_cells)

# ----------------------------------------------------------------------------------------------------------------------
## Variablen:
data = []
urls = []
i = 1
j = 1
k = 0
data_neuinf_ges = []
data_neuinf_ges = pd.DataFrame(data_neuinf_ges)
# data = pd.DataFrame(data)
# ----------------------------------------------------------------------------------------------------------------------
## Funktionsdefinitionen:
def first_five_files(arch_line,j):
    urllib.request.urlretrieve(arch_line, "date.xz")
    with lzma.open("date.xz", mode='rt', encoding='utf-8') as fin:
        file_content = fin.read().split('\n')
        # Problem: Letzte Zeile ist leer. Diese muss gelöscht werden, damit json.loads keinen Fehler erzeugt.
        file_content = file_content[:-1]
        #print(datetime.now().strftime("%H:%M:%S.%f"))
    for line in file_content:
        # data.append(json.loads(line))
        inline = json.loads(line)
        data.append(inline)
    df = pd.DataFrame(data)
        # Die ersten 4 Tage hatten eine andere Notation; deshalb müssen hierfür extra Spalten angelegt werden.
    if 'NeuerFall' not in df:
        df['NeuerFall'] = 1
    if "RefdatumISO" not in df:
        df["RefdatumISO"] = 1
    if "Refdatum" not in df:
        df["Refdatum"] = 1
    #
    df = df.drop(columns=["RefdatumISO", "Refdatum", "Datenstand", "ObjectId", "Meldedatum"])  # "DatenstandISO",
    #nur_neu = df.loc[df["NeuerFall"] == 1]
    #nur_corr = df.loc[df["NeuerFall"] == -1]
    #neue_daten = [data_neuinf_ges, nur_neu, nur_corr]
    #data_neuinf_ges = pd.concat(neue_daten)
    #data_neuinf_ges.to_csv("Datensatz_Neuinfektionen_gesamt.csv")
    df.to_csv("Datensatz_Neuinfektionen_gesamt.csv")
    #output_path = "Datensatz_Neuinfektionen_gesamt.csv"
    #df.to_csv(output_path, mode='a', header=not os.path.exists(output_path))
    del df
    gc.collect()
    print(f"{arch_line}_fertig")
    print(j)
    with open("urls_used.txt", "a+") as file_object:
    # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        check_log = file_object.read(100)
        if len(check_log) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(f"{arch_line}")
    with open('arch_todo.txt', 'r') as fin:
        arch_new = fin.read().splitlines(True)
    with open('arch_todo.txt', 'w') as fout:
        fout.writelines(arch_new[1:])


def all_other_files(arch_line):
    urllib.request.urlretrieve(arch_line, "date.xz")
    with lzma.open("date.xz", mode='rt', encoding='utf-8') as fin:
        file_content = fin.read().split('\n')
        # Problem: Letzte Zeile ist leer. Diese muss gelöscht werden, damit json.loads keinen Fehler erzeugt.
        file_content = file_content[:-1]
        #print(datetime.now().strftime("%H:%M:%S.%f"))
    for line in file_content:
        # data.append(json.loads(line))
        inline = json.loads(line)
        # print(inline)
        # print(datetime.now().strftime("%H:%M:%S.%f"))
        if inline["NeuerFall"] == 1 or inline["NeuerFall"] == -1:
            data.append(inline)
            # print(datetime.now().strftime("%H:%M:%S.%f"))
    df = pd.DataFrame(data)
    # print(datetime.now().strftime("%H:%M:%S.%f"))
    # print("hallowelt")
    # Die ersten 4 Tage hatten eine andere Notation; deshalb müssen hierfür extra Spalten angelegt werden.
    if 'NeuerFall' not in df:
        df['NeuerFall'] = 1
    if "RefdatumISO" not in df:
        df["RefdatumISO"] = 1
    if "Refdatum" not in df:
        df["Refdatum"] = 1
    #
    df = df.drop(columns=["RefdatumISO", "Refdatum", "Datenstand", "ObjectId", "Meldedatum"])  # "DatenstandISO",
    # nur_neu = df.loc[df["NeuerFall"] == 1]
    # nur_corr = df.loc[df["NeuerFall"] == -1]
    # neue_daten = [data_neuinf_ges, nur_neu, nur_corr]
    # data_neuinf_ges = pd.concat(neue_daten)
    # data_neuinf_ges.to_csv("Datensatz_Neuinfektionen_gesamt.csv")
    df.to_csv("Datensatz_Neuinfektionen_gesamt.csv", mode='a', header=False)
    # output_path = "Datensatz_Neuinfektionen_gesamt.csv"
    # df.to_csv(output_path, mode='a', header=not os.path.exists(output_path))
    del df
    gc.collect()
    print(f"{arch_line}_fertig")
    with open("urls_used.txt", "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        check_log = file_object.read(100)
        if len(check_log) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(f"{arch_line}")
    with open('arch_todo.txt', 'r') as fin:
        arch_new = fin.read().splitlines(True)
    with open('arch_todo.txt', 'w') as fout:
        fout.writelines(arch_new[1:])

# ----------------------------------------------------------------------------------------------------------------------


#archives = open("urls_used.txt", "r")
# print(archives)
#arch_files = archives.readlines()
#print(arch_files)
#print(type(arch_files))

archives_needed = open("urls_needed.txt", "r")
archives_done = open("urls_used.txt", "r")

#needed_data = archives_needed.readlines()
#done_data = archives_done.readlines()
#print(type(needed_data))

#for line1 in needed_data:
 #   i += 1
  #  print("1")
#
 #   for line2 in done_data:
  #      print("2")
   #     # matching line1 from both files
    #    if line1 == line2:
     #       print("right")
      #      input("3")
       # else:
        #    print("wrong")
         #   input("4")
          #  with open("arch_todo.txt", "a+") as urls_todo:
          #       urls_todo.write(f"\n {line1}")
        #break

#for i in range(len(needed_data)):
 #   if needed_data[i] != done_data[i]:
  #      to_write = needed_data[i]
   #     with open("arch_todo.txt", "a+") as urls_todo:
    #        urls_todo.write(f"\n {to_write}")


# closing files
#archives_needed.close()
#archives_done.close()
#urls_todo.close


arch_todo = open("arch_todo.txt", "r")
for arch_line in arch_todo:
    if os.stat("urls_used.txt").st_size == 0:
        if j<5:
            first_five_files(arch_line,j)
            j = j + 1
        else:
            all_other_files(arch_line)
    else:
        all_other_files(arch_line)

