from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/hurin', methods=['GET', 'POST'])
def calculate_hurin():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        c = request.form['c']
        d = request.form['d']
        e = request.form['e']

        result = 0

        if a == 'yes':
            result += 20
        if b == 'yes':
            result += 20
        if c == 'yes':
            result += 20
        if d == 'yes':
            result += 20
        if e == 'yes':
            result += 20

        return render_template('result.html', result=result)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
