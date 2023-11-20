import sqlite3


def addPlayer(overall_stat,position, name, pac, sho, pas, dri, def_value, phy, country, liga, club, card_type):
    conn = sqlite3.connect('spielerdaten.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Fussballspieler (overall_stat, position, name, pac, sho, pas, dri, def, phy, country, liga, club, card_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (overall_stat, position, name, pac, sho, pas, dri, def_value, phy, country, liga, club, card_type))
    conn.commit()
    conn.close()