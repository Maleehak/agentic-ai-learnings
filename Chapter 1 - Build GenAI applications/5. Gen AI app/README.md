# Activate virtual environment
source venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install requirements
python -m pip install -r requirements.txt


## Run to install style/css files

wget -O static/script.js "https://gist.githubusercontent.com/tenzinmigmar/0168709391266a8d8da7936f1a866c71/raw/95f4f4e1a1966b3f5183dd2f822cfcfd08d2238a/script.js"

wget -O static/styles.css "https://gist.githubusercontent.com/tenzinmigmar/278575598f79a4940993a1fc8640a60a/raw/24eda98885e854b01b4a46d1756112e91d3acc10/styles.css"
