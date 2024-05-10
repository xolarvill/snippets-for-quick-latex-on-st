import pandas as pd

df = pd.read_excel('snippets.xlsx')

l1 = []

for index, row in df.iterrows():
    l1.append(row.to_list())
    
print(len(l1))

form = '''<snippet>
    <content><![CDATA[
{syntax}
]]></content>
    <tabTrigger>{shortcut}</tabTrigger>
    <scope>text.tex.latex</scope>
</snippet>'''

for ltemp in l1:
    t1, t2 = ltemp[:2]  
    t1_file = f'{t1}.sublime-snippet'
    content = form.format(syntax=t2, shortcut=t1)
    with open(t1_file, 'w') as file:
        file.write(content)