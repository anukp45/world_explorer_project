<<<<<<< HEAD
# world_explorer
=======
# World Quest — Interactive World Explorer

A geography exploration and quiz game inspired by the provided architecture mockup. Explore a global map, take daily quizzes, join room-code duels, customize an avatar, and discover upcoming themed events.

## Tech stack

- Python 3.12+
- Flask
- SQLite
- HTML5 / CSS3 / JavaScript
- Leaflet.js
- OpenStreetMap tiles
- Browser local storage for the local player profile

## Features

- Interactive world map with 240+ country/territory, city, landmark, and island entries
- Searchable GeoNames gazetteer containing 5M+ populated-place entries, including cities, towns, and villages
- Country profiles with featured UNESCO places, representative food, area/population ranks, capitals, languages, population, landlocked status, and neighbours
- Search by place name, region, or country
- Filter by country and category
- Destination detail panel with rich description and image
- Five daily quiz themes with three questions each
- Solo quiz mode with score and answer explanations
- Multiplayer, turn-based duels using shareable six-character room codes
- Customizable explorer name and emoji avatar
- Upcoming geography events based on the current date
- Responsive layout for desktop and mobile screens

The bundled country coordinate catalog is derived from the [CountriesNow positions API](https://countriesnow.space/) and excludes Antarctica. Country profiles in `data/country_facts.json` combine [REST Countries data](https://github.com/mledoze/countries), [World Bank 2024 population data](https://data.worldbank.org/indicator/SP.POP.TOTL), [UNESCO World Heritage listings](https://whc.unesco.org/en/list/), and the non-definitive Wikipedia [List of national dishes](https://en.wikipedia.org/wiki/National_dish#By_country). Food examples are representative, not necessarily official national designations. Area ranks use the 2026 reference snapshot, compare catalog entries with available area figures, and include territories; area is not an annual estimate. In this catalog Russia is largest and Vatican City smallest by area. Population values show their source year; population ranks are likewise catalog comparisons, not sovereign-states-only rankings. Missing measurements are not guessed. Historical and disputed entries are identified as such.

City, town, and village search uses the [GeoNames worldwide gazetteer](https://www.geonames.org/), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The imported SQLite database is kept separate from the destination database to avoid loading millions of results on the initial map view. The included `data/settlements.sqlite` is built from the GeoNames `data/allCountries.zip` export. To rebuild it, run:

```bash
python scripts/build_settlements.py
```

The application searches the local gazetteer when a place name is entered, when a country is selected, or when “Cities & towns” is selected. Search results are paginated so the complete catalog can be browsed without rendering millions of markers at once. Island destinations are separately categorized as `Islands`.

To regenerate country profile rankings and featured places, ensure `data/settlements.sqlite`, `data/unesco-source.xml`, `data/national-dishes-wiki.json`, `data/rest-countries-source.json`, and `data/world-bank-population-2024.json` are present, then run:

```bash
python scripts/enrich_country_facts.py
```

Duels use SQLite and periodic browser polling for a simple, working prototype. They do not require an account, but are not a secure production matchmaking system.

## Run locally

1. Create and activate a virtual environment
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the app:

```bash
python app.py
```

4. Open the browser at: http://localhost:5000

## Project structure

```text
world_explorer/
├── app.py
├── requirements.txt
├── world_explorer.db
├── README.md
├── data/
│   ├── allCountries.zip
│   ├── countries.json
│   ├── country_facts.json
│   ├── settlements.sqlite
│   ├── rest-countries-source.json
│   ├── world-bank-population-2024.json
│   ├── unesco-source.xml
│   └── national-dishes-wiki.json
├── scripts/
│   ├── build_settlements.py
│   └── enrich_country_facts.py
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── app.js
└── templates/
    └── index.html
```

The SQLite database is created and seeded automatically the first time the app starts.
>>>>>>> 7b84728 (world_explorer)
