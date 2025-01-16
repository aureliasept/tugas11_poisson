from flask import Flask, render_template, request
from scipy.stats import poisson

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Ambil input dari form
            lambda_rate = float(request.form['lambda'])
            max_k = int(request.form['max_k'])

            # Hitung probabilitas untuk setiap k dari 0 hingga max_k
            probabilities = []
            for k in range(max_k + 1):
                prob = poisson.pmf(k, lambda_rate)
                probabilities.append({
                    'k': k,
                    'prob': prob,
                    'percentage': prob * 100
                })

            # Siapkan hasil untuk ditampilkan
            result = {
                'lambda_rate': lambda_rate,
                'max_k': max_k,
                'probabilities': probabilities
            }
        except Exception as e:
            result = {'error': str(e)}

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
