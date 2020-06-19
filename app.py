"""A web app displaying various restaurants and their menus.

Usage: flask run
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/restaurants/")
def show_restaurants():
    """Route handler for viewing all restaurants.

    Returns:
        An html template showing all restaurants
    """
    return "This page will show all the restaurants"


@app.route("/restaurants/new/")
def new_restaurant():
    """Route handler for creating a new restaurant.

    Returns:
        An html template with a form to create a new restaurant
    """
    return "This page will be for creating a new restaurant"


@app.route("/restaurants/<int:restaurant_id>/edit/")
def edit_restaurant(restaurant_id):
    """Route handler for modifying an existing restaurant.

    Args:
        restaurant_id: An int representing the id of the restaurant to modify

    Returns:
        An html template with a form to modify the given restaurant
    """
    return f"This page will be for editing restaurant {restaurant_id}"


@app.route("/restaurants/<int:restaurant_id>/delete/")
def delete_restaurant(restaurant_id):
    """Route handler to delete and existing restaurant.

    Args:
        restaurant_id: An int representing the id of the restaurant to delete

    Returns:
        An html template with a confirmation to delete the given restaurant
    """
    return f"This page will be for deleting restaurant {restaurant_id}"


@app.route("/restaurants/<int:restaurant_id>/")
@app.route("/restaurants/<int:restaurant_id>/menu/")
def show_menu_items(restaurant_id):
    """Route handler for displaying the menu for a given restaurant.

    Args:
        restaurant_id: An int representing the id of the restaurant whose menu
            is to be displayed

    Return:
        An html template with the given restaurant's menu displayed
    """
    return f"This page will show the menu for restaurant {restaurant_id}"


@app.route("/restaurants/<int:restaurant_id>/menu/new/")
def new_menu_item(restaurant_id):
    """Route handler for creating a new menu item for the given restaurant.

    Args:
        restaurant_id: An int representing the id of the restaurant to create
            the menu item for

    Returns:
        An html template with a form to create a new menu item
    """
    return (
        "This page will be for making a new menu item for restaurant "
        f"{restaurant_id}"
    )


@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/",)
def edit_menu_item(restaurant_id, menu_item_id):
    """Route handler for modifying an existing menu item.

    Args:
        restaurant_id: An int representing the restaurant the given menu item
            belongs to
        menu_item_id: An int representing the menu item to modify

    Returns:
        An html template with a form to modify the given menu item
    """
    return (
        f"This page will be for editing menu item {menu_item_id} at "
        f"restaurant {restaurant_id}"
    )


@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/",)
def delete_menu_item(restaurant_id, menu__item_id):
    """Route handler for deleting an existing menu item.

    Args:
        restaurant_id: An int representing the restaurant the given menu item
            belongs to
        menu_item_id: An int representing the menu item to delete

    Returns:
        An html template with a confirmation to delete the given menu item
    """
    return (
        f"This page will be for deleteing menu item {menu__item_id} at "
        f"restaurant {restaurant_id}"
    )


if __name__ == "__main__":
    app.run(debug=True)
