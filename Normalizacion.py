import csv
import re

# Normalizar nombres de creadores
def normalize_name(name):
    return ' '.join([word.capitalize() for word in name.split()])

# Normalizar tecnologías
def normalize_technologies(tech):
    return ', '.join([t.strip().title() for t in tech.split(',')])

# Normalizar ubicaciones
def normalize_location(location):
    location_mapping = {
        'US': 'United States',
        'EEUU': 'United States',
        'Algeria': 'Algeria',  # Ejemplo de estandarización
    }
    return location_mapping.get(location.strip(), location.strip())

# Normalizar enlaces
def normalize_link(link):
    if not link.startswith("https://"):
        return "https://" + link.strip()
    return link.strip()

# Normalizar títulos de aplicaciones
def normalize_title(title):
    return title.title().strip()

# Dividir creadores múltiples
def split_creators(creators):
    return [normalize_name(c.strip()) for c in re.split(',|&', creators)]

# Función para procesar el CSV y normalizar los datos
def normalize_data(file_path, output_file):
    with open(file_path, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames  # Obtener los nombres de las columnas
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        # Escribir el encabezado en el archivo de salida
        writer.writeheader()
        
        for row in reader:
            # Normalizar los datos de cada fila
            row['By'] = ', '.join(split_creators(row['By'])) if row['By'] else ''
            row['Built With'] = normalize_technologies(row['Built With']) if row['Built With'] else ''
            row['Location'] = normalize_location(row['Location']) if row['Location'] else ''
            row['YouTube Link'] = normalize_link(row['YouTube Link']) if row['YouTube Link'] else ''
            row['Project Link'] = normalize_link(row['Project Link']) if row['Project Link'] else ''
            row['Title'] = normalize_title(row['Title']) if row['Title'] else ''
            
            # Escribir la fila normalizada en el archivo de salida
            writer.writerow(row)

# Ejemplo de uso con un archivo CSV
file_path = 'C:/Users/jcia9/Escritorio/MuestraCSV.csv'  # Ruta del archivo de entrada
output_file = 'C:/Users/jcia9/Escritorio/NormalizedOutput.csv'  # Ruta del archivo de salida

# Normalizar los datos y guardarlos en un nuevo archivo CSV
normalize_data(file_path, output_file)

# Mensaje de confirmación
print(f"Normalización completada. El archivo normalizado se ha guardado en {output_file}.")
