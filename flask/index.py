from flask import Flask,request,render_template,flash,redirect,url_for
from Forms.login_form import LoginForm
from Forms.name import BulletinForm
from flask_bootstrap import Bootstrap

app=Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = '123456'


@app.route('/')
@app.route('/search/<keyword>')
def index(keyword=""):
    if  keyword=='':
        return render_template('index.html')
    else:
        return redirect('user')

@app.route('/user')
def user():
   return render_template('user.html',name='cly')

@app.route('/test')
def test():
    form = BulletinForm(request.form)
    return render_template("test.html", form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
@app.errorhandler(500)
def internal_server_error(e):
    return  "500"

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method =="GET":
        form = LoginForm()
        return render_template("login.html",form=form)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate():
            print("用户提交的数据用过格式验证，值为：%s"%form.data)
            return "登录成功"
        else:
            print(form.errors,"错误信息")
        return render_template("login.html",form=form)

@app.route('/find',methods=['post'])
def get():
    print(request.form['sb'])
    return 'shabijiusni%s'% request.form['sb']

if  __name__=='__main__':
    app.run(debug=True)
