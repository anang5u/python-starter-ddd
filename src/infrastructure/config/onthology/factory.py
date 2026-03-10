import json

# Fungsi untuk memuat patterns dari file JSONL
def load_dimension_patterns():
    metadata_map = {}
    patterns = []
    file_path = "config/onthology/dimensions.jsonl"
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            # Simpan pattern untuk spaCy
            patterns.append({"label": item["label"], "pattern": item["pattern"]})
            # Simpan metadata untuk mapping hasil akhir
            metadata_map[item["pattern"]] = item["data"]
    return metadata_map, patterns