import csv
import re

def text_filter(text, stopwords):
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    cleaned_text = cleaned_text.lower()
    words = cleaned_text.split()
    filtered_words = [word for word in words if word not in stopwords]
    filtered_text = ' '.join(filtered_words)
    return filtered_text

# Baca file CSV input
input_file = 'input_data.csv'
output_file = 'output_data.csv'
stopwords = ["ini", "adalah", "dan", "akan", "yang"]

with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Baca baris header
    data = []
    for row in reader:
        cleaned_row = [text_filter(cell, stopwords) for cell in row]
        data.append(cleaned_row)

# Simpan hasil ke file CSV output
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)  # Tulis baris header
    writer.writerows(data)  # Tulis data yang telah dibersihkan

print("Pembersihan data selesai. Hasil tersimpan dalam file", output_file)
