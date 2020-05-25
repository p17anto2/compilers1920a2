import re

out = ""

#Open and write the file to og string
with open('testpage.txt', 'r', encoding = 'utf-8') as file:
    out = file.read()

#Title
title = re.compile(r'<title>(.*)</title>')
for m in title.finditer(out):
    out = title.sub(m.group(1), out)

#Comments
comm = re.compile(r'<!.+?>')
for m in comm.finditer(out):
    out = comm.sub('', out)
    
#Script and Style
scst = re.compile(r'<script.*?</script>|<style.*?</style>', re.DOTALL)
for m in scst.finditer(out):
    out = scst.sub('', out)
    
#Links
#lin = re.compile(r'<a>(.*)</a>')


#Open the output.txt file and write the out string
with open('output.txt', 'w',  encoding = 'utf-8') as out_file:
    out_file.write(out)