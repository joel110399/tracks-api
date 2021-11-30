# SPOT App

App created using [Django](https://www.djangoproject.com/ "Django").

# Getting Started

### Clone the Repo

`$ git clone https://github.com/joel110399/tracks-api.git`

### Install the dependencies
- `$ cd tracks-api`  Go to the app folder.

- `$ pipenv shell` Create a virtual enviroment.

- `$ pip install -r requirements.txt` To install all the dependencies.


### Fill the database

- `$ python manage.py migrate` To create the tables in the database.

- `$ python manage.py filldatabase` I created this custom command to fetch the API using [Requests](https://docs.python-requests.org/en/latest/ "Requests") and fill the database.

### Running the app

- `$ python manage.py runserver` To start development server.

### App structure

- **Models**
	- **Artist**: The model to save the artists.
		- **name**: Artiste name.
		- **unique_id**: Artiste Id.
		- **url**: Artiste url.
	- **Genre**: The model to save the genres.
		- **name**: Genre name.
		- **unique_id**: Genre Id.
		- **url**: Genre url.
	- **Track**: The model to save the tracks.
		- **name**: Track name.
		- **unique_id**: Track Id.
		- **url**: Track url.
		- **release_date**: Track release date.
		- **kind**: Track kind.
		- **artist**: Reference to Artist Model.
		- **genre**: Reference to Genre Model.

- **Views**
	- **ArtistView**: The view to list and create the artists.

	- **GenreView**: The view to list and create the genres.

- **ViewSet**
	I decided to use a viewset for the tracks in order to better handle the filters and the 2 extra endpoints required for the tracks (top 50 popularity tracks and tracks grouped by genres).
	- **TrackViewSet**: Tracks view
		- **allowed http methods**: ['get', 'post', 'patch', 'delete']
		- **extra endpoints**:
			- **top_populars**: This endpoint return the top 50 popular tracks.
			- **grouped_tracks**: This endpoint return the tracks grouped by genres.

- **Urls**
To run the endpoints correctly we have to place the development server path followed by the endpoint name, for example:  `http://127.0.0.1:8000/artist`

	- The paths for each endpoints are the followings:

		-  artist: To list and create artists.
		- genre: To list and create genres.
		- track: To list, create, update and detele tracks.
		- top_populars: To list the top 50 popular tracks.
		- grouped_tracks: To list the tracks grouped by genres.







