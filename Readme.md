# Rent Share Calculator

A tiny desktop app (Tkinter, Python 3) that helps roommates split monthly costs fairly based on a formula and values stored in a CSV file.

> **Why this exists**: enter the month’s utilities and click **Calculate**. Rent, internet, and room price offsets are read from `Values.csv` so you don’t have to retype them, just change this in CSV file.

---

## Screenshots

> *Add a screenshot of the app window here once you run it (optional).*
> On macOS: `Shift ⌘ 4` • Windows: `Win + Shift + S` • Linux: your favorite tool

---

## Features

* Single‑window GUI built with Tkinter
* Reads configuration from editable `Values.csv`
* Press **Enter** to calculate
* Clear error message if utilities input is invalid

---

## How the share is calculated

Let:

* `rent` = total monthly rent
* `internet` = monthly internet bill
* `utilities` = monthly utilities you type in (power/water/etc.)
* `room1`, `room2` = fixed room offsets (e.g., if one room is larger, use a positive value for that room)
* `people = 2`

The calculation is:

```
share = (rent + internet + utilities - (room1 + room2)) / people
```

Each roommate’s base share is the same; individual room adjustments can be handled outside the app (or by extending it—see **Roadmap**).

---

## Quick start

### 1) Requirements

* **Python 3.9+** (works with 3.12 too)
* Tkinter comes with most Python installers. If missing on Linux: `sudo apt-get install python3-tk` (Debian/Ubuntu) or your distro equivalent.

### 2) Project structure

```
rent-share-calculator/
├── share_calc.py           # main Tkinter app (see code below)
├── Values.csv       # configuration (see example below)
└── README.md
```

### 3)  `Values.csv` is included

A single header row and a single data row are expected:

```csv
rent,internet,room1,room2
2000,80,500,800
```

> **Tip**: `room1` and `room2` are offsets that sum to the total room premium/discount. Positive means that room pays **more**; negative means that room pays **less**.

### 4) Run it

```bash
python app.py
```

Press **Enter** or click **Calculate** after typing the utilities amount.

---

## Packaging&#x20;

Create a single-file executable so roommates don’t need Python.

* **Windows**

  ```bash
  pip install pyinstaller
  pyinstaller --noconfirm --onefile --windowed share_calc.py
  ```

  Output is under `dist/app.exe`.

* **macOS (Intel/Apple Silicon)**

  ```bash
  pip install pyinstaller
  pyinstaller --noconfirm --onefile --windowed share_calc.py
  ```

  Output is under `dist/app`.

> You may need to allow the app in System Settings → Privacy & Security if macOS flags it.


---

## Troubleshooting

* **`Configuration Error: Config file not found`** → ensure `Values.csv` is in the same folder as `app.py`.
* **`Non-numeric value`** → verify all values in the data row are numbers.
* **No window appears on Linux** → ensure Tkinter is installed (see Requirements).


