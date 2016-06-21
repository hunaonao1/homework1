from flask import Flask,render_template,request,make_response,redirect,flash,get_flashed_messages

app=Flask(__name__) #define app
app.jinja_env.line_statement_prefix='#'

@app.route('/index/')
@app.route('/') #address
def index():
    return 'hello'#shouye

@app.route('/profile/<int:uid>',methods=['GET','POST'])
def profile(uid):
    colors=('red','green')
    infos={'songying':'abc','google':'def'}
    return render_template('profile.html',uid=uid,colors=colors,infos=infos)


@app.route('/request')
def request_demo():
    key=request.args.get('key','defaultkey')
    res=request.args.get('key','defaultkey')+'<br>'
    res=res+request.url+'++'+request.path+'<br>'
    for property in dir(request):
        res = res + str(property) + '|==|<br>' + str(eval('request.' + property)) + '<br>'
    response=make_response(res)
    response.set_cookie('sonfyingid','key')
    response.status='404'
    response.headers['songying']='hello~~'
    return response

@app.route('/newpath')
def newpath():
    return 'newpath'

@app.route('/re/<int:code>')
def rediect_demo(code):
    return redirect('/newpath',code=code)

@app.errorhandler(404)
def page_not_found(error):
    print error
    return render_template('not_found.html',url=request.url),404

@app.route('/admin')
def admin():
    key=request.args.get('key')
    if request.args['key'] == 'admin':
        return 'hello admin'
    else:
        raise ValueError()
    return 'xx'

if __name__=='__main__':
    app.run(debug=True)