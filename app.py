from flask import Flask, render_template, request

app = Flask(__name__)

def mgdl_to_mmoll(mgdl_value):
    conversion_factor = 0.0555
    mmoll_value = mgdl_value * conversion_factor
    return mmoll_value

def mmoll_to_mgdl(mmoll_value):
    conversion_factor = 18.02
    mgdl_value = mmoll_value * conversion_factor
    return mgdl_value

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        input_value = float(request.form['input_value'].replace(',', '.'))  # Ersetze das Komma durch einen Punkt
        conversion_type = request.form['conversion_type']

        if conversion_type == 'mgdl_to_mmoll':
            result = f"{input_value} mg/dL entsprechen {mgdl_to_mmoll(input_value):,.2f} mmol/L."
        elif conversion_type == 'mmoll_to_mgdl':
            result = f"{input_value} mmol/L entsprechen {mmoll_to_mgdl(input_value):,.2f} mg/dL."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=80)
