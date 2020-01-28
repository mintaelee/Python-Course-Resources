from fask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hi there!"

def app.run(port=5000):