from store import create_app, db
from store.models import Item, CartRow


app = create_app('dev')

@app.shell_context_processor
def context_processor():
    return dict(db = db, Item = Item, CartRow = CartRow)


if __name__ == "__main__":
    app.run()