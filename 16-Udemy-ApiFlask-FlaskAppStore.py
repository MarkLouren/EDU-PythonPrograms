from flask import Flask, jsonify, request, render_template
#jsonify convert dictionary into json string that will be used JS
#render_template - redering html template for the browser
app = Flask(__name__)

stores = [
    {
    'name': 'My Wonderful Sore',
    'items': [
          {
         'name': 'My Item',
          'price': 15.99
           }
         ]
     }
]

@app.route('/')
def home():
 return render_template('index.html')

#Don't forget to put index.html in the folder Templates
# POST - used to receive data
# GET - used to send data back only

#POST /store data: {name:}  # create new store
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()  # change json to dictionary
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>
@app.route('/store/<string:name>') # "htpps... /store/some_name
def get_store(name):
    # Iterate over stores # if the store name matches, return it
    # if none[match, return an error message
   for store in stores:
      if store['name'] == name:
        return jsonify(store)
   return jsonify({'message': 'store not found'})


#GET /store
@app.route('/store')
def get_stores():
   return jsonify({'stores':stores}) # convert list stores into dictionary, that jsonify uderstand


# POST /store/<string:name>/item {name:, price:} #create new item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_items_in_store(name):
    request_data=request.get_json()
    for store in stores:
        if store['name']== name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            stores['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': "Store not found"})


#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store ['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message': 'item not found'})



app.run(port=3001)


###########################################################
#### index.html in order to test own API draft ############
############################################################

<html>
<head>
<script type="text/javascript">
	function httpGetAsync(theUrl, callback) {
	    var xmlHttp = new XMLHttpRequest();
	    xmlHttp.onreadystatechange = function() {
	        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
	            callback(xmlHttp.responseText);
	    }
	    xmlHttp.open("GET", theUrl, true); // true for asynchronous
	    xmlHttp.send(null);
	}
	httpGetAsync('http://127.0.0.1:3001/store', function (response){
	  alert (response);
	})
</script>
</head>
<body>

<div id="myElement">
	Hello, world!
</div>

</body>
</html>
