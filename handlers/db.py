import sqlite3
from data.config import load_config
config = load_config("data/.env")

con = sqlite3.connect('data/db.db')
cur = con.cursor()


def db_users(user_id, username):

    cur.execute('''INSERT INTO users(id, username) VALUES(?, ?)''', (user_id, username,))
    try:
        con.commit()
    except: pass


def db_get_phrases():
    cur.execute('''SELECT * FROM "settings" WHERE key = ?''',('list',))
    while True:
        row = cur.fetchone()
        if row is None:
            break
        return row


def db_update_phrases(payload):
    cur.execute("""UPDATE "settings" SET value = ? WHERE key = ?""", (payload, 'list'))
    try:
        con.commit()
    except:
        pass

def db_get_users():
    cur.execute("""SELECT * FROM "users" """)
    while True:
        row = cur.fetchall()
        if row is None:
            break
        return row