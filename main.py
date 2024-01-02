from flask import Flask, render_template, request, redirect
import hashlib

app = Flask(__name__)

url_store = {}

def shorten_url(url):
    hash_object = hashlib.sha256(url.encode())
    hash_hex = hash_object.hexdigest()[:8]  # Taking first 8 characters of hash
    return hash_hex

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    if request.method == 'POST':
        url = request.form['url']
        short_url = shorten_url(url)
        url_store[short_url] = url
        return render_template('shortened.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    if short_code in url_store:
        return redirect(url_store[short_code])
    return "URL not found."

if __name__ == '__main__':
    app.run(debug=True)
