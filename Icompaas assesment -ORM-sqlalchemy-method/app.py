from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///icompaas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class InputData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_text = db.Column(db.String(255), nullable=False, unique=True)

def contains_sql_injection(input_string):
    #For defining a list of SQL injection characters
    sql_injection_patterns = ["'", '"', '=', ';', '--', 'UNION', 'SELECT', 'FROM', 'WHERE']

    #For checking if any SQL injection characters are present in the input string
    return any(pattern in input_string.upper() for pattern in sql_injection_patterns)

@app.route('/v1/sanitized/input/', methods=['POST'])
def check_sanitization():
    try:
        data = request.get_json()
        input_text = data.get('input', '')

        #For checking if the input is empty or contains only whitespace
        if not input_text.strip():
            return jsonify({'error': 'Empty input value'}), 400

        #For checking if the input contains any SQL injection characters
        if contains_sql_injection(input_text):
            result = {'result': 'unsanitized'}
        else:
            result = {'result': 'sanitized'}

        return jsonify(result)
    except Exception as e:
        app.logger.error(f"Error in check_sanitization route: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
