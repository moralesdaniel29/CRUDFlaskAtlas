from pymongo import MongoClient
import certifi

MONGO_URI = "mongodb+srv://danielmorales:calamardo_29@cluster0.fzhbw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["nombre_de_tu_base_de_datos"]
        return db
    except Exception as e:
        print(f"Error de conexión con la base de datos: {e}")
        return None
