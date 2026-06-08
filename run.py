
from src.app import create_app

# Esto busca un archivo llamado .env en la raíz y carga sus variables
from dotenv import load_dotenv
load_dotenv() 

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
