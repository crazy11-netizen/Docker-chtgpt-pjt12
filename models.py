from flask_mysqldb import MySQL

mysql = MySQL()


def init_app(app):
    mysql.init_app(app)


def get_all_products():
    cursor = mysql.connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            category,
            price,
            quantity
        FROM products
        ORDER BY id
    """)

    products = cursor.fetchall()
    cursor.close()

    return products


def add_product(name, category, price, quantity):
    cursor = mysql.connection.cursor()

    cursor.execute(
        """
        INSERT INTO products
        (name, category, price, quantity)
        VALUES (%s, %s, %s, %s)
        """,
        (name, category, price, quantity)
    )

    # Required for write/insert operations!
    mysql.connection.commit()
    cursor.close()


def get_product(product_id):

    cursor = mysql.connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            name,
            category,
            price,
            quantity
        FROM products
        WHERE id=%s
        """,
        (product_id,)
    )

    product = cursor.fetchone()

    cursor.close()

    return product


def update_product(product_id,
                   name,
                   category,
                   price,
                   quantity):

    cursor = mysql.connection.cursor()

    cursor.execute(
        """
        UPDATE products
        SET
            name=%s,
            category=%s,
            price=%s,
            quantity=%s
        WHERE id=%s
        """,
        (
            name,
            category,
            price,
            quantity,
            product_id
        )
    )

    mysql.connection.commit()

    cursor.close()


def delete_product(product_id):

    cursor = mysql.connection.cursor()

    cursor.execute(
        """
        DELETE FROM products
        WHERE id=%s
        """,
        (product_id,)
    )

    mysql.connection.commit()

    cursor.close()
