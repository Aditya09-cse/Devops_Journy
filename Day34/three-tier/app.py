from flask import Flask
import mysql.connector
import redis
import random

app = Flask(__name__)

@app.route("/")
def home():
    # Connect to MySQL
    db = mysql.connector.connect(
        host="mysql-db-1",
        user="root",
        password="root123",
        database="testdb"
    )

    cursor = db.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id INT AUTO_INCREMENT PRIMARY KEY,
            count INT
        )
    """)
    db.commit()

    # Get visit count
    cursor.execute("SELECT count FROM visits WHERE id=1")
    result = cursor.fetchone()

    if result is None:
        cursor.execute("INSERT INTO visits (count) VALUES (1)")
        db.commit()
        visits = 1
    else:
        visits = result[0] + 1
        cursor.execute("UPDATE visits SET count=%s WHERE id=1", (visits,))
        db.commit()

    cursor.close()
    db.close()

    # Redis
    cache = redis.Redis(host="redis-1", port=6379)
    random_number = random.randint(1, 1000)
    cache.set("random", random_number)

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Three-Tier App</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}

            body {{
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #667eea, #764ba2);
            }}

            .card {{
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(15px);
                padding: 40px;
                border-radius: 20px;
                text-align: center;
                width: 90%;
                max-width: 500px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                color: white;
                animation: fadeIn 0.8s ease-in-out;
            }}

            h2 {{
                margin-bottom: 25px;
                font-size: 28px;
                font-weight: 600;
            }}

            .stat {{
                background: rgba(255, 255, 255, 0.15);
                padding: 20px;
                margin: 15px 0;
                border-radius: 12px;
                font-size: 18px;
                transition: transform 0.3s ease;
            }}

            .stat:hover {{
                transform: translateY(-5px);
            }}

            .label {{
                display: block;
                font-size: 14px;
                opacity: 0.8;
                margin-bottom: 5px;
            }}

            .value {{
                font-size: 24px;
                font-weight: bold;
            }}

            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(10px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}

            footer {{
                margin-top: 25px;
                font-size: 13px;
                opacity: 0.7;
            }}
        </style>
    </head>

    <body>
        <div class="card">
            <h2>🚀 Three-Tier Application</h2>

            <div class="stat">
                <span class="label">Visit Count (MySQL)</span>
                <span class="value">{visits}</span>
            </div>

            <div class="stat">
                <span class="label">Random Number (Redis)</span>
                <span class="value">{random_number}</span>
            </div>

            <footer>
                Powered by Flask • MySQL • Redis
            </footer>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
