# MScanner

![Screencast from 2024-03-16 15-26-39](https://github.com/ICWR-TEAM/MScanner/assets/45759837/c832f320-1dff-4d35-9a32-19cc7b9894ab)


MScanner is a powerful and flexible malicious code scanner designed to assist security professionals and developers in identifying and mitigating malicious code within software projects. Built with Python, MScanner leverages a provided `wordlist.txt` for detecting a wide range of malware and malicious scripts, facilitating the process of code security analysis.

## Key Features

- **List-Based Detection**: Utilizes a customizable `wordlist.txt` to identify various types of malware, including viruses, trojans, and ransomware, within source code or applications.
- **Detailed Reports**: Provides detailed analysis reports, including the locations of files and the code of detected malware.
- **Customizable Word List**: The `wordlist.txt` file can be edited to add or remove terms, allowing for customized detection based on specific needs.
- **Open Source**: Developed as an open-source project with community support for continuous updates and security improvements.

## System Requirements

- Python 3.6+

## Installation

Clone the MScanner repository using git:

```bash
git clone https://github.com/ICWR-TEAM/MScanner/
cd MScanner
```

## Usage
To start a scan, run the following command in your project's root directory:
```bash
python scan.py -t <target_directory>
```
For other usage options, run help:
```bash
python scan.py -h
```

# Update
1. Code Optimization
2. Performance Enhancement

## Contributing
Contributions are highly appreciated. If you would like to contribute, please fork the repository, create your feature branch, and submit a pull request.

## License
MScanner is distributed under the MIT License. See the LICENSE file for more information.

## Contributing to Wordlist Development

We actively encourage our users to contribute to the development of the `wordlist.txt` to make detection even more comprehensive. By sharing your insights and adding new terms related to emerging threats, you can help in enhancing the effectiveness of MScanner for everyone.

To contribute, simply edit the `wordlist.txt` file to include new malicious terms you encounter and submit a pull request. We welcome contributions that help us stay ahead of threats and improve security for the community.

Your contributions will not only help in improving MScanner's detection capabilities but also in safeguarding the broader software development ecosystem against emerging malware and security threats.

