# ECB Interest Rate History

This project fetches and analyzes historical interest rate data from the European Central Bank (ECB). The project uses Python for data fetching, processing, and visualization.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/dynamique1/ecb_interestrate_history.git
    cd ecb_interestrate_history
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Fetch ECB interest rate data:**

    Run the script to scrape and save ECB interest rate data:

    ```bash
    python ecb_interestrates.py
    ```

    This will download the historical interest rate data from the ECB and save it to a local CSV file named `interest_rate_history.csv`.

2. **Analyze and visualize the data:**

    Open the Jupyter notebook `ecb_interest_analysis.ipynb` to analyze and visualize the data:

    ```bash
    jupyter notebook ecb_interest_analysis.ipynb
    ```

## Features

- Fetch historical interest rate data from the European Central Bank (ECB).
- Process and clean the data for analysis.
- Generate visualizations to display trends and patterns in the interest rate history.
- Cache data locally to avoid frequent API calls.

## Project Structure

- `ecb_interestrates.py`: Script to fetch historical interest rate data from the ECB.
- `ecb_interest_analysis.ipynb`: Jupyter notebook to analyze and visualize the fetched data.
- `interest_rate_history.csv`: CSV file containing the historical interest rate data.
- `requirements.txt`: List of required dependencies.
- `README.md`: Project documentation.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch`
5. Open a pull request.

Please ensure your code follows the project's coding conventions and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
