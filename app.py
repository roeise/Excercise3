from flask import Flask, render_template, redirect, url_for, request, session, jsonify
app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def mainHome():
        return render_template('Home.html')



@app.route('/Home')
def home():
    customer_registrated = True ##For now, currently no entry restriction
    if customer_registrated:
        return redirect(url_for("assignment3_1"))
    else:
        return 'You have to log-In'

@app.route('/Contact_Us')
def about():
    return render_template('Contact_Us.html')


@app.route('/assignment3_1')
def assignment3_1():
    return render_template('assignment3_1.html', user={'firstname': "דן", 'lastname': "ישראלי", 'gender': "m"},
                            Details=['29', 'עמק חפר','ישראל'], newFeed='בקרוב באתר, הקרמשניט המפורסם של סבתא רוזליה')

@app.route('/assignment3_2', methods=['GET', 'POST'])
def assignment_9():
    return render_template('assignment3_2.html', parameters=request.args)



@app.route('/search')
def search_form():
    users = [
        {
            "id": 7,
            "email": "adam.levin@reqres.in",
            "first_name": "Adam",
            "last_name": "Levin",
            "avatar": "https://static01.nyt.com/images/2018/07/08/fashion/05LIST-INYT2/05LIST-INYT2-superJumbo.jpg?quality=75&auto=webp"
        },
        {
            "id": 8,
            "email": "gal.gadot@reqres.in",
            "first_name": "Gal",
            "last_name": "Gadot",
            "avatar": "https://media.todaybirthdays.com/1985/04/30/gal-gadot.jpg"
        },
        {
            "id": 9,
            "email": "billie.elish@reqres.in",
            "first_name": "Billie",
            "last_name": "Eilish",
            "avatar": "https://media.todaybirthdays.com/2021/03/03/billie-eilish.jpg"
        },
        {
            "id": 10,
            "email": "dana.international@reqres.in",
            "first_name": "Dana",
            "last_name": "Internatinal",
            "avatar": "https://images.maariv.co.il/image/upload/f_auto,fl_lossy/c_fill,g_faces:center,w_948/522954"
        },
        {
            "id": 11,
            "email": "naftali.benette@reqres.in",
            "first_name": "Naftali",
            "last_name": "Benette",
            "avatar": "https://www.gov.il/BlobFolder/roleholder/bennett/he/%D7%91%D7%A0%D7%982.jpg"
        },
        {
            "id": 12,
            "email": "liran.Hultza-Afora@reqres.in",
            "first_name": "Liran",
            "last_name": "Hultza-Afora",
            "avatar": "https://img.mako.co.il/2014/08/13/boker_keshet_130814_liran_i.jpg"
        }
    ]
    if 'searchinput' in request.args:
        search = request.args['searchinput']
    else:
        search = ""
    if search == "":
        return render_template('assignment3_2.html', search=users)
    flag = False
    for user in users:
        if user['first_name'] == search or user['email'] == search:
            flag = True
            return render_template('assignment3_2.html', searchIsfound=user)
    if not flag:
        return render_template('assignment3_2.html', searchNotfound="Item not found!")


@app.route('/register', methods=['POST'])
def register_form():
    if 'username' in request.form:
        user_name = request.form['username']
        user_pass = request.form['password']
        user_email = request.form['email']
        user_nickname = request.form['nickname']
    else:
        user_name, user_pass, user_email, user_nickname = '', '', '', ''
    session['username'] = user_name
    session['password'] = user_pass
    session['email'] = user_email
    session['nickname'] = user_nickname
    return render_template('assignment3_2.html', user_name=user_name, user_pass=user_pass, user_email=user_email,
                           user_nickname=user_nickname)


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
        session.pop('password', None)
        session.pop('email', None)
        session.pop('nickname', None)
        return render_template('header.html')






app.config['SESSION_TYPE'] = 'filesystem'



if __name__ == "__main__":
    app.run()
