{
  "name": "Ward alarm",
  "description": "Ward alarm for hospital",
  "keywords": [
    "flask",
    "python"
  ],
  "repository": "https://github.com/AlienExists/ward_alarm",
  "scripts": {
    "postdeploy": "python -c 'from app import db; db.create_all()'"
  },
  "addons": [
    "heroku-postgresql"
  ]
}