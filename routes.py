from flask import render_template, request, redirect, url_for

from models import (
    get_all_products,
    add_product,
    get_product,
    update_product,
    delete_product
)


def register_routes(app):

    @app.route("/")
    def home():

        products = get_all_products()

        return render_template(
            "index.html",
            products=products
        )

    @app.route("/add", methods=["GET", "POST"])
    def add():

        if request.method == "POST":

            name = request.form["name"]
    
            category = request.form["category"]

            price = request.form["price"]

            quantity = request.form["quantity"]

            add_product(
                name,
                category,
                price,
                quantity
            )

            return redirect(url_for("home"))
        
        return render_template("add_product.html")



    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit(id):

        if request.method == "POST":
    
            update_product(
                id,
                request.form["name"],
                request.form["category"],
                request.form["price"],
                request.form["quantity"]
            )

            return redirect(url_for("home"))

        product = get_product(id)

        return render_template(
            "edit_product.html",
            product=product
        )

    @app.route("/delete/<int:id>")
    def delete(id):

        delete_product(id)

        return redirect(url_for("home"))
