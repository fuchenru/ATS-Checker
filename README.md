# ATS-Checker

![Result](https://d3kqdc25i4tl0t.cloudfront.net/articles/content/57aca545fa80af785f1df9127cf971fe_HeroWhatisanATS.jpg)

A Free Tool to Check if Your Resume is "ATS-Friendly"

Are you wondering if your resume is "ATS-friendly"? In today's job market, many companies use Applicant Tracking Systems (ATS) to filter and rank resumes based on specific criteria. If your resume isn't ATS-friendly, it may not be parsed correctly, and you could miss out on potential opportunities.

This project is a free website that allows you to check if your resume is ATS-friendly. Simply upload your resume, and the tool will analyze it to ensure that it can be parsed accurately by common ATS systems.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or later
- Flask
- PyPDF2

### Installation

Follow these steps to get your development environment set up:

1. **Clone the repository**

```bash
git clone https://github.com/fuchenru/ATS-Checker.git
```

2. **Install the required packages**

```bash
pip install -r requirements.txt
```

3. **Run the Flask application**

```bash
python ats.py
```

## Usage

Open your web browser and navigate to http://127.0.0.1:5000
Click the "Choose File" button and select a PDF resume from your local file system.
Click the "Submit" button to upload the file.
The extracted text content from the PDF resume will be displayed on the webpage.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.