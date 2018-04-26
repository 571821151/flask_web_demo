from flask_wtf import FlaskForm
from wtforms import StringField,HiddenField,SubmitField
class BaseForm(FlaskForm):
  id = HiddenField()

class BulletinForm(BaseForm):
  author = StringField("作者")
  submit=SubmitField("提交")
