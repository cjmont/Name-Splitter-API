from flask import Flask, request, jsonify
import nltk
from nltk.corpus import names

# Primero, descarguemos los nombres de nltk
# First, let's download the names from nltk
nltk.download('names')

# Crear un conjunto de todos los nombres conocidos por nltk
# Create an array of all names known to nltk
all_names = set(names.words())

app = Flask(__name__)

@app.route('/split_name', methods=['POST'])
def split_name_api():
    # obtiene datos de la solicitud POST 
    # get data from the POST request
    data = request.get_json()  
    fullname = data.get('fullname', '')

    parts = fullname.split()
    names = []
    surnames = []

    for part in parts:
        # Chequeamos en el conjunto de nombres para ver si una parte es un nombre conocido
        # Check the array of names to see if a part is a well-known name
        if part in all_names:
            names.append(part)
        # Si no es un nombre conocido, lo clasificamos como apellido  
        # If it's not a well-known name, classify it as last name
        else:  
            surnames.append(part)
            
    # Unimos los nombres y apellidos en strings separados
    # Join the first and last names into separate strings
    firstname = ' '.join(names)
    lastname = ' '.join(surnames)

    return jsonify({'firstname': firstname, 'lastname': lastname}), 200


if __name__ == '__main__':
    app.run(debug=True)
