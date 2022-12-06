from flask import render_template
import connexion

app = connexion.FlaskApp(__name__, specification_dir='./')
app.add_api('swagger.yml')

@app.route('/')
def index():
    return render_template('index.html')

app.run(port=8080, debug=True)