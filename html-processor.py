import re

out = ""

#Open and write the file to out string
with open('testpage.txt', 'r', encoding = 'utf-8') as file:
    out = file.read()

#Title
title = re.compile(r'<title>(.*)</title>')
for m in title.finditer(out):
    out = title.sub(m.group(1), out)

#Comments
comm = re.compile(r'<!.+?>')
for _ in comm.finditer(out):
    out = comm.sub('', out)
    
#Script and Style
scst = re.compile(r'<script.*?</script>|<style.*?</style>', re.DOTALL)
for _ in scst.finditer(out):
    out = scst.sub('', out)
    
#Links
lin = re.compile(r'<a.*? href="(.*)">.*</a>')
for m in lin.finditer(out):
    out = lin.sub(m.group(1), out)
    
#Tags
tag = re.compile(r'<.+?>', re.DOTALL)
for _ in tag.finditer(out):
    out = tag.sub('', out)

#HTML Entities
def ent_sub(m):
    if m == '&amp;': return '&'
    elif m == '&gt;': return '>'
    elif m == '&lt': return '<'
    else: return ' '
    
ent = re.compile(r'(&amp;)|(&gt;)|(&lt;)|(&nbsp;)')
out = ent.sub(ent_sub, out)

#Whitespace Organiser
sp = re.compile(r'\s+')
out = sp.sub(' ', out)


#Open the output.txt file and write the out string
with open('output.txt', 'w',  encoding = 'utf-8') as out_file:
    out_file.write(out)