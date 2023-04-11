from flask import Flask, render_template, request
from flask import jsonify
app = Flask(__name__)

@app.route('/add_host', methods=['POST'])
def add_host():
    data = request.json  # parse the JSON data from the request
    
    space_name = data.get('spaceName')  # retrieve the values from the dictionary
    org_name = data.get('orgName')
    email = data.get('email')
    password = data.get('password')
    api_url = data.get('apiurl')
    print(data)
    # do something with the data, like add a host to a database or make an API request
    return 'Host added successfully'


@app.route('/', methods=['GET'])
def home():
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
