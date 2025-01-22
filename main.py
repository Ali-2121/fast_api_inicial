from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return("Bienvenido/a","Hola personas de JS")

@app.get("/calculaEdad")
async def calcular_edad(nacimiento, actual):
    edad : int = actual - nacimiento
    return edad
print("Tu edad es: ", calcular_edad(2000,2025))