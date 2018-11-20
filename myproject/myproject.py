from flask import Flask
from kinocheck.controllers import check

app = Flask(__name__)
app.register_blueprint(check.app)
if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
