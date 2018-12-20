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
        SELECT commands.name, commands.type_id, types.name, commands.instruction, commands.times_used, commands.created, commands.updated
        FROM commands
        JOIN types
        on commands.type_id = types.id
        WHERE commands.name = ?
        ''', (name,))
        return Command(*self.cursor.fetchone())


class Command:

    def __init__(self, name, type_id, type_name, instruction, times_used, created, updated):
        self.name = name
        self.type_id = type_id
        self.type_name = type_name
        self.instruction = instruction
        self.times_used = times_used,
        self.created = created
        self.updated = updated

    def __str__(self):
        return "{} {}->{}".format(self.name, self.type_name, self.instruction)


if __name__ == "__main__":
    g = Gateway()
    g.create_schema()
    print(g.getCommand('Review'))
