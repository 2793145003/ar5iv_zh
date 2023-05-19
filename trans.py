from bs4 import BeautifulSoup
import time
from deep_translator import GoogleTranslator as Translator
import re

def translate_text(text):
    while True:
        try:
            print(text)
            translator = Translator(source='en', target='zh-CN')
            translation = translator.translate(text)
            print(translation)
            break
        except Exception as e:
            print(f"Translation error: {e}")
            time.sleep(30)
            continue
    return translation

def replace_tags(html):
    replaced_text = []
    while True:
        html = str(html)
        html = BeautifulSoup(html, 'html.parser')
        con = False
        for tag in html.find_all(True):
            if (
                (tag.string and '【占' not in tag.string) or tag.name == 'math'
                or tag.name == 'span' and 'footnote' in tag['id']
            ):
                replaced_text.append(str(tag))
                tag.replace_with(f'【占{len(replaced_text)-1}】')
                con = True
                break
        if not con:
            break
    
    replaced_html = str(html)
    return replaced_html, replaced_text

def trans_tags(tags):
    results = []
    for tag in tags:
        tag = BeautifulSoup(tag, 'html.parser')
        if tag.name == 'math':
            results.append(str(tag))
            continue
        if not tag.string:
            results.append(str(tag))
            continue
        s = tag.text
        if ' ' not in s:
            results.append(str(tag))
            continue
        trans = translate_text(s)
        tag.string.replace_with(trans)
        results.append(str(tag))
    return results

def remove_spaces_between_brackets(text):
    # 移除'【'与'】'之间的所有空格
    pattern = r'【\s*([^【】]+)\s*】'
    repl = lambda match: '【' + match.group(1).replace(' ', '') + '】'
    result = re.sub(pattern, repl, text)
    return result

def add_tags(paragraph, tags):
    paragraph = str(paragraph)
    paragraph = remove_spaces_between_brackets(paragraph)
    for i in range(len(tags)):
        paragraph = paragraph.replace(f'【占{i}】', tags[i])
    return paragraph

def translate_html(input_path, output_path):
    with open(input_path, 'r') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    paragraphs = soup.find_all('p')

    for paragraph in paragraphs:
        pure, tags = replace_tags(paragraph)
        pure = BeautifulSoup(pure, 'html.parser')
        original_text = pure.get_text()
        text = translate_text(original_text)
        pure.string = text
        tags = trans_tags(tags)
        pure = add_tags(pure, tags)
        attrs = paragraph.attrs
        result = f'<p {" ".join([f"{k}={v}" for k, v in attrs.items()])}>{pure}</p>'
        paragraph.insert_after(BeautifulSoup(result, 'html.parser'))

    with open(output_path, 'w') as f:
        f.write(str(soup))


if __name__ == "__main__": 
    # 示例用法
    input_html = "html/main.html"
    output_html = "html/paper.html"
    translate_html(input_html, output_html)