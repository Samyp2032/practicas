import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
dtype_dict = {
    'Vehicle Make': 'str',
    'Vehicle Model': 'str',
    'Vehicle Year': 'str'  # Usamos 'str' para tratar años de manera uniforme
}

# Ajusta la ruta al archivo CSV según sea necesario
crash_df = pd.read_csv('Crash_Reporting_-_Drivers_Data.csv', dtype=dtype_dict, low_memory=False)

print("           ¿Que es lo que mas afecta en los choques?                                                  ")


print("1.- Imprimimos todos los primeros 10 valores")
print(crash_df.head(10))
print("\n")
print("Para seguir pulsa enter")
input()

print("2.- Imprimimos todos los ultimos 10 valores")
print(crash_df.tail(10))
print("\n")
print("Para seguir pulsa enter")
input()

print("3.- Imprimimos el tamaño de nuestro dataset")
print(crash_df.shape)
print("\n")
print("Para seguir pulsa enter")
input()


def limpiar_datos(df):
    marcas_raras = ['N/A', 'UNKNOWN']
    modelos_raros = ['N/A', 'UNKNOWN']
    df_clean = df[~df['vehicle make'].isin(marcas_raras)]
    df_clean = df_clean[~df_clean['vehicle model'].isin(modelos_raros)]
    df_clean = df_clean.dropna(subset=['vehicle year'])
    df_clean.loc[:, 'vehicle year'] = pd.to_numeric(df_clean['vehicle year'], errors='coerce')
    df_clean = df_clean[df_clean['vehicle year'].between(1980, 2024)]
    return df_clean

# Aplicar limpieza de datos
crash_clean_df = limpiar_datos(crash_df)

print("4.- Imprimimos todas las columnas")
print(crash_df.columns.values)
print("\n")
print("Para seguir pulsa enter")
input()

print("5.- Imprimimos las filas")
print(crash_df.index.values)
print("\n")
print("Para seguir pulsa enter")
input()

print("6.- Imprimimos de la columna route type ordenamos")
print(crash_df['route type'].drop_duplicates().sort_values())
print("\n")
print("Para seguir pulsa enter")
input()

print("7.- Imprimimos de la columna route type ordenamos")
print(crash_df['road name'].drop_duplicates().sort_values())
print("\n")
print("Para seguir pulsa enter")
input()

print("8.- Imprimimos una funcion que saca los valores mas recurrentes de la columna que queremos")
def contar_valores():
    print("Algunos ejemplos: route type, road name, collision type, speed limit, vehicle make" )
    columna = str(input("Dame la columna: ")).lower()
    valores = crash_df[columna].value_counts()
    print(valores)

contar_valores()
print("\n")
print("Para seguir pulsa enter")
input()

def analisis_exploratorio(df):

    top_brands = df['vehicle make'].value_counts().head(30).index
    df_top_brands = df[df['vehicle make'].isin(top_brands)]
    
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df_top_brands, y='vehicle make', order=top_brands, palette='viridis')
    plt.title('Top 10 Marcas con Más Accidentes')
    plt.show()
    
    # Distribución de accidentes por año
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='vehicle year', palette='viridis')
    plt.title('Distribución de Accidentes por Año de Vehículo')
    plt.xticks(rotation=90)
    plt.show()
    
    # Distribución de accidentes por modelo de una marca específica
    marca = str(input("Dame la marca: ")).upper().strip()
    df_marca = df[df['vehicle make'].str.upper().str.strip() == marca]
    
    if not df_marca.empty:
        top_models = df_marca['vehicle model'].value_counts().head(10).index
        df_top_models = df_marca[df_marca['vehicle model'].isin(top_models)]
        
        plt.figure(figsize=(12, 6))
        sns.countplot(data=df_top_models, y='vehicle model', order=top_models, palette='viridis')
        plt.title(f'Top 10 Modelos de {marca} con Más Accidentes')
        plt.show()
    else:
        print(f"No se encontraron datos para la marca {marca}")

# Ejecutar análisis exploratorio
analisis_exploratorio(crash_clean_df)

def mostrar_modelos_por_marca(df):
    marca = input("Por favor ingresa la marca del vehículo: ").strip().upper()
    df_marca = df[df['vehicle make'] == marca]

    if not df_marca.empty:
        modelos_unicos = df_marca['vehicle model'].unique()
        print(f"Modelos de {marca}:")
        for modelo in modelos_unicos:
            print(modelo)
        return marca  # Devuelve la marca ingresada por el usuario
    else:
        print(f"No se encontraron modelos para la marca {marca}")
        return None

def mostrar_años_por_modelo(df, marca):
    modelo = input(f"Por favor ingresa el modelo del vehículo de la marca {marca}: ").strip().upper()
    df_modelo = df[(df['vehicle make'] == marca) & (df['vehicle model'] == modelo)]

    if not df_modelo.empty:
        # Crear un gráfico de barras horizontal
        plt.figure(figsize=(10, 6))
        sns.countplot(y='vehicle year', data=df_modelo)
        plt.xlabel('Frecuencia')
        plt.ylabel('Año del Vehículo')
        plt.title(f'Distribución del Modelo {modelo} de la Marca {marca} por Año')
        plt.tight_layout()
        plt.show()
    else:
        print(f"No se encontraron datos para el modelo {modelo} de la marca {marca}")

# Ejecutar la función para mostrar modelos por marca y guardar la marca
marca_seleccionada = mostrar_modelos_por_marca(crash_clean_df)

# Ejecutar la función para mostrar años por modelo y pasarle la marca seleccionada
if marca_seleccionada:
    mostrar_años_por_modelo(crash_clean_df, marca_seleccionada)
"""
def corregir_marca(df):
    columna = input("Por favor ingresa el nombre de la columna que deseas modificar: ").strip().lower()
    valor_buscar = input(f"Por favor ingresa el valor que deseas buscar en la columna '{columna}': ").strip().UPPER()
    nuevo_valor = input("Por favor ingresa el nuevo valor: ").strip().upper()

    pregunta = input(f"¿Estás seguro de que deseas cambiar '{valor_buscar}' a '{nuevo_valor}' en la columna '{columna}'? (s/n): ").strip().lower()
    if pregunta == 's':
        df[columna] = df[columna].str.replace(valor_buscar, nuevo_valor, case=False)
        df.to_csv('Crash_Reporting_-_Drivers_Data.csv', index=False)
        print("Se han guardado los cambios en el archivo CSV.")
    elif pregunta == 'n':
        print("No se han realizado cambios en el archivo CSV.")
    else:
        print("Respuesta no válida. No se han realizado cambios en el archivo CSV.")

# Llama a la función para corregir la marca en tu DataFrame y guardar los cambios en el archivo CSV si el usuario lo desea
corregir_marca(crash_df)
"""