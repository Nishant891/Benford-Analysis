
# 📊 Benford's Law Financial Analyzer

This project provides a shell-based tool to convert financial PDF reports (such as annual earnings, balance sheets, and income statements) into plain text for analysis using Benford’s Law and other statistical methods.

---

## 📁 Project Structure

- `converter.sh` — A simple shell script that uses `pdftotext` to extract readable data from financial PDFs.
- `data.txt` — The output file generated from a company’s financial report.
- `benfords_analysis.py` — Python script (optional) to analyze extracted data for statistical anomalies.
- `requirements.txt` — Python dependencies used in the analysis.

---

## 🔧 Dependencies

- **System Packages**
  - `poppler` (for `pdftotext`)
    ```bash
    sudo pacman -S poppler
    ```
  - `tk` (if using GUI with `tkinter`)
    ```bash
    sudo pacman -S tk
    ```

- **Python Libraries**
  Install with:
  ```bash
  pip install -r requirements.txt
  ```

---

## 🛠 Usage

### 1. Convert PDF Report to Text

Make the script executable:

```bash
chmod +x converter.sh
```

Then run:

```bash
./converter.sh reports.pdf data.txt
```

This will extract text from `reports.pdf` and save it into `data.txt`.

> Ensure that your input PDF is a machine-readable financial report (not scanned or image-based).

---

## 📈 Analyze the Data (Optional)

If you have a Python script to perform Benford's Law analysis, you can run:

```bash
python3 benfords_analysis.py data.txt
```

Make sure the script is set to parse the numeric content correctly.

---

## 📌 Notes

- Works best with structured financial PDFs (from public company disclosures).
- You can modify `converter.sh` for batch processing or format-specific parsing.

---

## 🧑‍💻 Author

Nishant Sharma  
Made with 💻 on Arch Linux.
