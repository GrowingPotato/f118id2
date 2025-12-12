import defs

with open('whitelist.txt', 'r', encoding='utf-8') as startfile:
    whitelist = startfile.read()

with open('filtered.txt', 'w', encoding='utf-8') as endfile:
        endfile.write(str(defs.form_filtered_dict(whitelist)))