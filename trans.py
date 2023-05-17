from bs4 import BeautifulSoup
import time
from deep_translator import GoogleTranslator as Translator
import re

def translate_text(text):
    print(text)
    translator = Translator(source='en', target='zh-CN')
    translation = translator.translate(text)
    print(translation)
    # time.sleep(3)
    return translation

def replace_math_content(string):
    pattern = r'(<math\b[^>]*>.*?<\/math>)'
    count = 1
    def repl(match):
        nonlocal count
        replaced_content = '【公式{}】'.format(count)
        count += 1
        return replaced_content

    replaced_string, num_replacements = re.subn(pattern, repl, string, flags=re.DOTALL)
    replaced_content = re.findall(pattern, string, flags=re.DOTALL)
    
    return replaced_string, replaced_content

def restore_math_content(string, replacements):
    pattern = r'【公式\d+】'

    def restore(match):
        replacement = replacements[restore.counter]
        restore.counter += 1
        return replacement

    restore.counter = 0

    restored_string = re.sub(pattern, restore, string)
    return restored_string

def translate_html(input_path, output_path):
    with open(input_path, 'r') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    paragraphs = soup.find_all('p')

    for paragraph in paragraphs:
        # original_text = paragraph.get_text()
        no_math_paragraph, math_contents = replace_math_content(str(paragraph))
        original_text = no_math_paragraph#.get_text()
        text = translate_text(original_text)
        translated_text = restore_math_content(text, math_contents)
        paragraph.insert_after(BeautifulSoup(f'{translated_text}', 'html.parser'))

    with open(output_path, 'w') as f:
        f.write(str(soup))



# 示例用法
input_html = "html/main.html"
output_html = "html/paper.html"
translate_html(input_html, output_html)