import uuid
import re
import json
from typing import List
from infrastructure.config.onthology.factory import load_ontology_patterns
from infrastructure.nlp.nlp_loader import nlp, ruler
from domain.entities.dimension import Dimension

# Load Patterns dan Mapping Metadata
dimension_meta, dimension_patterns = load_ontology_patterns("config/onthology/dimension.jsonl")
ruler.add_patterns(dimension_patterns)

def log_suggestion(name: str, log_file: str = "output/suggestion/dimensions.jsonl"):
    """Mencatat dimensi baru ke file log untuk kurasi manual."""
    suggested_code = re.sub(r"\s+", "_", name.lower().strip())
    suggestion = {
        "label": "DIMENSION",
        "pattern": name,
        "data": {
            "code": suggested_code,
            "name": name,
            "desc": f"Dimensi berdasarkan {name.lower()}"
        }
    }
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(suggestion) + "\n")

def identify_dimensions(title: str) -> List[Dimension]:
    results = []
    registered_texts = []

    # 1. Identifikasi yang REGISTERED (Gunakan spaCy EntityRuler)
    doc = nlp(title)
    for ent in doc.ents:
        if ent.label_ == "DIMENSION":
            meta = dimension_meta.get(ent.text)
            if meta:
                results.append(Dimension(
                    id=uuid.uuid4(),
                    code=meta["code"],
                    name=meta["name"],
                    description=meta.get("desc", "")
                ))
                registered_texts.append(ent.text.lower())

    # 2. Identifikasi yang UNREGISTERED menggunakan Regex
    # Pola: Ambil teks di antara 'Berdasarkan' dan 'di' (non-greedy)
    match = re.search(r"(?i)berdasarkan\s+(.*?)\s+di\b", title)
    
    if match:
        dimension_section = match.group(1)
        
        # Split menggunakan regex: memisahkan berdasarkan 'dan', 'serta', atau tanda koma/titik koma
        # \s+dan\s+ | \s+serta\s+ | [,/]
        raw_parts = re.split(r"\s+dan\s+|\s+serta\s+|[,/]", dimension_section)
        
        for part in raw_parts:
            clean_name = part.strip()
            if not clean_name:
                continue
            
            # Normalisasi untuk pengecekan (case-insensitive)
            clean_lower = clean_name.lower()
            
            # Cek apakah bagian ini sudah tercover oleh entitas REGISTERED
            # (misal: 'Jenis Kelamin' sudah ada di registered_texts)
            is_registered = any(clean_lower == reg or reg in clean_lower or clean_lower in reg 
                               for reg in registered_texts)
            
            if not is_registered:
                results.append(Dimension(
                    id=uuid.uuid4(),
                    code="UNREGISTERED",
                    name=clean_name,
                    description=f"Dimensi '{clean_name}' belum terdaftar di metadata resmi"
                ))

                # Otomatis catat ke log untuk peninjauan
                log_suggestion(clean_name)

    return results


# --- UJI COBA ---
# title_test = "Jumlah Penduduk Berdasarkan Jenis Kelamin dan Kabupaten/Kota di Jawa Barat"
# title_test = "Produktivitas Tanaman Tahunan Komoditi Karet Berdasarkan Kabupaten/Kota di Jawa Barat"

# "Pendidikan" belum ada di JSONL kita
# title_test = "Jumlah Lulusan Berdasarkan Jenis Kelamin dan Pendidikan di Jawa Barat"

title_test = "Tingkat Konsumsi Kelompok Pangan Padi-Padian Berdasarkan Jenis Pangan dan Kabupaten/Kota di Jawa Barat"

dimensions = identify_dimensions(title_test)

for d in dimensions:
    print(d)
