# Restaurant Menu App

A web app built in flask displaying various restaurants and their menus. This app allows users to create, update, and delete restaurants and menu items.

## Set-up

Set-up a virtual environment and activate it:

```bash
python3 -m venv env
source env/bin/activate
```

You should see (env) before your command prompt now. (You can type `deactivate` to exit the virtual environment any time.)

Install the requirements:

```bash
pip install -U pip
pip install -r requirements.txt
```

There is script included to initialize and set up the database:

```bash
Usage: populate_db.py
```

## Usage

Make sure you are in the virtual environment (you should see (env) before your command prompt). If not `source /env/bin/activate` to enter it.

```bash
Usage: flask run
```

## Screenshots

![Restaurants Page](https://i.imgur.com/oogd5Hh.png)

![Restaurant Menu Page](https://i.imgur.com/HpBtXL3.png)

![Add New Menu Item Form](https://i.imgur.com/qF8rAx6.png)

## Credit

[Udacity's Full Stack Foundations Course](https://www.udacity.com/course/full-stack-foundations--ud088)

## License

Restaurant Menu App is licensed under the [MIT license](https://github.com/danrneal/restaurant-menu-app/blob/master/LICENSE).
