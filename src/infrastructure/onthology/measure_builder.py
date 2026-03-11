import re
import json
import uuid
from typing import List, Dict, Optional
from domain.entities.measure import Measure
from infrastructure.config.onthology.factory import load_ontology_patterns
from infrastructure.nlp.nlp_loader import nlp, ruler

# Load Patterns dan Mapping Metadata
measure_meta, measure_patterns = load_ontology_patterns("config/onthology/measure.jsonl")
ruler.add_patterns(measure_patterns)

def log_measure_suggestion(name: str, log_file: str = "output/suggestion/measures.jsonl"):
    """Mencatat kandidat measure baru untuk ditinjau."""
    suggested_code = re.sub(r"\s+", "_", name.lower().strip())
    suggestion = {
        "label": "MEASURE",
        "pattern": name,
        "data": {
            "code": suggested_code,
            "unit": "TBD",
            "desc": f"Metrik pengukuran untuk {name.lower()}"
        }
    }
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(suggestion) + "\n")

def identify_measure(title: str, measure_metadata: Dict) -> Optional[Measure]:
    # 1. Cek REGISTERED Measure (Exact Match dari JSONL)
    for pattern, meta in measure_metadata.items():
        if re.search(rf"\b{re.escape(pattern)}\b", title, re.IGNORECASE):
            return Measure(
                id=uuid.uuid4(),
                code=meta["code"],
                name=meta["name"],
                unit=meta.get("unit", "-"),
                description=meta["desc"]
            )

    # 2. Cek UNREGISTERED Measure (Heuristic: Ambil teks sebelum 'Berdasarkan')
    match = re.search(r"^(.*?)\s+Berdasarkan", title, re.IGNORECASE)
    if match:
        raw_name = match.group(1).strip()
        # Catat ke log untuk pendaftaran masa depan
        log_measure_suggestion(raw_name)
        
        return Measure(
            id=uuid.uuid4(),
            code="UNREGISTERED",
            name=raw_name,
            unit="UNKNOWN",
            description=f"Measure '{raw_name}' belum terdaftar di metadata resmi"
        )
    
    return None

# --- EKSEKUSI ---
measure_official = {
    "Jumlah Penduduk": {"code": "pop_count", "name": "Jumlah Penduduk", "desc": "Total cacah jiwa", "unit": "Orang"}
}

titles = [
    "Jumlah Penduduk Berdasarkan Jenis Kelamin di Jawa Barat",
    "Produktivitas Tanaman Karet Berdasarkan Kabupaten/Kota di Jawa Barat"
]

for t in titles:
    m = identify_measure(t, measure_official)
    if m:
        print(f"Title: {t}\nResult: {m}\n")