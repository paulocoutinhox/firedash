from wtforms import Form, validators, IntegerField, FloatField


class DeviceDataOutByRandomForm(Form):
    amount = IntegerField('Amount', [validators.DataRequired()])

    datasets = IntegerField('Datasets', [validators.DataRequired()])

    min_value = FloatField('Minimum value', [validators.DataRequired()])

    max_value = FloatField('Maximum value', [validators.DataRequired()])
