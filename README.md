# movie-recommendation-API
an API that recommends a random movie in a given language, made with Django.

Url extension format to send: /rec/<language_name>

language_name should be one of **_en, de, tr_**  for English, German, and Turkish respectively.

But it works slow for Turkish and sometimes does not work for German and Turkish.

It returns a JSON object such as
{ "movie_name": "Honey, I Shrunk the Kids",
  "movie_year":	"1989" }
