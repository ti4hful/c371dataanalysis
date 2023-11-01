# Cintia Biro-Hajnal 1/11/23
class extract:
    def fromCSV(self, file_path, delimiter=",", quotechar="|"):
        try:
            if not file_path:
                raise FileNotFoundError("File path is missing. Please provide a valid file path.")
            import csv
            dataset = list()
            with open(file_path) as f:
                csv_file = csv.DictReader(f, delimiter=delimiter, quotechar=quotechar)
                for row in csv_file:
                    dataset.append(row)
            return dataset
        except FileNotFoundError as e:
            while True:
                print(f"Error: {e}")
                new_path = input("Enter a corrected CSV file path or type 'quit' to exit: ")
                if new_path.lower() == 'quit':
                    exit()
                try:
                    with open(new_path):
                        return self.fromCSV(new_path, delimiter, quotechar)
                except FileNotFoundError as e:
                    continue

    def fromJSON(self, file_path):
        try:
            if not file_path:
                raise FileNotFoundError("File path is missing. Please provide a valid file path.")
            import json
            dataset = list()
            with open(file_path) as json_file:
                dataset = json.load(json_file)
            return dataset
        except FileNotFoundError as e:
            while True:
                print(f"Error: {e}")
                new_path = input("Enter a corrected JSON file path or type 'quit' to exit: ")
                if new_path.lower() == 'quit':
                    exit()
                try:
                    with open(new_path):
                        return self.fromJSON(new_path)
                except FileNotFoundError as e:
                    continue

e = extract()
csv_file_path = r'own projects\C371_DA\5DataAnalysisandExceptionHandling\ASSIGNMENTS\car_data.csv'
json_file_path = r'own projects\C371_DA\5DataAnalysisandExceptionHandling\ASSIGNMENTS\test.json'

dataset1 = e.fromCSV(file_path=csv_file_path)
dataset2 = e.fromJSON(file_path=json_file_path)

print("CSV Data:")
for row in dataset1:
    print(row)

print("\nJSON Data:")
for item in dataset2:
    print(item)
