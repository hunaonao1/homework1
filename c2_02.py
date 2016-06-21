from flask import Flask

app=Flask(__name__) #define app

@app.route('/index/')
@app.route('/') #address
def index():
    return 'hello'#shouye

@app.route('/profile/<int:uid>')
def profile(uid):
    return 'profile:'+str(uid)

if __name__=='__main__':
    app.run(debug=True)