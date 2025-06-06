import os
import pandas as pd
import matplotlib.pyplot as plt

# === USER INPUT: Set your folder path ===
folder = 'PATH_TO_YOUR_FOLDER'  # <-- Replace with your folder containing .txt files

# Dictionary to store each file's spectrum as a pandas Series
spectra = {}

for filename in os.listdir(folder):
    if filename.endswith('.txt'):
        filepath = os.path.join(folder, filename)
        with open(filepath, 'r') as f:
            lines = f.readlines()
        # Find the line after 'XYDATA'
        data_start = None
        for idx, line in enumerate(lines):
            if line.strip() == 'XYDATA':
                data_start = idx + 1
                break
        if data_start is None:
            continue  # Skip files without XYDATA
        # Parse data lines
        data_lines = [l.strip() for l in lines[data_start:] if l.strip()]
        data = [l.split('\t') for l in data_lines]
        if not data:
            continue
        df = pd.DataFrame(data, columns=['Wavelength', 'CD_mdeg', 'HT_V', 'Absorbance'])
        # Convert to numeric
        df['Wavelength'] = pd.to_numeric(df['Wavelength'], errors='coerce')
        df['CD_mdeg'] = pd.to_numeric(df['CD_mdeg'], errors='coerce')
        # Use filename (without extension) as column name
        colname = os.path.splitext(filename)[0]
        # Store as Series with Wavelength as index
        spectra[colname] = df.set_index('Wavelength')['CD_mdeg']

# Combine all spectra into a single DataFrame, aligning by Wavelength
if spectra:
    combined_df = pd.DataFrame(spectra)
    combined_df.index.name = 'Wavelength'
    output_path = os.path.join(folder, 'cd_spectra_wide.xlsx')
    combined_df.to_excel(output_path)
    print(f'Data exported to {output_path}')

    # --- Plotting ---
    plt.figure(figsize=(8, 5))
    for col in combined_df.columns:
        plt.plot(combined_df.index, combined_df[col], label=col)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('CD [mdeg]')
    plt.title('CD Spectra (Wide Format)')
    plt.legend(fontsize='small', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    # Optionally adjust axes:
    # plt.xlim(200, 300)
    # plt.ylim(-10, 10)
    plt.show()
else:
    print('No data found to export.')
