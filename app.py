from flask import Flask, render_template
import time
app = Flask(__name__)

print( 'in flask app')


@app.route('/')
def hello():
    print("homepage should be loaded")
    data = [["Reddit", "Astrophysicist", "Redditor"], ["Google", "Googler", "Programmer"]]
    return render_template("webpage.html", data=data)

# # time.sleep(1800)
# app.run(port=8000, debug=True)
# # if __name__ == '__main__':
# #     create_app().run(debug=True)

# if __name__ != "__main__":
#     app.run()