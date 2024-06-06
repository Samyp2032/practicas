import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #Importamos librerias

# Cargar datos
dtype_dict = {
    'Vehicle Make': 'str',
    'Vehicle Model': 'str',
    'Vehicle Year': 'str'  # Usamos 'str' para tratar columnas de manera uniforme y no se dectecte otro valor
}

# Ajusta la ruta al archivo CSV según sea necesario
crash_df = pd.read_csv('Crash_Reporting_-_Drivers_Data.csv', dtype=dtype_dict, low_memory=False)

print("           ¿Qué es lo que más afecta en los choques?                                                  ") #Pregunta general de mi caso

print("1.- Imprimimos todos los primeros 10 valores") 
print(crash_df.head(10))
print("\n")
print("Para seguir pulsa enter")
input()

print("2.- Imprimimos todos los últimos 10 valores")
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
    # Eliminar filas con marcas de vehículos raros
    df_clean = df[~df['vehicle make'].isin(marcas_raras)]
    # Convertir la columna 'vehicle year' a tipo numérico
    df_clean['vehicle year'] = pd.to_numeric(df_clean['vehicle year'], errors='coerce')
    # Eliminar filas con modelos de vehículos raros
    df_clean = df_clean[~df_clean['vehicle model'].isin(modelos_raros)]
    # Eliminar filas con valores NaN en la columna 'vehicle year'
    df_clean = df_clean.dropna(subset=['vehicle year'])
    # Filtrar vehículos por año entre 1980 y 2024
    df_clean = df_clean[df_clean['vehicle year'].between(1980, 2024)]
    return df_clean

# Aplicar limpieza de datos
crash_clean_df = limpiar_datos(crash_df)

print("4.- Imprimimos todas las columnas")
print(crash_df.columns.sort_values())
print("\n")
print("Para seguir pulsa enter")
input()

print("5.- Imprimimos las filas")
print(crash_df.index.values)
print("\n")
print("Para seguir pulsa enter")
input()

print("6.- Imprimimos de la columna route type ordenamos")
conteo_tipos_ruta = crash_df['route type'].value_counts().sort_values(ascending=False)

print(conteo_tipos_ruta)
print("\n")
print("Para seguir pulsa enter")
input()

print("7.- Imprimimos de la columna road name ordenamos")
conteo_carreteras = crash_df['road name'].value_counts().sort_values(ascending=False)

print(conteo_carreteras)
print("\n")
print("Para seguir pulsa enter")
input()

print("8.- Imprimimos una función que saca los valores más recurrentes de la columna que queremos")
def contar_valores():
    """
    Esta función permite al usuario contar los valores únicos de una columna específica en el DataFrame crash_df.
    """
    while True:
        print("Algunos ejemplos: collision type, speed limit, vehicle make")
        columna = str(input("Dame la columna (o escribe 'salir' para finalizar): ")).lower()
        
        if columna == 'salir':
            break
        
        if columna not in crash_df.columns:
            print("¡La columna ingresada no existe en el DataFrame!")
            continue
        
        valores = crash_df[columna].value_counts().sort_values(ascending=False)
        print(valores)
        
contar_valores()
print("\n")
print("Para seguir pulsa enter")
input()

def analisis_exploratorio(df):

    # Análisis de las marcas más comunes en accidentes
    top_marcas = df['vehicle make'].value_counts().head(30).index
    df_top_marcas = df[df['vehicle make'].isin(top_marcas)]
    
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df_top_marcas, y='vehicle make', order=top_marcas, palette='viridis')
    plt.title('Top 10 Marcas con Más Accidentes')
    plt.show()
    
    # Distribución de accidentes por año del vehículo
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='vehicle year', palette='viridis')
    plt.title('Distribución de Accidentes por Año de Vehículo')
    plt.xticks(rotation=90)
    plt.show()
    
    # Distribución de accidentes por condiciones climáticas
    plt.figure(figsize=(10, 6))
    sns.countplot(y='weather', data=crash_df, palette='viridis')
    plt.xlabel('Frecuencia')
    plt.ylabel('Condiciones Climáticas')
    plt.title('Distribución de Accidentes por Condiciones Climáticas')
    plt.tight_layout()
    plt.show()
    
    # Distribución de accidentes a lo largo del tiempo
    plt.figure(figsize=(12, 6))
    crash_df['crash date/time'] = pd.to_datetime(crash_df['crash date/time'])
    crash_df['date'] = crash_df['crash date/time'].dt.date
    crash_df['date'].value_counts().sort_index().plot()
    plt.title('Distribución de Accidentes a lo largo del Tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Número de Accidentes')
    plt.grid(True)
    plt.show()
    
    # Análisis de frecuencia: Frecuencia de diferentes tipos de colisión
    plt.figure(figsize=(10, 6))
    sns.countplot(data=crash_df, x='collision type', palette='viridis', order=crash_df['collision type'].value_counts().index)
    plt.title('Frecuencia de Diferentes Tipos de Colisión')
    plt.xlabel('Tipo de Colisión')
    plt.ylabel('Número de Accidentes')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
        
    crash_df['crash_datetime'] = pd.to_datetime(crash_df['crash date/time'])

    # Extraer la hora del día de la columna de fecha y hora
    crash_df['hour'] = crash_df['crash_datetime'].dt.hour

    # Gráfico de distribución de accidentes por hora del día
    plt.figure(figsize=(10, 6))
    sns.histplot(data=crash_df, x='hour', bins=24, kde=True, color='skyblue')
    plt.xlabel('Hora del Día')
    plt.ylabel('Frecuencia de Accidentes')
    plt.title('Distribución de Accidentes por Hora del Día')
    plt.xticks(range(0, 24))
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()
    
    while True:
        # Distribución de accidentes por modelo de una marca específica
        marca = str(input("Dame la marca (o escribe 'salir' para finalizar): ")).upper().strip()
        
        if marca == 'SALIR':
            break
        
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

def corregir_marca(df):
    seguir = str(input("¿Quieres modificar algo?: "))
    if seguir.lower() == 'si':
        columna = input("Por favor ingresa el nombre de la columna que deseas modificar: ").strip().lower()
        valor_buscar = input(f"Por favor ingresa el valor que deseas buscar en la columna '{columna}': ").strip().upper()
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
    else:
        return

# Llama a la función para corregir la marca en tu DataFrame y guardar los cambios en el archivo CSV si el usuario lo desea
corregir_marca(crash_df)