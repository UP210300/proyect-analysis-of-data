import pandas as pd

def leer_csv_y_mostrar_10_primeras_filas(ruta_del_archivo):
    # Intentar leer el archivo CSV
    try:
        datos = pd.read_csv(ruta_del_archivo)
        
        # Mostrar las primeras 10 filas
        primeras_10_filas = datos.head(10)
        
        # Organizar los datos y devolverlos
        datos_organizados = primeras_10_filas.sort_values(by=primeras_10_filas.columns[0])
        
        return datos_organizados
        
    except Exception as e:
        return f"Error al leer el archivo CSV: {e}"

# Ruta del archivo CSV
ruta_del_archivo = r'C:\Users\sofia\OneDrive\Documentos\proyecto\cervical_cancer.csv'

# Llamada a la función y mostrar los resultados
resultados = leer_csv_y_mostrar_10_primeras_filas(ruta_del_archivo)
print(resultados)
