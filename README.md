
# WCB PDF Converter

## Description

A Python-based utility for converting White Cell Briefs (WCB) from PDF format to individual and combined PNG files.
This tool is primarily designed for CRO Phase II to facilitate the upload of WCB into the CP2 Cadre Screener Dashboard.

## Features

- Converts each page of a PDF into an individual PNG file.
- Verifies the existence of individual PNG files for each page.
- Combines individual PNG files into a single PNG image.

## Installation

### Prerequisites

- Python 3.x
- Pip

### Dependencies

- pdf2image
- PyPDF2
- PIL (Pillow)

Run the following command to install all required packages:

```bash
pip install pdf2image PyPDF2 Pillow
```

## Usage

### Command-line Arguments

The script accepts the following command-line arguments:

1. `pdf_path`: The path to the source PDF file.
2. `individual_output_folder`: The directory where individual PNGs will be saved.
3. `final_output_file`: The path where the final combined PNG will be saved.

```bash
python multi_step_pdf_to_png.py "path/to/pdf/file.pdf" "path/to/individual/output/folder" "path/to/final/output/file.png"
```

### In-code Configuration

Alternatively, you can specify the file paths directly in the code:

```python
pdf_path = "your/pdf/path.pdf"
individual_output_folder = "your/individual/png/folder"
final_output_file = "your/final/output/file.png"
```

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
