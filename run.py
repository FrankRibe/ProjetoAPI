from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Tabelas criadas com sucesso!")

    app.run(host='0.0.0.0', port=8000, debug=True)
