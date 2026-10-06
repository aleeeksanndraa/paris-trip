import os, json, time, urllib.request, urllib.parse, math, sys, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data.js")
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "geocache.json")
cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}

P = []
def add(id, name, cat, area, address, lat, lng, notes="", order=None, drinks=None, tags=(), **kw):
    d = dict(id=id, name=name, cat=cat, area=area, address=address, lat=lat, lng=lng)
    if order: d["order"] = order
    if drinks: d["drinks"] = drinks
    d["notes"] = notes
    d.update(kw)
    d.setdefault("status", "want")
    d["tags"] = list(tags)
    P.append(d)

# ───────── EAT ─────────
CH = dict(order=["Escargots", "Steak frites", "Boeuf bourguignon", "Chocolate mousse"])
add("chartier-grands-boulevards","Bouillon Chartier · Grands Boulevards","eat","Grands Boulevards","7 Rue du Faubourg Montmartre, 75009 Paris",48.8720,2.3432,
    "The original 1896 dining hall. Classic French dishes at low prices. No reservations, so expect a queue at peak times.", **CH,
    hours="Every day 11:30 – midnight", open="11:30-24:00", tags=["french classics","cheap","instagram","bouillon"])
add("chartier-montparnasse","Bouillon Chartier · Montparnasse","eat","Montparnasse","59 Boulevard du Montparnasse, 75006 Paris",48.8440,2.3245,
    "Art Nouveau dining room. No reservations, so expect a queue at peak times.", **CH,
    hours="Every day 11:30 – midnight", open="11:30-24:00", tags=["french classics","cheap","instagram","bouillon"])
add("chartier-gare-de-lest","Bouillon Chartier · Gare de l'Est","eat","Canal Saint-Martin","5 Rue du 8 Mai 1945, 75010 Paris",48.8758,2.3585,
    "Opposite Gare de l'Est. No reservations.", **CH, tags=["french classics","cheap","bouillon"])
add("les-philosophes","Les Philosophes","eat","Le Marais","28 Rue Vieille du Temple, 75004 Paris",48.8571,2.3584,
    "Marais bistro with a busy terrace. The French onion soup is the favourite.", order=["French onion soup"], tags=["french classics","terrace"])
add("bistrot-paul-bert","Bistrot Paul Bert","eat","Bastille & 11th","18 Rue Paul Bert, 75011 Paris",48.8524,2.3830,
    "One of the most loved classic bistros in Paris. Book a table.", order=["Steak au poivre with frites"], tags=["french classics"])
add("fontaine-de-mars","La Fontaine de Mars","eat","Eiffel Tower & Trocadéro","129 Rue Saint-Dominique, 75007 Paris",48.8575,2.3020,
    "Classic red-checked bistro a few minutes from the Eiffel Tower. Good to book.", order=["Duck confit","Escargots"], tags=["french classics"])
add("relais-entrecote","Le Relais de l'Entrecôte","eat","Saint-Germain","20 Rue Saint-Benoît, 75006 Paris",48.8550,2.3330,
    "Only one menu: salad, then steak frites with the secret house sauce, and a second serving. No reservations, so expect a queue.",
    order=["Steak frites with the house sauce"], tags=["french classics"])
add("au-pied-de-cochon","Au Pied de Cochon","eat","Montorgueil & Les Halles","6 Rue Coquillière, 75001 Paris",48.8634,2.3438,
    "Classic brasserie near Les Halles, open late.", order=["French onion soup"], tags=["french classics","late night"])
add("bouillon-julien","Bouillon Julien","eat","Grands Boulevards","16 Rue du Faubourg Saint-Denis, 75010 Paris",48.8710,2.3537,
    "Stunning Art Nouveau dining room with bouillon prices.", order=["Escargots","Steak frites"], tags=["french classics","cheap","instagram"])
add("bouillon-pigalle","Bouillon Pigalle","eat","Pigalle & Rue des Martyrs","22 Boulevard de Clichy, 75018 Paris",48.8826,2.3387,
    "Big, lively and cheap French classics near Pigalle.", order=["Boeuf bourguignon"], tags=["french classics","cheap"])
add("train-bleu","Le Train Bleu","eat","Bastille & Gare de Lyon","Place Louis-Armand, Gare de Lyon, 75012 Paris",48.8447,2.3734,
    "Belle Époque restaurant inside Gare de Lyon, with gilded painted ceilings. Worth it for the room. Book ahead.", tags=["french classics","instagram"])
add("breizh-cafe","Breizh Café","eat","Le Marais","109 Rue Vieille du Temple, 75003 Paris",48.8605,2.3631,
    "The best-known crêperie in Paris.", order=["Buckwheat galette","Salted butter caramel crêpe"], drinks=["Breton cider"], tags=["crêpes"])
add("as-du-fallafel","L'As du Fallafel","eat","Le Marais","34 Rue des Rosiers, 75004 Paris",48.8574,2.3591,
    "Famous falafel pita in the old Jewish quarter. Takeaway window or seats inside.", order=["Falafel pita"],
    hours="Closed Friday evening and Saturday", closed=["sat"], tags=["cheap"])
add("pink-mamma","Pink Mamma","eat","Pigalle & Rue des Martyrs","20 bis Rue de Douai, 75009 Paris",48.8818,2.3329,
    "Italian restaurant over four floors with a plant-filled glass-roofed top floor. Very Instagrammable.", order=["Truffle pasta"], tags=["instagram"])
add("higuma","Higuma","eat","Little Tokyo","32 bis Rue Sainte-Anne, 75001 Paris",48.8667,2.3355,
    "Busy, cheap ramen counter. A Rue Sainte-Anne classic.", order=["Ramen","Gyoza"], tags=["japanese","cheap"])
add("kunitoraya","Kunitoraya","eat","Little Tokyo","5 Rue Villedo, 75001 Paris",48.8660,2.3355,
    "Handmade udon. There's almost always a queue.", order=["Udon"], tags=["japanese"])
add("sanukiya","Sanukiya","eat","Little Tokyo","9 Rue d'Argenteuil, 75001 Paris",48.8652,2.3337,
    "Hand-pulled udon, hot or cold. Long lines at peak hours.", order=["Udon"], tags=["japanese","cheap"])
add("dosanko-larmen","Dosanko Larmen","eat","Little Tokyo","40 Rue Sainte-Anne, 75002 Paris",48.8676,2.3356,
    "Small place with huge ramen bowls and great gyoza.", order=["Ramen","Gyoza"], tags=["japanese","cheap"])
add("pho-14","Pho 14","eat","Chinatown","129 Avenue de Choisy, 75013 Paris",48.8254,2.3609,
    "Popular Vietnamese pho in Chinatown. Quick and cheap.", order=["Pho"], tags=["asian","cheap"])
add("dong-huong","Dong Huong","eat","Belleville","14 Rue Louis Bonnet, 75011 Paris",48.8709,2.3786,
    "Long-running Vietnamese restaurant in Belleville.", order=["Pho","Bò bún"], tags=["asian","cheap"])

# ───────── DRINK ─────────
add("little-red-door","Little Red Door","drink","Le Marais","60 Rue Charlot, 75003 Paris",48.8634,2.3630,
    "Regularly listed among the world's best cocktail bars. Look for the small red door. Arrive early or expect a wait.", tags=["cocktails"])
add("le-syndicat","Le Syndicat","drink","Grands Boulevards","51 Rue du Faubourg Saint-Denis, 75010 Paris",48.8717,2.3537,
    "Cocktails made only with French spirits, behind a poster-covered front.", tags=["cocktails"])
add("candelaria","Candelaria","drink","Le Marais","52 Rue de Saintonge, 75003 Paris",48.8633,2.3637,
    "Hidden cocktail bar through a door at the back of a small taqueria.", tags=["cocktails"])
add("danico","Danico","drink","Louvre & Tuileries","6 Rue Vivienne, 75002 Paris",48.8667,2.3388,
    "Cocktail bar at the back of the Daroco restaurant, next to Galerie Vivienne.", tags=["cocktails"])
add("bar-hemingway","Bar Hemingway","drink","Opéra","15 Place Vendôme, 75001 Paris",48.8680,2.3290,
    "Small wood-panelled bar inside the Ritz. Classic and expensive. Dress smart.", tags=["cocktails","classic"])
add("harrys-bar","Harry's New York Bar","drink","Opéra","5 Rue Daunou, 75002 Paris",48.8697,2.3315,
    "Historic bar where the Bloody Mary is said to have been invented.", drinks=["Bloody Mary"], tags=["cocktails","classic"])
add("le-perchoir","Le Perchoir Ménilmontant","drink","Belleville","14 Rue Crespin du Gast, 75011 Paris",48.8667,2.3824,
    "The rooftop bar that started the Paris trend, with views towards Sacré-Cœur. Rooftops can close in bad weather, so check before going.",
    bestTime="Sunset", tags=["rooftop","view","cocktails","instagram"])
add("les-ombres","Les Ombres","drink","Eiffel Tower & Trocadéro","27 Quai Branly, 75007 Paris",48.8610,2.2975,
    "Rooftop restaurant and bar on the Musée du quai Branly, directly facing the Eiffel Tower. Book for dinner.",
    bestTime="After dark, when the tower sparkles on the hour", tags=["rooftop","view","instagram"])
add("terrass-hotel","Terrass'' Hôtel rooftop","drink","Montmartre","12 Rue Joseph de Maistre, 75018 Paris",48.8866,2.3326,
    "Rooftop bar on top of a Montmartre hotel with a view over Paris to the Eiffel Tower.", bestTime="Sunset", tags=["rooftop","view","cocktails"])
add("baron-rouge","Le Baron Rouge","drink","Bastille & Gare de Lyon","1 Rue Théophile Roussel, 75012 Paris",48.8494,2.3779,
    "Lively, old-school wine bar by the Marché d'Aligre. Wine straight from the barrel.", tags=["wine","cheap"])
add("frenchie-bar-a-vins","Frenchie Bar à Vins","drink","Montorgueil & Les Halles","6 Rue du Nil, 75002 Paris",48.8677,2.3478,
    "Wine bar with excellent small plates. No reservations, so go early.", tags=["wine"])

# ───────── CAFÉS ─────────
add("cafe-de-flore","Café de Flore","cafe","Saint-Germain","172 Boulevard Saint-Germain, 75006 Paris",48.8541,2.3325,
    "Classic Paris café since the 1880s. The photo is under the white awning outside.", drinks=["Hot chocolate","Café crème"],
    tags=["classic","instagram","terrace","hot chocolate"])
add("deux-magots","Les Deux Magots","cafe","Saint-Germain","6 Place Saint-Germain-des-Prés, 75006 Paris",48.8540,2.3333,
    "Famous literary café next door to Café de Flore. Terrace facing the church.", drinks=["Hot chocolate"], tags=["classic","terrace","hot chocolate"])
add("maison-rose","La Maison Rose","cafe","Montmartre","2 Rue de l'Abreuvoir, 75018 Paris",48.8874,2.3397,
    "The pink house. The most photographed café front in Paris.", bestTime="Before 9:00, for the photo without crowds", tags=["instagram"])
add("le-consulat","Le Consulat","cafe","Montmartre","18 Rue Norvins, 75018 Paris",48.8864,2.3399,
    "Picture-postcard corner café near Place du Tertre.", tags=["instagram","classic","terrace"])
add("deux-moulins","Café des Deux Moulins","cafe","Montmartre","15 Rue Lepic, 75018 Paris",48.8847,2.3337,
    "The café from the film Amélie.", order=["Crème brûlée"], tags=["film"])
add("angelina","Angelina Rivoli","cafe","Louvre & Tuileries","226 Rue de Rivoli, 75001 Paris",48.8650,2.3284,
    "Belle Époque tea room. Famous for thick hot chocolate and the Mont-Blanc. Expect a queue.",
    order=["Mont-Blanc"], drinks=["L'Africain hot chocolate"], tags=["hot chocolate","pastry","instagram","rainy"])
add("kitsune-palais-royal","Café Kitsuné Palais Royal","cafe","Louvre & Tuileries","51 Galerie de Montpensier, 75001 Paris",48.8653,2.3373,
    "Small coffee bar inside the Palais-Royal gardens. Fox-shaped biscuits.", drinks=["Matcha latte","Coffee"],
    hours="Mon–Sat 9:00–18:30, Sun 10:00–18:30", open="09:00-18:30", openOn={"sun":"10:00-18:30"}, tags=["matcha","coffee","instagram"])
add("cafe-marly","Le Café Marly","cafe","Louvre & Tuileries","93 Rue de Rivoli, 75001 Paris",48.8617,2.3357,
    "Terrace under the Louvre arcades looking straight at the glass pyramid.", tags=["view","terrace","instagram"])
add("boot-cafe","Boot Café","cafe","Le Marais","19 Rue du Pont aux Choux, 75003 Paris",48.8606,2.3654,
    "Tiny coffee shop in a former cobbler's shop, with a blue shopfront.", drinks=["Coffee","Matcha"], tags=["coffee","matcha","instagram"])
add("ob-la-di","Ob-La-Di","cafe","Le Marais","54 Rue de Saintonge, 75003 Paris",48.8635,2.3637,
    "Small, bright café. Popular for matcha and brunch.", drinks=["Matcha latte"], tags=["matcha","coffee"])
add("cafeotheque","La Caféothèque","cafe","Le Marais","52 Rue de l'Hôtel de Ville, 75004 Paris",48.8549,2.3567,
    "Specialty coffee roaster by the Seine.", tags=["coffee"])
add("shakespeare-cafe","Shakespeare and Company Café","cafe","Latin Quarter","37 Rue de la Bûcherie, 75005 Paris",48.8526,2.3471,
    "Café beside the famous English bookshop, facing Notre-Dame.", tags=["coffee","books"])
add("carette","Carette Trocadéro","cafe","Eiffel Tower & Trocadéro","4 Place du Trocadéro et du 11 Novembre, 75016 Paris",48.8633,2.2872,
    "Classic tea room near the Trocadéro. Good stop before Eiffel Tower photos.", order=["Macarons"], tags=["pastry","macarons","terrace"])
add("laduree-champs","Ladurée Champs-Élysées","cafe","Champs-Élysées","75 Avenue des Champs-Élysées, 75008 Paris",48.8711,2.3031,
    "The famous macaron house in its grand tea-room setting.", order=["Macarons"], tags=["macarons","instagram","rainy"])

# ───────── PASTRY ─────────
def pastry(id,name,area,address,lat,lng,order,notes,tags,**kw): add(id,name,"pastry",area,address,lat,lng,notes,order=order,tags=tags,**kw)
pastry("pierre-herme-bonaparte","Pierre Hermé","Saint-Germain","72 Rue Bonaparte, 75006 Paris",48.8516,2.3326,
    ["Ispahan (rose, lychee, raspberry)","Macarons: Ispahan, Mogador, Mosaïc"],"Ranked best pâtisserie in the world by La Liste 2026. Takeaway shop.",["macarons","top pick"])
pastry("laduree-royale","Ladurée Royale","Opéra","16 Rue Royale, 75008 Paris",48.8697,2.3226,
    ["Macarons: salted caramel, pistachio","Ispahan"],"The original Ladurée shop and tea room. The prettiest pastel macarons and boxes.",["macarons","instagram","tea room","rainy"])
pastry("carette-vosges","Carette Place des Vosges","Le Marais","25 Place des Vosges, 75003 Paris",48.8559,2.3659,
    ["Macarons","Millefeuille"],"Tea room under the arcades of Place des Vosges. Some say the best macarons in Paris, with a crunchier bite.",["macarons","tea room","terrace"])
pastry("dalloyau","Dalloyau","Champs-Élysées","101 Rue du Faubourg Saint-Honoré, 75008 Paris",48.8726,2.3112,
    ["Opéra cake","Macarons"],"Historic pastry house dating back to 1682. Home of the Opéra cake.",["macarons","historic"])
pastry("stohrer","Stohrer","Montorgueil & Les Halles","51 Rue Montorgueil, 75002 Paris",48.8649,2.3470,
    ["Baba au rhum","Puits d'amour","Éclairs"],"The oldest pâtisserie in Paris, founded in 1730. The baba au rhum was created here. Beautiful painted interior.",["baba au rhum","éclairs","historic","instagram"])
pastry("fou-de-patisserie","Fou de Pâtisserie","Montorgueil & Les Halles","45 Rue Montorgueil, 75002 Paris",48.8646,2.3470,
    ["Pastries from top Paris chefs"],"One shop selling pastries from many of the city's best chefs. Good for trying several in one stop.",["fruit pastries","éclairs","millefeuille"])
pastry("cedric-grolet-opera","Cédric Grolet Opéra","Opéra","35 Avenue de l'Opéra, 75002 Paris",48.8680,2.3333,
    ["Trompe-l'œil fruit pastries","Croissant"],"Pastries that look exactly like real fruit. Very Instagrammable. Expect a queue.",["fruit pastries","croissants","instagram","top pick"])
pastry("ritz-comptoir","Ritz Paris Le Comptoir","Opéra","38 Rue Cambon, 75001 Paris",48.8681,2.3285,
    ["Madeleines","Marbled cake"],"Small pastry counter of the Ritz hotel, at the back on Rue Cambon. Known for its madeleines.",["madeleines","luxury"])
pastry("eclair-de-genie","L'Éclair de Génie","Le Marais","14 Rue Pavée, 75004 Paris",48.8559,2.3608,
    ["Éclairs"],"Rows of colourful éclairs in many flavours.",["éclairs","instagram"])
pastry("jacques-genin","Jacques Genin","Le Marais","133 Rue de Turenne, 75003 Paris",48.8628,2.3647,
    ["Millefeuille, made to order","Caramels"],"Chocolatier famous for a millefeuille assembled when you order it, plus soft caramels.",["millefeuille","chocolate","caramels"])
pastry("sebastien-gaudard","Sébastien Gaudard","Pigalle & Rue des Martyrs","22 Rue des Martyrs, 75009 Paris",48.8786,2.3394,
    ["Paris-Brest","Millefeuille"],"Classic French pastries done perfectly, in a pretty old-style shop.",["millefeuille","choux","classic"])
pastry("mamiche","Mamiche","Pigalle & Rue des Martyrs","45 Rue Condorcet, 75009 Paris",48.8800,2.3446,
    ["Babka","Cream puffs"],"Popular neighbourhood bakery. Known for chocolate babka and cream puffs.",["choux","viennoiserie"])
pastry("odette","Odette","Latin Quarter","77 Rue Galande, 75005 Paris",48.8523,2.3469,
    ["Choux cream puffs"],"Cream puffs in a little green-and-white house across the river from Notre-Dame.",["choux","instagram"])
pastry("aki-boulangerie","Aki Boulangerie","Little Tokyo","16 Rue Sainte-Anne, 75001 Paris",48.8659,2.3357,
    ["Matcha pastries","Melon pan","Onigiri"],"Japanese-French bakery on Rue Sainte-Anne. Matcha viennoiseries and bento lunches.",["japanese","matcha","viennoiserie"])
pastry("du-pain-et-des-idees","Du Pain et des Idées","Canal Saint-Martin","34 Rue Yves Toudic, 75010 Paris",48.8706,2.3628,
    ["Pistachio-chocolate escargot","Pain des amis"],"Bakery known for the pistachio-chocolate escargot pastry. Takeaway only.",["viennoiserie","croissants","top pick"],
    hours="Closed weekends", closed=["sat","sun"])
pastry("la-parisienne","La Parisienne","Grands Boulevards","12 Rue du Faubourg Poissonnière, 75010 Paris",48.8714,2.3484,
    ["Butter croissant","Pain au chocolat"],"2nd place, Best Butter Croissant of Greater Paris 2025.",["croissants","pain au chocolat","award"])
pastry("mille-et-un","Boulangerie Mille et Un","Saint-Germain","32 Rue Saint-Placide, 75006 Paris",48.8497,2.3266,
    ["Butter croissant","Pain au chocolat"],"3rd place, Best Butter Croissant of Greater Paris 2025.",["croissants","pain au chocolat","award"])
pastry("rabineau","Boulangerie Moderne Rabineau","Latin Quarter","16 Rue des Fossés-Saint-Jacques, 75005 Paris",48.8455,2.3443,
    ["Butter croissant"],"4th place, Best Butter Croissant of Greater Paris 2025. Near the Panthéon.",["croissants","award"])
pastry("utopie","Boulangerie Utopie","Bastille & 11th","20 Rue Jean-Pierre Timbaud, 75011 Paris",48.8653,2.3671,
    ["Croissant","Black sesame éclair"],"Creative bakery loved for its croissants and unusual flavours.",["croissants","éclairs","viennoiserie"])

# ───────── SHOP ─────────
add("repetto","Repetto","shop","Opéra","22 Rue de la Paix, 75002 Paris",48.8694,2.3312,
    "The original Repetto shop, open since 1959 next to the Opéra. Famous ballet flats, including the 'Cendrillon' made for Brigitte Bardot.",
    tags=["shoes","fashion","instagram"])
add("buly","Officine Universelle Buly","shop","Saint-Germain","6 Rue Bonaparte, 75006 Paris",48.8562,2.3343,
    "Beautiful old-apothecary-style shop. Combs (including Japanese boxwood), brushes, soaps and perfumes. Ask about name calligraphy on your purchase.",
    tags=["hair","beauty","instagram"])
add("maison-caillau","Maison Caillau","shop","Champs-Élysées","124 Rue du Faubourg Saint-Honoré, 75008 Paris",48.8740,2.3106,
    "French artisan hair accessories: combs, hair clips, headbands and bows.", hours="Mon–Sat 10:00–19:00",
    open="10:00-19:00", closed=["sun"], tags=["hair","fashion"])
add("la-bonne-brosse","La Bonne Brosse","shop","Louvre & Tuileries","18 Rue de Richelieu, 75001 Paris",48.8640,2.3366,
    "Handmade hairbrushes and combs.", tags=["hair","beauty"])
add("alexandre-de-paris","Alexandre de Paris","shop","Louvre & Tuileries","La Samaritaine, 9 Rue de la Monnaie, 75001 Paris",48.8590,2.3428,
    "Hair clips, barrettes and combs made in France, inside La Samaritaine.", tags=["hair","fashion"])
add("samaritaine","La Samaritaine","shop","Louvre & Tuileries","9 Rue de la Monnaie, 75001 Paris",48.8589,2.3424,
    "Art Nouveau department store by the Pont Neuf, with a glass roof and peacock frieze.", tags=["department store","fashion","beauty","instagram","rainy"])
add("bon-marche","Le Bon Marché","shop","Saint-Germain","24 Rue de Sèvres, 75007 Paris",48.8510,2.3245,
    "The most elegant department store in Paris. Fashion, beauty and the famous escalators.", tags=["department store","fashion","beauty","rainy"])
add("grande-epicerie","La Grande Épicerie de Paris","shop","Saint-Germain","38 Rue de Sèvres, 75007 Paris",48.8507,2.3237,
    "Huge luxury food hall next to Le Bon Marché. The best place for food gifts: chocolate, jams, salted butter caramel.", tags=["food & gifts","rainy"])
add("citypharma","Citypharma","shop","Saint-Germain","26 Rue du Four, 75006 Paris",48.8530,2.3335,
    "The famous cheap pharmacy for French skincare (La Roche-Posay, Avène, Caudalie, Nuxe). Very busy, so go early.",
    hours="Open every day, Sundays until 20:00", tags=["beauty"])
add("diptyque","Diptyque","shop","Latin Quarter","34 Boulevard Saint-Germain, 75005 Paris",48.8497,2.3519,
    "The original Diptyque shop, since 1961. Candles and perfume.", tags=["beauty","home"])
add("merci","Merci","shop","Le Marais","111 Boulevard Beaumarchais, 75003 Paris",48.8604,2.3666,
    "Concept store with fashion, home goods and a café. The red Fiat in the courtyard is the photo.", tags=["fashion","home","instagram"])
add("mariage-freres","Mariage Frères","shop","Le Marais","30 Rue du Bourg-Tibourg, 75004 Paris",48.8578,2.3549,
    "Historic French tea house with a shop and a colonial-style tea room.", tags=["food & gifts","tea room"])
add("sezane","Sézane L'Appartement","shop","Grands Boulevards","1 Rue Saint-Fiacre, 75002 Paris",48.8702,2.3462,
    "The Paris flagship of the French fashion brand, set up like an apartment.", tags=["fashion"])
add("dehillerin","E.Dehillerin","shop","Montorgueil & Les Halles","18 Rue Coquillière, 75001 Paris",48.8636,2.3433,
    "Old chef's cookware shop, open since 1820. Copper pans and kitchen tools.", tags=["home"])
add("shakespeare-books","Shakespeare and Company","shop","Latin Quarter","37 Rue de la Bûcherie, 75005 Paris",48.8526,2.3471,
    "The famous English-language bookshop facing Notre-Dame.", tags=["books","instagram","rainy"])
add("enfants-rouges","Marché des Enfants Rouges","shop","Le Marais","39 Rue de Bretagne, 75003 Paris",48.8628,2.3619,
    "The oldest covered market in Paris, with food stalls for lunch.", hours="Closed Mondays", closed=["mon"], tags=["markets","cheap"])
add("saint-ouen","Marché aux Puces de Saint-Ouen","shop","Saint-Ouen (flea market)","Rue des Rosiers, 93400 Saint-Ouen",48.9017,2.3427,
    "The biggest antiques and flea market in the world. Open Saturday to Monday, so Saturday 31 Oct or Sunday 1 Nov fit your trip.",
    hours="Saturday to Monday", closed=["tue","wed","thu","fri"], tags=["markets","vintage"])
add("tang-freres","Tang Frères","shop","Chinatown","48 Avenue d'Ivry, 75013 Paris",48.8257,2.3628,
    "Huge Asian supermarket. Fun for snacks and sweets.", tags=["food & gifts"])

# ───────── GO ─────────
add("galerie-dior","La Galerie Dior","go","Champs-Élysées","11 Rue François 1er, 75008 Paris",48.8670,2.3047,
    "Dior exhibition. Booked for 30 Oct at 12:30.", hours="11:00 – 19:00, last entry 17:30. Closed Tuesdays.",
    open="11:00-19:00", closed=["tue"], tags=["fashion","museum","rainy"])
add("louvre","Louvre","go","Louvre & Tuileries","Rue de Rivoli, 75001 Paris",48.8611,2.3358,
    "To book. Date not chosen yet.", hours="9:00 – 18:00, Wed and Fri until 21:00. Closed Tuesdays.",
    open="09:00-18:00", openOn={"wed":"09:00-21:00","fri":"09:00-21:00"}, closed=["tue"],
    bookingUrl="https://www.louvre.fr", bookAhead="Book a timed ticket online. Popular slots sell out days ahead.",
    tags=["museum","landmark","to book","rainy"])
add("versailles","Palace of Versailles","go","Versailles (day trip)","Place d'Armes, 78000 Versailles",48.8049,2.1204,
    "To book. Date not chosen yet. Plan for most of a day.", hours="Closed Mondays", closed=["mon"],
    bookingUrl="https://www.chateauversailles.fr", bookAhead="Book a timed ticket online and go early.",
    tags=["landmark","day trip","to book"])
add("orsay","Musée d'Orsay","go","Saint-Germain","Esplanade Valéry Giscard d'Estaing, 75007 Paris",48.8600,2.3266,
    "Impressionists in a former railway station. Don't miss the giant clock window on the 5th floor, looking over the Seine to Sacré-Cœur.",
    hours="9:30 – 18:00, Thu until 21:45. Closed Mondays.", open="09:30-18:00", openOn={"thu":"09:30-21:45"}, closed=["mon"],
    bestTime="Thursday evening is quieter", status="maybe", tags=["museum","view","instagram","rainy"])
add("eiffel-tower","Eiffel Tower","go","Eiffel Tower & Trocadéro","Champ de Mars, 5 Avenue Anatole France, 75007 Paris",48.8584,2.2945,
    "The view from the top is the classic one.", bestTime="After dark it sparkles for 5 minutes every hour on the hour",
    bookingUrl="https://www.toureiffel.paris", bookAhead="Book summit tickets on the official site. They sell out.",
    tags=["landmark","view","to book"])
add("trocadero","Trocadéro","go","Eiffel Tower & Trocadéro","Place du Trocadéro et du 11 Novembre, 75016 Paris",48.8620,2.2880,
    "The best classic view and photo of the Eiffel Tower. Free.", bestTime="Early morning for no crowds, or on the hour after dark for the sparkle",
    tags=["view","instagram","free","landmark"])
add("bir-hakeim","Pont de Bir-Hakeim","go","Eiffel Tower & Trocadéro","Pont de Bir-Hakeim, 75015 Paris",48.8556,2.2877,
    "Two-level bridge with an iron colonnade and an Eiffel Tower view. A popular photo spot.", bestTime="Morning light",
    tags=["instagram","free","view"])
add("invalides","Les Invalides (Napoleon's tomb)","go","Eiffel Tower & Trocadéro","129 Rue de Grenelle, 75007 Paris",48.8565,2.3127,
    "Golden dome with Napoleon's tomb and the army museum.", tags=["museum","landmark","rainy"])
add("sacre-coeur","Sacré-Cœur","go","Montmartre","35 Rue du Chevalier de la Barre, 75018 Paris",48.8867,2.3431,
    "White basilica on the hill with a panoramic view over Paris from the steps. Free entry.", bestTime="Sunset from the steps",
    tags=["view","church","free","landmark"])
add("place-du-tertre","Place du Tertre","go","Montmartre","Place du Tertre, 75018 Paris",48.8865,2.3408,
    "Square full of painters, 2 minutes from Sacré-Cœur. Walk on to Rue de l'Abreuvoir and La Maison Rose.", tags=["free"])
add("moulin-rouge","Moulin Rouge","go","Pigalle & Rue des Martyrs","82 Boulevard de Clichy, 75018 Paris",48.8841,2.3322,
    "The red windmill. Free to see from outside.", bestTime="After dark, when it's lit up", tags=["instagram","landmark","free"])
add("notre-dame","Notre-Dame","go","Île de la Cité","6 Parvis Notre-Dame, 75004 Paris",48.8530,2.3499,
    "Reopened after the restoration. Entry is free. Other sites selling tickets are not official.",
    hours="Weekdays 7:50–19:00 (Thu until 22:00), weekends 8:15–19:30",
    open="07:50-19:00", openOn={"thu":"07:50-22:00","sat":"08:15-19:30","sun":"08:15-19:30"},
    bookingUrl="https://www.notredamedeparis.fr", bookAhead="Free time-slot reservation opens 48 hours ahead. Only use notredamedeparis.fr.",
    tags=["church","free","landmark","to book","rainy"])
add("sainte-chapelle","Sainte-Chapelle","go","Île de la Cité","10 Boulevard du Palais, 75001 Paris",48.8554,2.3450,
    "Chapel with floor-to-ceiling stained glass.", bestTime="A sunny day, when the light comes through the glass",
    bookingUrl="https://www.sainte-chapelle.fr", bookAhead="Book a time slot online.", tags=["church","instagram","to book","rainy"])
add("arc-de-triomphe","Arc de Triomphe","go","Champs-Élysées","Place Charles de Gaulle, 75008 Paris",48.8738,2.2950,
    "Climb to the rooftop for a view down the Champs-Élysées to the Eiffel Tower. Use the underground passage to cross.",
    bestTime="Sunset", tags=["view","landmark"])
add("champs-elysees","Champs-Élysées","go","Champs-Élysées","Avenue des Champs-Élysées, 75008 Paris",48.8698,2.3076,
    "Walk from the Arc de Triomphe down towards Place de la Concorde.", tags=["free","landmark"])
add("musee-ysl","Musée Yves Saint Laurent","go","Champs-Élysées","5 Avenue Marceau, 75116 Paris",48.8650,2.2997,
    "YSL's former couture house. A good match with the Dior gallery.", hours="Closed Mondays", closed=["mon"], tags=["fashion","museum","rainy"])
add("pont-alexandre-iii","Pont Alexandre III","go","Champs-Élysées","Pont Alexandre III, 75008 Paris",48.8639,2.3136,
    "The most ornate bridge in Paris, with gold statues and an Eiffel Tower view.", bestTime="Sunset", tags=["instagram","free","view"])
add("palais-garnier","Palais Garnier","go","Opéra","Place de l'Opéra, 75009 Paris",48.8720,2.3316,
    "The opera house. The grand staircase and foyer are open for visits.", tags=["landmark","instagram","rainy"])
add("galeries-lafayette","Galeries Lafayette","go","Opéra","40 Boulevard Haussmann, 75009 Paris",48.8738,2.3320,
    "See the stained-glass dome inside, then go up to the free rooftop terrace for the view.", bestTime="Sunset on the rooftop",
    tags=["view","free","instagram","rainy","department store"])
add("orangerie","Musée de l'Orangerie","go","Louvre & Tuileries","Jardin des Tuileries, 75001 Paris",48.8638,2.3227,
    "Monet's Water Lilies in two oval rooms. Small, about 1 hour.", hours="9:00 – 18:00. Closed Tuesdays.",
    open="09:00-18:00", closed=["tue"], tags=["museum","rainy"])
add("tuileries","Jardin des Tuileries","go","Louvre & Tuileries","Place de la Concorde to the Louvre, 75001 Paris",48.8635,2.3275,
    "Garden between the Louvre and Place de la Concorde. Good walk between museums.", tags=["garden","free"])
add("palais-royal","Palais-Royal gardens","go","Louvre & Tuileries","8 Rue de Montpensier, 75001 Paris",48.8638,2.3370,
    "Quiet garden with the black-and-white striped columns, a popular photo spot. Café Kitsuné is here.", tags=["garden","instagram","free"])
add("galerie-vivienne","Galerie Vivienne","go","Louvre & Tuileries","4 Rue des Petits Champs, 75002 Paris",48.8665,2.3398,
    "The prettiest covered passage, with a mosaic floor and glass roof.", tags=["instagram","rainy","free"])
add("passage-panoramas","Passage des Panoramas","go","Grands Boulevards","11 Boulevard Montmartre, 75002 Paris",48.8711,2.3418,
    "The oldest covered passage in Paris (1799). Small restaurants and old stamp shops.", tags=["rainy","free"])
add("place-des-vosges","Place des Vosges","go","Le Marais","Place des Vosges, 75004 Paris",48.8556,2.3655,
    "The oldest planned square in Paris, with red-brick arcades. Start a Marais walk here.", tags=["free"])
add("luxembourg","Jardin du Luxembourg","go","Saint-Germain","Rue de Médicis, 75006 Paris",48.8462,2.3372,
    "Palace gardens with the pond and green chairs.", tags=["garden","free"])
add("rue-cremieux","Rue Crémieux","go","Bastille & Gare de Lyon","Rue Crémieux, 75012 Paris",48.8471,2.3708,
    "Pedestrian street of pastel houses. People live here, so keep it quiet.", bestTime="Morning, when it's quiet", tags=["instagram","free"])
add("chinatown","Chinatown","go","Chinatown","Avenue de Choisy, 75013 Paris",48.8270,2.3600,
    "Europe's largest Chinatown, between Avenue de Choisy and Avenue d'Ivry. Pho, dim sum, bubble tea and the Tang Frères supermarket.",
    tags=["neighbourhood","free"])
add("little-tokyo","Little Tokyo (Rue Sainte-Anne)","go","Little Tokyo","Rue Sainte-Anne, 75001 Paris",48.8665,2.3355,
    "The Japanese quarter: ramen, udon, Japanese bakeries and grocery shops, with Korean spots on the side streets.", tags=["neighbourhood"])
add("belleville","Belleville","go","Belleville","Rue de Belleville, 75020 Paris",48.8722,2.3810,
    "Paris's second Chinatown, with street art on Rue Dénoyez and the Parc de Belleville view.", tags=["neighbourhood","free"])
add("little-india","Little India (Passage Brady)","go","Grands Boulevards","46 Rue du Faubourg Saint-Denis, 75010 Paris",48.8722,2.3535,
    "Covered passage full of Indian restaurants.", tags=["neighbourhood"])
add("parc-de-belleville","Parc de Belleville","go","Belleville","47 Rue des Couronnes, 75020 Paris",48.8710,2.3848,
    "Hillside park with one of the best free views over Paris to the Eiffel Tower.", bestTime="Sunset", tags=["view","free","garden"])

# ───────── DO ─────────
add("seine-cruise","Seine river cruise","do","Eiffel Tower & Trocadéro","Port de la Bourdonnais, 75007 Paris",48.8597,2.2930,
    "About 1 hour on the river past the main sights.", bestTime="Evening, when the Eiffel Tower is lit", tags=["boat","evening","view"])
add("marais-walk","Walk around Le Marais","do","Le Marais","Place des Vosges, 75004 Paris",48.8556,2.3655,
    "Small streets, boutiques and cafés. Go from Place des Vosges to Rue des Rosiers and Rue de Bretagne.", tags=["walk","free"])
add("montmartre-walk","Walk around Montmartre","do","Montmartre","Place des Abbesses, 75018 Paris",48.8844,2.3385,
    "Go from Abbesses up to Sacré-Cœur, Place du Tertre, Rue de l'Abreuvoir and La Maison Rose. Take the funicular if you're tired.",
    tags=["walk","free","instagram"])
add("canal-walk","Walk along Canal Saint-Martin","do","Canal Saint-Martin","Quai de Valmy, 75010 Paris",48.8710,2.3640,
    "Iron footbridges, locks and cafés along the water. Combine with Du Pain et des Idées.", tags=["walk","free","instagram"])
add("street-art-denoyez","Street art on Rue Dénoyez","do","Belleville","Rue Dénoyez, 75020 Paris",48.8710,2.3790,
    "A short street covered in ever-changing graffiti.", tags=["free","instagram"])
add("moulin-rouge-show","Moulin Rouge show","do","Pigalle & Rue des Martyrs","82 Boulevard de Clichy, 75018 Paris",48.8841,2.3322,
    "The classic cabaret show.", bookingUrl="https://www.moulinrouge.fr", bookAhead="Book online well ahead. Evening shows sell out.",
    status="maybe", tags=["evening","to book"])


# ───────── manual hour fixes (OSM has seasonal rules the app can't read) ─────────
FIX = {
  "eiffel-tower":   dict(open="09:30-23:45", hours="9:30 – 23:45 every day"),
  "arc-de-triomphe":dict(open="10:00-22:30", hours="10:00 – 22:30 every day"),
  "sainte-chapelle":dict(open="09:00-17:00", hours="9:00 – 17:00 every day (October to March)"),
  "versailles":     dict(open="09:00-17:30", closed=["mon"], hours="9:00 – 18:30 until 31 Oct, 9:00 – 17:30 from 1 Nov. Closed Mondays."),
  "sacre-coeur":    dict(open="06:00-22:30", hours="6:00 – 22:30 every day"),
}
for p in P:
    if p["id"] in FIX: p.update(FIX[p["id"]])

# ───────── opening hours from OpenStreetMap (tools/fetch_hours.py) ─────────
import re as _re
OSM_SKIP = {  # wrong venue matched, or seasonal rules: keep our own info
  "chartier-montparnasse","bouillon-pigalle","kunitoraya","kitsune-palais-royal","du-pain-et-des-idees","palais-royal",
  "rue-cremieux","little-tokyo","belleville","luxembourg","le-perchoir","frenchie-bar-a-vins","moulin-rouge",
  "pont-alexandre-iii","mille-et-un","citypharma","eiffel-tower","arc-de-triomphe","sainte-chapelle","versailles",
  "sacre-coeur","louvre","orsay","notre-dame","galerie-dior","orangerie","maison-caillau",
}
DK = ["mo","tu","we","th","fr","sa","su"]; DKEY = ["mon","tue","wed","thu","fri","sat","sun"]
DNAME = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
def parse_oh(oh):
    s = oh.strip()
    if s == "24/7": return {d: "00:00-24:00" for d in DKEY}, []
    s = _re.sub(r"\b(Mo|Tu|We|Th|Fr|Sa|Su),\s+(?=(Mo|Tu|We|Th|Fr|Sa|Su)\b)", r"\1,", s)
    rules = []
    for part in s.split(";"):
        rules += [r.strip() for r in _re.split(r",\s+(?=(?:Mo|Tu|We|Th|Fr|Sa|Su)(?:-(?:Mo|Tu|We|Th|Fr|Sa|Su))?(?:,(?:Mo|Tu|We|Th|Fr|Sa|Su))*\s+\d)", part) if r.strip()]
    days = {}
    for r in rules:
        if r.startswith("PH") or r.startswith("SH"): continue   # holiday-only rules
        r = _re.sub(r",?\s*PH\b", "", r).strip()
        if not r or _re.search(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|20\d\d)\b", r): continue
        m = _re.match(r"^((?:Mo|Tu|We|Th|Fr|Sa|Su)(?:-(?:Mo|Tu|We|Th|Fr|Sa|Su))?(?:,(?:Mo|Tu|We|Th|Fr|Sa|Su)(?:-(?:Mo|Tu|We|Th|Fr|Sa|Su))?)*)?\s*(.*)$", r)
        spec, times = m.group(1), m.group(2).strip()
        sel = []
        if not spec: sel = list(range(7))
        else:
            for item in spec.split(","):
                if "-" in item:
                    a, b = DK.index(item[:2].lower()), DK.index(item[3:5].lower())
                    i = a
                    while True:
                        sel.append(i)
                        if i == b: break
                        i = (i + 1) % 7
                else: sel.append(DK.index(item.lower()))
        if times in ("off", "closed"): val = None
        else:
            rng = []
            for t in times.split(","):
                t = t.strip()
                mm = _re.match(r"^(\d\d):(\d\d)-(\d\d):(\d\d)$", t)
                if not mm: return None
                end = t[6:]
                if end == "00:00": end = "24:00"
                rng.append(t[:5] + "-" + end)
            if not rng: return None
            val = ",".join(rng)
        for i in sel: days[DKEY[i]] = val
    if not days: return None
    openOn = {k: v for k, v in days.items() if v}
    closed = [k for k, v in days.items() if v is None]
    return openOn, closed

def hours_text(openOn, closed):
    vals = []
    for k in DKEY:
        vals.append(openOn.get(k) if k in openOn else ("closed" if k in closed else None))
    out, i = [], 0
    while i < 7:
        j = i
        while j + 1 < 7 and vals[j + 1] == vals[i]: j += 1
        if vals[i] is not None:
            label = DNAME[i] if i == j else f"{DNAME[i]}–{DNAME[j]}"
            v = "closed" if vals[i] == "closed" else vals[i].replace("-", " – ").replace(",", ", ").replace("24:00", "midnight")
            out.append(f"{label} {v}")
        i = j + 1
    if len(out) == 1 and out[0] == "Mon–Sun 00:00 – midnight": return "Open 24 hours"
    if len(out) == 1 and out[0].startswith("Mon–Sun "): return "Every day " + out[0][8:]
    return " · ".join(out)

OSM_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "osm_hours.json")
osm = json.load(open(OSM_PATH)) if os.path.exists(OSM_PATH) else {}
for p in P:
    r = osm.get(p["id"])
    if not r or p["id"] in OSM_SKIP or "open" in p: continue
    parsed = parse_oh(r["opening_hours"])
    if not parsed: continue
    openOn, closed = parsed
    closed = sorted(set(closed) | set(c for c in p.get("closed", []) if c not in openOn), key=DKEY.index)
    if openOn: p["openOn"] = openOn
    if closed: p["closed"] = closed
    elif "closed" in p: del p["closed"]
    p["hours"] = hours_text(openOn, closed)
    p["hoursSource"] = "osm"

# ───────── average bill / entry price ─────────
PRICE = {
  # eat (per person, main + drink)
  "chartier-grands-boulevards":"€20–30 per person","chartier-montparnasse":"€20–30 per person","chartier-gare-de-lest":"€20–30 per person",
  "les-philosophes":"€30–45 per person","bistrot-paul-bert":"€60–80 per person","fontaine-de-mars":"€50–70 per person",
  "relais-entrecote":"€35–45 per person","au-pied-de-cochon":"€40–60 per person","bouillon-julien":"€20–30 per person",
  "bouillon-pigalle":"€20–30 per person","train-bleu":"€70–100 per person","breizh-cafe":"€20–30 per person",
  "as-du-fallafel":"€10–15 per person","pink-mamma":"€30–45 per person","higuma":"€12–18 per person","kunitoraya":"€20–30 per person",
  "sanukiya":"€15–22 per person","dosanko-larmen":"€15–20 per person","pho-14":"€12–18 per person","dong-huong":"€12–18 per person",
  # drink
  "little-red-door":"€16–18 per cocktail","le-syndicat":"€14–16 per cocktail","candelaria":"€14–16 per cocktail","danico":"€16–18 per cocktail",
  "bar-hemingway":"€30–40 per cocktail","harrys-bar":"€15–20 per cocktail","le-perchoir":"€14–18 per cocktail","les-ombres":"€18–22 per cocktail",
  "terrass-hotel":"€16–20 per cocktail","baron-rouge":"€4–7 per glass of wine","frenchie-bar-a-vins":"€8–14 per glass of wine",
  # cafés (drink + something small)
  "cafe-de-flore":"€10–18 per person","deux-magots":"€10–18 per person","maison-rose":"€15–25 per person","le-consulat":"€15–25 per person",
  "deux-moulins":"€15–25 per person","angelina":"€15–25 per person","kitsune-palais-royal":"€5–10 per person","cafe-marly":"€20–40 per person",
  "boot-cafe":"€5–10 per person","ob-la-di":"€8–15 per person","cafeotheque":"€4–8 per person","shakespeare-cafe":"€5–10 per person",
  "carette":"€15–25 per person","laduree-champs":"€15–30 per person",
  # pastry
  "pierre-herme-bonaparte":"€2.50–3.50 per macaron · €8–10 per pastry","laduree-royale":"€2.50–3.50 per macaron · €8–10 per pastry",
  "carette-vosges":"€2.50–3.50 per macaron · €15–25 sitting down","dalloyau":"€2.50–3.50 per macaron · €7–10 per cake",
  "stohrer":"€5–8 per pastry","fou-de-patisserie":"€6–12 per pastry","cedric-grolet-opera":"€15–20 per pastry","ritz-comptoir":"€4–8 per item",
  "eclair-de-genie":"€6–9 per éclair","jacques-genin":"€10–15 for the millefeuille","sebastien-gaudard":"€6–9 per pastry","mamiche":"€3–6 per item",
  "odette":"€2–4 per cream puff","aki-boulangerie":"€3–8 per item","du-pain-et-des-idees":"€4–6 per pastry","la-parisienne":"€1.50–2.50 per croissant",
  "mille-et-un":"€1.50–2.50 per croissant","rabineau":"€1.50–2.50 per croissant","utopie":"€1.50–6 per item",
  # sights (2026 entry, adult)
  "galerie-dior":"€16 full price · €12 reduced (ages 10–26, students)","louvre":"€22 for EU visitors · €32 for non-EU visitors",
  "orsay":"€16 online · €14 on site · €12 on Thursday evenings · free for EU residents aged 18–25",
  "versailles":"Palace ticket €21 · Passport (whole estate) €35 until 31 Oct, €25 from 1 Nov","sainte-chapelle":"€22","arc-de-triomphe":"€22",
  "orangerie":"€11","invalides":"€17","seine-cruise":"From €17","eiffel-tower":"See the official site",
}
for p in P:
    if p["id"] in PRICE: p["price"] = PRICE[p["id"]]
    elif "free" in p["tags"] and p["cat"] in ("go","do"): p["price"] = "Free"

# Rebuild data.js:  python3 tools/build_data.py   (add --geo to look up new addresses on OpenStreetMap)
# ───────── geocode (OpenStreetMap Nominatim) ─────────
def geocode(q):
    if q in cache: return cache[q]
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode({"q": q, "format": "json", "limit": 1, "countrycodes": "fr"})
    import subprocess
    try:
        out = subprocess.run(["curl","-s","-m","20","-A","paris-trip-app/1.0 (personal trip planner)",url],capture_output=True,text=True).stdout
        res = json.loads(out) if out.strip().startswith("[") else []
    except Exception as e:
        res = []
    time.sleep(1.1)
    cache[q] = [float(res[0]["lat"]), float(res[0]["lon"])] if res else None
    json.dump(cache, open(CACHE, "w"))
    return cache[q]

def dist(a, b):
    R=6371; r=math.radians
    h=math.sin(r(b[0]-a[0])/2)**2+math.cos(r(a[0]))*math.cos(r(b[0]))*math.sin(r(b[1]-a[1])/2)**2
    return 2*R*math.asin(math.sqrt(h))

report = []
if "--geo" in sys.argv:
    for p in P:
        q = p["address"]
        g = geocode(q)
        if g and dist(g, (p["lat"], p["lng"])) < 1.2:
            p["lat"], p["lng"] = round(g[0], 5), round(g[1], 5)
            report.append(f"ok    {p['id']:28} {dist(g,(p['lat'],p['lng'])):.2f}")
        else:
            report.append(f"KEEP  {p['id']:28} geocode={g} manual=({p['lat']},{p['lng']})" + (f" d={dist(g,(p['lat'],p['lng'])):.2f}km" if g else ""))
    print("\n".join(r for r in report if r.startswith("KEEP")))
    print(sum(r.startswith("ok") for r in report), "geocoded,", sum(r.startswith("KEEP") for r in report), "kept manual")

ids = [p["id"] for p in P]; assert len(ids) == len(set(ids)), "duplicate ids"

# ───────── write data.js ─────────
def js(v):
    return json.dumps(v, ensure_ascii=False)

ORDER = ["id","name","cat","area","address","lat","lng","price","order","drinks","notes","bestTime","hours","hoursSource","open","openOn","closed","bookingUrl","bookAhead","price","link","status","tags"]
def place_js(p):
    lines = []
    for k in ORDER:
        if k in p:
            lines.append(f"    {k}: {js(p[k])},")
    return "  {\n" + "\n".join(lines) + "\n  },"

sections = [("eat","Eat"),("drink","Drink"),("cafe","Cafés"),("pastry","Pastry"),("shop","Shop"),("go","Go"),("do","Do")]
body = []
for cat, label in sections:
    body.append(f"\n  // ── {label} ──")
    body += [place_js(p) for p in P if p["cat"] == cat]

INFO = {
  "sections": [
    {"id":"getting","title":"Getting around","c":"do","items":[
      {"t":"Metro, RER and train ticket: €2.55","d":"One ticket per journey anywhere in the Paris region (2026 price). Bus and tram tickets are €2.05. Paper tickets are gone: load tickets onto a Navigo Easy card (€2 at station counters and machines) or onto your phone in the Île-de-France Mobilités app."},
      {"t":"You can't tap a bank card at metro gates yet","d":"Contactless bank cards only work on buses and a few lines for now. Buy a ticket first."},
      {"t":"Arriving at Gare du Nord","d":"Your Eurostar arrives at Gare du Nord. From there, metro lines 4 and 5 and the RER B, D and E go across the city. The official taxi rank is outside the station; ignore anyone offering a ride inside."},
      {"t":"Taxis from the station","d":"Taxis from Gare du Nord run on the meter (the fixed fares are only for the airports). Uber, Bolt and G7 also pick up here."},
      {"t":"Uber, Bolt and G7","d":"All work in Paris. G7 is the main official taxi company and has its own app."},
      {"t":"Walking","d":"Central Paris is compact. Most places in this app are 15–30 minutes apart on foot, and walking is often faster than the metro for short trips."},
      {"t":"Montmartre funicular","d":"Takes you up the hill to Sacré-Cœur on a normal metro ticket."},
    ]},
    {"id":"know","title":"Good to know","c":"cafe","items":[
      {"t":"Always say “Bonjour”","d":"When you walk into a shop, café or bakery, say bonjour first. It makes a big difference to how you're treated."},
      {"t":"Tipping","d":"Service is already included in the price. Round up or leave €1–2 for coffee, and 5–10% for great service at dinner if you like."},
      {"t":"Tap water is free","d":"Ask for “une carafe d'eau” instead of bottled water."},
      {"t":"Coffee costs more at a table","d":"Standing at the bar is cheaper than sitting at a table or on the terrace."},
      {"t":"Meal times","d":"Lunch is 12:00–14:30 and dinner usually starts 19:30. Many restaurants close between lunch and dinner, but brasseries and bouillons serve all day."},
      {"t":"Museum closing days","d":"The Louvre, Orangerie and Dior gallery close on Tuesdays. Musée d'Orsay, Versailles and Musée Yves Saint Laurent close on Mondays."},
      {"t":"Sunday 1 November is a public holiday","d":"All Saints' Day. Many shops and some bakeries are closed. Most museums and sights stay open."},
      {"t":"Winter time","d":"France changes to winter time on 25 October, before you arrive. Sunset is around 17:30, so plan views and photos for about 17:00."},
      {"t":"Plugs","d":"Type E sockets, 230 V."},
      {"t":"What to drink","d":"Café crème is coffee with milk, “un café” is an espresso. Try a kir (white wine with blackcurrant liqueur) or kir royal (with champagne) as an apéritif."},
    ]},
    {"id":"avoid","title":"Tourist traps to avoid","c":"drink","items":[
      {"t":"Friendship-bracelet sellers","d":"Mostly at the bottom of the Sacré-Cœur steps. They tie a bracelet on your wrist, then demand money. Keep your hands in your pockets and keep walking."},
      {"t":"Petition clipboards","d":"People asking you to sign a petition near the Eiffel Tower and Louvre. It's a distraction for pickpocketing. Say no and walk on."},
      {"t":"The “found a gold ring” trick","d":"Someone ‘finds’ a ring next to you and offers to sell it. It's fake."},
      {"t":"Shell games on bridges","d":"The players in the crowd are part of the team. You can't win."},
      {"t":"Pickpockets","d":"Most common on metro lines 1 and 4, the RER B, at Gare du Nord and around the Eiffel Tower. Don't leave your phone on a café table by the street."},
      {"t":"Unofficial taxis","d":"Ignore anyone offering a ride inside the airport. Use the official taxi rank or an app."},
      {"t":"Restaurants right next to top sights","d":"Places with picture menus and people inviting you in are usually poor value. Walk two streets away."},
      {"t":"Fake Notre-Dame tickets","d":"Entry is free. Only reserve on notredamedeparis.fr."},
      {"t":"Currency exchange counters","d":"Rates at airports and tourist areas are bad. Pay by card, and if a card machine asks, choose to pay in euros."},
    ]},
  ],
  "phrases": [
    {"fr":"Bonjour / Bonsoir","say":"bohn-zhoor / bohn-swahr","en":"Hello / Good evening. Say it when you walk in anywhere."},
    {"fr":"Merci (beaucoup)","say":"mehr-see (boh-koo)","en":"Thank you (very much)"},
    {"fr":"S'il vous plaît","say":"seel voo pleh","en":"Please"},
    {"fr":"Pardon / Excusez-moi","say":"par-dohn / ex-kew-zay mwah","en":"Sorry / Excuse me"},
    {"fr":"Parlez-vous anglais ?","say":"par-lay voo ahn-gleh","en":"Do you speak English?"},
    {"fr":"Une table pour deux, s'il vous plaît","say":"ewn tah-bluh poor duh","en":"A table for two, please"},
    {"fr":"Je voudrais…","say":"zhuh voo-dreh","en":"I would like…"},
    {"fr":"Deux croissants, s'il vous plaît","say":"duh krwah-sahn","en":"Two croissants, please"},
    {"fr":"Une boîte de macarons","say":"ewn bwaht duh ma-ka-rohn","en":"A box of macarons"},
    {"fr":"Un café / Un café crème","say":"uhn ka-fay / ka-fay krem","en":"An espresso / A coffee with milk"},
    {"fr":"Un chocolat chaud","say":"uhn sho-ko-la shoh","en":"A hot chocolate"},
    {"fr":"Une carafe d'eau","say":"ewn ka-raf doh","en":"A jug of tap water (free)"},
    {"fr":"Sur place / À emporter","say":"sewr plahs / ah ahm-por-tay","en":"To eat in / To take away"},
    {"fr":"L'addition, s'il vous plaît","say":"la-dee-syohn","en":"The bill, please"},
    {"fr":"C'est combien ?","say":"say kohm-byan","en":"How much is it?"},
    {"fr":"Où sont les toilettes ?","say":"oo sohn lay twa-let","en":"Where are the toilets?"},
    {"fr":"Je suis allergique à…","say":"zhuh swee a-lehr-zheek ah","en":"I'm allergic to…"},
    {"fr":"Au revoir, bonne journée","say":"oh ruh-vwahr, bun zhoor-nay","en":"Goodbye, have a good day"},
  ],
  "emergency": [
    {"num":"112","t":"All emergencies","d":"Works from any phone. English spoken."},
    {"num":"15","t":"Medical emergency (SAMU)","d":""},
    {"num":"17","t":"Police","d":""},
    {"num":"18","t":"Fire brigade","d":""},
    {"num":"114","t":"Emergency by text message","d":"If you can't speak on the phone."},
  ],
}

DAY_NOTES = {
  "2026-10-28": "Arrival day: train arrives at Gare du Nord at 11:43. Idea for lunch: Bouillon Chartier Gare de l'Est is a short walk from the station. The Louvre is open until 21:00 tonight.",
  "2026-10-29": "Thursday. Musée d'Orsay is open until 21:45 and Notre-Dame until 22:00, good for an evening visit.",
  "2026-10-30": "Friday. Dior exhibition at 12:30. The Louvre is open until 21:00.",
  "2026-10-31": "Saturday. Busiest day at museums and shops. L'As du Fallafel is closed. The Saint-Ouen flea market is open.",
  "2026-11-01": "Sunday and a public holiday (All Saints' Day). Many shops and some bakeries are closed; most museums and sights stay open. The Saint-Ouen flea market is open.",
  "2026-11-02": "Departure day: train leaves Gare du Nord at 18:15. Ask the hotel to keep your bags after check-out. Musée d'Orsay, Versailles, Musée Yves Saint Laurent and the Marché des Enfants Rouges are closed on Mondays.",
}

out = f'''// ─────────────────────────────────────────────────────────────
// Trip content. This is the only file that holds your plans.
// ─────────────────────────────────────────────────────────────

const TRIP = {{
  title: "Paris",
  start: "2026-10-28",
  end: "2026-11-02",    // departure day
  arrival:   {{ time: "11:43", where: "Gare du Nord" }},
  departure: {{ time: "18:15", where: "Gare du Nord" }},
  stay: null,           // hotel being booked: {{ name: "", address: "", phone: "", lat: 0, lng: 0 }}
}};

// cat: "eat" | "drink" | "cafe" | "pastry" | "shop" | "go" | "do"
// status: "want" | "maybe" | "skip"
// open: "HH:MM-HH:MM" every day · openOn: per-day hours · closed: days it's shut
// tags drive the filters and lists: "view", "instagram", "neighbourhood", "rainy", "free", "to book", …
const PLACES = [{"".join(chr(10) + b for b in body)}
];

// Planned and booked things, shown in the calendar.
const EVENTS = [
  {{
    id: "train-to-paris",
    date: "2026-10-28",
    start: "08:10",
    end: "11:43",
    title: "Eurostar to Paris",
    where: "Paris Gare du Nord",
    address: "18 Rue de Dunkerque, 75010 Paris",
    booked: true,
    details: [
      ["From", "Amsterdam Centraal 08:10"],
      ["To", "Paris Gare du Nord 11:43"],
      ["Class", "Eurostar Standard · direct, 3 h 33 min"],
      ["Coach", "17"],
      ["Seats", "31 and 32"],
    ],
    notes: "",
  }},
  {{
    id: "train-home",
    date: "2026-11-02",
    start: "18:15",
    end: "21:50",
    title: "Eurostar home",
    where: "Paris Gare du Nord",
    address: "18 Rue de Dunkerque, 75010 Paris",
    booked: true,
    details: [
      ["From", "Paris Gare du Nord 18:15"],
      ["To", "Amsterdam Centraal 21:50"],
      ["Class", "Eurostar Standard · direct, 3 h 35 min"],
      ["Coach", "16"],
      ["Seats", "31 and 32"],
    ],
    notes: "Gare du Nord is busy at rush hour. Leave enough time to get there with your bags.",
  }},
  {{
    id: "dior-exhibition",
    date: "2026-10-30",
    start: "12:30",
    title: "Dior exhibition",
    placeId: "galerie-dior",
    booked: true,
    confirmation: "",
    notes: "3 tickets. Open them under Plan → Our tickets on your phone. Entry is guaranteed within 30 minutes of your time slot. No large bags or suitcases allowed inside.",
  }},
];

// Notes shown on each day in the Plan tab.
const DAY_NOTES = {json.dumps(DAY_NOTES, ensure_ascii=False, indent=2)};

// Info tab.
const INFO = {json.dumps(INFO, ensure_ascii=False, indent=2)};
'''
open(OUT, "w").write(out)
print("wrote", len(P), "places")
