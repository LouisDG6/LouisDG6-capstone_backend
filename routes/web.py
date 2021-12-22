"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, Route, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Get("/", "BakeryController@index").name("index"),
        Get("/@id", "BakeryController@show").name("show"),
        Post("/", "BakeryController@create").name("create"),
        Put("/@id", "BakeryController@update").name("update"),
        Delete("/@id","BakeryController@destroy").name("destroy")
        
    ], prefix="/bigmomscakies", name="bigmomscakies")
]

