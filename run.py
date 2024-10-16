from app import app, db

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            print("Tabelas criadas com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao criar as tabelas: {e}")
    app.run(debug=True)