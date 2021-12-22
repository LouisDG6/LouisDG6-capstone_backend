""" A BakeryController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Bakery import Bakery

class BakeryController(Controller):
    """Class Docstring Description
    """

    def __init__(self, request: Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", BakeryController)
        """
        id = self.request.param("id")
        return Bakery.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", BakeryController)
        """
        return Bakery.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", BakeryController)
        """
        name = self.request.input("name")
        details = self.request.input("details")
        bakery = Bakery.create({"name": name, "details": details})
        return bakery

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", BakeryController)
        """
        name = self.request.input("name")
        details = self.request.input("details")
        id = self.request.param("id")
        Bakery.where("id", id).update({"name":name, "details": details})
        return Bakery.where("id", id).get()

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", BakeryController)
        """
        id = self.request.param("id")
        bakery = Bakery.where("id", id).get()
        Bakery.where("id", id).delete()
        return bakery