import PyPDF2
import os

def merge_pdfs(pdf_list, output_filename):
    """Merges multiple PDFs into a single PDF."""
    merger = PyPDF2.PdfMerger()
    
    for pdf in pdf_list:
        if os.path.exists(pdf):
            merger.append(pdf)
        else:
            print(f"File not found: {pdf}")
    
    merger.write(output_filename)
    merger.close()
    print(f"Merged PDF saved as: {output_filename}")

if __name__ == "__main__":
    pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]  # Replace with actual filenames
    output_file = "merged_output.pdf"
    merge_pdfs(pdf_files, output_file)
