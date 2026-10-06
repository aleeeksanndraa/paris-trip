# Looks up opening hours for every place on OpenStreetMap (one Overpass request)
# and saves the matches to tools/osm_hours.json for build_data.py to use.
#   python3 tools/fetch_hours.py
import json, os, re, subprocess, unicodedata, math, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.argv = [sys.argv[0]]                      # build_data runs without --geo when imported
import importlib.util
spec = importlib.util.spec_from_file_location("bd", os.path.join(HERE, "build_data.py"))
bd = importlib.util.module_from_spec(spec); spec.loader.exec_module(bd)

STOP = set("cafe le la les de des du d l boulangerie bar restaurant paris patisserie bouillon maison the and chez musee "
           "rue avenue place pont jardin walk around along show street art on a au aux et".split())
def norm(s):
    s = unicodedata.normalize("NFD", s); s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]+", " ", s.lower())
def keys(name):
    return [w for w in norm(name.split("·")[0] + " " + (name.split("·")[1] if "·" in name else "")).split() if len(w) >= 4 and w not in STOP]

places = [p for p in bd.P if p["cat"] in ("eat","drink","cafe","pastry","shop","go")]
import time
els = []
for i in range(0, len(places), 20):
    batch = places[i:i+20]
    q = "[out:json][timeout:90];(" + "".join(f'nwr(around:120,{p["lat"]},{p["lng"]})[name][opening_hours];' for p in batch) + ");out tags center;"
    for attempt in range(3):
        out = subprocess.run(["curl", "-s", "-m", "120", "-A", "paris-trip-app/1.0", "--data-urlencode", f"data={q}",
                              "https://overpass-api.de/api/interpreter"], capture_output=True, text=True).stdout
        try: els += json.loads(out)["elements"]; break
        except Exception: time.sleep(8)
    else: print("batch", i, "failed")
    time.sleep(3)
print(len(els), "OSM venues with hours nearby")

def dist(a, b):
    R=6371; r=math.radians
    h=math.sin(r(b[0]-a[0])/2)**2+math.cos(r(a[0]))*math.cos(r(b[0]))*math.sin(r(b[1]-a[1])/2)**2
    return 2*R*math.asin(math.sqrt(h))*1000

res = {}
for p in places:
    k = keys(p["name"])
    best = None
    for e in els:
        c = e.get("center") or {"lat": e.get("lat"), "lon": e.get("lon")}
        if c["lat"] is None: continue
        d = dist((p["lat"], p["lng"]), (c["lat"], c["lon"]))
        if d > 150: continue
        on = norm(e["tags"].get("name", ""))
        if k and any(w in on.split() or w in on for w in k):
            if not best or d < best[0]: best = (d, e)
    if best:
        res[p["id"]] = {"osm_name": best[1]["tags"]["name"], "opening_hours": best[1]["tags"]["opening_hours"], "m": round(best[0])}
prev_path = os.path.join(HERE, "osm_hours.json")
prev = json.load(open(prev_path)) if os.path.exists(prev_path) else {}
prev.update(res); res = prev
json.dump(res, open(prev_path, "w"), ensure_ascii=False, indent=1)
print(len(res), "of", len(places), "matched")
for pid, r in res.items(): print(f"{pid:28} {r['m']:4}m  {r['osm_name'][:30]:30}  {r['opening_hours']}")
