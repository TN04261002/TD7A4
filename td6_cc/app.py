from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	with open('/mnt/text_file.txt', 'r') as f:
		content = f.read()
	return content
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
