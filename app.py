from flask import Flask, render_template, jsonify, request
import subprocess
import time
import json
import platform
from test_scripts.python import chudnovsky_algorithm

app = Flask(__name__)

# Function to get Python version
def get_python_version():
    result = subprocess.run(['python', '--version'], capture_output=True, text=True)
    return result.stdout.strip()

# Function to get Java version
def get_java_version():
    result = subprocess.run(['java', '-version'], capture_output=True, text=True)
    return result.stderr.splitlines()[0].strip()

# Function to get Node.js (JavaScript) version
def get_js_version():
    result = subprocess.run(['node', '--version'], capture_output=True, text=True)
    return result.stdout.strip()

# Function to run Python Pi test
def run_python_test():
    start_time = time.time()
    for _ in range(100):
        # Call the optimized Pi function
        pi = chudnovsky_algorithm(1000)  # Number of iterations for accuracy
    end_time = time.time()
    return end_time - start_time

# Function to run Java Pi test
def run_java_test():
    start_time = time.time()
    # Run the Java Pi calculation
    result = subprocess.run(['java', 'PiCalculation'], capture_output=True, text=True)
    end_time = time.time()
    return end_time - start_time

# Function to run JavaScript Pi test
def run_js_test():
    start_time = time.time()
    # Run the JS Pi calculation
    result = subprocess.run(['node', 'test_scripts/js_test.js'], capture_output=True, text=True)
    end_time = time.time()
    return end_time - start_time

# Function to collect system information
def get_system_info():
    return {
        'System': platform.system(),
        'Platform': platform.platform(),
        'Processor': platform.processor()
    }

# Function to load results from JSON file dynamically
def load_results():
    try:
        with open('results.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'languages': {}}  # Initialize an empty structure if file does not exist

# Function to save results to a JSON file dynamically
def save_results(results):
    with open('results.json', 'w') as file:
        json.dump(results, file, indent=4)

def run_tests():
    # Test execution times
    python_time = run_python_test()
    java_time = run_java_test()
    js_time = run_js_test()

    print("asd")
    print(python_time)

    # Collect versions and system info
    system_info = get_system_info()

    # Load existing results (or initialize if not available)
    results = load_results()

    # Add new data under 'languages'
    results['languages'].update({
        'python': {
            'version': get_python_version(),
            'time': python_time
        },
        'java': {
            'version': get_java_version(),
            'time': java_time
        },
        'javascript': {
            'version': get_js_version(),
            'time': js_time
        }
    })

    # Save the updated results
    save_results(results)

# Route to display the results (and update dynamically)
@app.route('/')
def index():
    results = load_results()  # Dynamically load results from JSON
    # Render the results on the page
    return render_template('index.html', results=results)

# Route to handle test execution
@app.route('/run_tests', methods=['POST'])
def run_tests_route():
    run_tests()
    return "Tests executed and results saved", 200

if __name__ == '__main__':
    app.run(debug=True)
