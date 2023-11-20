import sqlite3

# Verbindung zur Datenbank herstellen oder erstellen, wenn sie nicht existiert
conn = sqlite3.connect('meine_datenbank.db')

# Ein Cursor-Objekt erstellen, um SQL-Abfragen auszuführen
cursor = conn.cursor()

# Daten für den neuen Spieler
overall_stat = 85
position = 'Stürmer'
name = 'Lionel Messi'
pac = 90
sho = 92
pas = 86
dri = 95
def_value = 32
phy = 59
country = 'Argentinien'
card_type = 'Keine Karte'

# SQL-INSERT-Abfrage ausführen, um den Spieler hinzuzufügen
cursor.execute("INSERT INTO Fussballspieler (overall_stat, position, name, pac, sho, pas, dri, def, phy, country, card_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
               (overall_stat, position, name, pac, sho, pas, dri, def_value, phy, country, card_type))

# Änderungen in der Datenbank speichern
conn.commit()

# Verbindung schließen
conn.close()
