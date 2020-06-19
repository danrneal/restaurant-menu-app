"""Model objects used to model data for the db.

Attributes:
    engine: A sqlalchemy Engine object with a connection to the sqlite db

Classes:
    Base()
    Restaurant()
    MenuItem()
"""

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Restaurant(Base):
    """A model representing a restaurant.

    Attributes:
        id: An int that serves as the unique identifier for the restaurant
        name: A str representing the name of the restaurant
    """

    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    @property
    def serialize(self):
        """Serializes the restaurant object as a dict.

        Returns:
            restaurant: A dict representing the restaurant object
        """
        restaurant = {"id": self.id, "name": self.name}
        return restaurant


class MenuItem(Base):
    """A model representing a menu item.

    Attributes:
        id: An int that serves as the unique identifier for the menu item
        name: A str representing the name of the menu item
        course: A str representing the course the menu item belongs to
        description: A str respresenting a description of the menu item
        price: A str representing the price of the menu item
        restaurant_id: The id of the restaurant the menu item belongs to
    """

    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        """Serializes the menu item object as a dict.

        Returns:
            restaurant: A dict representing the menu item object
        """
        menu_item = {
            "id": self.id,
            "name": self.name,
            "course": self.course,
            "description": self.description,
            "price": self.price,
        }
        return menu_item


engine = create_engine("sqlite:///restaurant_menu.db")

Base.metadata.create_all(engine)
