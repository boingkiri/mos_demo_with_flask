from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    data={
            'level': 60,
            'point': 360,
            'exp': 45000
        }
    if request.method == "POST":
        user = request.form.get('user')
        A = request.form.get('A')
        B = request.form.get('B')
        print(user)
        print(A)
        print(B)
        with open('tmp.txt','w') as f:
            if A == 'on':
                f.writelines('A\n')
            elif B == 'on':
                f.writelines('B\n')
            else:
                f.writelines('None\n')
    elif request.method == 'GET':
        print('GETGET')
        user = "반원웡원"
    return render_template(
        'index.html',
        user=user,
        data=data
    )

if __name__=="__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
        )