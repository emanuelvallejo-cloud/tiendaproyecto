mport certifi
from pymongo import MongoClient

# 1. Reemplaza con tu cadena de conexión real de MongoDB Atlas
MONGO_URI = "mongodb+srv://cesarvallejo:FuckMuslimsHateArabia_000.l.@cluster0.diubi7k.mongodb.net/?appName=Cluster0"

try:
    # Conectar a MongoDB Atlas (usando certifi para evitar errores de SSL)
    client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())

    # Crear/Seleccionar la base de datos y la colección
    db = client["mi_tienda"]
    collection = db["tienda"]

    # Datos de los productos a insertar
    productos_iniciales = [
        {
            "nombre": "Laptop Gamer",
            "precio": 1200.50,
            "stock": 15,
            "proveedor": {
                "nombre": "TechDistribuidores S.A.",
                "contacto": "proveedor1@tech.com",
            },
            "categoria": "Electrónica",
        },
        {
            "nombre": "Teclado Mecánico RGB",
            "precio": 85.00,
            "stock": 40,
            "proveedor": {
                "nombre": "Accesorios Globales",
                "contacto": "ventas@accglobal.com",
            },
            "categoria": "Periféricos",
        },
        {
            "nombre": "Monitor 4K 27''",
            "precio": 350.00,
            "stock": 8,
            "proveedor": {
                "nombre": "TechDistribuidores S.A.",
                "contacto": "proveedor1@tech.com",
            },
            "categoria": "Electrónica",
        },
    ]

    # Limpiar la colección existente (opcional, por si re-ejecutas) y meter los nuevos
    collection.delete_many({})
    resultado = collection.insert_many(productos_iniciales)

    print(
        f"¡Éxito! Se insertaron {len(resultado.inserted_ids)} productos en la base de datos."
    )

except Exception as e:
    print(f"Hubo un error al conectar o insertar: {e}")
