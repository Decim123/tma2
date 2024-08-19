import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Выполняем команду для удаления всех записей из таблицы tasks
cursor.execute("DELETE FROM tasks")

# Сохраняем изменения
conn.commit()

# Закрываем соединение с базой данных
conn.close()

print("Содержимое таблицы tasks было успешно удалено.")
