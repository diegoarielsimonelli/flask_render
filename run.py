from src.app import create_app  # <-- Asegúrate de que tenga el "src." adelante

from dotenv import load_dotenv
load_dotenv() 

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
