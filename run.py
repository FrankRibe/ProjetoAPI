from app import app, db

if __name__ == '__main__':
    # Criar as tabelas no banco de dados dentro do contexto da aplicação
    with app.app_context():
        db.create_all()
        print("Tabelas criadas com sucesso!")

    # Rodar o servidor
    app.run(debug=True)