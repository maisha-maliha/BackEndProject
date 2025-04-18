from .mysql_connector import mysql_database_connection
from schemas import Article


@mysql_database_connection
def add_news(data: list[Article], database, cursor) -> bool:
    """saved the top 3 latest news into a database"""
    # Ensure table exists
    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS latest_news (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(500),
                description TEXT,
                url TEXT,
                published_at TEXT
            )
        """
        )

        # Insert top 3 articles
        insert_query = """
            INSERT INTO latest_news 
            (title, description, url, published_at)
            VALUES (%s, %s, %s, %s)
        """

        for article in data:
            cursor.execute(
                insert_query,
                (
                    article.title,
                    article.description,
                    str(article.url),
                    article.published_at,
                ),
            )

        database.commit()
    except Exception as err:
        return False

    return True
