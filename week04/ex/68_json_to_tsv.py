def json_to_tsv(json_name, tsv_name):
    import json
    import os
    import csv
    if os.path.isfile(f"D:/New Folder/Test2/C/{json_name}.json"):
        f = open(f"D:/New Folder/Test2/C/{json_name}.json")
        data = json.load(f)
        f.close()
        out = open(f"D:/New Folder/Test2/C/{tsv_name}.tsv", 'w')
        dw = csv.writer(out, delimiter='\t')
        data2 = data[0].keys()
        dw.writerow(data2)
        for i in range(len(data)):
            dw.writerow(data[i].values())
        out.close()
        return 1
    else:
        return 0
print(json_to_tsv("bc_test", "output"))