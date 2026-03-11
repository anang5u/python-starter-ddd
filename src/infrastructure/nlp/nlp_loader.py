import spacy

# 1. Setup NLP Pipeline
# nlp = spacy.load("id_core_news_lg")
# ruler = nlp.add_pipe("entity_ruler", before="ner")
# Membuat pipeline kosong bahasa Indonesia
nlp = spacy.blank("id")

# Menambahkan entity_ruler
# ruler = nlp.add_pipe("entity_ruler")

# Opsi B: Jika ingin tetap ada urutan dengan NER (harus buat ner dulu)
nlp.add_pipe("ner")
ruler = nlp.add_pipe("entity_ruler", before="ner")

# 3. WAJIB: Inisialisasi pipeline
# Ini akan menyiapkan komponen 'ner' agar siap digunakan meskipun masih kosong
nlp.initialize()