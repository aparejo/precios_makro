import requests
import pandas as pd

url = "http://192.168.10.14/bgapi.php"
params = {
    "modulo": "INV",
    "funcion": "LISTA_DE_PRECIOS",
    "codigo_desde": "C00045000",
    "codigo_hasta": "C00050000"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    try:
        data = response.json()["items"]

        # Filtrar los valores decimales en el campo "EXIS_TOTAL"
        filtered_data = []
        for item in data:
            exis_total = item.get("EXIS_TOTAL")
            if exis_total and "." in exis_total:
                try:
                    exis_total_decimal = float(exis_total)
                    item["EXIS_TOTAL"] = exis_total_decimal
                    filtered_data.append(item)
                except ValueError:
                    pass

        # Crear un DataFrame de pandas con los datos filtrados
        df = pd.DataFrame(filtered_data)

        # Guardar los resultados en un archivo Excel
        df.to_excel("resultados.xlsx", index=False)
        print("Los resultados se han guardado en 'resultados.xlsx'.")
    except ValueError:
        print("La respuesta del API no es un JSON válido.")
else:
    print(f"Error al realizar la solicitud: {response.status_code}")