
from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields import StringField,SubmitField


from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
app.config['SECRET_KEY']='mclkjllcjvlblcvjbljcvjb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///autl.db'
db = SQLAlchemy(app)



class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120),  nullable=False)
     
    def __str__(self):
        return self.title




class Form(FlaskForm):
    title=StringField('name',validators=[DataRequired()])
    desc=StringField('desc',validators=[DataRequired()])
    submit=SubmitField('add')




@app.route('/',methods=['GET','POST'])
def home():
    form=Form()

    if form.validate_on_submit():
        title=form.title.data
        desc=form.desc.data
        todo=Todo(title=title,description=desc)

        db.session.add(todo)
        db.session.commit()

        form.title.data=''
        form.desc.data=''
        
    allTodo=Todo.query.all()




    return render_template('index.html',form=form,allTodo=allTodo)



if __name__=='__main__':
     app.run(debug=True,port=8000)


