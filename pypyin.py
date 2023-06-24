from flask import Flask, request, render_template
import subprocess
import os,time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    print ("got it")

    start_time = time.time()

    # Run your command here.

    
    if request.method == 'POST':
        prompt = request.form.get('prompt', 'default_prompt')
        pyfile = request.form.get('pyfile', 'default_pyfile')

        with open(prompt, 'w') as f:
            f.write(request.form.get('prompt_text', ''))
        
        with open(pyfile, 'w') as f:
            f.write(request.form.get('pyfile_text', ''))

        cmd = ["/usr/local/bin/bito", "-p", prompt, "-f", pyfile]

        with open('out.txt', 'w') as f:
            subprocess.run(cmd, stdout=f)

        with open('out.txt', 'r') as f:
            output = f.read()

        end_time = time.time()
        total_time = end_time - start_time

        return render_template('home.html', output=output,total_time=total_time)

    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='localhost',port=6000)
