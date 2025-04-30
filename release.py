import re

def parse_line(line):
    regex = r"(?P<title>.*) by @(?P<author>.*) in (?=http)(?P<uri>.*)"
    match = re.match(regex, line).groupdict()
    return (match['title'], match['author'], match['uri'])

with open("release.txt") as f:
    release_lines=f.readlines()
other=[]
normal=[]
renovate=[]
for line in release_lines:
    if line[:2] == "* ":
        rest_of_line = line[2:]
        title, author, uri = parse_line(rest_of_line)
        new_authorless_line = f"* [{title}]({uri})"
        new_line = f"{new_authorless_line} by @{author}"
        if "@renovate" in line:
            renovate.append(new_authorless_line)
        else:
            normal.append(new_line)
    else:
        other.append(line)
for line in other:
    print (line)
for line in normal:
    print (line)

print ("#### Renovate")
for line in sorted(renovate):
    print (line)

    
    

