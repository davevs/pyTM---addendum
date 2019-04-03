# !/usr/bin/env python3

from pytm.pytm import TM, Server, Datastore, Dataflow, Boundary, Actor, ExternalEntity, Process

tm = TM("Basic threat model")
tm.description = "DFD for storytelling exercise"

# Define boundaries
User = Boundary("User")
API = Boundary("Internet facing")
DB = Boundary("Database")

test = ExternalEntity("test")
test.implementsNonce = False

# Define actors
user = Actor("User")
user.inBoundary = User

# Define components
api_search = Server("api_search")
api_search.inBoundary = API
api_search.inScope = True
api_search.providesConfidentiality = True

api_reservation = Server("api_reservation")
api_reservation.inBoundary = API
api_reservation.inScope = True

api_rating = Server("api_rating")
api_rating.inBoundary = API
api_rating.inScope = True

db_search = Datastore("Restaurants")
db_search.inBoundary = DB
db_search.inScope = True
db_search.authenticatesSource = True

db_rating = Datastore("Ratings")
db_rating.inBoundary = DB
db_rating.inScope = False

db_reservations = Datastore("Reservations")
db_reservations.inBoundary = DB
db_reservations.inScope = False

# Define flows
search_user_to_api = Dataflow(user, api_search, "User enters search")
search_user_to_api.isEncrypted = True #JIRA TEST-0001
search_user_to_api.order =1
search_api_to_db = Dataflow(api_search, db_search, "Search critirea")
search_api_to_db.order = 2
search_db_to_api = Dataflow(db_search, api_search, "Results")
search_db_to_api.order = 3
search_api_to_user = Dataflow(api_search, user, "Results")
search_api_to_user.order = 4

reservation_user_to_api = Dataflow(user, api_reservation, "User enters reservation")
reservation_user_to_api.isEncrypted = True
reservation_user_to_api.order =5
reservation_api_to_db = Dataflow(api_reservation, db_reservations, "Check availability")
reservation_api_to_db.order = 6
reservation_db_to_api = Dataflow(db_reservations, api_reservation, "Returns availability")
reservation_db_to_api.order = 7
reservation_api_to_user = Dataflow(api_reservation, user, "Reservation status")
reservation_api_to_user.order = 8

rating_user_to_api = Dataflow(user, api_rating, "User gives rating")
rating_user_to_api.order = 9
rating_api__to_db = Dataflow(api_rating, db_rating, "Rating")
rating_api__to_db.order = 10
rating_db_to_api = Dataflow(db_rating, api_rating, "New rating")
rating_db_to_api.order = 11
rating_api_to_user = Dataflow(api_rating, user, "Thank you")

rating_api_to_user.order = 12
tm.process()