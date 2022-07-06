import sys
import PyPDF2

args_list = sys.argv[1:]
# args_list = [a for i, a in enumerate(sys.argv) if i > 0]
# the code above returns the same list, but using enumerate() which returns an (index, value) tuple
# print(args_list)


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for f in pdf_list:
        merger.append(f)
        # merger.append(PyPDF2.PdfFileReader(f, 'rb'))
        # we can also use the code above in case of running into any non binary file error.
    merger.write('mergedfile.pdf')


if __name__ == '__main__':
    pdf_merger(args_list)
