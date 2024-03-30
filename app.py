from flask import Flask, render_template

# 實例：Instance
app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/about')
def about():
        return render_template('about.html')

@app.route('/admin/dashboard')
def admin_dashboard():
        return render_template('admin/dashboard.html')

if __name__ == '__main__':
    app.run()