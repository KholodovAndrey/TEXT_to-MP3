"""Данный скрипт преобразовывает файл любого из текстовых форматов
.pdf, .docx, .txt или .rtf в mp3 файл.

This script converts a file of any of the following text formats:
.pdf, .docx, .txt, or .rtf into an mp3 file.
"""

from pathlib import Path

import docx2txt
import pdfplumber
from art import tprint
from gtts import gTTS
from striprtf.striprtf import rtf_to_text


def pdf_to_text(file_path='test.pdf'):
    """Данная функция забирает текст из pdf файла."""
    with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
        pages = [page.extract_text() for page in pdf.pages]
    text = ''.join(pages)
    text = text.replace('\n', '')
    return text


def txt_to_text(file_path='test.txt'):
    """Данная функция забирает текст из txt файла."""
    with open(file=file_path, encoding='utf-8') as txt:
        text = txt.read()
    text = text.replace('\n', ' ')
    return text


def rtf_in_text(file_path='test.txt'):
    """Данная функция забирает текст из rtf файла."""
    with open(file_path) as infile:
        content = infile.read()
        text = rtf_to_text(content)
    text = text.replace('\n', ' ')
    return text


def docx_to_mp3(file_path='testru.docx'):
    """Данная функция забирает текст из docx файла."""
    text = docx2txt.process(file_path)
    text = text.replace('\n', '')
    return text


def text_to_mp3(text, file_path, language='en'):
    """Функция для преобразования текстовой строки в mp3 файл."""
    output = gTTS(text=text, lang=language, slow=False)
    file_name = Path(file_path).stem
    output.save(f'{file_name}.mp3')
    return (f'[+] {file_name}.mp3 was saved successfully!',
            '---Have a good day!---')


def main():
    """Основной скрипт.
    Выбор формата, приветствие, выбор языка и само преобразование."""

    global converse
    form = input('''Choose input format: 'pdf', 'txt', 'rtf' or 'docx': ''')
    tprint('%s--TO--MP3' % form.upper(), font='bulbhead')
    file_path = input('''\nEnter a file's path: ''')
    language = input('''Choose language: 'en' or 'ru': ''')
    if form == 'docx' and Path(file_path).suffix == '.docx':
        converse = docx_to_mp3(file_path)
    elif form == 'pdf' and Path(file_path).suffix == '.pdf':
        converse = pdf_to_text(file_path=file_path)
    elif form == 'txt' and Path(file_path).suffix == '.txt':
        converse = txt_to_text(file_path=file_path)
    elif form == 'rtf' and Path(file_path).suffix == '.rtf':
        converse = rtf_in_text(file_path=file_path)

    if Path(file_path).is_file():
        print('File exists!')
        print(f'[+] Original file: {Path(file_path).name}')
        print('[+] Processing...')
        print(text_to_mp3(converse, file_path, language=language))
    else:
        print('File not exists, check the file path!')


if __name__ == '__main__':
    main()
