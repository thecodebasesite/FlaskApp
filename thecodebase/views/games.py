

import json
from datetime import datetime

from flask import session
from flask import render_template
from flask import request
from flask import Blueprint


from thecodebase.content import Games
from thecodebase.lib.dbconnect import Cursor
from thecodebase.lib.wrappers import mobile_not_supported, login_required

GAMES_DICT = Games()

games = Blueprint('games', __name__, template_folder='templates')

@games.route('/post-score', methods=['POST'])
def post_score():
    score = request.form['score']
    select_sql = """
    SELECT username, score, time FROM Score
    JOIN users ON users.uid = Score.uid
    ORDER BY score DESC, time DESC
    """
    with Cursor() as cur:
        cur.execute("INSERT INTO Score (score, uid, time) VALUES (%s, %s, %s)", 
            (score, session.get('uid'), datetime.now(),)
        )
        cur.execute(select_sql)
        data = cur.fetchmany(10)

    data_list = []
    for line in data:
        username, score, date = line
        data_list.append([username.replace('ä', 'a').replace('ö', 'o'), score, str(date)])

    return json.dumps(data_list)


@games.route('/games/')
def games_view():
    kwargs = dict(
        game=True,
        bg='gaming_header.jpg',
        GAMES_DICT=GAMES_DICT,
        page_title='Games'
    )
    return render_template("games.html", **kwargs)

def create_game(game, resources):
    kwargs = dict(
         game=True,
         bg='gaming_header.jpg',
         page_title=game.title,
         folder=game.url,
         resources=resources
    )
    games.route('/games/{}/'.format(game.url), endpoint=game.url)(
        mobile_not_supported(
                login_required(
                    lambda: render_template('phaser-game.html', **kwargs)
                )
            )
        )

for game, resources in GAMES_DICT.items():
    create_game(game, resources)