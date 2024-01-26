from node_modules import flask, render_template;

app = flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask app on https://192.168.12.140:5000
    app.run(debug=True, host='https://fuzzy-acorn-w695wgp9qvj255wr-5000.app.github.dev/', port=5000, ssl_context='adhoc')
