from flask import Flask,redirect
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/aboutme')
def aboutme():
    return "TheQuyen WebDeveloper NoPet NoCrush"

@app.route('/school')
def school():
    return redirect('http://techkids.vn')
if __name__ == '__main__':
  app.run(debug=True)
