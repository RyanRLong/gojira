import sqlite3


class Gateway:

    def __init__(self):
        self.conn = sqlite3.connect('example.db')
        self.cursor = self.conn.cursor()
        self.create_schema()

    def __del__(self):
        self.conn.close()

    def table_exists(self, table_name):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = ?", (table_name,))
        return self.cursor.fetchone() is not None

    def create_schema(self):
        # Create table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS commands (
        name TEXT PRIMARY_KEY NOT NULL UNIQUE, 
        type_id INTEGER NOT NULL, 
        instruction TEXT NOT NULL,
        times_used INTEGER NOT NULL, 
        created TEXT NOT NULL, 
        updated TEXT NOT NULL)
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS `types` ( 
        `id` INTEGER PRIMARY KEY AUTOINCREMENT, 
        `name` TEXT NOT NULL UNIQUE )
        ''')
        self.conn.commit()

    def insert(self, name, type_id, instruction, times_used, created):
        self.cursor.execute(
            "INSERT INTO commands (name, type_id, instruction, times_used, created, updated) VALUES (?,?,?,?,?,datetime('now'))",
            (name, type_id, instruction, times_used, created,))
        self.conn.commit()

    def getCommand(self, name):
        self.cursor.execute('''
        SELECT commands.name, types.name, commands.instruction, commands.times_used, commands.created, commands.updated
        FROM commands
        JOIN types
        on commands.type_id = types.id
        WHERE commands.name = ?
        ''', (name,))
        return self.cursor.fetchone()



if __name__ == "__main__":
    g = Gateway()
    g.create_schema()
    print(g.getCommand('Review'))
