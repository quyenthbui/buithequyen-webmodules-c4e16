from flask import Flask, render_template
app = Flask(__name__)

users = {
    'quy': {    'Ten': 'Dinh Quy',
                'Tuoi': 30
            },
    'tuananh': {   'Ten':'Tuan Anh',
                    'Tuoi': 35
            },
    'hoa': {    'Ten': 'Hoa',
                'Tuoi': 26
    }
}

@app.route('/user/<username>')
def user(username):
    if username in users:
        return render_template('user.html', users=users[username])

    else:
        return 'No User Found'


if __name__ == '__main__':
  app.run(debug=True)
