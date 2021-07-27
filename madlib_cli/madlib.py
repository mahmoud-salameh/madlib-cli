import re
def read_template(filepath: str) -> str:
    if filepath != "assets/read_template.txt":
        raise FileNotFoundError('no path found')
    with open(filepath, 'r') as file:
        file_content = file.read()
    return file_content.strip()

def parse_template(file_content:str):
    parse= re.findall(r'\{(.*?)\}', file_content)
    for item in parse:    
        file_content=file_content.replace((item),'',2)
    return file_content, tuple(parse)


def merge(file_content,parse):
    updatedText=file_content.format(*parse)

    with open('assets/test_merge.txt','w') as result:
        result.write(updatedText)
    return updatedText