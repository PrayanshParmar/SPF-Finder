# SPF-Finder
SPF-Finder is a python script to find spf record of a domain - it can find spf of domain in bulk.

## Installation

1. You need python3, pip3, git

2. Fork/Clone/Download this repo
    `https://github.com/PrayanshParmar/SPF-Finder.git`
 
3. Navigate to the directory
    `cd SPF-Finder`

## SPF_Finder -h
```
usage: python3 spf.py [-h] [-v] [-d] [-l] domain_name/input_file [-o] output_file
------------------------------------------------------------------------------------------------    
-h, --help         Help section
-v, --version      Show version
-d, --domain       for single domain
-l, --inputfile    Input file of domain name (support only ".txt")
-o, --outputfile   Output file name (support only ".txt")
------------------------------------------------------------------------------------------------

```

## Usage

### For single scan
`$ python3 spf.py -d domain`

### For Bulk scan without output_file
`$ python3 spf.py -l input_file`
- Only support `.txt` Input_file extension.
- file must contain only `domain name one by one.`
![image](https://user-images.githubusercontent.com/103236128/200896923-48c03dc6-098a-4a8a-af26-0b43aafc3ba1.png)

### For Bulk scan with output_file
`$ python3 spf.py -l input_file -o output_file`
- Only support `.txt` Input_file and Output_file extension.
- file must contain only `domain name one by one.`

























