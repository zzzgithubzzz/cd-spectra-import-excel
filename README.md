# CD Spectra Batch Import and Visualization Script

This Python script automates the import, pruning, and visualization of multiple circular dichroism (CD) spectrum `.txt` files. It is designed for researchers who need to extract the data section from many files, combine them into a single Excel sheet (wide format), and visualize all spectra together.

## Features

- **Batch Import:** Reads all `.txt` files in a specified folder.
- **Header Skipping:** Only imports the data section after the `XYDATA` marker in each file.
- **Wide Format Output:** Combines all spectra into a single Excel file, with each file's `CD_mdeg` values as a separate column aligned by wavelength.
- **Automated Plotting:** Plots all spectra together, with each curve labeled by filename.
- **Customizable:** Axis limits and plot appearance can be easily adjusted in the script.

## How to Use

1. **Install dependencies:**
    ```
    pip install pandas matplotlib openpyxl
    ```

2. **Edit the script:**
    - Set the `folder` variable near the top of the script to the path containing your CD `.txt` files.

3. **Run the script:**
    ```
    python cd_spectra_wide.py
    ```

4. **Results:**
    - `cd_spectra_wide.xlsx` will appear in your data folder, containing all spectra in wide format.
    - A plot window will display all spectra for visual comparison.

## File Format Assumptions

- Each `.txt` file contains metadata, followed by a line with `XYDATA`, then tab-delimited data columns:
    ```
    (metadata lines)
    XYDATA
    260.0   4.5   0.1   0.02
    261.0   4.3   0.1   0.02
    ...
    ```

- Columns are assumed to be: `Wavelength`, `CD_mdeg`, `HT_V`, `Absorbance`.

## Customization

- To adjust axis ranges, uncomment and edit the `plt.xlim()` and `plt.ylim()` lines in the script.
- To further process or normalize data, modify the pandas DataFrame operations as needed.

## How This Script Evolved

This script was developed in response to a real-world need to automate the batch import and analysis of CD spectrum data, as discussed in detail [here](https://github.com/yourusername/yourrepo/issues/1) (link to your discussion or issue if desired). It is designed for robust, reproducible scientific data processing and visualization.

## License

MIT License (or your choice)

## Contributions

Pull requests and suggestions are welcome!

---

**Contact:**  
For questions or improvements, please open an issue or contact the maintainer.
