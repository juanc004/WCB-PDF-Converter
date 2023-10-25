# Import required libraries
from pdf2image import convert_from_path
from PyPDF2 import PdfReader
from PIL import Image
import os

# Function to convert a single PDF page to a PNG image
def convert_single_page_to_png(pdf_path, output_folder, page_number):
    """Convert a single PDF page to PNG.
    
    Args:
        pdf_path (str): The path to the PDF file.
        output_folder (str): The folder where the PNG image will be saved.
        page_number (int): The page number to convert.
    """
    images = convert_from_path(pdf_path, first_page=page_number, last_page=page_number)
    for i, image in enumerate(images):
        image_path = f"{output_folder}/page_{page_number}.png"
        image.save(image_path)
        print(f"Saved {image_path}")

# Function to verify if individual PNG files for each page exist
def verify_individual_png_files(output_folder, total_pages):
    """Verify the existence of individual PNG files for each page.
    
    Args:
        output_folder (str): The folder where the PNG images are saved.
        total_pages (int): The total number of pages.
    
    Returns:
        bool: True if all PNG files exist, False otherwise.
    """
    for page_number in range(1, total_pages + 1):
        image_path = f"{output_folder}/page_{page_number}.png"
        if not os.path.exists(image_path):
            print(f"Missing PNG for page {page_number}")
            return False
    return True

# Function to combine individual PNG files into a single PNG image
def combine_individual_pngs(output_folder, output_file):
    """Combine individual PNGs into a single PNG file.
    
    Args:
        output_folder (str): The folder containing individual PNG files.
        output_file (str): The path to save the combined PNG file.
    """
    png_files = [f"{output_folder}/page_{i + 1}.png" for i in range(total_pages)]
    images = [Image.open(png) for png in png_files]
    
    total_width = images[0].width
    total_height = sum(image.height for image in images)
    
    new_image = Image.new("RGB", (total_width, total_height))
    
    y_offset = 0
    for image in images:
        new_image.paste(image, (0, y_offset))
        y_offset += image.height
    
    new_image.save(output_file)
    print(f"Saved combined image as {output_file}")

# Main function to manage the multi-step PDF to PNG conversion
def multi_step_pdf_to_png(pdf_path, individual_output_folder, final_output_file):
    """Orchestrates the conversion of a PDF to individual PNGs and then a single PNG.
    
    Args:
        pdf_path (str): The path to the PDF file.
        individual_output_folder (str): The folder to save individual PNGs.
        final_output_file (str): The path to save the final combined PNG.
    """
    # Get the total number of pages in the PDF
    pdf = PdfReader(open(pdf_path, "rb"))
    global total_pages
    total_pages = len(pdf.pages)
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(individual_output_folder):
        os.makedirs(individual_output_folder)
    
    # Step 1: Convert each PDF page to an individual PNG file
    for page_number in range(1, total_pages + 1):
        convert_single_page_to_png(pdf_path, individual_output_folder, page_number)
    
    # Step 2: Verify each PNG file
    if not verify_individual_png_files(individual_output_folder, total_pages):
        print("Verification failed. Exiting.")
        return
    
    # Step 3: Combine individual PNGs into a single PNG
    combine_individual_pngs(individual_output_folder, final_output_file)

# Hardcoded paths and standard dimensions; replace these with actual paths
pdf_path = "pathname"
individual_output_folder = "pathname"
final_output_file = "pathname"

# Run the multi-step conversion function
multi_step_pdf_to_png(pdf_path, individual_output_folder, final_output_file)
