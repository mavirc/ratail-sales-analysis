#Funcion para ver los tipos de datos por columna
def data_type():
    type = []
    for columns in df.columns:
        type.append((columns, df[columns].dtype))
    print("The type of data is:")
    for column, dtype in type:
        print(f"{column}: {dtype}")
