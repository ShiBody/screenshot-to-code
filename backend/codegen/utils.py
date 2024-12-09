import re
import os
LOCAL_DIR = '/Users/xiaoxshi/Desktop/brainstorm/brainStormFinal'

PATTERN = r'(?:\w+\.\w+:?\n)?\n*```[\w]*\n[\s\S]*?```'
SMALL_PATTERN = r'([\w.]+)\n*```[\w]*\n([\s\S]*?)```'

def extract_html_content(text: str):
    # store to local dir
    matches = re.findall(PATTERN, text, re.MULTILINE)
    if not matches:
        return
    if not os.path.exists(LOCAL_DIR):
        os.mkdir(LOCAL_DIR)
    for i in matches:
        smallMatches = re.findall(SMALL_PATTERN, i)
        if not smallMatches:
            continue
        for j in smallMatches:
            fileName, fileContent = j
            with open(os.path.join(LOCAL_DIR, fileName), 'w') as file:
                file.write(fileContent)


TEST_RES = '/Users/xiaoxshi/Desktop/brainstorm/test/res_12091353.txt'
if __name__ == '__main__':
    with open(TEST_RES, 'r+') as file:
        text = file.read()
        extract_html_content(text)