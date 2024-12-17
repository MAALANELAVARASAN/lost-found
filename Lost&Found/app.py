from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
@app.route('/index')
def index():
    hobbies = ["Lost Keys", "Wallet", "Backpack", "Mobile Phone", "Documents"]  # Changed to lost/found items
    return render_template("index.html", hobbies=hobbies)

# About route
@app.route('/about')
def about():
    return render_template("about.html")

# Contact route
@app.route('/contact')
def contact():
    return render_template("contact.html")

# Others route
@app.route('/others')
def others():
    return render_template("others.html")

# Report route to handle GET and POST requests
@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        # Retrieve form data
        item_name = request.form['item_name']
        item_type = request.form['item_type']
        description = request.form['description']
        contact = request.form['contact']

        # Print form data to the console (or process/store as needed)
        print(f"Item Reported: {item_name}")
        print(f"Type: {item_type}")
        print(f"Description: {description}")
        print(f"Contact: {contact}")

        # After submission, redirect back to the home page or a thank-you page
        return redirect(url_for('index'))

    # Render a template for the report page
    return render_template("report.html")

if __name__ == '__main__':
    app.run(debug=True)
