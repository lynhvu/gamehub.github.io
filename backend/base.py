from flask import Flask, Response
import json

companyData = [{ "name": "Naughty Dog",
                 "description": "Established in 1984, Naughty Dog is one of the most successful and prolific game development studios in the world and a flagship first-party studio within PlayStation Studios. From creating the iconic Crash Bandicoot and Jak and Daxter series to modern franchises like Uncharted and The Last of Us, Naughty Dog is responsible for some of the most critically acclaimed and commercially successful games on Sony’s PlayStation platforms. Through its use of cutting-edge technology and evocative, character-driven storytelling, Naughty Dog has received hundreds of industry and media awards, while developing a passionate fan base of millions of players around the globe.",
                 "location": "United States",
                 "year": "1984",
                 "genre": "Adventure",
                 "games": ["Uncharted 2: Among Thieves - Limited Edition Collector's Box",
                           "The Last of Us Remastered",
                           "The Last of Us",
                           "The Last of Us Part II",
                           "Uncharted 4: A Thief's End",
                           "Uncharted: Legacy of Thieves Collection",
                           "Uncharted: The Nathan Drake Collection - Special Edition",
                           "Uncharted 3 Drake's Deception - Game of the Year Edition",
                           "Uncharted 2: Among Thieves"],
                 "img": "https://images.igdb.com/igdb/image/upload/t_logo_med/bcpeptiqicy9g0gn4nur.png"},
               { "name": "Obsidian Entertainment",
                 "description": "Obsidian Entertainment is an American video game developer based in Irvine, California. Former employees of Black Isle Studios founded it. The studio is well-known for their critically acclaimed RPGs such as Pillars of Eternity series, Star Wars Knights of the Old Republic II: The Sith Lords and Fallout New Vegas. Obsidian’s projects often use well-established franchises as a setting. The first two projects developed by the studio were sequels to Star Wars: Knights of the Old Republic and Neverwinter Nights. In 2014 Ubisoft released South Park: The Stick of Truth developed by Obsidian. The game was an RPG based on South Park franchise. It was a commercial success with more than 5 million copies sold worldwide in two years and was well received by critics, players, and fans of the show alike. The developer also created several games using their original IPs: Alpha Protocol, Pillars of Eternity series and Tyranny all of which were either RPGs or included role-playing elements in gameplay.",
                 "location": "United States",
                 "year": "2003",
                 "genre": "Role-Playing (RPG)",
                 "games": ["Fallout: New Vegas - Ultimate Edition",
                           "Star Wars: Knights of the Old Republic II - The Sith Lords",
                           "Fallout: New Vegas",
                           "Neverwinter Nights 2: Mask of the Betrayer",
                           "Neverwinter Nights 2: Platinum",
                           "South Park: The Stick of Truth",
                           "Tyranny",
                           "Neverwinter Nights 2",
                           "Fallout: New Vegas - Old World Blues"],
                 "img": "https://images.igdb.com/igdb/image/upload/t_logo_med/cl1my.png"},
               { "name": "Valve Corporation",
                 "description": "Valve's debut title, Half-Life, was released in 1998. It won more than 50 game of the year awards, and PC Gamer even called it the Best PC Game Ever. Since then, we've released dozens of titles that changed the world. Today, millions of people play our games every day.",
                 "location": "United States",
                 "year": "1996",
                 "genre": "Adventure",
                 "games": ["Half-Life: Alyx",
                           "Portal 2",
                           "Half-Life 2",
                           "The Orange Box",
                           "Half-Life",
                           "Half-Life 2: Episode Two",
                           "Portal",
                           "Portal: Still Alive",
                           "Counter Strike"],
                 "img": "https://images.igdb.com/igdb/image/upload/t_logo_med/cl2he.png"}]

membersData = [{ "name": "Linh Vu",
    "year": "Junior",
    "major": "Computer Science & Math",
    "skills": "Project management, Full stack web development",
    "picture": "../StyleAndImg/logo2.png"
},
{
    "name": "1",
    "year": "1",
    "major": "1",
    "skills": "1",
    "picture": "../StyleAndImg/logo2.png"
},
{
    "name": "2",
    "year": "2",
    "major": "2",
    "skills": "2",
    "picture": "../StyleAndImg/logo2.png"
},
{
    "name": "3",
    "year": "3",
    "major": "3",
    "skills": "3",
    "picture": "../StyleAndImg/logo2.png"
},
{
    "name": "4",
    "year": "4",
    "major": "4",
    "skills": "4",
    "picture": "../StyleAndImg/logo2.png"
},
{
    "name": "5",
    "year": "5",
    "major": "5",
    "skills": "5",
    "picture": "../StyleAndImg/logo2.png"
}
]

api = Flask(__name__)

@api.route('/profiles/')
def profiles():
    data = json.dump(membersData)
    return Response(data)

@api.route('/compdata/')
def companies():
    data = json.dumps(companyData)
    return Response(data)   

if __name__ == "__main__":
	api.run(host = "127.0.0.1", port = 5000)
