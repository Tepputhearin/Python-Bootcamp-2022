def tsv_to_json(tsv_name, json_name):
    import json
    import os
    list = []
    if os.path.isfile(f"D:/New Folder/Test2/C/{tsv_name}.tsv"):
        file = open(f"D:/New Folder/Test2/C/{tsv_name}.tsv", 'r')
        data = file.readline()
        titles = [t.strip() for t in data.split("\t")]
        for line in file:
            d = {}
            for t, f in zip(titles, line.split('\t')):
                d[t] = f.strip()
                list.append(d)
        output_file = open(f"D:/New Folder/Test2/C/{json_name}.json", 'w', encoding='utf-8')
        output_file.write(json.dumps(list, indent=4))
        return 1
    else:
        return 0
print(tsv_to_json("output", "input"))