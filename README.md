# 🧠 PDF Outline Extractor
**Adobe India Hackathon – Round 1**

This project implements a lightweight and intelligent **PDF outline extractor** that identifies and structures document content based on font sizes — mimicking how a human would identify headings in a document.

Using `PyMuPDF`, it processes one or more PDFs and outputs a clean JSON outline with:
- 📌 Title
- 🏷️ Headings: H1, H2, H3 (based on font size)
- 📄 Page numbers for each heading

---

## 🧰 Tech Stack

- **Python 3.10**
- **PyMuPDF (fitz) v1.23.5**
- **Docker** (for portability and isolation)

---

## 📂 Input / Output

- **Input**: Place all PDFs inside the `input/` directory.
- **Output**: For each PDF, a corresponding `.json` file will be generated in `output/`.

---

## 🐳 How to Build & Run

### 🔧 Build  & Run the Docker Image
```bash
docker build --platform linux/amd64 -t pdfoutline:solution .
docker run --rm -v ${PWD}\input:/app/input -v ${PWD}\output:/app/output --network none pdfoutline:solution

