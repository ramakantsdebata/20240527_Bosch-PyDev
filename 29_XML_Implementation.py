import xml.etree.ElementTree as ET
from xml.dom import minidom

# Parsing XML Data
def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for book in root.findall('book'):
        title = book.find('title').text
        author = book.find('author').text
        year = book.find('year').text
        price = book.find('price').text
        genres = [genre.text for genre in book.find('genres').findall('genre')]

        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Year: {year}")
        print(f"Price: {price}")
        print(f"Genres: {', '.join(genres)}\n")

# Adding New Book
def add_new_book(file_path, new_book_data):
    tree = ET.parse(file_path)
    root = tree.getroot()

    new_book = ET.Element('book')
    ET.SubElement(new_book, 'title').text = new_book_data['title']
    ET.SubElement(new_book, 'author').text = new_book_data['author']
    ET.SubElement(new_book, 'year').text = str(new_book_data['year'])
    ET.SubElement(new_book, 'price').text = str(new_book_data['price'])
    
    genres = ET.SubElement(new_book, 'genres')
    ET.SubElement(genres, 'genre').text = new_book_data['genre']

    root.append(new_book)

    # Pretty print the XML
    rough_string = ET.tostring(root, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_data = reparsed.toprettyxml(indent="  ")

    # Write the pretty-printed XML to file
    with open('updated_data.xml', 'w') as f:
        f.write(pretty_data)

if __name__ == "__main__":
    # Path to the XML file
    xml_file_path = 'data.xml'
    
    # Parsing the XML file and printing the contents
    parse_xml(xml_file_path)
    
    # New book data to be added
    new_book = {
        'title': 'Python Programming',
        'author': 'Guido van Rossum',
        'year': 2022,
        'price': 39.99,
        'genre': 'Programming'
    }
    
    # Adding the new book and writing to a new file
    add_new_book(xml_file_path, new_book)
