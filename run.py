from app import app, db

# Defina as configurações do servidor
app.config["HOST"] = '127.0.0.1'  # Defina o host aqui
app.config["PORT"] = 8000  # Defina a porta aqui
app.config['DEBUG'] = True  # Habilite o modo debug, se necessário

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            print("Tabelas criadas com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao criar as tabelas: {e}")

    app.run(host=app.config["HOST"],
            port=app.config["PORT"], debug=app.config['DEBUG'])
