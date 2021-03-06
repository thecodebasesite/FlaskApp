from collections import namedtuple

Card = namedtuple('Card', ['title', 'url', 'image', 'description'])

def Projects():
    Project = namedtuple('Project', ['title', 'url', 'html_file', 'image'])
    
    python = Card(
        title='Python',
        url='python',
        image='python_logo.png',
        description="Python is my strongest language. It's the main language I've used professionally."
    )

    java = Card(
        title='Java',
        url='java',
        image='java_logo.png',
        description="I learned Java in University of Helsinki. I've also used it in my work at SprintIT.",
    )


    web_development = Card(
        title='Web Development',
        url='web-development',
        image='web-development.jpg',
        description="This website is an example of my skills with Flask and Bootstrap. I've also learned alot about deploying servers from my work at SprintIT.",
    )
    c_c_plus = Card(
        title='C/C++',
        url='C-C++',
        image='c++.png',
        description="I've studied the basics of C/C++. There's alot I'd like to do with C++ for example rewrite some of the games I've made with pygame.",
    )
    javascript = Card(
        title='JavaScript',
        url='javascript',
        image='javascript.png',
        description="I aspire to master JavaScript, since I've already encountered it in my work as an Odoo developer, but also in personal projects.",
    )

    return {
        python : [
            Project('Odoo', 'odoo', 'odoo.html', 'odoo.jpg'),
            Project('Tower Defence', 'TowerDefence', 'tdgame.html', 'tdgame.png'),
            Project('Bemarifield', 'Bemarifield', 'bemarifield.html', 'bemarifield.png'),
            Project('Physics 2D', 'Physics', 'physics.html', 'physics.gif'),

        ],
        java : [
            Project('Game Of Life', 'game-of-life', 'game-of-life.html', 'game-of-life.gif'),
            Project('Asteroids', 'asteroids', 'asteroids.html', 'asteroids.png'),
            Project('Tic Tac Toe', 'tic-tac-toe', 'tic-tac-toe.html', 'tic-tac-toe.png'),
            Project('Falling Sand', 'falling-sand', 'falling-sand.html', 'falling-sand.gif'),
        ],
        c_c_plus : [
            Project('C-practice', 'c-harjoitus', 'c-practice.html', 'c-practice.png'),
            Project('Python C-extension', 'c-extension', 'c-extension.html', 'c-extension.png'),
        ],
        javascript : [
            Project('Phaser.js', 'phaser-js', 'phaser.html', 'phaser_logo.png'),
            Project('jQuery', 'jquery', False, 'under_construction.png'),
            Project('React.js', 'react-js', False, 'under_construction.png'),
            Project('Node.js', 'node-js', False, 'under_construction.png'),
            Project('Bacon.js', 'bacon-js', False, 'under_construction.png'),
            
        ],
        web_development : [
            Project('The Codebase', 'thecodebase', 'thecodebase.html', 'server_combined.jpg'),
            Project('Django', 'django', False, 'under_construction.png'),
        ],
    }
    

def Games():

    platform = Card(
        title='Platform Game',
        url='platform-game',
        image='platform_game.png',
        description='Collect as many starts as you can, but beware of the bombs! See if you can get the highest score.'
    )
    eat = Card(
        title='Eat Game',
        url='eat-game',
        image='eat_game.png',
        description="Eat the baddies when they are vulnerable, but watch out when they're not!"
    )

    return {
        platform : ['config.js', 'Preloader.js', 'Leaderboard.js', 'GamePlay.js'],
        eat : ['config.js', 'eat-game.js']
    }
