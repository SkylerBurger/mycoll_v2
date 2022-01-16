from models import Movie, MyCollUser
from database import session

sphere = Movie(title="Sphere",
               release_year=1998,
               overview="What's up?",
               mpaa_rating="R",
               runtime_minutes=120,
               image_link="hi",
               tmdb_page_link="hello"
               )

skyler = MyCollUser(name="Skyler", age=33)

session.add(sphere)
session.add(skyler)
session.commit()
