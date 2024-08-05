from flask import Flask
import threading
from controllers.monitor_controller import monitor_controller
from controllers.openai_controller import openai_controller

app = Flask(__name__)

# TODO: Add all your controllers here
app.register_blueprint(monitor_controller)
app.register_blueprint(openai_controller)

if __name__ == "__main__":
   # threading.Thread(target=consume_messages, daemon=True).start()
    app.run(host='0.0.0.0', port=8080)

