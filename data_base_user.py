import sqlite3

# -------------------------


def add_to_bd (user_id , guesses , all_user_info ):
        
    try :

        conn = sqlite3.connect("infobase.db")
        cursor = conn.cursor()
        print("ready setup")


        cursor.execute("INSERT OR IGNORE INTO `users` (`user_id` , `answers`, `all_user_info`) VALUES (?, ?, ?)", (user_id, guesses, all_user_info, ))

        users = cursor.execute("SELECT * FROM `users`")
        print(users.fetchall())
            
        conn.commit()

    # -------------------------


    except sqlite3.Error as error :
        print ('Errror: ', error)

    # -------------------------

    finally :
        if (conn):
            conn.close()