# demo-superset
Demo project using Apache Superset data exploration and visualization platform for Spotify API fetched data.

## Description



## Getting Started

### Dependencies

* OS: WSL2 run on Windows 10
* Data processing: Conda enviroment with required Python packages (See `conda_env.yml` file).
* Data Viz: [Apache Superset](https://github.com/apache/superset) or [Preset](https://preset.io/).

### Installing

* For data fetching and processing, a Conda environment `spotipy` in `conda_env.yml` is used. For the installation type in terminal:
    ```
    conda env create -f conda_env.yml
    ```

* Personal creditantials must be stored in `.env` that is not version contorolled. To get the creditantials see [this](https://blog.devgenius.io/explore-your-favorite-music-data-with-spotify-api-2510a635947c) tutorial. The files strucutre is:
    ```
    USER_ID=...
    PLAYLIST_ID=...
    CLIENT_ID=...
    CLIENT_SECRET=...
    ```
    Paste requrired Spotify IDs instead of the dots.

* The easiset way to get Apache Superset is with [Docker](https://docker.com/) by dowloading [the latest Docker image](https://hub.docker.com/r/apache/superset) and running it on your machine. Alternatively, use [Preset](https://preset.io/) - a cloud based version of Apache Superset.


### Executing program

* Once the Conda enviroment is installed and Spotify IDs are saved in `.env` file, the Python sript can be run to fetch a playlist's data.

1. Activate the Conda environment
    ```
    conda activate spotipy
    ```
2. Run the Python script
    ```
    python src/fetch_data.py
    ```
    The playlist data will be saved in `.csv` format in `data/` directory - `data/spotify_playlist.csv`.

3. Upload the data to Apache Superset or Preset. I've used Preset services.

## Authors

Igors Dubanevics - [igordub](https://github.com/igordub)


## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)