import os
import fitz  # PyMuPDF
import json

def classify_heading(size):
    if size >= 18:
        return "H1"
    elif size >= 14:
        return "H2"
    elif size >= 12:
        return "H3"
    return None

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = ""
    seen = set()

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                text = " ".join([span["text"].strip() for span in line["spans"] if span["text"].strip()])
                if not text or text in seen:
                    continue
                size = line["spans"][0]["size"]
                level = classify_heading(size)
                if level:
                    seen.add(text)
                    outline.append({
                        "level": level,
                        "text": text,
                        "page": page_num + 1
                    })

    if outline:
        title = outline[0]["text"]

    return {
        "title": title,
        "outline": outline
    }

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            full_path = os.path.join(input_dir, filename)
            result = extract_outline(full_path)
            output_file = filename.replace(".pdf", ".json")
            with open(os.path.join(output_dir, output_file), "w") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
