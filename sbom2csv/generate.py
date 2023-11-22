import argparse
import json
import csv

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def write_csv(components, output_file):
    headers = ["Name", "Version", "Description", "Developer", "License", "User Document"]

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for component in components:
            name = component.get("name", "")
            version = component.get("version", "")
            description = component.get("description", "")
            developer = component.get("author", "")  # Using 'author' as 'developer'
            license = component.get("licenses", [{}])[0].get("license", {}).get("id", "")
            user_document = next((ref['url'] for ref in component.get("externalReferences", []) if ref.get("type") == "website"), "")

            writer.writerow([name, version, description, developer, license, user_document])

def main():
    parser = argparse.ArgumentParser(description='Convert SBOM JSON to CSV')
    parser.add_argument('-i', '--input', required=True, help='Input JSON file path')
    parser.add_argument('-o', '--output', required=True, help='Output CSV file path')
    parser.add_argument('-f', '--format', choices=['csv'], required=True, help='Output file format')

    args = parser.parse_args()

    if args.format == 'csv':
        json_data = read_json(args.input)
        if 'components' in json_data:
            write_csv(json_data['components'], args.output)
        else:
            print("JSON file does not contain 'components' key.")
    else:
        print("Unsupported format.")

if __name__ == "__main__":
    main()
