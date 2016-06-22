#coding:utf-8
from flask import Flask,render_template,request,make_response,redirect,flash,get_flashed_messages
import logging
from logging.handlers import RotatingFileHandler

app=Flask(__name__) #define app
app.jinja_env.line_statement_prefix='#'
app.secret_key='songying'

@app.route('/index/')
@app.route('/') #address
def index():
    res=''
    for msg,category in get_flashed_messages(with_categories=True):
        res=res+category+msg+'<br>'
    res+='hello'
    return res #shouye

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
'''
@app.route('/admin')
def admin():
    key=request.args.get('key')
    if request.args['key'] == 'admin':
        return 'hello admin'
    else:
        raise ValueError()
    return 'xx'
'''
@app.route('/login')
def login():
    app.logger.info('log success')
    flash('登录成功','info')
    return 'ok'
    #return redirect('/')

@app.route('/log/<level>/<msg>/')
def log(level,msg):
    dict={'warn': logging.WARN,'error':logging.ERROR,'info':logging.INFO}
    if dict.has_key(level):
        app.logger.log(dict[level],msg)
    return 'logged:'+msg

def set_logger():
    info_file_handler=RotatingFileHandler('D:\\logs\\info.txt')
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)

    warn_file_handler=RotatingFileHandler('D:\\logs\\warn.txt')
    warn_file_handler.setLevel(logging.WARN)
    app.logger.addHandler(warn_file_handler)

    error_file_handler = RotatingFileHandler('D:\\logs\\error.txt')
    error_file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_handler)

if __name__=='__main__':
    set_logger()
    app.run(debug=True)