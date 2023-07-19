from app import AppFactory

app = AppFactory.create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5010)
