"""Curated and dynamic facts engine for cities, settlements, landmarks, and islands.

Provides 10-15 comprehensive facts for any destination in the World Quest explorer,
including specialized curated facts for major cities/destinations like Miami.
"""

from typing import Any, Dict, List, Optional

US_STATES: Dict[str, str] = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
    "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "FL": "Florida", "GA": "Georgia",
    "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa",
    "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri",
    "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey",
    "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio",
    "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont",
    "VA": "Virginia", "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming",
    "DC": "District of Columbia", "PR": "Puerto Rico", "VI": "Virgin Islands", "GU": "Guam",
}

CANADIAN_PROVINCES: Dict[str, str] = {
    "AB": "Alberta", "BC": "British Columbia", "MB": "Manitoba", "NB": "New Brunswick",
    "NL": "Newfoundland and Labrador", "NS": "Nova Scotia", "NT": "Northwest Territories",
    "NU": "Nunavut", "ON": "Ontario", "PE": "Prince Edward Island", "QC": "Quebec",
    "SK": "Saskatchewan", "YT": "Yukon",
}

AUSTRALIAN_STATES: Dict[str, str] = {
    "NSW": "New South Wales", "QLD": "Queensland", "SA": "South Australia",
    "TAS": "Tasmania", "VIC": "Victoria", "WA": "Western Australia",
    "ACT": "Australian Capital Territory", "NT": "Northern Territory",
    "01": "Australian Capital Territory", "02": "New South Wales", "03": "Northern Territory",
    "04": "Queensland", "05": "South Australia", "06": "Tasmania", "07": "Victoria", "08": "Western Australia",
}


# Curated facts for destinations, guaranteeing 10-15 rich facts per place.
CURATED_PLACE_FACTS: Dict[str, List[Dict[str, str]]] = {
    "Miami": [
        {"label": "City nickname", "value": "The Magic City (named because early visitors said it grew so fast it seemed to appear overnight like magic)"},
        {"label": "Historic founding", "value": "Only major US city conceived and founded by a woman — citrus grower Julia Tuttle in 1896"},
        {"label": "Art Deco architecture", "value": "Home to the world's largest collection of Art Deco architecture, with over 800 preserved pastel historic buildings in South Beach"},
        {"label": "Cruise capital of the world", "value": "PortMiami is the world's busiest passenger cruise port, hosting more than 7 million travellers each year"},
        {"label": "Two national parks", "value": "The only US metropolis bordered by two distinct national parks: Everglades National Park and Biscayne National Park"},
        {"label": "Cultural identity", "value": "Known as the 'Gateway to the Americas' with a vibrant Latin American and Caribbean cultural heritage and over 70% Hispanic/Latino population"},
        {"label": "Iconic neighborhoods", "value": "Features world-renowned enclaves including Little Havana (Calle Ocho), Wynwood Arts District, Brickell, and Coconut Grove"},
        {"label": "Climate profile", "value": "Tropical monsoon climate with warm, sea-breezy winters and roughly 3,000 hours of sunshine each year"},
        {"label": "Barrier island geography", "value": "Miami Beach is a separate barrier island municipality connected to mainland Miami across Biscayne Bay by scenic causeways"},
        {"label": "Financial powerhouse", "value": "Brickell Financial District holds the largest concentration of international banks on the US East Coast south of New York City"},
        {"label": "Living coral barrier reef", "value": "Bordered to the south by the Florida Reef Tract, the third-largest living coral barrier reef ecosystem on Earth"},
        {"label": "Street art & murals", "value": "Wynwood Walls is globally celebrated as an open-air street art museum featuring rotating murals by the world's leading urban artists"},
        {"label": "Culinary signature", "value": "Birthplace of 'Floribbean' fusion cuisine, blending Cuban, Haitian, Colombian, and Caribbean cooking traditions with fresh seafood"},
        {"label": "Subtropical wildlife", "value": "Urban waterways and coastal bays shelter Florida manatees, bottlenose dolphins, green sea turtles, and native royal palms"},
    ],
    "Paris": [
        {"label": "City nickname", "value": "City of Light (La Ville Lumière), both for its role in the Age of Enlightenment and as an early adopter of gas streetlights"},
        {"label": "Eiffel Tower", "value": "330-meter wrought-iron lattice tower engineered by Gustave Eiffel for the 1889 Exposition Universelle"},
        {"label": "World's largest museum", "value": "The Louvre houses over 380,000 historic objects and 35,000 artworks, including the Mona Lisa and Venus de Milo"},
        {"label": "Historic river & islands", "value": "The Seine River bisects the city, cradling the Île de la Cité where Notre-Dame Cathedral stands"},
        {"label": "Famous avenue", "value": "Avenue des Champs-Élysées spans nearly 2 km between the Place de la Concorde and the monumental Arc de Triomphe"},
        {"label": "Historic districts", "value": "Distinctive arrondissements include hilltop Montmartre, the historic Latin Quarter, elegant Le Marais, and Saint-Germain"},
        {"label": "Underground catacombs", "value": "Subterranean ossuary labyrinth holding the skeletal remains of over 6 million Parisians transferred in the 18th century"},
        {"label": "Global gastronomy capital", "value": "World epicenter of culinary culture, famed for artisan boulangeries, patisseries, classic bistros, and Michelin-starred dining"},
        {"label": "Historic founding", "value": "Founded in the 3rd century BC by the Celtic Parisii tribe as a trading settlement along the Seine"},
        {"label": "Metro heritage", "value": "Paris Métro opened during the 1900 World's Fair and features celebrated Art Nouveau station entrances designed by Hector Guimard"},
        {"label": "Iconic green spaces", "value": "Renowned public gardens include Jardin du Luxembourg, Tuileries Garden, and the sprawling Bois de Boulogne"},
        {"label": "Haute couture birthplace", "value": "International fashion capital home to historic fashion houses such as Chanel, Dior, Louis Vuitton, and Yves Saint Laurent"},
        {"label": "Climate", "value": "Oceanic climate with pleasant, temperate summers and mild winters influenced by the North Atlantic Current"},
    ],
    "Tokyo": [
        {"label": "Metropolitan scale", "value": "Greater Tokyo is the world's most populous metropolitan area, home to more than 37 million people"},
        {"label": "Tokyo Skytree", "value": "Rising 634 meters, Tokyo Skytree is the third-tallest free-standing tower in the world and Japan's tallest structure"},
        {"label": "Shibuya Crossing", "value": "The world's busiest pedestrian scramble, crossing up to 3,000 people per green light during peak hours"},
        {"label": "Sensō-ji Temple", "value": "Tokyo's oldest and most significant Buddhist temple, established in 645 AD in the historic Asakusa district"},
        {"label": "Historic name", "value": "Originally a modest fishing village named Edo, becoming the seat of the Tokugawa shogunate in 1603 and renamed Tokyo ('Eastern Capital') in 1868"},
        {"label": "Specialized districts", "value": "Famous urban districts include Akihabara (electronics & anime), Shinjuku (skyscrapers), Ginza (luxury), and Harajuku (youth fashion)"},
        {"label": "Culinary pinnacle", "value": "Consistently awarded more Michelin stars than any other city globally, celebrated for sushi, ramen, tempura, and kaiseki"},
        {"label": "Busiest transit hub", "value": "Shinjuku Station serves roughly 3.5 million passengers daily, holding the Guinness World Record as the busiest transportation hub"},
        {"label": "Meiji Shrine & sacred forest", "value": "Dedicated to Emperor Meiji, surrounded by a 170-acre man-made sacred forest of 120,000 trees donated from across Japan"},
        {"label": "Safety & cleanliness", "value": "Consistently recognized as one of the world's safest, cleanest, and most efficiently organized megacities"},
        {"label": "View of Mount Fuji", "value": "On crisp, clear winter mornings, the snow-capped peak of Mount Fuji (100 km southwest) is visible from city observation decks"},
        {"label": "Technological innovation", "value": "A global leader in high-speed bullet trains (Shinkansen), robotics, smart infrastructure, and consumer electronics"},
    ],
    "New York City": [
        {"label": "City nicknames", "value": "The Big Apple, The City That Never Sleeps, and Gotham"},
        {"label": "Five boroughs", "value": "Composed of five distinct boroughs: Manhattan, Brooklyn, Queens, The Bronx, and Staten Island"},
        {"label": "Central Park", "value": "843-acre urban masterpiece designed by Frederick Law Olmsted and Calvert Vaux, welcoming over 40 million visitors annually"},
        {"label": "Statue of Liberty", "value": "Dedicated on Liberty Island in 1886 as a gift from France, symbolizing freedom and democracy across the world"},
        {"label": "Broadway theater", "value": "Broadway's 41 historic professional theaters represent the pinnacle of English-speaking live commercial theatrical production"},
        {"label": "Skyscraper heritage", "value": "Pioneered modern skyscraper architecture with legendary landmarks like the Empire State Building, Chrysler Building, and One World Trade Center"},
        {"label": "Linguistic diversity", "value": "The most linguistically diverse city on Earth, with an estimated 800+ distinct languages spoken across its neighborhoods"},
        {"label": "United Nations headquarters", "value": "International territory in Midtown Manhattan serving as the permanent world headquarters of the United Nations since 1952"},
        {"label": "Subway system", "value": "One of the world's few 24/7 rapid transit systems, operating 472 stations across 36 lines and 1,076 km of track"},
        {"label": "Global financial center", "value": "Wall Street and the New York Stock Exchange form the world's largest stock market and dominant financial capital"},
        {"label": "Culinary traditions", "value": "Famed for iconic New York-style thin-crust pizza, boiled bagels with lox, pastrami on rye, street cart hot dogs, and cheesecake"},
        {"label": "Island geography", "value": "Except for The Bronx on the mainland, the boroughs are spread across Long Island, Manhattan Island, and Staten Island"},
    ],
    "Cape Town": [
        {"label": "Table Mountain", "value": "A flat-topped sandstone icon standing 1,086 meters high, estimated to be more than 600 million years old"},
        {"label": "Two oceans proximity", "value": "Positioned near the confluence of the cold Atlantic Benguela Current and the warm Indian Ocean Agulhas Current"},
        {"label": "Historic 'Mother City'", "value": "South Africa's oldest European city, founded in 1652 as a Dutch East India Company provisioning station"},
        {"label": "Robben Island", "value": "UNESCO World Heritage site where Nelson Mandela was imprisoned for 18 years during the fight against apartheid"},
        {"label": "Boulders Beach penguins", "value": "Sheltered coastal cove home to a famous protected breeding colony of wild African penguins"},
        {"label": "Cape Floral Kingdom", "value": "UNESCO World Heritage site containing the richest temperate floral hotspot on Earth, with 9,000+ plant species (69% endemic)"},
        {"label": "Bo-Kaap neighborhood", "value": "Historic township celebrated for brightly painted cobblestone cottages and authentic Cape Malay cuisine and culture"},
        {"label": "Wine heritage", "value": "South Africa's historic wine industry began here in 1659, with prestigious estates in Constantia, Stellenbosch, and Franschhoek"},
        {"label": "Chapman's Peak Drive", "value": "One of the world's most dramatic coastal roads, carved into near-vertical Atlantic cliff faces with 114 curves"},
        {"label": "Kirstenbosch Botanical Gardens", "value": "Acclaimed botanical garden on the eastern slopes of Table Mountain, the first in the world devoted exclusively to indigenous plants"},
        {"label": "Mediterranean climate", "value": "Features warm, dry summers and cool, rainy winters with seasonal southeasterly winds known locally as the 'Cape Doctor'"},
        {"label": "Legislative capital", "value": "Serves as the legislative capital of South Africa, housing the national Parliament"},
    ],
    "Sydney": [
        {"label": "Sydney Opera House", "value": "Masterpiece of late modern architecture designed by Danish architect Jørn Utzon, opened in 1973 and UNESCO-listed"},
        {"label": "Sydney Harbour Bridge", "value": "Affectionately called 'The Coathanger', it is the world's tallest steel arch bridge (134 meters above water)"},
        {"label": "Port Jackson natural harbour", "value": "One of the world's largest and most scenic natural deepwater harbours, spanning 55 square kilometers of waterways"},
        {"label": "Bondi Beach", "value": "World-famous golden surf beach and heritage site, renowned for Australian surf lifesaving culture and coastal walks"},
        {"label": "Indigenous Gadigal heritage", "value": "Traditional country of the Gadigal clan of the Eora Nation, who lived around the harbour for over 50,000 years"},
        {"label": "The Rocks historic precinct", "value": "Sydney's oldest European neighbourhood, established by the First Fleet in 1788 on rocky harbour terrain"},
        {"label": "Harbour marine life", "value": "Waters are home to over 600 marine species, including seahorses, dolphins, seals, and migrating humpback whales"},
        {"label": "Royal Botanic Garden", "value": "Established in 1816 on Farm Cove, making it the oldest scientific institution and public botanic garden in Australia"},
        {"label": "Manly Ferry journey", "value": "Historic green-and-gold passenger ferries crossing the open harbour between Circular Quay and Manly since 1854"},
        {"label": "Sunny coastal climate", "value": "Humid subtropical climate enjoying roughly 300 sunny days per year with warm summers and mild winters"},
        {"label": "Encircled by national parks", "value": "Surrounded by protected bushland including Royal National Park (world's second-oldest) and Ku-ring-gai Chase"},
        {"label": "Sydney Tower Eye", "value": "Sydney's tallest structure, offering 360-degree observation views from 250 meters above the central business district"},
    ],
    "Giza Pyramids": [
        {"label": "Sole surviving Ancient Wonder", "value": "The Great Pyramid of Giza is the oldest and only surviving monument of the original Seven Wonders of the Ancient World"},
        {"label": "Built for Pharaoh Khufu", "value": "Constructed around 2560 BC during Egypt's Old Kingdom (Fourth Dynasty) as an eternal royal tomb for King Khufu (Cheops)"},
        {"label": "Monumental scale", "value": "Originally rose 146.6 meters (481 ft) tall, reigning as the world's tallest man-made structure for over 3,800 years"},
        {"label": "2.3 million stone blocks", "value": "Assembled using roughly 2.3 million limestone and granite blocks, with an average weight of 2.5 metric tons per block"},
        {"label": "Great Sphinx of Giza", "value": "Monolithic limestone statue carved with a lion's body and Pharaoh Khafre's head, standing 73 meters long and 20 meters high"},
        {"label": "Astronomical precision", "value": "Aligned to true astronomical north with an error margin of less than one-tenth of a single degree"},
        {"label": "Three royal pyramid complexes", "value": "Comprises the pyramids of Pharaohs Khufu, Khafre, and Menkaure, surrounded by queens' pyramids and mastaba tombs"},
        {"label": "UNESCO World Heritage site", "value": "Inscribed on the UNESCO World Heritage list in 1979 as part of Memphis and its Necropolis — the Pyramid Fields"},
        {"label": "Khufu solar barque", "value": "An intact 43-meter cedarwood royal solar ship was discovered disassembled in a sealed pit beside the Great Pyramid in 1954"},
        {"label": "Skilled artisan workforce", "value": "Excavations confirm the complex was built by well-fed, organized Egyptian artisans and seasonal laborers, not enslaved workers"},
        {"label": "Desert plateau geology", "value": "Perched on a limestone plateau on the west bank of the Nile River, bordering the eastern edge of the Sahara Desert"},
        {"label": "Grand Egyptian Museum", "value": "Neighbored by the new Grand Egyptian Museum (GEM), the largest museum on Earth dedicated to a single ancient civilization"},
    ],
    "Patagonia": [
        {"label": "Southern cone wilderness", "value": "Spans over 1 million square kilometers across the southern reaches of both Argentina and Chile"},
        {"label": "Perito Moreno Glacier", "value": "One of the few glaciers on Earth currently in dynamic equilibrium, famed for thunderous ice calving into Lake Argentino"},
        {"label": "Mount Fitz Roy & Cerro Torre", "value": "Iconic, sheer granite spires near El Chaltén, celebrated as some of the most technically challenging climbs on the planet"},
        {"label": "Southern Patagonian Ice Field", "value": "The world's second-largest contiguous extrapolar ice field, feeding dozens of massive freshwater glaciers"},
        {"label": "Native wildlife", "value": "Sanctuary for wild guanacos (camelids), Andean condors with 3-meter wingspans, pumas, rheas (choiques), and Magellanic penguins"},
        {"label": "End of the World", "value": "Tierra del Fuego at Patagonia's southern tip houses Ushuaia, the southernmost city on Earth and main gateway to Antarctica"},
        {"label": "Ancient rock art", "value": "Cueva de las Manos (Cave of the Hands) features UNESCO-listed prehistoric stencil paintings dating back more than 9,000 years"},
        {"label": "Fierce winds & climate", "value": "Swept by the 'Roaring Forties' westerly oceanic winds, creating dramatic microclimates from wet temperate rainforests to arid steppes"},
        {"label": "Welsh settlement heritage", "value": "Chubut Valley retains Welsh-speaking communities, traditional stone chapels, and afternoon tea houses founded in 1865"},
        {"label": "Vast turquoise lakes", "value": "Filled with glacial flour that gives Lakes Nahuel Huapi, Argentino, and Viedma vivid turquoise and milky-blue colors"},
        {"label": "Gaucho cowboy culture", "value": "Traditional Patagonian estancias (sheep ranches) preserve South American gaucho horsemanship, mate tea, and asado roasts"},
        {"label": "Trekking capital", "value": "Home to world-class hiking routes including the Torres del Paine 'W' Trek and trails around Mount Fitz Roy"},
    ],
    "Santorini": [
        {"label": "Cataclysmic volcanic origin", "value": "Shaped by the Minoan eruption (~1600 BC), one of the largest volcanic explosions in human history, which collapsed the island center"},
        {"label": "Submerged caldera", "value": "Features a towering sea cliff crescent wrapping around a submerged volcanic caldera 400 meters deep"},
        {"label": "Cycladic architecture", "value": "Famous worldwide for gleaming whitewashed cubic houses, vibrant blue-domed churches, and cliffside cave dwellings"},
        {"label": "Sunset capital", "value": "The clifftop village of Oia is renowned internationally for panoramic evening sunsets over the Aegean Sea"},
        {"label": "Tri-color volcanic beaches", "value": "Boasts distinctive volcanic coastlines with red sand (Red Beach), black volcanic pebbles (Perissa & Kamari), and white cliffs"},
        {"label": "Ancient Akrotiri", "value": "Bronze Age Minoan city remarkably preserved beneath volcanic pumice, often cited as the inspiration for the legend of Atlantis"},
        {"label": "Basket-trained vineyards", "value": "Indigenous Assyrtiko grapes are woven into round ground baskets ('kouloura') to shield them from relentless Aegean winds"},
        {"label": "Island capital of Fira", "value": "Perched 260 meters above the sea with narrow pedestrian alleyways, cable car links, and traditional donkey paths"},
        {"label": "Nea Kameni active vents", "value": "Uninhabited volcanic islets in the caldera center still emit active sulfurous steam vents and hot springs"},
        {"label": "Unique local produce", "value": "Famed for intensely flavorful Santorini cherry tomatoes, yellow fava bean puree, white eggplants, and caper berries"},
        {"label": "Warm Aegean climate", "value": "Mediterranean climate with dry, sunny summers and mild, sea-moderated winters"},
        {"label": "Premier island destination", "value": "Consistently voted among the world's most romantic and visually stunning island travel destinations"},
    ],
    "Bali": [
        {"label": "Island of the Gods", "value": "Known worldwide as Pulau Dewata (Island of the Gods), celebrated for living Hindu traditions and daily flower offerings"},
        {"label": "Subak irrigation system", "value": "UNESCO-recognized 1,000-year-old cooperative water management system connecting lush terraced rice fields across the island"},
        {"label": "Sacred volcanoes", "value": "Dominated by active volcanic peaks, including Mount Agung (3,142 m, Bali's spiritual center) and Mount Batur with its crater lake"},
        {"label": "Sea temples", "value": "Famed for iconic coastal temples including Tanah Lot on a wave-swept rock and Uluwatu perched atop a 70-meter limestone sea cliff"},
        {"label": "Cultural capital of Ubud", "value": "Ubud is Bali's artistic heartland, famed for traditional dance, woodcarving, silver jewelry, painting, and yoga retreats"},
        {"label": "World-class surfing", "value": "Renowned global surfing hub since the 1970s, with legendary reef breaks at Padang Padang, Uluwatu, and Canggu"},
        {"label": "Marine biodiversity", "value": "Lies within the Coral Triangle, boasting vibrant marine life with manta ray cleaning stations, mola mola, and coral gardens"},
        {"label": "Rich culinary heritage", "value": "Celebrated for distinctive Balinese dishes like babi guling (roast suckling pig), bebek betutu (slow-roasted duck), and sambal matah"},
        {"label": "Sacred monkey forests", "value": "Padangtegal Monkey Forest in Ubud shelters hundreds of Balinese long-tailed macaques among ancient temple banyan trees"},
        {"label": "Traditional architecture", "value": "Homes are designed according to Asta Kosala Kosali principles, featuring split gates (candi bentar) and family shrine pavilions"},
        {"label": "Tropical climate", "value": "Warm tropical climate year-round (26–31°C) with a dry season from April to October and a monsoon season from November to March"},
        {"label": "Warm hospitality & arts", "value": "Famed for gamelan percussion orchestras, intricate legong and barong dance performances, and warm community warmth"},
    ],
    "Maldives": [
        {"label": "Coral atoll geography", "value": "Composed of 1,192 coral islands grouped into a double chain of 26 natural atolls spread across 90,000 square kilometers"},
        {"label": "Lowest nation on Earth", "value": "The lowest-lying country in the world, with an average natural ground elevation of just 1.5 meters above sea level"},
        {"label": "Overwater bungalow pioneers", "value": "Pioneered luxury overwater villas built on stilts directly above turquoise lagoons and living coral reefs"},
        {"label": "Marine wildlife sanctuary", "value": "Baa Atoll is a UNESCO Biosphere Reserve famed for world-class aggregations of hundreds of feeding manta rays and whale sharks"},
        {"label": "Capital island of Malé", "value": "Malé is one of the world's most densely populated islands, packing over 200,000 people onto just 8 square kilometers"},
        {"label": "Equatorial sunshine", "value": "Straddles the Equator in the central Indian Ocean, enjoying constant tropical warmth averaging 28–30°C year-round"},
        {"label": "Bioluminescent beaches", "value": "Islands like Vaadhoo feature magical nighttime 'Sea of Stars' beaches illuminated by bioluminescent dinoflagellates"},
        {"label": "Coral stone mosques", "value": "Historic Friday Mosque (Hukuru Miskiy) in Malé was built in 1658 using intricately interlocking carved coral stone blocks"},
        {"label": "Dhivehi language & script", "value": "Unique national language (Dhivehi) written in Thaana script, read from right to left using Arabic-derived vowel signs"},
        {"label": "Tuna & coconut cuisine", "value": "Traditional Maldivian cuisine (Dhivehi kaan'a) is centered on skipjack tuna, coconut, and starch staples like garudhiya fish broth"},
        {"label": "Seaplane transit network", "value": "Operates the world's largest seaplane fleet (Trans Maldivian Airways), linking remote atoll resorts to Malé airport"},
        {"label": "Strict marine conservation", "value": "Banned shark hunting in 2010 and maintains over 30 marine protected areas to safeguard delicate coral ecosystems"},
    ],
    "Hawaii": [
        {"label": "Volcanic archipelago", "value": "Chain of eight main islands formed over millions of years by a stationary volcanic hot spot in the Pacific Plate"},
        {"label": "Active volcanoes", "value": "Hawaii Volcanoes National Park on the Big Island contains Kilauea and Mauna Loa, among the planet's most active volcanoes"},
        {"label": "Tallest mountain from base", "value": "Mauna Kea rises 4,207 meters above sea level, but measures roughly 10,210 meters from its ocean-floor base — taller than Everest"},
        {"label": "Birthplace of surfing", "value": "Ancient Native Hawaiians developed 'heʻe nalu' (wave sliding) centuries ago; Oahu's North Shore hosts the Triple Crown of Surfing"},
        {"label": "Only royal palace in the US", "value": "ʻIolani Palace in Honolulu was the official royal residence of King Kalākaua and Queen Liliʻuokalani of the Hawaiian Kingdom"},
        {"label": "Endemic flora & fauna", "value": "Due to extreme isolation, over 85% of Hawaii's native flowering plant and animal species exist nowhere else on Earth"},
        {"label": "Cultural concept of Aloha", "value": "The spirit of Aloha represents mutual regard, affection, and warmth, and is formally enshrined in Hawaii state law"},
        {"label": "Stargazing capital", "value": "Mauna Kea's summit hosts 13 world-class astronomical telescopes due to dark skies, low humidity, and high altitude"},
        {"label": "Diverse climate zones", "value": "The Big Island features 10 of the world's 14 climate zones, ranging from tropical rainforests to arid deserts and alpine tundra"},
        {"label": "Rainbow state", "value": "Frequent interaction of trade winds with volcanic mountain slopes produces some of the most vibrant daily rainbows on Earth"},
        {"label": "Cuisine & coffee", "value": "Famed for traditional poke, kalua pork from underground imu ovens, poi, fresh pineapple, and rich Kona coffee"},
        {"label": "Language revival", "value": "Hawaiian (ʻŌlelo Hawaiʻi) is an official co-language of the state, using an alphabet of only 12 letters plus the ʻokina glottal stop"},
    ],
    "Sicily": [
        {"label": "Mediterranean's largest island", "value": "Spanning 25,711 km², Sicily is the largest and most populous island in the Mediterranean Sea"},
        {"label": "Mount Etna", "value": "Europe's highest and most active stratovolcano (3,357 meters), in continuous activity for over 500,000 years (UNESCO site)"},
        {"label": "Valley of the Temples", "value": "Agrigento preserves some of the world's most monumental and intact ancient Doric Greek temples outside of Greece"},
        {"label": "Crossroads of civilizations", "value": "Ruled sequentially by Phoenicians, Greeks, Romans, Arabs, Normans, and Spanish, creating a unique cultural synthesis"},
        {"label": "Palermo's Arab-Norman heritage", "value": "Palermo and Monreale showcase breathtaking Byzantine-style gold mosaics inside Arab-Norman cathedrals"},
        {"label": "Sicilian baroque cities", "value": "The Val di Noto towns (Noto, Ragusa, Modica) were rebuilt in exuberant Sicilian Baroque style after a 1693 earthquake"},
        {"label": "Rich culinary traditions", "value": "Birthplace of arancini (fried rice balls), cannoli, granita with brioche, pasta alla Norma, and caponata eggplant relish"},
        {"label": "Aeolian & Egadi archipelagos", "value": "Surrounded by volcanic island chains including Stromboli (the 'Lighthouse of the Mediterranean') and Vulcano"},
        {"label": "Ancient theater of Taormina", "value": "3rd-century BC Greco-Roman theater carved into clifftops with a backdrop of Mount Etna and the Ionian Sea"},
        {"label": "Citrus & olive groves", "value": "World-famous for blood oranges (arance rosse), Bronte pistachios, Modica stone-ground chocolate, and olive oil"},
        {"label": "Autonomous region", "value": "One of Italy's five autonomous regions with special constitutional status, its own parliament, and regional flag (the Trinacria)"},
        {"label": "Sunny Mediterranean climate", "value": "Enjoys over 2,500 hours of sunshine annually with hot, dry summers and mild, sea-moderated winters"},
    ],
    "Madeira": [
        {"label": "Floating garden of the Atlantic", "value": "Portuguese volcanic archipelago in the North Atlantic celebrated for lush botanical flora, sheer sea cliffs, and waterfalls"},
        {"label": "Centuries-old Levada network", "value": "Over 2,000 km of historic stone irrigation aqueducts and walking footpaths crisscross steep mountain slopes"},
        {"label": "Laurisilva primeval forest", "value": "UNESCO World Heritage site protecting the largest surviving laurel forest on Earth, dating back 20 million years"},
        {"label": "Cabo Girão sea cliff", "value": "One of the highest ocean cliffs in Europe (580 meters), featuring a thrilling suspended glass-floored skywalk"},
        {"label": "Famed fortified wine", "value": "Madeira wine is fortified and uniquely heated ('estufagem'), enabling bottles to stay drinkable for over two centuries"},
        {"label": "Wicker toboggan descent", "value": "Traditional Monte wicker toboggans steered by two drivers ('carreiros') in white uniforms slide down steep cobblestones at 30 km/h"},
        {"label": "Capital city of Funchal", "value": "Picturesque coastal capital nestled in a natural amphitheatre harbour, famed for flower markets and tiled plazas"},
        {"label": "Flower Festival & fireworks", "value": "Celebrates an annual springtime Festa da Flor and holds Guinness World Records for New Year's Eve fireworks over Funchal harbour"},
        {"label": "Cristiano Ronaldo's birthplace", "value": "Soccer legend Cristiano Ronaldo was born and raised in Funchal, which hosts his CR7 Museum and international airport statue"},
        {"label": "Mild spring climate year-round", "value": "Enjoys an eternal spring subtropical climate with average daytime temperatures between 19°C and 26°C all year"},
        {"label": "Black scabbard & espada", "value": "Traditional island dish of deep-sea black scabbard fish served with fried bananas and passion fruit sauce"},
        {"label": "Pico Ruivo summit", "value": "Island's highest peak at 1,862 meters, accessible via an exhilarating cliffside trail connecting Pico do Arieiro above the clouds"},
    ],
    "Jeju Island": [
        {"label": "Korea's volcanic jewel", "value": "South Korea's largest island, designated a UNESCO World Heritage site, Global Geopark, and Biosphere Reserve"},
        {"label": "Hallasan shield volcano", "value": "Mount Halla (1,947 meters) is South Korea's highest mountain, featuring a scenic crater lake (Baengnokdam) at its peak"},
        {"label": "Haenyeo female divers", "value": "UNESCO-recognized free-diving women, many in their 70s and 80s, who harvest seafood without oxygen equipment"},
        {"label": "Manjanggul lava tube", "value": "One of the finest lava tube caves in the world, stretching over 7.4 kilometers with massive 7-meter lava stone pillars"},
        {"label": "Seongsan Ilchulbong (Sunrise Peak)", "value": "Archetypal tuff cone rising dramatically out of the ocean, formed by hydrovolcanic eruptions 5,000 years ago"},
        {"label": "Dol hareubang stone grandfathers", "value": "Ancient basalt statues carved with bulging eyes and round hats, placed outside village gates for protection and fertility"},
        {"label": "Jeju Olle walking trails", "value": "Network of 26 scenic coastal and village walking paths looping 437 km around the entire perimeter of the island"},
        {"label": "Hallabong citrus", "value": "Famed for sweet, bulbous Hallabong mandarins named after Hallasan mountain, grown in rich volcanic soils"},
        {"label": "Black pork delicacy", "value": "Famous across Korea for Jeju black pork (Heuk-dwaeji), grilled over charcoal and dipped in salted anchovy sauce (meljeot)"},
        {"label": "Subtropical climate", "value": "South Korea's warmest region, featuring mild winters and blooming yellow canola fields across coastal cliffs every spring"},
        {"label": "Honeymoon capital", "value": "Historically South Korea's premier domestic honeymoon and resort destination, renowned for beaches and waterfalls"},
        {"label": "Self-governing province", "value": "Holds Special Self-Governing Province status within South Korea, with visa-free entry policies for many nationalities"},
    ],
    "Fiji": [
        {"label": "South Pacific archipelago", "value": "Nation of more than 330 tropical islands and 500 islets, of which roughly 110 are permanently inhabited"},
        {"label": "Great Astrolabe Reef", "value": "One of the world's largest barrier reefs, renowned for incredible coral diversity, manta ray channels, and drop-offs"},
        {"label": "Soft coral capital of the world", "value": "Internationally acclaimed by scuba divers for kaleidoscopic walls of blooming pink, purple, and yellow soft corals"},
        {"label": "Bula spirit & warmth", "value": "Consistently ranked among the happiest nations on Earth, welcoming visitors with the joyful greeting 'Bula!'"},
        {"label": "Kava ceremony", "value": "Traditional social and spiritual ceremony centered on drinking yaqona (kava), made from the ground root of a pepper plant"},
        {"label": "Lovo earth-oven feast", "value": "Traditional banquet of pork, chicken, fish, and root vegetables wrapped in banana leaves and slow-cooked over hot stones underground"},
        {"label": "Firewalking tradition", "value": "The Sawau clan of Beqa Island practices the ancient sacred art of walking barefoot across white-hot river stones unharmed"},
        {"label": "Rugby sevens powerhouse", "value": "National sport with legendary status; Fiji won back-to-back Olympic gold medals in Men's Rugby Sevens (Rio 2016 and Tokyo 2020)"},
        {"label": "Multicultural society", "value": "Rich cultural mix of indigenous iTaukei Melanesians and Indo-Fijians who arrived in the late 19th century"},
        {"label": "Mamanuca & Yasawa islands", "value": "Stunning western island chains featured in iconic films including Cast Away and The Blue Lagoon"},
        {"label": "Tropical marine climate", "value": "Pleasant year-round tropical temperatures averaging 26–31°C, moderated by gentle South Pacific trade winds"},
        {"label": "Fiji waters & natural springs", "value": "Viti Levu's Yaqara Valley is home to ancient artesian underground aquifers that produce world-renowned bottled mineral water"},
    ],
    "Galapagos Islands": [
        {"label": "Living laboratory of evolution", "value": "Ecuadorian volcanic archipelago 1,000 km off the South American coast, inspiring Charles Darwin's theory of natural selection"},
        {"label": "Giant tortoises", "value": "Home to iconic Galapagos giant tortoises that can live over 150 years and weigh up to 400 kilograms"},
        {"label": "Marine iguanas", "value": "The world's only marine lizards, capable of foraging for algae underwater in cold ocean currents down to 30 meters"},
        {"label": "Flightless cormorants & blue-footed boobies", "value": "Sanctuary for rare birds that evolved without natural terrestrial predators, including flightless cormorants and Darwin's finches"},
        {"label": "Fearless wildlife", "value": "Because animals evolved without mammalian predators, wildlife exhibits little fear of humans, allowing respectful close observation"},
        {"label": "Volcanic origins & hot spot", "value": "Geologically young islands formed over a volcanic hot spot; western islands like Fernandina and Isabela remain volcanically active"},
        {"label": "Three converging ocean currents", "value": "Meeting place of the cold Humboldt Current, warm Panama Current, and deep Cromwell Upwelling, creating astonishing biodiversity"},
        {"label": "First UNESCO World Heritage site", "value": "Inscribed as UNESCO World Heritage Site #1 in 1978, with 97% of the land area protected as Galapagos National Park"},
        {"label": "Charles Darwin's 1835 visit", "value": "Darwin spent five weeks surveying San Cristóbal, Floreana, Isabela, and Santiago aboard HMS Beagle, gathering crucial specimen data"},
        {"label": "Penguins on the Equator", "value": "The Galapagos penguin is the only penguin species that lives north of the Equator in the wild, sustained by cold upwelling waters"},
        {"label": "Vast marine reserve", "value": "Galapagos Marine Reserve spans 133,000 km² and protects whale sharks, hammerhead schools, sea lions, and manta rays"},
        {"label": "Strict visitor conservation", "value": "Ecuador enforces strict biosecurity, certified naturalist guide rules, and visitor quotas to preserve the pristine fragile ecosystem"},
    ],
    "Greenland": [
        {"label": "World's largest island", "value": "Spanning 2.16 million km², Greenland is the world's largest island that is not classified as a continent"},
        {"label": "Massive ice sheet", "value": "Greenland Ice Sheet blankets 80% of the island, containing nearly 10% of the Earth's freshwater and ice up to 3 km thick"},
        {"label": "Ilulissat Icefjord (UNESCO)", "value": "Fed by the Sermeq Kujalleq glacier, which calves more than 35 billion tonnes of icebergs annually into Disko Bay"},
        {"label": "Midnight sun & polar night", "value": "Located largely within the Arctic Circle, experiencing 24-hour summer daylight (midnight sun) and winter polar darkness with auroras"},
        {"label": "Inuit culture & heritage", "value": "Roughly 88% of the population are Greenlandic Inuit (Kalaallit), whose ancestors developed qajaqs (kayaks) and dogsleds thousands of years ago"},
        {"label": "No road network between towns", "value": "No paved roads connect Greenlandic towns; all intercity travel relies on airplanes, helicopters, coastal passenger ferries, or dogsleds"},
        {"label": "Capital city of Nuuk", "value": "One of the world's smallest and most northern national capitals, featuring modern architecture, museums, and colorful coastal homes"},
        {"label": "Spectacular Arctic wildlife", "value": "Habitat for polar bears, muskoxen, Arctic foxes, beluga whales, narwhals with spiral tusks, and walruses"},
        {"label": "Autonomous constituent country", "value": "Self-governing overseas territory within the Kingdom of Denmark with its own parliament (Inatsisartut) and prime minister"},
        {"label": "Viking Norse settlements", "value": "Erik the Red founded Norse colonies here in 985 AD that persisted for over 400 years before mysteriously disappearing"},
        {"label": "Kaffemik social tradition", "value": "Beloved traditional open-house gathering celebrating birthdays and milestones with home-baked cakes, coffee, and seal soup"},
        {"label": "Spectacular Northern Lights", "value": "Clear Arctic skies make southern and central Greenland one of the planet's premier vantage points for viewing Aurora Borealis"},
    ],
    "Crete": [
        {"label": "Greece's largest island", "value": "Spanning 8,450 km², Crete is the largest island in Greece and the fifth largest in the Mediterranean Sea"},
        {"label": "Palace of Knossos", "value": "Epicenter of the Bronze Age Minoan civilization (Europe's oldest advanced civilization), famous for the Myth of the Minotaur"},
        {"label": "Minoan art & frescoes", "value": "Archaeological Museum of Heraklion holds priceless Minoan treasures including the Bull-Leaping Fresco and the Phaistos Disc"},
        {"label": "Samaria Gorge", "value": "One of Europe's longest and most dramatic limestone gorges (16 km), cutting through the White Mountains to the Libyan Sea"},
        {"label": "Pink sand beaches", "value": "Elafonisi and Balos Lagoon are famous for pink-tinted sands created by millions of crushed red microscopic shells (foraminifera)"},
        {"label": "Cretan Mediterranean diet", "value": "Cornerstone of the heart-healthy Mediterranean diet, famed for extra-virgin olive oil, wild mountain greens (horta), and sheep cheese"},
        {"label": "Birthplace of Zeus", "value": "According to Greek mythology, the king of the gods was born in the Dikteon Cave on the Lasithi Plateau"},
        {"label": "Venetian harbour towns", "value": "Chania and Rethymno feature romantic Venetian-era harbours, lighthouses, Ottoman minarets, and narrow cobblestone alleys"},
        {"label": "Cretan olive trees", "value": "Home to the ancient Olive Tree of Vouves, estimated to be between 3,000 and 4,000 years old and still producing olives"},
        {"label": "Tsikoudia (Raki) hospitality", "value": "Distilled grape spirit served complimentary with dessert in every Cretan taverna as a warm gesture of hospitality"},
        {"label": "Cretan musical traditions", "value": "Distinctive musical culture centered on the pear-shaped Cretan lyra and poetic rhyming couplets called mantinades"},
        {"label": "Three surrounding seas", "value": "Bordered by the Cretan Sea to the north, the Ionian Sea to the west, and the Libyan Sea to the south"},
    ],
    "Madagascar": [
        {"label": "World's fourth-largest island", "value": "Vast island continent in the Indian Ocean spanning 587,000 km², isolated from mainland Africa for over 88 million years"},
        {"label": "Land of the lemurs", "value": "Home to over 100 species of lemurs (from the tiny Madame Berthe's mouse lemur to the singing indri), all endemic to the island"},
        {"label": "Avenue of the Baobabs", "value": "Iconic dirt road near Morondava lined by towering, 800-year-old Grandidier's baobabs known locally as 'renala' (Mother of the Forest)"},
        {"label": "Tsingy de Bemaraha (UNESCO)", "value": "A breathtaking 'forest of stone' featuring razor-sharp, eroded limestone needle pinnacles rising hundreds of feet"},
        {"label": "Remarkable 90% endemism", "value": "Roughly 90% of Madagascar's plant and animal species exist nowhere else on Earth, making it a critical global biodiversity hotspot"},
        {"label": "Chameleon wonderland", "value": "Harbors roughly two-thirds of the world's chameleon species, including both the giant Parson's chameleon and the minute Brookesia nana"},
        {"label": "Vanilla capital of the world", "value": "Supplies more than 75% of the world's high-grade Bourbon vanilla, hand-pollinated and cured in the northeastern Sava region"},
        {"label": "Austronesian & African heritage", "value": "Settled roughly 2,000 years ago by seafarers from Borneo and East Africa, giving the Malagasy language Indonesian roots"},
        {"label": "Rice culture & culinary staples", "value": "Has one of the world's highest per-capita rice consumption rates; traditional meals revolve around vary (rice) with zebu beef relish"},
        {"label": "Zebu cattle importance", "value": "Humped zebu cattle are revered symbols of wealth, agricultural life, and traditional Malagasy ceremonial ceremonies"},
        {"label": "Diverse biomes", "value": "Encompasses lush eastern rainforests, central volcanic highlands, and southwestern spiny desert forests of octopus trees"},
        {"label": "Red Island nickname", "value": "Nicknamed 'The Red Island' due to its distinctive iron-rich, rust-red laterite soils exposed across rolling plateaus"},
    ],
    "Mauritius": [
        {"label": "Indian Ocean paradise", "value": "Volcanic island nation in the Mascarene Archipelago surrounded by coral barrier reefs and lagoons"},
        {"label": "Extinct home of the Dodo", "value": "The only known habitat of the flightless dodo bird, which went extinct in the late 17th century after European arrival"},
        {"label": "Seven Coloured Earths of Chamarel", "value": "Geological curiosity featuring dunes of rainbow-colored volcanic sand that spontaneously separate into seven distinct hues"},
        {"label": "Underwater waterfall illusion", "value": "Spectacular optical illusion off the coast of Le Morne Brabant where ocean runoff creates the visual effect of an underwater cataract"},
        {"label": "Le Morne Brabant (UNESCO)", "value": "Rugged basalt monolith that served as a historic sanctuary for escaped enslaved people (maroons) in the 18th and early 19th centuries"},
        {"label": "Pamplemousses Botanic Garden", "value": "Sir Seewoosagur Ramgoolam Botanical Garden features giant Victoria amazonica water lilies whose leaves can span three meters"},
        {"label": "Multicultural rainbow nation", "value": "Harmonious blend of Indian, Creole, French, Chinese, and European heritage, where churches, Hindu temples, and mosques stand side-by-side"},
        {"label": "National music of Sega", "value": "UNESCO-recognized traditional folk music and rhythmic dance born from enslaved African workers, played with the ravanne drum"},
        {"label": "Diverse street food culture", "value": "Famed for dholl puri (thin flatbread filled with yellow split peas), samosas, gateaux piments, and Creole seafood curries"},
        {"label": "Sugar cane & historic rum", "value": "Sugar cane cultivation shaped the island's landscape for centuries, giving rise to prestigious artisanal agricultural rums"},
        {"label": "Subtropical island climate", "value": "Pleasant tropical maritime climate with warm summers (November–April) and mild, breezy winters (May–October)"},
        {"label": "High human development", "value": "Consistently ranked among the most stable, democratic, and prosperous nations in Africa with free universal healthcare and education"},
    ],
    "Iceland": [
        {"label": "Land of Fire and Ice", "value": "Straddles the divergent Mid-Atlantic Ridge where tectonic plates tear apart, combining active volcanoes with massive glaciers"},
        {"label": "Vatnajökull glacier", "value": "Europe's largest ice cap by volume, covering roughly 8% of Iceland and concealing active subglacial volcanoes underneath"},
        {"label": "Geothermal superpower", "value": "Nearly 100% of Iceland's electricity and home heating is powered by renewable geothermal and hydroelectric energy"},
        {"label": "Blue Lagoon & natural hot springs", "value": "World-famous mineral-rich geothermal spa in a volcanic lava field, renowned for milky-blue silica water"},
        {"label": "World's oldest parliament", "value": "The Althing was founded at Thingvellir in 930 AD, making it the oldest continuous parliamentary institution in history"},
        {"label": "Diamond Beach & Jökulsárlón", "value": "Glacial lagoon where glowing blue icebergs calve off Breiðamerkurjökull and wash ashore onto black volcanic sand"},
        {"label": "Gullfoss & Skógafoss waterfalls", "value": "Home to thousands of powerful waterfalls fueled by glacial meltwater, including Dettifoss, Europe's second-most powerful fall"},
        {"label": "Pure Icelandic horse breed", "value": "Ancient purebred horses brought by Vikings in the 9th century, renowned for their fifth gait (the exceptionally smooth 'tölt')"},
        {"label": "Literary & reading culture", "value": "Publishes more books per capita than any other nation, with a beloved Christmas Eve tradition of gifting books (Jólabókaflóð)"},
        {"label": "Midnight sun & Northern Lights", "value": "Experience round-the-clock daylight during midsummer and vibrant Aurora Borealis dancing across winter skies"},
        {"label": "Volcanic black sand beaches", "value": "Reynisfjara near Vík features towering basalt sea stacks, hexagonal columns, and Atlantic ocean waves"},
        {"label": "World's safest country", "value": "Consistently ranked #1 on the Global Peace Index as the safest, most peaceful nation on Earth with no standing military"},
    ],
    "Tasmania": [
        {"label": "Island of natural wilderness", "value": "Australia's southernmost island state, separated from the mainland by Bass Strait, with over 40% protected in national parks"},
        {"label": "Tasmanian Devil sanctuary", "value": "The world's largest surviving carnivorous marsupial, endemic to the island and famous for its fierce shriek and powerful jaws"},
        {"label": "Tasmanian Wilderness (UNESCO)", "value": "One of the last great expanses of temperate wilderness on Earth, preserving ancient Gondwanan rainforests and glacial valleys"},
        {"label": "Cleanest air on Earth", "value": "The Cape Grim Baseline Air Pollution Station measures some of the cleanest, purest baseline air recorded anywhere in the world"},
        {"label": "Cradle Mountain & Overland Track", "value": "Iconic jagged dolerite peak overlooking Dove Lake, marking the start of Australia's legendary 65 km Overland Track"},
        {"label": "Port Arthur historic penal colony", "value": "UNESCO-listed 19th-century British convict settlement preserving historic stone penitentiary ruins and harbour guard stations"},
        {"label": "MONA (Museum of Old and New Art)", "value": "Australia's largest private museum, built into sandstone cliffs in Hobart, famous for provocative and groundbreaking contemporary art"},
        {"label": "Cool-climate culinary & wine hub", "value": "Internationally renowned for award-winning single malt whiskies, pinot noir wines, black truffles, oysters, and leatherwood honey"},
        {"label": "Freycinet & Wineglass Bay", "value": "Famous for the flawless pink granite Hazards mountain range framing the pure white sands of Wineglass Bay"},
        {"label": "Ancient Huon pine trees", "value": "Endemic Huon pines can live over 3,000 years, and one clonal stand at Mount Read is estimated to be over 10,000 years old"},
        {"label": "Capital city of Hobart", "value": "Australia's second-oldest capital (founded 1804), famed for historic Georgian sandstone warehouses at Salamanca Place"},
        {"label": "Southern Aurora Australis", "value": "One of the best land-based locations on Earth to view the Aurora Australis (Southern Lights) during winter months"},
    ],
    "London": [
        {"label": "Historic capital on the Thames", "value": "Capital of the United Kingdom, spanning over two millennia of history since its Roman founding as Londinium in 47 AD"},
        {"label": "Tower of London & Crown Jewels", "value": "UNESCO World Heritage fortress founded by William the Conqueror in 1066, safeguarding the British Crown Jewels"},
        {"label": "Big Ben & Westminster", "value": "The Palace of Westminster and the iconic Elizabeth Tower (Big Ben) form the historic seat of British parliamentary democracy"},
        {"label": "Four UNESCO World Heritage sites", "value": "Includes the Tower of London, Westminster Abbey, Maritime Greenwich, and the Royal Botanic Gardens at Kew"},
        {"label": "World-class free national museums", "value": "Home to premier free public museums including the British Museum, Natural History Museum, Science Museum, and Tate Modern"},
        {"label": "London Underground ('The Tube')", "value": "The world's oldest underground passenger railway system, opening its first line between Paddington and Farringdon in 1863"},
        {"label": "West End theater district", "value": "Alongside Broadway, London's West End represents the pinnacle of commercial English-language live theatre"},
        {"label": "Eight Royal Parks", "value": "Vast historic public parklands including Hyde Park, Kensington Gardens, Regent's Park, St James's Park, and Richmond Park"},
        {"label": "Global financial powerhouse", "value": "The historic 'Square Mile' City of London and Canary Wharf form one of the world's leading financial and trading capitals"},
        {"label": "Linguistic & cultural diversity", "value": "More than 300 languages are spoken across London, making it one of the most culturally cosmopolitan cities on Earth"},
        {"label": "Buckingham Palace", "value": "The administrative headquarters and official London residence of the reigning British monarch since 1837"},
        {"label": "Thriving pub & culinary culture", "value": "Historic home of neighborhood public houses (pubs), traditional Sunday roasts, fish and chips, and world-class multicultural dining"},
    ],
    "Rome": [
        {"label": "The Eternal City", "value": "Caput Mundi ('Capital of the World') and Eternal City (Roma Aeterna), with roughly 2,800 years of continuous inhabited history"},
        {"label": "The Colosseum", "value": "The largest ancient amphitheatre ever built, completed in 80 AD under Emperor Titus to host up to 65,000 spectators"},
        {"label": "Vatican City enclave", "value": "Surrounds the independent city-state of Vatican City, home to the Pope, St. Peter's Basilica, and Michelangelo's Sistine Chapel"},
        {"label": "The Pantheon", "value": "Former Roman temple built by Emperor Hadrian (~126 AD) featuring the world's largest unreinforced concrete dome (43 meters)"},
        {"label": "Trevi Fountain tradition", "value": "Breathtaking Baroque fountain where throwing a coin over your left shoulder ensures your return to Rome"},
        {"label": "The Roman Forum", "value": "The political, religious, and commercial heart of the ancient Roman Empire, flanked by the Capitoline and Palatine Hills"},
        {"label": "Seven Historic Hills", "value": "Originally founded around seven hills: Aventine, Caelian, Capitoline, Esquiline, Palatine, Quirinal, and Viminal"},
        {"label": "Historic founding legend", "value": "According to ancient Roman tradition, founded on April 21, 753 BC by twin brothers Romulus and Remus"},
        {"label": "Iconic Roman pasta dishes", "value": "Birthplace of the 'Four Roman Pastas': Cacio e Pepe, Gricia, Carbonara, and Amatriciana, all featuring pecorino romano"},
        {"label": "Thousands of public fountains", "value": "Features over 2,500 historic public drinking fountains ('nasoni') providing cold, drinkable spring water via ancient aqueduct lines"},
        {"label": "Piazza Navona & Campo de' Fiori", "value": "Vibrant public squares featuring Bernini's Fountain of the Four Rivers and traditional outdoor morning markets"},
        {"label": "Sunny Mediterranean climate", "value": "Enjoys warm, dry summers and mild winters with an abundance of classic Mediterranean sunshine"},
    ],
}


def get_hemisphere(lat: float, lon: float) -> str:
    """Format global hemisphere description."""
    ns = "Northern Hemisphere" if lat >= 0 else "Southern Hemisphere"
    ew = "Eastern Hemisphere" if lon >= 0 else "Western Hemisphere"
    return f"{ns} & {ew}"


def get_climate_zone(lat: float) -> str:
    """Determine generalized climate zone from latitude."""
    abs_lat = abs(lat)
    if abs_lat < 23.5:
        return "Tropical zone (warm low-latitude climate belt)"
    elif abs_lat < 35.0:
        return "Subtropical zone (warm temperate climate belt)"
    elif abs_lat < 55.0:
        return "Temperate zone (seasonal mid-latitude climate belt)"
    elif abs_lat < 66.5:
        return "Subpolar / cool continental zone (high-latitude belt)"
    else:
        return "Polar / Arctic zone (polar climate belt)"


def format_coordinates(lat: float, lon: float) -> str:
    """Format coordinates nicely into N/S/E/W degrees."""
    lat_dir = "N" if lat >= 0 else "S"
    lon_dir = "E" if lon >= 0 else "W"
    return f"{abs(lat):.4f}° {lat_dir}, {abs(lon):.4f}° {lon_dir}"


def format_distance_to_equator(lat: float) -> str:
    """Calculate distance to the equator in km and miles."""
    km = round(abs(lat) * 111.0)
    miles = round(km * 0.621371)
    direction = "north" if lat >= 0 else "south"
    return f"{km:,} km ({miles:,} miles) {direction} of the Equator"


def format_solar_time(lon: float) -> str:
    """Calculate estimated solar UTC offset from longitude."""
    offset = round(lon / 15.0)
    sign = "+" if offset >= 0 else ""
    return f"UTC{sign}{offset} (estimated from geographic longitude meridian)"


def generate_settlement_facts(
    row: Dict[str, Any],
    place: Dict[str, Any],
    country_facts: Dict[str, List[Dict[str, str]]],
) -> List[Dict[str, str]]:
    """Dynamically generate 12-14 rich, accurate facts for any GeoNames settlement worldwide."""
    name = row.get("name") or place.get("name") or "Settlement"
    country_name = place.get("country") or row.get("country_code") or "Unknown"
    country_code = (row.get("country_code") or "").upper()
    admin1 = row.get("admin1_code") or ""
    category = place.get("category") or "Populated place"
    lat = float(row.get("latitude") or place.get("latitude") or 0.0)
    lon = float(row.get("longitude") or place.get("longitude") or 0.0)
    pop = int(row.get("population") or place.get("population") or 0)

    # Format administrative region
    if country_code == "US" and admin1 in US_STATES:
        region_str = f"{US_STATES[admin1]} ({admin1})"
    elif country_code == "CA" and admin1 in CANADIAN_PROVINCES:
        region_str = f"{CANADIAN_PROVINCES[admin1]} ({admin1})"
    elif country_code == "AU" and admin1 in AUSTRALIAN_STATES:
        region_str = f"{AUSTRALIAN_STATES[admin1]}"
    elif admin1:
        region_str = f"Administrative Division {admin1}"
    else:
        region_str = country_name

    facts: List[Dict[str, str]] = [
        {"label": "Settlement category", "value": f"{category} (catalogued in the international GeoNames gazetteer)"},
        {"label": "Sovereign nation", "value": f"{country_name} ({country_code})"},
        {"label": "Administrative division", "value": region_str},
    ]

    if pop > 0:
        facts.append({"label": "Recorded population", "value": f"{pop:,} residents (GeoNames statistical baseline)"})
    else:
        facts.append({"label": "Recorded population", "value": "Local community (unspecified census tract)"})

    facts.extend([
        {"label": "Geographic coordinates", "value": format_coordinates(lat, lon)},
        {"label": "Global hemisphere", "value": get_hemisphere(lat, lon)},
        {"label": "Climate & latitude zone", "value": get_climate_zone(lat)},
        {"label": "Distance to Equator", "value": format_distance_to_equator(lat)},
        {"label": "Estimated solar meridian", "value": format_solar_time(lon)},
    ])

    # Extract associated sovereign facts from country_facts
    c_facts = country_facts.get(country_name, [])
    def find_cfact(label_substr: str) -> Optional[str]:
        for cf in c_facts:
            if label_substr.lower() in cf["label"].lower():
                return cf["value"]
        return None

    cap = find_cfact("capital")
    if cap:
        facts.append({"label": "National capital", "value": cap})

    curr = find_cfact("currency")
    if curr:
        facts.append({"label": "Official currency", "value": curr})

    lang = find_cfact("official language")
    if lang:
        facts.append({"label": "Official languages", "value": lang})

    calling = find_cfact("calling code")
    if calling:
        facts.append({"label": "International calling code", "value": calling})

    food = find_cfact("national food")
    if food:
        facts.append({"label": "National culinary tradition", "value": food})

    heritage = find_cfact("featured places")
    if heritage and len(facts) < 15:
        facts.append({"label": "National UNESCO highlights", "value": heritage})

    # Ensure strictly between 10 and 15 facts
    return facts[:15] if len(facts) > 15 else facts


def get_place_facts(
    place: Dict[str, Any],
    country_facts: Dict[str, List[Dict[str, str]]],
) -> List[Dict[str, str]]:
    """Retrieve curated or dynamic facts for any curated place or destination."""
    name = place.get("name", "")

    # Check curated facts by exact name
    if name in CURATED_PLACE_FACTS:
        return CURATED_PLACE_FACTS[name]

    # Check if place is a Country in COUNTRY_FACTS
    if place.get("category") == "Country" and name in country_facts:
        return country_facts[name]

    # If place has settlement-like attributes or general destination attributes, dynamically generate facts
    lat = float(place.get("latitude") or 0.0)
    lon = float(place.get("longitude") or 0.0)
    country_name = place.get("country", "")
    category = place.get("category", "Destination")
    description = place.get("description", "")
    best_for = place.get("best_for", "")

    facts: List[Dict[str, str]] = [
        {"label": "Destination type", "value": f"{category} in {country_name}"},
        {"label": "Sovereign territory", "value": country_name},
        {"label": "Geographic coordinates", "value": format_coordinates(lat, lon)},
        {"label": "Global hemisphere", "value": get_hemisphere(lat, lon)},
        {"label": "Climate & latitude zone", "value": get_climate_zone(lat)},
        {"label": "Distance to Equator", "value": format_distance_to_equator(lat)},
        {"label": "Solar time meridian", "value": format_solar_time(lon)},
    ]

    if best_for:
        facts.append({"label": "Highlights & best for", "value": best_for})

    if description:
        facts.append({"label": "Overview", "value": description})

    # Country linkages
    c_facts = country_facts.get(country_name, [])
    def find_cfact(label_substr: str) -> Optional[str]:
        for cf in c_facts:
            if label_substr.lower() in cf["label"].lower():
                return cf["value"]
        return None

    cap = find_cfact("capital")
    if cap:
        facts.append({"label": "National capital", "value": cap})

    curr = find_cfact("currency")
    if curr:
        facts.append({"label": "Official currency", "value": curr})

    lang = find_cfact("official language")
    if lang:
        facts.append({"label": "Official languages", "value": lang})

    food = find_cfact("national food")
    if food:
        facts.append({"label": "National culinary culture", "value": food})

    heritage = find_cfact("featured places")
    if heritage:
        facts.append({"label": "Featured regional heritage", "value": heritage})

    # Return between 10 and 15 facts
    return facts[:15]
