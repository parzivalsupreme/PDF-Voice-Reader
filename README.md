# PDF Reader with Text to Speech

### Description
This script is used to read a PDF file and convert the text to speech using the pyttsx3 library. The script prompts the user to input the page numbers they would like to read and stores the pages in variables. The text is then extracted from each page and stored in separate variables. The script then enters an infinite loop where it prints the text from each page and converts it to speech using the function defined at the beginning of the script.

### Requirements
1. Python 3
2. PyPDF2 library
3. pyttsx3 library

### Usage
1. Install Python 3, PyPDF2, and pyttsx3 by running the following command:
```pip install PyPDF2 pyttsx3```
2. Download the PDF file that you want to read.
3. Replace the file path in the following line with the file path of the PDF file on your computer:
```reader =PdfReader(r"C:\Users\Elijah\Downloads\The Handmaids Tale [full text].pdf")```
4. Run the script by entering the following command in the terminal:
```python pdf_reader.py```
5. Enter the page numbers you would like to read when prompted. The script will read the text from the specified pages and convert it to speech.

### Note
The script will run indefinitely until it is manually stopped. To stop the script, press CTRL + C in the terminal.










