import sqlite3

def connectToDatabase():

    connection = sqlite3.connect("WordDatabase.db")
    cursor = connection.cursor()

    return (connection, cursor)

def commitAndClose(con):

    con.commit()
    con.close()

def createTable(cur):

    cur.execute('''CREATE TABLE words (
                        word_id integer NOT NULL UNIQUE,
                        surface text NOT NULL,
                        learning_state integer NOT NULL)
                        ''')

def insertToDb(cur, morpheme):

    w_id = morpheme.word_id()
    print(w_id)
    surface = morpheme.surface()
    learning_state = 0
    try:
        cur.execute(f"INSERT INTO words (word_id, surface, learning_state) VALUES ({w_id}, '{surface}', {learning_state})")
    except sqlite3.IntegrityError:
        pass

def updateLearningState(cur, morpheme, state):

    w_id = morpheme.word_id()
    cur.execute(f"UPDATE words SET learning_state={state} WHERE word_id={w_id}")