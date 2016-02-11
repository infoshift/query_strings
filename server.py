from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/resource')
def api_resource():
    # Set a value to a specific key in the query string.
    # ?key=value
    key = request.args.get('key')

    # Set a list of values to a specific key in the query
    # string. You can retrieve this using a specific. 
    # ?list[]=1&list[]=2
    list_ = request.args.getlist('list[]')

    # Set a boolean value to a specific key in the query
    # string.
    # ?boolean  # True
    boolean = 'boolean' in request.args

    return jsonify({
        'key': key,
        'list': list_,
        'boolean': boolean,
    })
