from flask import Flask, redirect, url_for, request, render_template,flash


app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')


@app.route('/databases',methods=['GET','POST'])
def add_dbs():
    if request.method == 'POST':
        error = None
        name = request.form["name"]
        if not name:
            error = 'El nombre  de la base de datos es requerido'
        if error is None:
            db = NewDb(name)
            res = db.create_db()
            if res:
                return redirect(url_for('index'))

    ##flash(error)
    return render_template('databases.html')
@app.route('/databases/<int:id>',methods=['PUT','DELETE'])
def databases(id):
    pass
if __name__ == '__main__':
    app.run(debug=True)