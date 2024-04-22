from ebooklib import epub
import ebooklib, sys, warnings
from bs4 import BeautifulSoup


class ReadFB2:

    def __init__(self, book_path):
        self.book_path = book_path
        self.info = []


    def read_book(self):
        with open(self.book_path, 'r', encoding='utf-8') as xml:
            soup = BeautifulSoup(xml.read(), 'xml')
            self.info.append(soup.find('book-title').text)
            self.info.append(soup.find('author').text.replace('\n', ' '))
            self.info.append(soup.find('publish-info').publisher.text)
            self.info.append(soup.find('publish-info').year.text)


class ReadEpub:

    def __init__(self, book_path):
        self.book_path = book_path
        self.info = []


    def read_book(self):
        warnings.filterwarnings("ignore")
        book = epub.read_epub(self.book_path)
        lst = [book.get_metadata('DC', 'title'), book.get_metadata('DC', 'creator'),
            book.get_metadata('DC', 'publisher'), book.get_metadata('DC', 'date')]
        
        self.info = [item[0][0] if item else '' for item in lst]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        fileneme = sys.argv[1]

        try:
            if fileneme.endswith('.fb2'):
                rb = ReadFB2(fileneme)
                rb.read_book()
                print(rb.info)
            elif fileneme.endswith('.epub'):
                re = ReadEpub(fileneme)
                re.read_book()
                print(re.info)
            else:
                raise Exception('Unsuitable file format')
        except FileNotFoundError as e:
            raise e
    else:
        raise Exception('Missing required arguments')