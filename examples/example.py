import flask
import openapi_ui_bundles

app = flask.Flask(__name__, static_folder=openapi_ui_bundles.swagger_ui.static_path, static_url_path='/')

if __name__ == "__main__":
    app.run()
