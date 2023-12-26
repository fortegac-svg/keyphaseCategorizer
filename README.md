# keyphaseCategorizer

## Overview
`keyphaseCategorizer` is an innovative tool designed to automate the categorization of cybersecurity logs from various vendors. By integrating automated processes with manual review, it enhances the accuracy and efficiency of log analysis, crucial for proactive cybersecurity threat detection and response.

## Key Features
- **Automated Categorization**: Leverages vendor-specific keyword files for initial log entry categorization.
- **Manual Review Process**: Incorporates expert review to refine automated categorization results.
- **Customizable Keywords**: Adapts to evolving cybersecurity threats with editable keyword files.
- **Pre-Production Data Enhancement**: Validates and ensures data accuracy before production deployment.
- **Machine Learning Readiness**: Prepares datasets for use in enhancing machine learning models.

## Installation

### Prerequisites
- Python 3.x
- Pandas library

### Setup
Clone the repository:
git clone https://github.com/fortegac-svg/keyphaseCategorizer.git

Install the required dependencies:
pip install pandas


## Usage
Ensure `Uncategorized.xlsx` and `keywords.csv` are placed in the working directory. Execute the tool with the following command:
python categorize_logs.py <path/to/logfile.csv> <path/to/keywords.csv> <path/to/outputfile.csv>


## Input File Format
- `Uncategorized.xlsx`: Should contain log entries with 'Device Event Class ID' and 'Description'.
- `keywords.csv`: Comprises categorization rules and keywords for each category.

## Contributing
We welcome contributions to `keyphaseCategorizer`. To contribute:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact
- Francisco Ortega - [fortega@opentext.com](mailto:fortega@opentext.com)

Project Link: [https://github.com/fortegac-svg/keyphaseCategorizer](https://github.com/fortegac-svg/keyphaseCategorizer)
