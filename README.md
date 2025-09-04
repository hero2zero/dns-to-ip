# DNS to IP Converter

A Python script that resolves DNS names to IP addresses and outputs the results in text or CSV format.

## Features

- Reads DNS names from a text file (one per line)
- Resolves each DNS name to its corresponding IP address
- Supports multiple output formats: tab-separated text or tab-delimited CSV
- Error handling for failed DNS resolutions
- Console output option
- Auto-generates output filenames

## Usage

### Basic Examples

```bash
# Convert DNS names to text file
python3 dns_to_ip.py input_dns.txt

# Convert to CSV format
python3 dns_to_ip.py input_dns.txt -f csv

# Specify custom output file
python3 dns_to_ip.py input_dns.txt -o results.csv -f csv

# Print results to console only
python3 dns_to_ip.py input_dns.txt --print
```

### Command Line Options

```
positional arguments:
  input_file            Text file containing DNS names (one per line)

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file path
  -f {text,csv}, --format {text,csv}
                        Output format: text or csv (default: text)
  --print               Print results to console instead of file
```

## Input Format

Create a text file with DNS names, one per line:

```
google.com
github.com
stackoverflow.com
python.org
microsoft.com
```

## Output Formats

### Text Format (Default)
Tab-separated columns with proper alignment:
```
DNS Name                            IP Address     
--------------------------------------------------
google.com                          142.250.191.14 
github.com                          140.82.113.4   
stackoverflow.com                   151.101.1.69   
```

### CSV Format
Tab-delimited CSV file:
```
DNS Name	IP Address
google.com	142.250.191.14
github.com	140.82.113.4
stackoverflow.com	151.101.1.69
```

## Error Handling

If a DNS name cannot be resolved, the script will show an error message instead of an IP address:
```
invalid-domain.test    ERROR: [Errno -2] Name or service not known
```

## Requirements

- Python 3.6+
- No external dependencies (uses built-in libraries only)

## Installation

1. Clone this repository or download the script
2. Make the script executable (optional):
   ```bash
   chmod +x dns_to_ip.py
   ```

## Example

Using the included example file:

```bash
# Run with example DNS names
python3 dns_to_ip.py example_dns.txt

# Output will be saved as example_dns_resolved.txt
```

## License

This project is open source and available under the MIT License.