import re

words = ["Python Parm", "Java, JavaScript", "C Pillow"]

for w in words:
    m = re.match("(P\w+)\W(P\w+)", w)
    if(m):
        print(m.groups())

def changeDateFormat(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)

dt1 = "2025-01-02"
print(changeDateFormat(dt1))

def extractDateURL(url):
    return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})', url)

text = "python exercises, php exercises, c exercises"
pattern = 'exercises'
for match in re.finditer(pattern,text):
    s = match.start()
    e = match.end()
    print("Found {0} at {1}:{2}".format(text[s:e],s,e))

text = text.replace(" ", "_")
print(text)


url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
print(extractDateURL(url1))



