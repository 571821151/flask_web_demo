from wtforms import Form
#新版本的flask中都会提示现在这种import方法已经过时，最新的import应该是from flask_wtf import Form
from wtforms import StringField,BooleanField,HiddenField,TextAreaField,DateTimeField
from wtforms.validators import Required

class BaseForm(Form):
  id = HiddenField()

class BulletinForm(BaseForm):
  author = StringField("作者")
