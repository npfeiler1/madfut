CREATE TABLE Fussballspieler (
    id INTEGER PRIMARY KEY,
    overall_stat INTEGER,
    position TEXT,
    name TEXT,
    pac INTEGER,
    sho INTEGER,
    pas INTEGER,
    dri INTEGER,
    def INTEGER,
    phy INTEGER,
    country TEXT,
    liga TEXT,
    club TEXT,
    card_type TEXT
);

INSERT INTO Fussballspieler (overall_stat, position, name, pac, sho, pas, dri, def, phy, country, card_type)
VALUES (85, 'Stürmer', 'Lionel Messi', 90, 92, 86, 95, 32, 59, 'Argentinien', 'Keine Karte');
