"""Ubermelon shopping application Flask server.

Provides web interface for browsing melons, seeing detail about a melon, and
put melons in a shopping cart.

Authors: Joel Burton, Christian Fernandez, Meggie Mahnken, Katie Byers.
"""

from flask import Flask, render_template, redirect, flash, session, request
import jinja2

import melons, customers

app = Flask(__name__)

# A secret key is needed to use Flask sessioning features
app.secret_key = 'this-should-be-something-unguessable'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = jinja2.StrictUndefined

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True


@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")


@app.route("/melons")
def list_melons():
    """Return page showing all the melons ubermelon has to offer"""

    melon_list = melons.get_all()
    return render_template("all_melons.html",
                           melon_list=melon_list)


@app.route("/melon/<melon_id>")
def show_melon(melon_id):
    """Return page showing the details of a given melon.

    Show all info about a melon. Also, provide a button to buy that melon.
    """

    melon = melons.get_by_id(melon_id)
    print(melon)
    return render_template("melon_details.html",
                           display_melon=melon)


@app.route("/cart")
def show_shopping_cart():
    """Display content of shopping cart."""

    # check to see if a "cart" key has been added to the session:
    if "cart" not in session:

        # flash a warning message
        flash("No items in cart!")

        return redirect("/cart")
    else:
        # get the cart dictionary out of the session
        cart = session["cart"]

        # create a list to hold each Melon object
        all_melons = []

        # create a variable to track the total cost of the order
        total_order_cost = 0

        # iterate through each Melon object in the cart
        for melon_id in cart:
            # get the corresponding Melon object
            melon = melons.get_by_id(melon_id)

            # set a melon-specific quantity attribute
            melon.quantity = cart[melon_id]

            # set a melon-specific total price attribute
            melon.total = melon.quantity * melon.price

            # add melon.total to total cost of the order
            total_order_cost += melon.total

            # add the Melon object to the list of all Melon objects
            all_melons.append(melon)

    return render_template("cart.html", 
                            all_melons=all_melons, 
                            total_order_cost=total_order_cost)


@app.route("/add_to_cart/<melon_id>")
def add_to_cart(melon_id):
    """Add a melon to cart and redirect to shopping cart page.

    When a melon is added to the cart, redirect browser to the shopping cart
    page and display a confirmation message: 'Melon successfully added to
    cart'."""

    # check if the key "cart" is already added in the session (session = {"cart": {melon_id: count}})
    if "cart" in session:
        cart = session["cart"]
    else:
        # if the key "cart" does not exist in the session, create one and set it to an empty Dictionary object
        cart = session["cart"] = {}

    # check if the desired melon id is the cart, and if not, put it in; increment the count for that melon id by 1
    # cart[melon_id] is the key
    cart[melon_id] = cart.get(melon_id, 0) + 1

    # flash a success message
    flash("Success! Melon added to cart.")

    # redirect the user to the cart page
    return redirect("/cart")


@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site.

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """
    
    # get user-provided name and password from request.form object
    email = request.form.get("email")
    password = request.form.get("password")
    
    # use customers.get_by_email() to retrieve corresponding Customer
    if email in customers:
        customer = customers.get_by_email(email)

        if password == customer.password:
            session["logged_in_customer_email"] = customer.email

            # flash a success message
            flash("Log-in successful!")
            
            return redirect("/melons")
        else:

            # flash a warning message
            flash("Incorrect password.")

            return redirect("/login", methods=["GET"])
    else:
        # flash a warning message
        flash("Log-in failed!")

        return redirect("/login", methods=["GET"])


@app.route("/checkout")
def checkout():
    """Checkout customer, process payment, and ship melons."""

    # For now, we'll just provide a warning. Completing this is beyond the
    # scope of this exercise.

    flash("Sorry! Checkout will be implemented in a future version.")
    return redirect("/melons")


        
@app.route("/logout")
def process_logout():
    """Delete session and log-out user."""

    session.pop('logged_in_customer_email')

    flash("Logged out.")
    return redirect("/melons")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
