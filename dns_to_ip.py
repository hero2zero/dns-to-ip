#!/usr/bin/env python3

import argparse
import socket
import csv
import sys
from pathlib import Path

def resolve_dns(hostname):
    """
    Resolve a DNS name to an IP address.
    
    Args:
        hostname (str): The DNS name to resolve
        
    Returns:
        str: The IP address or error message
    """
    try:
        ip_address = socket.gethostbyname(hostname.strip())
        return ip_address
    except socket.gaierror as e:
        return f"ERROR: {e}"

def read_dns_names(file_path):
    """
    Read DNS names from a text file.
    
    Args:
        file_path (str): Path to the input file
        
    Returns:
        list: List of DNS names
    """
    try:
        with open(file_path, 'r') as file:
            dns_names = [line.strip() for line in file if line.strip()]
        return dns_names
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def write_text_output(results, output_file):
    """
    Write results to a text file.
    
    Args:
        results (list): List of tuples (dns_name, ip_address)
        output_file (str): Output file path
    """
    with open(output_file, 'w') as file:
        file.write(f"{'DNS Name':<35} {'IP Address':<15}\n")
        file.write("-" * 50 + "\n")
        for dns_name, ip_address in results:
            file.write(f"{dns_name:<35} {ip_address:<15}\n")

def write_csv_output(results, output_file):
    """
    Write results to a CSV file.
    
    Args:
        results (list): List of tuples (dns_name, ip_address)
        output_file (str): Output file path
    """
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['DNS Name', 'IP Address'])
        writer.writerows(results)

def main():
    parser = argparse.ArgumentParser(description='Convert DNS names to IP addresses')
    parser.add_argument('input_file', help='Text file containing DNS names (one per line)')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('-f', '--format', choices=['text', 'csv'], default='text',
                       help='Output format: text or csv (default: text)')
    parser.add_argument('--print', action='store_true', 
                       help='Print results to console instead of file')
    
    args = parser.parse_args()
    
    # Validate input file
    if not Path(args.input_file).exists():
        print(f"Error: Input file '{args.input_file}' does not exist.")
        sys.exit(1)
    
    # Read DNS names from file
    dns_names = read_dns_names(args.input_file)
    
    if not dns_names:
        print("Error: No DNS names found in the input file.")
        sys.exit(1)
    
    print(f"Processing {len(dns_names)} DNS names...")
    
    # Resolve DNS names to IP addresses
    results = []
    for dns_name in dns_names:
        ip_address = resolve_dns(dns_name)
        results.append((dns_name, ip_address))
        print(f"Resolved: {dns_name} -> {ip_address}")
    
    # Output results
    if args.print:
        # Print to console
        print("\nResults:")
        print("-" * 50)
        for dns_name, ip_address in results:
            print(f"{dns_name:<30} {ip_address}")
    else:
        # Write to file
        if not args.output:
            # Generate default output filename
            input_stem = Path(args.input_file).stem
            extension = 'csv' if args.format == 'csv' else 'txt'
            output_file = f"{input_stem}_resolved.{extension}"
        else:
            output_file = args.output
        
        if args.format == 'csv':
            write_csv_output(results, output_file)
        else:
            write_text_output(results, output_file)
        
        print(f"\nResults written to: {output_file}")

if __name__ == '__main__':
    main()