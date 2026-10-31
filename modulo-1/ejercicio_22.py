

def stock_desde_archivo(nombre_arvhivo):
    
    try:
        with open(nombre_arvhivo) as f:
            count = {}
            
            for linea in f:
                linea = linea.strip()
                producto, cantidad = linea.split(",")
                cantidad = int(cantidad)
                
                if producto in count:
                    count[producto] += cantidad
                else:
                    count[producto] = cantidad
                    
            return count
    except FileNotFoundError:
        print(f"archivo no encontrado: {nombre_archivo}")
        return None
    
    
print(stock_desde_archivo("archivos-txt/inventario.txt"))
                