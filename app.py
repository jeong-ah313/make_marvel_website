from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

##
@app.route('/movie')
def movie():
    return render_template('movie.html')

@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/character')
def character():
    return render_template('character.html')

@app.route('/worldview')
def worldview():
    return render_template('worldview.html')


# templates/character.html
# templates/pages/Avengers.html
#
@app.route('/pages/Avengers')
def Avengers():
    return render_template('/pages/Avengers.html')
#
@app.route('/pages/Others')
def Others():
    return render_template('/pages/Others.html')
#
@app.route('/pages/poster')
def poster():
    return render_template('/pages/poster.html')
#
@app.route('/pages/text')
def text():
    return render_template('/pages/text.html')

## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    name_receive = request.form['name_give']
    movie_receive = request.form['movie_give']
    review_receive = request.form['review_give']

    doc = {
        'name': name_receive,
        'movie': movie_receive,
        'review': review_receive
    }

    db.moviereview.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})


@app.route('/review', methods=['GET'])
def read_reviews():
    reviews = list(db.moviereview.find({}, {'_id': False}))
    return jsonify({'all_reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)