"""A web app displaying various restaurants and their menus.

Usage: flask run
"""

from flask import Flask, render_template

app = Flask(__name__)

restaurant = {"name": "The CRUDdy Crab", "id": "1"}
restaurants = [
    {"name": "The CRUDdy Crab", "id": "1"},
    {"name": "Blue Burgers", "id": "2"},
    {"name": "Taco Hut", "id": "3"},
]
menu_items = [
    {
        "name": "Cheese Pizza",
        "description": "made with fresh cheese",
        "price": "$5.99",
        "course": "Entree",
        "id": "1",
    },
    {
        "name": "Chocolate Cake",
        "description": "made with Dutch Chocolate",
        "price": "$3.99",
        "course": "Dessert",
        "id": "2",
    },
    {
        "name": "Caesar Salad",
        "description": "with fresh organic vegetables",
        "price": "$5.99",
        "course": "Entree",
        "id": "3",
    },
    {
        "name": "Iced Tea",
        "description": "with lemon",
        "price": "$.99",
        "course": "Beverage",
        "id": "4",
    },
    {
        "name": "Spinach Dip",
        "description": "creamy dip with fresh spinach",
        "price": "$1.99",
        "course": "Appetizer",
        "id": "5",
    },
]
menu_item = {
    "name": "Cheese Pizza",
    "description": "made with fresh cheese",
    "price": "$5.99",
    "course": "Entree",
}


@app.route("/")
@app.route("/restaurants/")
def show_restaurants():
    """Route handler for viewing all restaurants.

    Returns:
        An html template showing all restaurants
    """
    return render_template("restaurants.html", restaurants=restaurants)


@app.route("/restaurants/new/")
def new_restaurant():
    """Route handler for creating a new restaurant.

    Returns:
        An html template with a form to create a new restaurant
    """
    return render_template("new_restaurant.html")


@app.route("/restaurants/<int:restaurant_id>/edit/")
def edit_restaurant(restaurant_id):
    """Route handler for modifying an existing restaurant.

    Args:
        restaurant_id: An int representing the id of the restaurant to modify

    Returns:
        An html template with a form to modify the given restaurant
    """
    return render_template("edit_restaurant.html", restaurant=restaurant)


@app.route("/restaurants/<int:restaurant_id>/delete/")
def delete_restaurant(restaurant_id):
    """Route handler to delete and existing restaurant.

    Args:
        restaurant_id: An int representing the id of the restaurant to delete

    Returns:
        An html template with a confirmation to delete the given restaurant
    """
    return render_template("delete_restaurant.html", restaurant=restaurant)


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
    appetizers = [
        menu_item
        for menu_item in menu_items
        if menu_item["course"] == "Appetizer"
    ]
    entrees = [
        menu_item
        for menu_item in menu_items
        if menu_item["course"] == "Entree"
    ]
    desserts = [
        menu_item
        for menu_item in menu_items
        if menu_item["course"] == "Dessert"
    ]
    beverages = [
        menu_item
        for menu_item in menu_items
        if menu_item["course"] == "Beverage"
    ]
    uncategorized = [
        menu_item
        for menu_item in menu_items
        if menu_item["course"]
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


@app.route("/restaurants/<int:restaurant_id>/menu/new/")
def new_menu_item(restaurant_id):
    """Route handler for creating a new menu item for the given restaurant.

    Args:
        restaurant_id: An int representing the id of the restaurant to create
            the menu item for

    Returns:
        An html template with a form to create a new menu item
    """
    return render_template("new_menu_item.html", restaurant_id=restaurant_id)


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
    return render_template("edit_menu_item.html", menu_item=menu_item)


@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/",)
def delete_menu_item(restaurant_id, menu_item_id):
    """Route handler for deleting an existing menu item.

    Args:
        restaurant_id: An int representing the restaurant the given menu item
            belongs to
        menu_item_id: An int representing the menu item to delete

    Returns:
        An html template with a confirmation to delete the given menu item
    """
    return render_template("delete_menu_item.html", menu_item=menu_item)


if __name__ == "__main__":
    app.run(debug=True)
