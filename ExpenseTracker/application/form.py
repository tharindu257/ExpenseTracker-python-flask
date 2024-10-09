from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class UserDataForm(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                                choices=[('income', 'income'),
                                        ('expense', 'expense')])
    category = SelectField("Category", validators=[DataRequired()],
                                            choices =[('Salary', 'Salary'),
                                            ('Rent', 'Rent'),
                                            ('Investment', 'Investment'),
                                            ('Side Bussiness', 'Side Bussiness'),
                                            ('Food', 'Food'),
                                            ('Cloths', 'Cloths'),
                                            ('Educations', 'Educations'),
                                            ('Other', 'Other')
                                            ]
                            )
    amount = IntegerField('Amount', validators = [DataRequired()])                                   
    submit = SubmitField('Generate Report')                            