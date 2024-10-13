from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process form data
        name = request.form.get('name')
        age = request.form.get('age')
        
        # Simple validation
        if not name or not age:
            return render_template('index.html', error="Please fill out all fields.")
        
        try:
            age = int(age)
        except ValueError:
            return render_template('index.html', error="Age must be a number.")
        
        # Process data (for this example, we'll just return it)
        result = f"Hello, {name}! You are {age} years old."
        return render_template('index.html', result=result)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)