from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///flask_wtforms"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False 
# app.config["TESTING"] = True
# app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def homepage():
    """Show homepage with available pets."""
    
    pets = Pet.query.all()

    return render_template("index.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        
        new_pet = Pet(name=name, species=species, photo=photo, age=age, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Added {name} the {species}", "success")
        return redirect("/add")

    else:

        return render_template(
            "add_pet.html", form=form)


@app.route("/edit/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit the pet listing."""
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo = form.photo.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.commit()
        flash(f"Updated {pet.name} the {pet.species}", "success")
        return redirect(f"/edit/{pet_id}")

    else:

        return render_template(
            "edit_pet.html", form=form, pet=pet)

# @app.route("/add", methods=["GET", "POST"])
# def add_snack():
#     """Snack add form; handle adding."""

#     form = AddSnackForm()

#     if form.validate_on_submit():
#         name = form.name.data
#         price = form.price.data
#         flash(f"Added {name} at {price}")
#         return redirect("/add")

#     else:
#         return render_template(
#             "snack_add_form.html", form=form)


# @app.route("/users/<int:uid>/edit", methods=["GET", "POST"])
# def edit_user(uid):
#     """Show user edit form and handle edit."""

#     user = User.query.get_or_404(uid)
#     form = UserForm(obj=user)

#     if form.validate_on_submit():
#         user.name = form.name.data
#         user.email = form.email.data
#         db.session.commit()
#         flash(f"User {uid} updated!")
#         return redirect(f"/users/{uid}/edit")

#     else:
#         return render_template("user_form.html", form=form)
