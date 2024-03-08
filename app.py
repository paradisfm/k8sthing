from flask import Flask, render_template, request, redirect

app = Flask(__name__)

items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    items.append(name)
    return redirect('/')

@app.route('/update', methods=['POST'])
def update():
    old = request.form['old']
    new = request.form['new']
    if old in items:
        index = items.index(old)
        items[index] = new
    else:
        items.append[old]
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    name = request.form('name')
    if name in items:
        items.remove(name)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)