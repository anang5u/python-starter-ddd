import os
import json

def load_ontology_patterns(file_path: str):
    """
    Memuat patterns dari file JSONL untuk metadata Ontologi.
    Dapat digunakan untuk dimension.jsonl maupun measure.jsonl.
    """
    metadata_map = {}
    patterns = []
    
    if not os.path.exists(file_path):
        print(f"Peringatan: File {file_path} tidak ditemukan.")
        return metadata_map, patterns

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line: continue
            
            item = json.loads(line)
            pattern_text = item["pattern"]
            
            # Simpan pattern untuk recognizer (spaCy/Regex)
            patterns.append({
                "label": item["label"], 
                "pattern": pattern_text
            })
            
            # Simpan metadata lengkap untuk mapping hasil akhir
            metadata_map[pattern_text] = item["data"]
            
    return metadata_map, patterns