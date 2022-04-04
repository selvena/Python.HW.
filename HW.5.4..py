enum = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("EX.4.new.txt", 'w', encoding="utf-8") as new_f:
        with open("EX.4.txt", encoding="utf-8") as ol_f:
            new_f.writelines([line.replace(line.split()[0], enum.get(line.split()[0])) for line in ol_f])