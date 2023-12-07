import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el conjunto de datos
file_path = r'C:\Users\sofia\OneDrive\Documentos\proyecto\cervical_cancer.csv'
df = pd.read_csv(file_path)

# Reemplazar "?" con NaN para facilitar el manejo de los datos faltantes
df.replace('?', pd.NA, inplace=True)

# Convertir columnas numéricas a tipo float
numeric_columns = ['Age', 'Number of sexual partners', 'First sexual intercourse', 'Num of pregnancies', 'Smokes (years)', 'Smokes (packs/year)', 'Hormonal Contraceptives (years)', 'IUD (years)', 'STDs (number)', 'STDs: Number of diagnosis', 'STDs: Time since first diagnosis', 'STDs: Time since last diagnosis']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Imputar valores faltantes solo en columnas numéricas
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Imprimir la información de encabezado para verificar los nombres de las columnas
print(df.head())

# Imprimir estadísticas descriptivas
print(df.describe())

# Visualizar la relación entre la edad y el número de parejas sexuales
plt.scatter(df['Age'], df['Number of sexual partners'])
plt.xlabel('Age')
plt.ylabel('Number of sexual partners')
plt.title('Scatter Plot: Age vs Number of Sexual Partners')
plt.show()

# Histograma de la edad del primer coito
df['First sexual intercourse'].plot(kind='hist', bins=10, edgecolor='black')
plt.xlabel('First Sexual Intercourse')
plt.ylabel('Frequency')
plt.title('Histogram: First Sexual Intercourse Age')
plt.show()

# Visualizar la relación entre ETS y el riesgo de cáncer cervical
std_columns = ['STDs (number)', 'STDs: Number of diagnosis', 'STDs: Time since first diagnosis', 'STDs: Time since last diagnosis']
df_std = df[std_columns]
df_std['Biopsy'] = df['Biopsy']
df_std_corr = df_std.corr()

# PLOTTING THE HEATMAP FOR CORRELATION MATRIX OF ETS FEATURES
plt.figure(figsize=(10, 8))
plt.title('Correlation Matrix - ETS Features vs Biopsy')
sns.heatmap(df_std_corr, annot=True, cmap='coolwarm', linewidths=.5)
plt.show()
