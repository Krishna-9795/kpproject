from flask import Flask, request, jsonify

app = Flask(__name__)
#sadades
# a simple endpoint that returns a JSON response
app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

# an endpoint that accepts POST requests and returns a JSON response
app.route('/greet', methods=['POST'])
def greet():
    name = request.json.get('name')
    if name:
        return jsonify({'message': f'Hello, {name}!'})
    else:
        return jsonify({'error': 'Name parameter is missing.'}), 400

if __name__ == '__main__':
    app.run()