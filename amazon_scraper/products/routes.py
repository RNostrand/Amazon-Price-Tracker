from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from amazon_scraper import db
from amazon_scraper.models import User, Product
from amazon_scraper.functions.product import extractProduct, transformProduct

products = Blueprint('products', __name__)

@products.route("/product/<string:asin>", methods=['GET', 'POST'])
def product(asin):
    soup = extractProduct(asin)
    product = transformProduct(soup)
    print(product.get('asin'))
    if request.method == 'POST':
        savedProduct = Product(asin=product.get('asin'), image=product.get('image'), name=product.get('name'), price=product.get('price'), stars=product.get('stars'), ratings=product.get('ratings'), author=current_user)
        db.session.add(savedProduct)
        db.session.commit()
        flash('Your product has been saved!', 'success')
        return redirect(url_for('products.user_products'))
    return render_template('product.html', product=product, title='Product')


@products.route("/user/products")
def user_products():
    email = current_user.email
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(email=email).first_or_404()  
    products = Product.query.filter_by(author=user).paginate(page = page) 
    return render_template('user_products.html', products=products, user=user)

@products.route("/user/product/<string:asin>", methods=['GET', 'POST'])
def user_product(asin):
    product= Product.query.filter_by(asin=asin).first_or_404()
    if request.method == 'POST':
        deletedProduct = product
        if product.author != current_user:
            abort(403)
        db.session.delete(deletedProduct)
        db.session.commit()
        flash('Your product has been removed!', 'success')
        return redirect(url_for('products.user_products'))
    return render_template('user_product.html', product=product, title='Product')
        
# @products.route("/post/new", methods=['GET', 'POST'])
# @login_required
# def new_post():
#     form = PostForm()
#     if form.validate_on_submit():
#         post = Post(title=form.title.data, content=form.content.data, author=current_user)
#         db.session.add(post)
#         db.session.commit()
#         flash('Your post has been created!', 'success')
#         return redirect(url_for('main.home'))
#     return render_template('create_post.html', title='New Post', form=form, legend='New Post')


# @products.route("/post/<int:post_id>")
# def post(post_id):
#     post = Post.query.get_or_404(post_id)
#     return render_template('post.html', title=post.title, post=post)


# @products.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
# @login_required
# def update_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     form = PostForm()
#     if form.validate_on_submit():
#         post.title = form.title.data
#         post.content = form.content.data
#         db.session.commit()
#         flash('Your post has been updated!', 'success')
#         return redirect(url_for('posts.post', post_id=post.id))
#     elif request.method == 'GET':
#         form.title.data = post.title
#         form.content.data = post.content
#     return render_template('create_post.html', title='New Post', form=form, legend='New Post')


# @products.route("/post/<int:post_id>/delete", methods=['POST'])
# @login_required
# def delete_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     db.session.delete(post)
#     db.session.commit()
#     flash('Your post has been deleted!', 'success')
#     return redirect(url_for('main.home'))