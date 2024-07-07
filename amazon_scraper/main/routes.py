from flask import render_template, request, Blueprint, redirect, url_for
from amazon_scraper.models import Product
from amazon_scraper.main.forms import SearchForm
from amazon_scraper.functions.search import extractSearch, transformSearch

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
@main.route("/home", methods=["GET", "POST"])
def home():
    form = SearchForm()
    query = ""
    if form.validate_on_submit():
        query = form.search.data
        return redirect(url_for("main.search", query=query, page=1))
    return render_template("home.html", form=form, query=query)


@main.route("/search/", methods=["GET", "POST"])
def searchHome():
    form = SearchForm()
    if form.validate_on_submit():
        query = form.search.data
        return redirect(url_for("main.search", query=query, page=1))
    return render_template(
        "search.html",
        form=form,
    )


@main.route("/search/<string:query>/<int:page>", methods=["GET", "POST"])
def search(query, page=1):
    soup = extractSearch(query, page)
    products = transformSearch(soup)
    form = SearchForm()
    if form.validate_on_submit():
        query = form.search.data
        return redirect(url_for("main.search", query=query, page=1))
    return render_template("search.html", form=form, query=query, products=products)


@main.route("/about")
def about():
    return render_template("about.html", title="About")
