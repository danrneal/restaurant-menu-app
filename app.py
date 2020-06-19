"""A web app displaying various restaurants and their menus.

Usage: flask run
"""

from flask import (
    Flask,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, MenuItem, Restaurant

engine = create_engine("sqlite:///restaurant_menu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


@app.route("/")
@app.route("/restaurants/")
def show_restaurants():
    """Route handler for viewing all restaurants.

    Returns:
        An html template showing all restaurants
    """
    restaurants = session.query(Restaurant).all()
    return render_template("restaurants.html", restaurants=restaurants)


@app.route("/restaurants/new/", methods=["GET", "POST"])
def new_restaurant():
    """Route handler for creating a new restaurant.

    Returns:
        An html template with a form to create a new restaurant
    """
    if request.method == "GET":
        return render_template("new_restaurant.html")

    restaurant = Restaurant(name=request.form.get("name"))
    session.add(restaurant)
    session.commit()
    flash("New Restaurant Created!")

    return redirect(url_for("show_restaurants"))


@app.route("/restaurants/<int:restaurant_id>/edit/", methods=["GET", "POST"])
def edit_restaurant(restaurant_id):
    """Route handler for modifying an existing restaurant.

    Args:
        restaurant_id: An int representing the id of the restaurant to modify

    Returns:
        An html template with a form to modify the given restaurant
    """
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()

    if request.method == "GET":
        return render_template("edit_restaurant.html", restaurant=restaurant)

    for field in request.form:
        if len(request.form.get(field)) > 0:
            setattr(restaurant, field, request.form.get(field))

    session.add(restaurant)
    session.commit()
    flash("Restaurant Updated!")

    return redirect(url_for("show_restaurants"))


@app.route("/restaurants/<int:restaurant_id>/delete/", methods=["GET", "POST"])
def delete_restaurant(restaurant_id):
    """Route handler to delete and existing restaurant.

    Args:
        restaurant_id: An int representing the id of the restaurant to delete

    Returns:
        An html template with a confirmation to delete the given restaurant
    """
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()

    if request.method == "GET":
        return render_template("delete_restaurant.html", restaurant=restaurant)

    session.delete(restaurant)
    session.commit()
    flash("Restaurant Deleted!")

    return redirect(url_for("show_restaurants"))


@app.route("/restaurants/<int:restaurant_id>/")
@app.route("/restaurants/<int:restaurant_id>/menu/")
def show_menu_items(restaurant_id):
    """Route handler for displaying the menu for a given restaurant.

    Args:
        restaurant_id: An int representing the id of the restaurant whose menu
            is to be displayed

    Returns:
        An html template with the given restaurant's menu displayed
    """
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    menu_items = (
        session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    )

    appetizers = [
        menu_item
        for menu_item in menu_items
        if menu_item.course == "Appetizer"
    ]
    entrees = [
        menu_item for menu_item in menu_items if menu_item.course == "Entree"
    ]
    desserts = [
        menu_item for menu_item in menu_items if menu_item.course == "Dessert"
    ]
    beverages = [
        menu_item for menu_item in menu_items if menu_item.course == "Beverage"
    ]
    uncategorized = [
        menu_item
        for menu_item in menu_items
        if menu_item.course
        not in ("Appetizer", "Entree", "Dessert", "Beverage")
    ]

    return render_template(
        "menu_items.html",
        restaurant=restaurant,
        menu_items=len(menu_items) > 0,
        appetizers=appetizers,
        entrees=entrees,
        desserts=desserts,
        beverages=beverages,
        uncategorized=uncategorized,
    )


@app.route(
    "/restaurants/<int:restaurant_id>/menu/new/", methods=["GET", "POST"]
)
def new_menu_item(restaurant_id):
    """Route handler for creating a new menu item for the given restaurant.

    Args:
        restaurant_id: An int representing the id of the restaurant to create
            the menu item for

    Returns:
        An html template with a form to create a new menu item
    """
    if request.method == "GET":
        return render_template(
            "new_menu_item.html", restaurant_id=restaurant_id
        )

    menu_item = MenuItem(
        name=request.form.get("name"),
        course=request.form.get("course"),
        description=request.form.get("description"),
        price=request.form.get("price"),
        restaurant_id=restaurant_id,
    )
    session.add(menu_item)
    session.commit()
    flash("New Menu Item Created!")

    return redirect(url_for("show_menu_items", restaurant_id=restaurant_id))


@app.route(
    "/restaurants/<int:restaurant_id>/menu/<int:menu_item_id>/edit/",
    methods=["GET", "POST"],
)
def edit_menu_item(restaurant_id, menu_item_id):
    """Route handler for modifying an existing menu item.

    Args:
        restaurant_id: An int representing the id of the restaurant the given
            menu item belongs to
        menu_item_id: An int representing the id of the menu item to modify

    Returns:
        An html template with a form to modify the given menu item
    """
    menu_item = session.query(MenuItem).filter_by(id=menu_item_id).one()

    if request.method == "GET":
        return render_template("edit_menu_item.html", menu_item=menu_item)

    for field in request.form:
        if len(request.form.get(field)) > 0:
            setattr(menu_item, field, request.form.get(field))

    session.add(menu_item)
    session.commit()
    flash("Menu Item Updated!")

    return redirect(url_for("show_menu_items", restaurant_id=restaurant_id))


@app.route(
    "/restaurants/<int:restaurant_id>/menu/<int:menu_item_id>/delete/",
    methods=["GET", "POST"],
)
def delete_menu_item(restaurant_id, menu_item_id):
    """Route handler for deleting an existing menu item.

    Args:
        restaurant_id: An int representing the id of the restaurant the given
            menu item belongs to
        menu_item_id: An int representing the id of the menu item to delete

    Returns:
        An html template with a confirmation to delete the given menu item
    """
    menu_item = session.query(MenuItem).filter_by(id=menu_item_id).one()

    if request.method == "GET":
        return render_template("delete_menu_item.html", menu_item=menu_item)

    session.delete(menu_item)
    session.commit()
    flash("Menu Item Deleted!")

    return redirect(url_for("show_menu_items", restaurant_id=restaurant_id))


@app.route("/api/restaurants/")
def restaurants_api():
    """Route handler for api endpoint retreiving all restaurants.

    Returns:
        response: A json object containing all restaurants
    """
    restaurants = session.query(Restaurant).all()
    response = jsonify(
        restaurants=[restaurant.serialize for restaurant in restaurants]
    )

    return response


@app.route("/api/restaurants/<int:restaurant_id>/")
@app.route("/api/restaurants/<int:restaurant_id>/menu/")
def menu_items_api(restaurant_id):
    """Route handler for api endpoint retreiving menu items for a restaurant.

    Args:
        restaurant_id: An int representing the id of the restaurant whose menu
            items are to be retrieved

    Returns:
        response: A json object containing all menu items for a given
            restaurant
    """
    menu_items = (
        session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    )
    response = jsonify(
        menu_items=[menu_item.serialize for menu_item in menu_items]
    )

    return response


@app.route("/api/restaurants/<int:restaurant_id>/menu/<int:menu_id>/")
def menu_item_api(restaurant_id, menu_id):  # pylint: disable=unused-argument
    """Route handler for api endpoint retreiving a specific menu item.

    Args:
        restaurant_id: An int representing the id of the restaurant the given
            menu item to be retrieved belongs to (unused)
        menu_item_id: An int representing the id of the menu item to be
            retrieved

    Returns:
        response: A json object containing the given menu item
    """
    menu_item = session.query(MenuItem).filter_by(id=menu_id).one()
    response = jsonify(menu_item=menu_item.serialize)

    return response


if __name__ == "__main__":
    app.run(debug=True)
