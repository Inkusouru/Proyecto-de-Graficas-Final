import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def generar_graficas():
    graficas = []
    
    # 1. Grafica de Lineas para venta de dulces
    data_dulces = {'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'], 
                   'Ventas': [1500, 1800, 1700, 2000, 1900]}
    df_dulces = pd.DataFrame(data_dulces)
    plt.figure()
    df_dulces.plot(x='Mes', y='Ventas', kind='line', title='Venta de Dulces')
    plt.xlabel('Mes')
    plt.ylabel('Ventas ($)')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graficas.append(base64.b64encode(buffer.getvalue()).decode('utf-8'))
    buffer.close()
    plt.close()
    
    # 2. Grafica de Barras para venta de consumibles
    data_consumibles = {'Producto': ['Café', 'Té', 'Snacks', 'Refrescos'], 
                        'Ventas': [3000, 2500, 4000, 3500]}
    df_consumibles = pd.DataFrame(data_consumibles)
    plt.figure()
    df_consumibles.plot(x='Producto', y='Ventas', kind='bar', title='Venta de Consumibles')
    plt.xlabel('Producto')
    plt.ylabel('Ventas ($)')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graficas.append(base64.b64encode(buffer.getvalue()).decode('utf-8'))
    buffer.close()
    plt.close()
    
    # 3. Grafica de Dispersion de perdidas aproximadas
    data_perdidas = {'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'], 
                     'Pérdidas': [200, 250, 300, 350, 400]}
    df_perdidas = pd.DataFrame(data_perdidas)
    plt.figure()
    df_perdidas.plot(x='Mes', y='Pérdidas', kind='scatter', title='Pérdidas Aproximadas')
    plt.xlabel('Mes')
    plt.ylabel('Pérdidas ($)')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graficas.append(base64.b64encode(buffer.getvalue()).decode('utf-8'))
    buffer.close()
    plt.close()
    
    # 4. Grafica de Pastel de productos con mas ventas
    data_productos = {'Producto': ['Dulces', 'Snacks', 'Refrescos', 'Café'], 
                      'Ventas': [2500, 4000, 3500, 3000]}
    df_productos = pd.DataFrame(data_productos)
    plt.figure()
    df_productos.set_index('Producto').plot(kind='pie', y='Ventas', autopct='%1.1f%%', title='Productos con Mas Ventas')
    plt.ylabel('')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graficas.append(base64.b64encode(buffer.getvalue()).decode('utf-8'))
    buffer.close()
    plt.close()
    
    # 5. Histograma de ventas a largo plazo
    data_largo_plazo = {'Ventas': [300, 400, 450, 500, 550, 600, 700, 800, 850, 900]}
    df_largo_plazo = pd.DataFrame(data_largo_plazo)
    plt.figure()
    df_largo_plazo['Ventas'].plot(kind='hist', title='Ventas a Largo Plazo', bins=5)
    plt.xlabel('Rango de Ventas ($)')
    plt.ylabel('Frecuencia')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graficas.append(base64.b64encode(buffer.getvalue()).decode('utf-8'))
    buffer.close()
    plt.close()

    # 6. Gráfica de Cajas de ventas mediano plazo (no estoy seguro si este tipo de grafica se usa para esto jaja)
    data_mediano_plazo = {
        'Ventas': [500, 520, 540, 600, 610, 620, 580, 570, 560, 550]
    }
    df_mediano_plazo = pd.DataFrame(data_mediano_plazo)
    plt.figure()
    df_mediano_plazo.boxplot(column=['Ventas'])
    plt.title('Ventas a Mediano Plazo')
    plt.ylabel('Ventas ($)')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graficas.append(base64.b64encode(buffer.getvalue()).decode('utf-8'))
    buffer.close()
    plt.close()
    
    return graficas
