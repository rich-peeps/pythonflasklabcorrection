from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.route("/")
def index():
    """
    Default route for the company
    """
    return "Welcome to Flatiron Cars"

@app.route("/<model>")
def show_model(model):
    """
    Route that checks whether a given model exists in our fleet.
    - If it exists in existing_models: return
      "Flatiron {model} is in our fleet!"
    - Otherwise: return
      "No models called {model} exists in our catalog."
    """

    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        # NOTE: no period at the end to match the test exactly
        return f"No models called {model} exists in our catalog"

if __name__ == "__main__":
    app.run(debug=True)
