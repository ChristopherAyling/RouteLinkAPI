# Route Link API

An API for accessing data contained in the [Priority Route Link Details](https://data.qld.gov.au/dataset/travel-times-for-key-priority-routes/resource/41091c5c-f952-46df-949a-a329a2531f41) dataset.

Built as an example of `REST`, `SQL`, `PANDAS` and `FLASK` usage.

## Installation

```sh
# how to setup a virtual environment
python -m venv env
env\Scripts\activate
```

```sh
git clone https://github.com/ChristopherAyling/RouteLinkAPI.git
cd RouteLinkAPI
pip install -r requirements.txt
```

## Running

### Development

```sh
python app.py
```

### Production

```sh
python app.py --prod
```

## Usage

All returns are `JSON` formatted.

```
GET /routes

GET /routes/<int>

GET /search?query=<string>
```