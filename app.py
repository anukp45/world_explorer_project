import json
import sqlite3
import string
from datetime import date
from pathlib import Path
from random import SystemRandom

from flask import Flask, jsonify, render_template, request

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "world_explorer.db"
COUNTRIES_PATH = BASE_DIR / "data" / "countries.json"
COUNTRY_FACTS_PATH = BASE_DIR / "data" / "country_facts.json"
SETTLEMENTS_DB_PATH = BASE_DIR / "data" / "settlements.sqlite"

app = Flask(__name__)
COUNTRY_FACTS = json.loads(COUNTRY_FACTS_PATH.read_text(encoding="utf-8"))
COUNTRY_NAMES_BY_CODE = {}
COUNTRY_CODES_BY_NAME = {}
for country_name, facts in COUNTRY_FACTS.items():
    iso_codes = next((fact["value"] for fact in facts if fact["label"] == "ISO country codes"), None)
    if iso_codes:
        country_code = iso_codes.split("/", maxsplit=1)[0].strip().upper()
        COUNTRY_NAMES_BY_CODE[country_code] = country_name
        COUNTRY_CODES_BY_NAME[country_name.casefold()] = country_code

SETTLEMENT_TYPE_LABELS = {
    "PPLC": "National capital",
    "PPLA": "Regional capital",
    "PPLA2": "Administrative city",
    "PPLA3": "Administrative town",
    "PPLA4": "Locality",
    "PPL": "City / town",
    "PPLL": "Village",
    "PPLX": "Neighbourhood",
}

ISLANDS = [
    ("Bali", "Indonesia", "Asia", -8.3405, 115.0920, "A volcanic Indonesian island known for terraced rice fields, temples, and beaches.", "Surfing, temples, food"),
    ("Maldives", "Maldives", "Asia", 3.2028, 73.2207, "A tropical nation of coral atolls, clear lagoons, and colourful reef life.", "Snorkelling, beaches, marine life"),
    ("Hawaii", "United States", "North America", 19.8968, -155.5828, "A Pacific archipelago shaped by volcanic landscapes, native Hawaiian culture, and ocean life.", "Volcanoes, surfing, hiking"),
    ("Sicily", "Italy", "Europe", 37.5990, 14.0154, "The Mediterranean's largest island, rich in ancient sites, coastal towns, and regional cuisine.", "History, food, coastlines"),
    ("Madeira", "Portugal", "Europe", 32.7607, -16.9595, "A Portuguese Atlantic island celebrated for its rugged peaks, gardens, and walking trails.", "Hiking, gardens, scenery"),
    ("Jeju Island", "South Korea", "Asia", 33.4996, 126.5312, "A volcanic island with lava tubes, waterfalls, and a distinctive coastal culture.", "Nature, caves, beaches"),
    ("Fiji", "Fiji", "Oceania", -17.7134, 178.0650, "A South Pacific archipelago with coral reefs, welcoming villages, and forested islands.", "Diving, culture, beaches"),
    ("Galapagos Islands", "Ecuador", "South America", -0.9538, -90.9656, "A remote volcanic archipelago famed for unique wildlife and conservation history.", "Wildlife, nature, snorkelling"),
    ("Greenland", "Greenland", "North America", 72.0000, -40.0000, "The world's largest island, with vast ice sheets, Arctic settlements, and dramatic fjords.", "Arctic scenery, wildlife, culture"),
    ("Crete", "Greece", "Europe", 35.2401, 24.8093, "Greece's largest island, combining mountain villages, Minoan history, and Mediterranean beaches.", "History, hiking, food"),
    ("Madagascar", "Madagascar", "Africa", -19.0000, 46.7000, "A large island nation with distinctive wildlife, baobab trees, and varied ecosystems.", "Wildlife, nature, landscapes"),
    ("Mauritius", "Mauritius", "Africa", -20.2000, 57.5000, "An Indian Ocean island known for lagoons, volcanic scenery, and a blend of cultures.", "Beaches, hiking, culture"),
    ("Iceland", "Iceland", "Europe", 64.9631, -19.0208, "A North Atlantic island of glaciers, volcanoes, waterfalls, and geothermal landscapes.", "Geology, road trips, scenery"),
    ("Tasmania", "Australia", "Oceania", -41.4545, 145.9707, "An Australian island state with protected wilderness, rugged coasts, and distinctive wildlife.", "Hiking, wildlife, coastlines"),
]

from daily_challenges import (
    CHALLENGE_METADATA,
    get_daily_challenge,
    get_daily_challenges,
    get_question_by_id,
    public_challenge_dto,
)

EVENTS = [
    {"title": "International Mountain Day", "month": 12, "day": 11, "description": "Take on a high-altitude geography challenge and explore mountain destinations."},
    {"title": "World Wetlands Day", "month": 2, "day": 2, "description": "Discover wetlands, migratory birds, and the places that protect them."},
    {"title": "Earth Day Explorer", "month": 4, "day": 22, "description": "A special round about Earth's ecosystems and conservation landmarks."},
    {"title": "World Oceans Day", "month": 6, "day": 8, "description": "Dive into island, ocean, and marine-life questions."},
    {"title": "Indigenous Peoples' Day", "month": 8, "day": 9, "description": "Explore the lands, histories, and cultures of Indigenous peoples."},
]

LEGACY_COUNTRY_ALIASES = {
    "AmericanSamoa": "American Samoa",
    "Bolivia, Plurinational State of Bolivia": "Bolivia",
    "Brunei Darussalam": "Brunei",
    "Congo, The Democratic Republic of the": "Democratic Republic of the Congo",
    "Czech Republic": "Czechia",
    "East Timor": "Timor-Leste",
    "Iran, Islamic Republic of": "Iran",
    "Libyan Arab Jamahiriya": "Libya",
    "Macedonia, The Former Yugoslav Republic of": "North Macedonia",
    "Moldova, Republic of": "Moldova",
    "Republic of Serbia": "Serbia",
    "Swaziland": "Eswatini",
    "The Bahamas": "Bahamas",
    "Tanzania, United Republic of": "Tanzania",
    "United Republic of Tanzania": "Tanzania",
    "United States of America": "United States",
    "Venezuela, Bolivarian Republic of": "Venezuela",
    "eSwatini": "Eswatini",
    "Congo": "Republic of the Congo",
}


def get_db_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def get_json_payload():
    payload = request.get_json(silent=True)
    return payload if isinstance(payload, dict) else {}


def get_challenge(challenge_id, date_str=None, difficulty="mixed"):
    return get_daily_challenge(challenge_id, date_str=date_str, difficulty=difficulty)


def public_challenge(challenge):
    return public_challenge_dto(challenge)


def init_db():
    with get_db_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS places (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                country TEXT NOT NULL,
                region TEXT NOT NULL,
                category TEXT NOT NULL,
                latitude REAL NOT NULL,
                longitude REAL NOT NULL,
                description TEXT NOT NULL,
                image_url TEXT,
                best_for TEXT
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS duel_rooms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT NOT NULL UNIQUE,
                challenge_id TEXT NOT NULL,
                host_name TEXT NOT NULL,
                host_avatar TEXT NOT NULL,
                guest_name TEXT,
                guest_avatar TEXT,
                created_at TEXT NOT NULL
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS duel_answers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                room_code TEXT NOT NULL,
                player_name TEXT NOT NULL,
                question_id TEXT NOT NULL,
                is_correct INTEGER NOT NULL,
                UNIQUE (room_code, player_name, question_id)
            )
            """
        )

        existing_count = connection.execute("SELECT COUNT(*) FROM places").fetchone()[0]
        if existing_count == 0:
            connection.executemany(
                """
                INSERT INTO places (name, country, region, category, latitude, longitude, description, image_url, best_for)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    ("Paris", "France", "Europe", "City", 48.8566, 2.3522, "The City of Light blends art, history, and iconic landmarks with a timeless European charm.", "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1200&q=80", "Architecture, culture, food"),
                    ("Tokyo", "Japan", "Asia", "City", 35.6762, 139.6503, "A fast-moving metropolis where tradition, innovation, and neon-lit nightlife collide beautifully.", "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?auto=format&fit=crop&w=1200&q=80", "Food, nightlife, shopping"),
                    ("New York City", "United States", "North America", "City", 40.7128, -74.0060, "A global hub for culture, art, and commerce known for its skyline and diverse neighborhoods.", "https://images.unsplash.com/photo-1499092346589-b9b6be3e94b2?auto=format&fit=crop&w=1200&q=80", "Museums, skyline, food"),
                    ("Cape Town", "South Africa", "Africa", "Nature", -33.9249, 18.4241, "A dramatic coastal city framed by mountains, beaches, and renowned wine country.", "https://images.unsplash.com/photo-1521295121783-8a321d551ad2?auto=format&fit=crop&w=1200&q=80", "Hiking, beaches, scenery"),
                    ("Sydney", "Australia", "Oceania", "Nature", -33.8688, 151.2093, "Famous for its harbour, iconic bridge, and relaxed coastal lifestyle with unforgettable views.", "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?auto=format&fit=crop&w=1200&q=80", "Harbour views, beaches, urban life"),
                    ("Giza Pyramids", "Egypt", "Africa", "Heritage", 29.9792, 31.1342, "Ancient wonders rising from the desert, offering a powerful connection to one of the world's oldest civilizations.", "https://images.unsplash.com/photo-1572252009286-268acec5ca0a?auto=format&fit=crop&w=1200&q=80", "History, archaeology, photography"),
                    ("Patagonia", "Argentina", "South America", "Adventure", -50.0, -72.0, "Wild landscapes of glaciers, mountains, and deep blue lakes that feel untouched and vast.", "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?auto=format&fit=crop&w=1200&q=80", "Trekking, landscapes, wildlife"),
                    ("Santorini", "Greece", "Europe", "Landmark", 36.3932, 25.4615, "A clifftop island with whitewashed villages, blue domes, and stunning sunsets over the Aegean Sea.", "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?auto=format&fit=crop&w=1200&q=80", "Sunsets, architecture, island views"),
                ],
            )

        countries = json.loads(COUNTRIES_PATH.read_text(encoding="utf-8"))
        for country in countries:
            connection.execute(
                """
                INSERT INTO places (name, country, region, category, latitude, longitude, description, image_url, best_for)
                SELECT ?, ?, ?, 'Country', ?, ?, ?, '', ?
                WHERE NOT EXISTS (
                    SELECT 1 FROM places WHERE name = ? AND country = ? AND category = 'Country'
                )
                """,
                (
                    country["name"],
                    country["name"],
                    country["region"],
                    country["latitude"],
                    country["longitude"],
                    f"Explore {country['name']} and discover its geography, destinations, and culture.",
                    "Cities, culture, nature",
                    country["name"],
                    country["name"],
                ),
            )
            connection.execute(
                """
                UPDATE places
                SET region = ?, latitude = ?, longitude = ?
                WHERE name = ? AND country = ? AND category = 'Country'
                """,
                (
                    country["region"],
                    country["latitude"],
                    country["longitude"],
                    country["name"],
                    country["name"],
                ),
            )

        for alias, canonical_name in LEGACY_COUNTRY_ALIASES.items():
            connection.execute(
                """
                DELETE FROM places
                WHERE name = ? AND country = ? AND category = 'Country'
                  AND EXISTS (
                      SELECT 1 FROM places
                      WHERE name = ? AND country = ? AND category = 'Country'
                  )
                """,
                (alias, alias, canonical_name, canonical_name),
            )

        for name, country, region, latitude, longitude, description, best_for in ISLANDS:
            connection.execute(
                """
                INSERT INTO places (name, country, region, category, latitude, longitude, description, image_url, best_for)
                SELECT ?, ?, ?, 'Islands', ?, ?, ?, '', ?
                WHERE NOT EXISTS (
                    SELECT 1 FROM places WHERE name = ? AND country = ? AND category = 'Islands'
                )
                """,
                (name, country, region, latitude, longitude, description, best_for, name, country),
            )

        country_names = {
            row[0] for row in connection.execute("SELECT name FROM places WHERE category = 'Country'").fetchall()
        }
        missing_facts = country_names.difference(COUNTRY_FACTS)
        if missing_facts:
            missing_names = ", ".join(sorted(missing_facts))
            raise RuntimeError(f"Country facts are missing for: {missing_names}")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/places")
def get_places():
    search = request.args.get("search", "").strip()
    country = request.args.get("country", "").strip()
    category = request.args.get("category", "").strip()

    query = "SELECT * FROM places WHERE 1 = 1"
    params = []

    if country:
        query += " AND country = ?"
        params.append(country)
    if category and category != "all":
        query += " AND category = ?"
        params.append(category)
    if search:
        like = f"%{search}%"
        query += " AND (name LIKE ? OR country LIKE ? OR region LIKE ? OR description LIKE ?)"
        params.extend([like, like, like, like])

    query += " ORDER BY name ASC"
    with get_db_connection() as connection:
        rows = connection.execute(query, params).fetchall()
    return jsonify([dict(row) for row in rows])


@app.route("/api/places/<int:place_id>")
def get_place(place_id):
    with get_db_connection() as connection:
        row = connection.execute("SELECT * FROM places WHERE id = ?", (place_id,)).fetchone()
    if row is None:
        return jsonify({"error": "Place not found"}), 404
    place = dict(row)
    if place["category"] == "Country":
        place["facts"] = COUNTRY_FACTS[place["name"]]
    return jsonify(place)


@app.route("/api/filters")
def get_filters():
    with get_db_connection() as connection:
        countries = [
            row[0] for row in connection.execute("SELECT DISTINCT country FROM places ORDER BY country ASC").fetchall()
        ]
        categories = [
            row[0] for row in connection.execute("SELECT DISTINCT category FROM places ORDER BY category ASC").fetchall()
        ]
    categories.append("Cities & towns")
    return jsonify({"countries": countries, "categories": categories})


@app.route("/api/settlements")
def search_settlements():
    if not SETTLEMENTS_DB_PATH.is_file():
        return jsonify({
            "error": "The worldwide settlement catalog has not been built. Run python scripts/build_settlements.py.",
        }), 503

    search = request.args.get("search", "").strip()
    country = request.args.get("country", "").strip()
    try:
        limit = min(max(int(request.args.get("limit", "25")), 1), 100)
        offset = min(max(int(request.args.get("offset", "0")), 0), 5_300_000)
    except ValueError:
        return jsonify({"error": "Limit and offset must be whole numbers"}), 400

    if len(search) == 1:
        return jsonify({"error": "Enter at least two characters to search settlements"}), 400

    conditions = []
    parameters = []
    if search:
        escaped_search = search.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
        pattern = f"{escaped_search}%"
        conditions.append("(name LIKE ? ESCAPE '\\' OR ascii_name LIKE ? ESCAPE '\\')")
        parameters.extend([pattern, pattern])
    if country:
        country_code = COUNTRY_CODES_BY_NAME.get(country.casefold())
        if country_code is None and len(country) == 2:
            country_code = country.upper()
        if country_code is None:
            return jsonify({"error": "Country not found"}), 404
        conditions.append("country_code = ?")
        parameters.append(country_code)

    where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""
    search_order = "population DESC, name COLLATE NOCASE" if not search else (
        "CASE WHEN name = ? COLLATE NOCASE OR ascii_name = ? COLLATE NOCASE THEN 0 ELSE 1 END, "
        "population DESC, name COLLATE NOCASE"
    )
    if search:
        parameters.extend([search, search])

    try:
        connection = sqlite3.connect(
            f"file:{SETTLEMENTS_DB_PATH.as_posix()}?mode=ro",
            uri=True,
        )
        connection.row_factory = sqlite3.Row
        try:
            rows = connection.execute(
                f"""
                SELECT geonameid, name, ascii_name, latitude, longitude, country_code,
                       admin1_code, feature_code, population
                FROM settlements
                {where_clause}
                ORDER BY {search_order}
                LIMIT ? OFFSET ?
                """,
                [*parameters, limit + 1, offset],
            ).fetchall()
        finally:
            connection.close()
    except sqlite3.Error:
        app.logger.exception("Failed to query the worldwide settlement catalog")
        return jsonify({"error": "Could not search the settlement catalog"}), 500

    has_more = len(rows) > limit
    results = []
    for row in rows[:limit]:
        country_name = COUNTRY_NAMES_BY_CODE.get(row["country_code"], row["country_code"])
        place_type = SETTLEMENT_TYPE_LABELS.get(row["feature_code"], "Populated place")
        results.append({
            "id": f"geonames:{row['geonameid']}",
            "name": row["name"],
            "country": country_name,
            "country_code": row["country_code"],
            "region": row["admin1_code"] or country_name,
            "category": place_type,
            "latitude": row["latitude"],
            "longitude": row["longitude"],
            "population": row["population"],
            "description": f"{place_type} listed in the GeoNames worldwide settlement catalog.",
            "best_for": f"Explore {place_type.lower()}s and nearby places",
        })

    return jsonify({
        "results": results,
        "offset": offset,
        "next_offset": offset + len(results),
        "has_more": has_more,
        "limit": limit,
        "source": "GeoNames",
    })


@app.route("/api/challenges")
def get_challenges():
    target_date = request.args.get("date", date.today().isoformat())
    difficulty = request.args.get("difficulty", "mixed").lower()
    challenges = get_daily_challenges(date_str=target_date, difficulty=difficulty)
    return jsonify({
        "date": target_date,
        "difficulty": difficulty,
        "available_difficulties": ["mixed", "easy", "medium", "hard"],
        "scoring": {
            "correct": 10,
            "incorrect": -2,
            "max_score": 100,
            "questions_count": 10,
        },
        "challenges": [public_challenge(challenge) for challenge in challenges],
    })


@app.route("/api/challenges/<challenge_id>/answer", methods=["POST"])
def answer_challenge(challenge_id):
    payload = get_json_payload()
    question_id = payload.get("question_id")
    selected_index = payload.get("selected_index")

    question = get_question_by_id(challenge_id, question_id)
    if question is None:
        return jsonify({"error": "Question not found"}), 404
    if not isinstance(selected_index, int) or isinstance(selected_index, bool) or not 0 <= selected_index < len(question["choices"]):
        return jsonify({"error": "Select one of the available answers"}), 400

    correct = (selected_index == question["answer"])
    points = 10 if correct else -2

    return jsonify({
        "correct": correct,
        "points": points,
        "correct_index": question["answer"],
        "explanation": question["explanation"],
        "difficulty": question.get("difficulty", "medium"),
    })


@app.route("/api/events")
def get_events():
    today = date.today()
    events = []
    for event in EVENTS:
        event_date = date(today.year, event["month"], event["day"])
        if event_date < today:
            event_date = date(today.year + 1, event["month"], event["day"])
        events.append({
            "title": event["title"],
            "date": event_date.isoformat(),
            "description": event["description"],
        })
    return jsonify(sorted(events, key=lambda event: event["date"]))


def player_name(payload):
    name = payload.get("player_name")
    if not isinstance(name, str) or not name.strip() or len(name.strip()) > 24:
        return None
    return name.strip()


def duel_state(connection, room, current_player):
    answer_rows = connection.execute(
        """
        SELECT player_name,
               COUNT(*) AS answered,
               SUM(CASE WHEN is_correct = 1 THEN 10 ELSE -2 END) AS score
        FROM duel_answers
        WHERE room_code = ?
        GROUP BY player_name
        """,
        (room["code"],),
    ).fetchall()
    scores = {row["player_name"]: {"answered": row["answered"], "score": row["score"] or 0} for row in answer_rows}
    host_stats = scores.get(room["host_name"], {"answered": 0, "score": 0})
    guest_stats = scores.get(room["guest_name"], {"answered": 0, "score": 0}) if room["guest_name"] else {"answered": 0, "score": 0}
    challenge = get_challenge(room["challenge_id"])
    is_host = current_player == room["host_name"]
    other_name = room["guest_name"] if is_host else room["host_name"]
    other_stats = guest_stats if is_host else host_stats
    current_stats = host_stats if is_host else guest_stats
    return {
        "code": room["code"],
        "status": "waiting" if not room["guest_name"] else "playing",
        "player_name": current_player,
        "opponent_name": other_name,
        "opponent_avatar": room["guest_avatar"] if is_host else room["host_avatar"],
        "score": current_stats["score"],
        "answered": current_stats["answered"],
        "opponent_score": other_stats["score"],
        "opponent_answered": other_stats["answered"],
        "question_count": len(challenge["questions"]),
        "challenge": public_challenge(challenge),
        "complete": bool(room["guest_name"]) and host_stats["answered"] == len(challenge["questions"]) and guest_stats["answered"] == len(challenge["questions"]),
    }


@app.route("/api/duels", methods=["POST"])
def create_duel():
    payload = get_json_payload()
    name = player_name(payload)
    challenge = get_challenge(payload.get("challenge_id", "world-tour"))
    if name is None:
        return jsonify({"error": "Enter a player name of 1 to 24 characters"}), 400
    if challenge is None:
        return jsonify({"error": "Choose a valid challenge"}), 400

    avatar = payload.get("avatar", "🌍")
    if not isinstance(avatar, str) or len(avatar) > 8:
        return jsonify({"error": "Choose a valid avatar"}), 400

    alphabet = string.ascii_uppercase + string.digits
    with get_db_connection() as connection:
        for _ in range(5):
            code = "".join(SystemRandom().choices(alphabet, k=6))
            try:
                connection.execute(
                    "INSERT INTO duel_rooms (code, challenge_id, host_name, host_avatar, created_at) VALUES (?, ?, ?, ?, ?)",
                    (code, challenge["id"], name, avatar, date.today().isoformat()),
                )
                break
            except sqlite3.IntegrityError:
                continue
        else:
            return jsonify({"error": "Could not create a duel room. Please try again."}), 503
        room = connection.execute("SELECT * FROM duel_rooms WHERE code = ?", (code,)).fetchone()
        return jsonify(duel_state(connection, room, name)), 201


@app.route("/api/duels/<code>/join", methods=["POST"])
def join_duel(code):
    payload = get_json_payload()
    name = player_name(payload)
    if name is None:
        return jsonify({"error": "Enter a player name of 1 to 24 characters"}), 400

    avatar = payload.get("avatar", "🌍")
    if not isinstance(avatar, str) or len(avatar) > 8:
        return jsonify({"error": "Choose a valid avatar"}), 400

    with get_db_connection() as connection:
        room = connection.execute("SELECT * FROM duel_rooms WHERE code = ?", (code.upper(),)).fetchone()
        if room is None:
            return jsonify({"error": "Duel room not found"}), 404
        if room["host_name"] == name:
            return jsonify({"error": "Join from a different player name"}), 400
        if room["guest_name"] and room["guest_name"] != name:
            return jsonify({"error": "This duel room already has two players"}), 409
        connection.execute(
            "UPDATE duel_rooms SET guest_name = ?, guest_avatar = ? WHERE code = ? AND guest_name IS NULL",
            (name, avatar, code.upper()),
        )
        room = connection.execute("SELECT * FROM duel_rooms WHERE code = ?", (code.upper(),)).fetchone()
        return jsonify(duel_state(connection, room, name))


@app.route("/api/duels/<code>")
def get_duel(code):
    name = request.args.get("player_name", "").strip()
    with get_db_connection() as connection:
        room = connection.execute("SELECT * FROM duel_rooms WHERE code = ?", (code.upper(),)).fetchone()
        if room is None:
            return jsonify({"error": "Duel room not found"}), 404
        if name not in (room["host_name"], room["guest_name"]):
            return jsonify({"error": "Player is not part of this duel"}), 403
        return jsonify(duel_state(connection, room, name))


@app.route("/api/duels/<code>/answer", methods=["POST"])
def answer_duel(code):
    payload = get_json_payload()
    name = player_name(payload)
    question_id = payload.get("question_id")
    selected_index = payload.get("selected_index")
    with get_db_connection() as connection:
        room = connection.execute("SELECT * FROM duel_rooms WHERE code = ?", (code.upper(),)).fetchone()
        if room is None:
            return jsonify({"error": "Duel room not found"}), 404
        if name not in (room["host_name"], room["guest_name"]):
            return jsonify({"error": "Player is not part of this duel"}), 403
        if not room["guest_name"]:
            return jsonify({"error": "Waiting for another player to join"}), 409

        challenge = get_challenge(room["challenge_id"])
        stats = connection.execute(
            "SELECT COUNT(*) FROM duel_answers WHERE room_code = ? AND player_name = ?",
            (room["code"], name),
        ).fetchone()[0]
        if stats >= len(challenge["questions"]):
            return jsonify({"error": "You have completed this duel"}), 409

        question = challenge["questions"][stats]
        if question_id != question["id"]:
            return jsonify({"error": "Answer the next question in the duel"}), 400
        if not isinstance(selected_index, int) or isinstance(selected_index, bool) or not 0 <= selected_index < len(question["choices"]):
            return jsonify({"error": "Select one of the available answers"}), 400

        correct = selected_index == question["answer"]
        points = 10 if correct else -2
        try:
            connection.execute(
                "INSERT INTO duel_answers (room_code, player_name, question_id, is_correct) VALUES (?, ?, ?, ?)",
                (room["code"], name, question["id"], int(correct)),
            )
        except sqlite3.IntegrityError:
            return jsonify({"error": "This question has already been answered"}), 409

        updated_room = connection.execute("SELECT * FROM duel_rooms WHERE code = ?", (room["code"],)).fetchone()
        return jsonify({
            "correct": correct,
            "points": points,
            "correct_index": question["answer"],
            "explanation": question["explanation"],
            "duel": duel_state(connection, updated_room, name),
        })


init_db()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
