import json

with open('nomoi.json', encoding='utf-8') as json_file:
    nomoi = json.load(json_file)
    
for nomos in nomoi:
    # print(f"{nomos['name']} ({nomos['capital']})")
    nomos['density'] = nomos['population'] / nomos['area']

# print(len(nomoi))
# for nomos in nomoi[15:35]:
#     print(f"{nomos['id']} {nomos['name']} ({nomos['capital']})")
    
with open('nomoi_density.json', 'w', encoding='utf-8') as json_file:
    json.dump(nomoi, json_file, ensure_ascii=False, indent=4)