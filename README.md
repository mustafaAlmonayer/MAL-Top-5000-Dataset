# Myanimelist(MAL) Top 5000 Anime Dateset

this dataset contains the 5000 highest rank anime (shows and movies) this dataset will provide you with all the information for knowing what features deos the highest animes share from the season of the realse to the voice actors and prodocers you can find all the information that an anime containts in this dataset.

# Dataset Description 

Welcome to the world of golden anime shows and movies! This dataset provides a golden mind to people who want to know what makes an anime hit the high ranks. Whether you're a data scientist, analyst, or AI Engineer you will find this data very helpful .

# Features:

Column  | Def  
--------|---- 
mal_id | myanimelist id. 
url  | url for myanimelist.
images | list of images url .
trailer | info about the trailer.
approved | boolean for approval.
titles | list of titles.
title | universal title.
title_english | title in english.
title_japanese | title in japanese.
title_synonyms | other titles for the anime.
type | type of the show TV..etc.
source | source of the anime Managa..etc.
episodes | number of episodes.
status | airing status.
aired | info about airing data.
duration | duration of the episode.
rating | age rating.
score | myanimelist score.
scored_by | number of users who scored the anime.
rank | myanimelist rank
popularity | live popularity rank eg 1,2,3...etc. 
members | number of the members(Followers).
favorites | number of users who saved it in favorites
synopsis | anime summery
background | background of the story
season | which season did the anime air
year | year of air
broadcast | info about the date, days of the week, time of air.
producers | producers of the anime.
licensors | licensors of the anime.
studios | production studio.
genres | anime genres.
explicit_genres | only explicit genres if it has one
themes | theme of the anime Military..etc.
demographics | main demographics for the anime.
relations | related animes.
theme | openin and ending theme songs names.
external | external links where you can find more about the anime.
streaming | streaming platforms CrunchyRoll...etc.

# Record Example

```json
{
	"data": {
		"mal_id": 5114,
		"url": "https://myanimelist.net/anime/5114/Fullmetal_Alchemist__Brotherhood",
		"images": {
			"jpg": {
				"image_url": "https://cdn.myanimelist.net/images/anime/1208/94745.jpg",
				"small_image_url": "https://cdn.myanimelist.net/images/anime/1208/94745t.jpg",
				"large_image_url": "https://cdn.myanimelist.net/images/anime/1208/94745l.jpg"
			},
			"webp": {
				"image_url": "https://cdn.myanimelist.net/images/anime/1208/94745.webp",
				"small_image_url": "https://cdn.myanimelist.net/images/anime/1208/94745t.webp",
				"large_image_url": "https://cdn.myanimelist.net/images/anime/1208/94745l.webp"
			}
		},
		"trailer": {
			"youtube_id": "--IcmZkvL0Q",
			"url": "https://www.youtube.com/watch?v=--IcmZkvL0Q",
			"embed_url": "https://www.youtube.com/embed/--IcmZkvL0Q?enablejsapi=1&wmode=opaque&autoplay=1",
			"images": {
				"image_url": "https://img.youtube.com/vi/--IcmZkvL0Q/default.jpg",
				"small_image_url": "https://img.youtube.com/vi/--IcmZkvL0Q/sddefault.jpg",
				"medium_image_url": "https://img.youtube.com/vi/--IcmZkvL0Q/mqdefault.jpg",
				"large_image_url": "https://img.youtube.com/vi/--IcmZkvL0Q/hqdefault.jpg",
				"maximum_image_url": "https://img.youtube.com/vi/--IcmZkvL0Q/maxresdefault.jpg"
			}
		},
		"approved": true,
		"titles": [
			{ "type": "Default", "title": "Fullmetal Alchemist: Brotherhood" },
			{ "type": "Synonym", "title": "Hagane no Renkinjutsushi: Fullmetal Alchemist" },
			{ "type": "Synonym", "title": "Fullmetal Alchemist (2009)" },
			{ "type": "Synonym", "title": "FMA" },
			{ "type": "Synonym", "title": "FMAB" },
			{ "type": "Japanese", "title": "\u92fc\u306e\u932c\u91d1\u8853\u5e2b FULLMETAL ALCHEMIST" },
			{ "type": "English", "title": "Fullmetal Alchemist: Brotherhood" },
			{ "type": "French", "title": "Fullmetal Alchemist Brotherhood" }
		],
		"title": "Fullmetal Alchemist: Brotherhood",
		"title_english": "Fullmetal Alchemist: Brotherhood",
		"title_japanese": "\u92fc\u306e\u932c\u91d1\u8853\u5e2b FULLMETAL ALCHEMIST",
		"title_synonyms": [
			"Hagane no Renkinjutsushi: Fullmetal Alchemist",
			"Fullmetal Alchemist (2009)",
			"FMA",
			"FMAB"
		],
		"type": "TV",
		"source": "Manga",
		"episodes": 64,
		"status": "Finished Airing",
		"airing": false,
		"aired": {
			"from": "2009-04-05T00:00:00+00:00",
			"to": "2010-07-04T00:00:00+00:00",
			"prop": { "from": { "day": 5, "month": 4, "year": 2009 }, "to": { "day": 4, "month": 7, "year": 2010 } },
			"string": "Apr 5, 2009 to Jul 4, 2010"
		},
		"duration": "24 min per ep",
		"rating": "R - 17+ (violence & profanity)",
		"score": 9.1,
		"scored_by": 2061018,
		"rank": 1,
		"popularity": 3,
		"members": 3247224,
		"favorites": 221299,
		"synopsis": "After a horrific alchemy experiment goes wrong in the Elric household, brothers Edward and Alphonse are left in a catastrophic new reality. Ignoring the alchemical principle banning human transmutation, the boys attempted to bring their recently deceased mother back to life. Instead, they suffered brutal personal loss: Alphonse's body disintegrated while Edward lost a leg and then sacrificed an arm to keep Alphonse's soul in the physical realm by binding it to a hulking suit of armor.\n\nThe brothers are rescued by their neighbor Pinako Rockbell and her granddaughter Winry. Known as a bio-mechanical engineering prodigy, Winry creates prosthetic limbs for Edward by utilizing \"automail,\" a tough, versatile metal used in robots and combat armor. After years of training, the Elric brothers set off on a quest to restore their bodies by locating the Philosopher's Stone\u2014a powerful gem that allows an alchemist to defy the traditional laws of Equivalent Exchange.\n\nAs Edward becomes an infamous alchemist and gains the nickname \"Fullmetal,\" the boys' journey embroils them in a growing conspiracy that threatens the fate of the world.\n\n[Written by MAL Rewrite]",
		"background": null,
		"season": "spring",
		"year": 2009,
		"broadcast": {
			"day": "Sundays",
			"time": "17:00",
			"timezone": "Asia/Tokyo",
			"string": "Sundays at 17:00 (JST)"
		},
		"producers": [
			{
				"mal_id": 17,
				"type": "anime",
				"name": "Aniplex",
				"url": "https://myanimelist.net/anime/producer/17/Aniplex"
			},
			{
				"mal_id": 58,
				"type": "anime",
				"name": "Square Enix",
				"url": "https://myanimelist.net/anime/producer/58/Square_Enix"
			},
			{
				"mal_id": 143,
				"type": "anime",
				"name": "Mainichi Broadcasting System",
				"url": "https://myanimelist.net/anime/producer/143/Mainichi_Broadcasting_System"
			},
			{
				"mal_id": 1155,
				"type": "anime",
				"name": "Studio Moriken",
				"url": "https://myanimelist.net/anime/producer/1155/Studio_Moriken"
			}
		],
		"licensors": [
			{
				"mal_id": 102,
				"type": "anime",
				"name": "Funimation",
				"url": "https://myanimelist.net/anime/producer/102/Funimation"
			},
			{
				"mal_id": 493,
				"type": "anime",
				"name": "Aniplex of America",
				"url": "https://myanimelist.net/anime/producer/493/Aniplex_of_America"
			}
		],
		"studios": [
			{ "mal_id": 4, "type": "anime", "name": "Bones", "url": "https://myanimelist.net/anime/producer/4/Bones" }
		],
		"genres": [
			{ "mal_id": 1, "type": "anime", "name": "Action", "url": "https://myanimelist.net/anime/genre/1/Action" },
			{
				"mal_id": 2,
				"type": "anime",
				"name": "Adventure",
				"url": "https://myanimelist.net/anime/genre/2/Adventure"
			},
			{ "mal_id": 8, "type": "anime", "name": "Drama", "url": "https://myanimelist.net/anime/genre/8/Drama" },
			{
				"mal_id": 10,
				"type": "anime",
				"name": "Fantasy",
				"url": "https://myanimelist.net/anime/genre/10/Fantasy"
			}
		],
		"explicit_genres": [],
		"themes": [
			{
				"mal_id": 38,
				"type": "anime",
				"name": "Military",
				"url": "https://myanimelist.net/anime/genre/38/Military"
			}
		],
		"demographics": [
			{
				"mal_id": 27,
				"type": "anime",
				"name": "Shounen",
				"url": "https://myanimelist.net/anime/genre/27/Shounen"
			}
		],
		"relations": [
			{
				"relation": "Adaptation",
				"entry": [
					{
						"mal_id": 25,
						"type": "manga",
						"name": "Fullmetal Alchemist",
						"url": "https://myanimelist.net/manga/25/Fullmetal_Alchemist"
					}
				]
			},
			{
				"relation": "Alternative version",
				"entry": [
					{
						"mal_id": 121,
						"type": "anime",
						"name": "Fullmetal Alchemist",
						"url": "https://myanimelist.net/anime/121/Fullmetal_Alchemist"
					}
				]
			},
			{
				"relation": "Side story",
				"entry": [
					{
						"mal_id": 6421,
						"type": "anime",
						"name": "Fullmetal Alchemist: Brotherhood Specials",
						"url": "https://myanimelist.net/anime/6421/Fullmetal_Alchemist__Brotherhood_Specials"
					},
					{
						"mal_id": 9135,
						"type": "anime",
						"name": "Fullmetal Alchemist: The Sacred Star of Milos",
						"url": "https://myanimelist.net/anime/9135/Fullmetal_Alchemist__The_Sacred_Star_of_Milos"
					}
				]
			},
			{
				"relation": "Spin-off",
				"entry": [
					{
						"mal_id": 7902,
						"type": "anime",
						"name": "Fullmetal Alchemist: Brotherhood - 4-Koma Theater",
						"url": "https://myanimelist.net/anime/7902/Fullmetal_Alchemist__Brotherhood_-_4-Koma_Theater"
					}
				]
			}
		],
		"theme": {
			"openings": [
				"1: \"again\" by YUI (eps 1-14)",
				"2: \"Hologram (\u30db\u30ed\u30b0\u30e9\u30e0)\" by NICO Touches the Walls (eps 15-26)",
				"3: \"Golden Time Lover (\u30b4\u30fc\u30eb\u30c7\u30f3\u30bf\u30a4\u30e0\u30e9\u30d0\u30fc)\" by Sukima Switch (eps 27-38)",
				"4: \"Period\" by Chemistry (eps 39-50)",
				"5: \"Rain (\u30ec\u30a4\u30f3)\" by SID (eps 51-62)"
			],
			"endings": [
				"1: \"Uso (\u5618)\" by SID (eps 1-14)",
				"2: \"LET IT OUT\" by Miho Fukuhara (eps 15-26)",
				"3: \"Tsunaida Te (\u3064\u306a\u3044\u3060\u624b)\" by Lil'B (eps 27-38)",
				"4: \"Shunkan Sentimental (\u77ac\u9593\u30bb\u30f3\u30c1\u30e1\u30f3\u30bf\u30eb)\" by SCANDAL (eps 39-50)",
				"5: \"RAY OF LIGHT\" by Nakagawa Shouko (eps 51-62)",
				"6: \"Rain (\u30ec\u30a4\u30f3)\" by SID (eps 63)",
				"7: \"Hologram (\u30db\u30ed\u30b0\u30e9\u30e0)\" by NICO Touches the Walls (eps 64)"
			]
		},
		"external": [
			{ "name": "Official Site", "url": "http://www.hagaren.jp/fa/" },
			{ "name": "@hagaren_anime", "url": "https://twitter.com/hagaren_anime" },
			{ "name": "AniDB", "url": "https://anidb.net/perl-bin/animedb.pl?show=anime&aid=6107" },
			{ "name": "ANN", "url": "https://www.animenewsnetwork.com/encyclopedia/anime.php?id=10216" },
			{ "name": "Wikipedia", "url": "https://en.wikipedia.org/wiki/Fullmetal_Alchemist:_Brotherhood" },
			{
				"name": "Wikipedia",
				"url": "https://ja.wikipedia.org/wiki/%E9%8B%BC%E3%81%AE%E9%8C%AC%E9%87%91%E8%A1%93%E5%B8%AB_FULLMETAL_ALCHEMIST"
			},
			{ "name": "Syoboi", "url": "https://cal.syoboi.jp/tid/1575" }
		],
		"streaming": [
			{ "name": "Crunchyroll", "url": "http://www.crunchyroll.com/series-271031" },
			{ "name": "Funimation", "url": "https://www.funimation.com/shows/fullmetal-alchemist-brotherhood" }
		]
	}
}

```



# Things You Need

* python 3

* BeautifulSoup4 lib

* pymongo lib

* mongodb server Local or hosted

## Running Cleanning And Profiling Notebook

* pandas

* matplotlib

* nltk

* pandarallel

* textblob

* wordcloud
