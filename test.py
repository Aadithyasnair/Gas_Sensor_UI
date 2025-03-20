from flask import Flask, jsonify, render_template

app = Flask(__name__)

def classify_gas_level(ppm):
    """Classify gas level based on PPM value"""
    if ppm <= 50:
        return 'Green'
    elif ppm <= 75:
        return 'Yellow'
    elif ppm <= 100:
        return 'Orange'
    else:
        return 'Red'

# Static gas data
GAS_DATA = [
    {'id': 1, 'address': '123 Main St Something', 'coordinates': [13.096318532366581, 77.61926944793747], 'ppm': 76},
    {'id': 2, 'address': '456 Oak St Elmwood', 'coordinates': [13.095318532366581, 77.61726944793747], 'ppm': 20},
    {'id': 3, 'address': '789 Pine St Downtown', 'coordinates': [13.089318532366581, 77.61226944793747], 'ppm': 70},
    {'id': 4, 'address': '321 Birch Rd Suburbia', 'coordinates': [13.082318532366581, 77.60526944793747], 'ppm': 62},
    {'id': 5, 'address': '101 Maple Ave Northpark', 'coordinates': [13.075318532366581, 77.59826944793747], 'ppm': 94},
    {'id': 6, 'address': '202 Cedar Dr Riverside', 'coordinates': [13.068318532366581, 77.59126944793747], 'ppm': 42},
    {'id': 7, 'address': '303 Elm St Midtown', 'coordinates': [13.061318532366581, 77.58426944793747], 'ppm': 55},
    {'id': 8, 'address': '404 Pine St Hillside', 'coordinates': [13.054318532366581, 77.57726944793747], 'ppm': 66},
    {'id': 9, 'address': '505 Oak St Greenfield', 'coordinates': [13.047318532366581, 77.57026944793747], 'ppm': 75},
    {'id': 10, 'address': '606 Maple Rd Lakeside', 'coordinates': [13.040318532366581, 77.56326944793747], 'ppm': 23},
    {'id': 11, 'address': '707 Birch St Hillcrest', 'coordinates': [13.033318532366581, 77.55626944793747], 'ppm': 77},
    {'id': 12, 'address': '808 Spruce St Westwood', 'coordinates': [13.026318532366581, 77.54926944793747], 'ppm': 88},
    {'id': 13, 'address': '909 Willow Ln Eastend', 'coordinates': [13.019318532366581, 77.54226944793747], 'ppm': 33},
    {'id': 14, 'address': '1010 Redwood Ct Sunnyvale', 'coordinates': [13.012318532366581, 77.53526944793747], 'ppm': 50},
    {'id': 15, 'address': '1111 Aspen Ave Oakwood', 'coordinates': [13.005318532366581, 77.52826944793747], 'ppm': 110},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/gas_data', methods=['GET'])
def get_gas_data():
    gas_data = [
        {
            'id': entry['id'],
            'coordinates': entry['coordinates'],
            'gasLevel': classify_gas_level(entry['ppm']),
            'ppm': entry['ppm'],
            'address': entry['address']
        }
        for entry in GAS_DATA
    ]
    return jsonify(gas_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
