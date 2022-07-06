import sys
import os
import PyPDF2
from pdfmerger import pdf_merger

pdf_files = sys.argv[1:]
watermark = './Resources/wtr.pdf'


def watermark_applier(pdf_list):
    merge_list = []
    for f in pdf_list:
        with open(f, 'rb') as input_file, open(watermark, 'rb') as watermark_file:
            writer = PyPDF2.PdfFileWriter()
            input_pdf = PyPDF2.PdfFileReader(input_file)
            watermark_pdf = PyPDF2.PdfFileReader(watermark_file)
            watermark_page = watermark_pdf.getPage(0)
            marked_file = f'watermarked_{os.path.basename(f)}'
            for i in range(input_pdf.getNumPages()):
                pdf_page = input_pdf.getPage(i)
                pdf_page.merge_page(watermark_page)
                writer.addPage(pdf_page)

            with open(marked_file, 'wb') as watermarked_file:
                writer.write(watermarked_file)
                merge_list.append(marked_file)
    return merge_list


merge_or_not = input(
    'Do you also want to merge your files afterwards? (yes or no): ')

while merge_or_not != 'yes' and merge_or_not != 'no':
    merge_or_not = input('Please enter yes or no: ')
    continue

if __name__ == '__main__':
    if merge_or_not == 'yes':
        pdf_merger(watermark_applier(pdf_files))
    else:
        watermark_applier(pdf_files)
