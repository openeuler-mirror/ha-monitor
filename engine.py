from com.application import create_app
app = create_app(__name__)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8900)
