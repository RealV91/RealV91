import json

class MovieNotFoundError(Exception):
    pass #esercizio 18

# definisco la classe che rappresenta la libreria di film presenti nel file json
class MovieLibrary:
    def __init__(self, json_file):
        # salvo il percorso del file json in un attributo della classe che chiamo json_file
        self.json_file = json_file
        # ora cerco di aprire il file json in modalità lettura, se il file esiste carico i dati al suo interno in un attributo chiamato movies
        # se il file non viene trovato lancio un'eccezione con un messaggio personalizzato ( esercizio #17 )
        try:
            with open(self.json_file, "r") as file:
                self.movies = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.json_file}")
    
    # creo un metodo privato della classe per aggiornare il file JSON con i dati più recenti
    # apro il file in modalità scrittura sovrascrivendo il contenuto esistente
    # infine con json.dump converto la struttura Python in formato JSON rendendolo più leggibile
    def __update_json_file(self):
        with open(self.json_file, "w") as file:
            json.dump(self.movies, file, indent=4)

    # esercizi
    # 1 Creo un metodo che restituisce la lista completa dei film presenti nella libreria.
    def get_movies(self):
        return self.movies

    # 2 Creo un dizionario con i dettagli forniti della libreria per aggiungere un nuovo film alla lista
    def add_movie(self, title, director, year, genres):
        new_movie = {
            "title": title,
            "director": director,
            "year": year,
            "genres": genres
        }
        self.movies.append(new_movie)
        # ora aggiorno il file json con la modifica
        self.__update_json_file()

    # 3 creo una funzione che rimuove dalla lista un film
    def remove_movie(self, title):
        for movie in self.movies:
            # Confronto il titolo del film con quelli della libreria mettendo tutto in minuscolo risolvendo il problema del case sensitive
            if movie["title"].lower() == title.lower():
                # Rimuovo il film dalla lista
                self.movies.remove(movie)
                # Aggiorno il file JSON con la lista modificata
                self.__update_json_file()
                # Restituisco il film che è stato rimosso
                return movie 
        # Se il film non viene trovato, sollevo un'eccezione
        raise MovieNotFoundError("Movie was not found") #esercizio 18
    
    # 4 Aggiorno i dettagli di un film esistente nella collezione
    def update_movie(self, title, director=None, year=None, genres=None):
        # Cerco il film da aggiornare e modifico solo i campi non nulli forniti come parametri.
        for movie in self.movies: 
            if movie['title'].lower() == title.lower():
                if director is not None:
                    movie['director'] = director
                if year is not None:
                    movie['year'] = year
                if genres is not None:
                    movie['genres'] = genres
                # Aggiorno il file JSON con le nuove informazioni del film.
                self.__update_json_file()
                return movie
        raise MovieNotFoundError("Movie was not found") #esercizio 18
    
    # 5 Restituisco una lista di tutti i titoli dei film
    def get_movie_titles(self):
        # creo una lista contenente tutti i film che sono presenti nella libreria        
        return [movie["title"] for movie in self.movies]
    
    # 6 Restituisco il numero totale dei film nella libreria
    def count_movies(self):
        # restituisco la lunghezza della lista di film che equivale al numero totale dei film presenti nella libreria
        return len(self.movies)

    # 7 restituisco un film in base al titolo
    def get_movie_by_title(self, title):
        # Cerco nella libreria e restituisco il film con il titolo corrispondente a quello richiesto
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                return movie
        raise MovieNotFoundError("Film non trovato")
    
    # 8 restituisco una lista di tutti i film che contengono una sottostringa nel titolo
    def get_movies_by_title_substring(self, substring):
        # filtro la lista dei film nella libreria per trovare quelli che contengono la sottostringa nel titolo specificato
        return [movie for movie in self.movies if substring in movie["title"]]
    
    # 9 Restituisco una lista di tutti i film pubblicati in un anno specifico
    def get_movies_by_year(self, year):
        # filtro i film restituendo solo quelli che sono stati pubblicati nell'anno specificato
        return [movie for movie in self.movies if movie["year"] == year]
    
    # 10 conto il numero di film di uno specifico regista
    def count_movies_by_director(self, director):
        # conto quanti film presenti nella libreria sono stati diretti da uno specifico regista mettendo tutto in minuscolo risolvendo il problema del case sensitive  
        return sum(1 for movie in self.movies if movie["director"].lower() == director.lower())
        
    # 11 Restituisco una lista di tutti i film presenti nella libreria con un genere specifico
    def get_movies_by_genre(self, genre):
        # filtro la lista di film per trovare tutti quelli che hanno lo stesso genere specificato mettendo tutto in minuscolo risolvendo il problema del case sensitive
        return [movie for movie in self.movies if genre.lower() in (g.lower() for g in movie["genres"])]       
    
    # 12 Restituisco il film più vecchio della lista
    # creo una funzione per ottenere l'anno del film
    def get_movie_year(self, movie):
        return movie["year"]
    
    # ora creo un metodo che mi restituisca il film più vecchio
    def get_oldest_movie(self):
        # uso il metodo get_movie_year come chiave per trovare il film più vecchio
        oldest_movie = min(self.movies, key=self.get_movie_year)
        return oldest_movie["title"]

    # 13 Restituisco la media degli anni di rilascio dei film 
    def get_average_year(self):
        total_years = sum(movie["year"] for movie in self.movies)
        # l'operatore / restituisce sempre un numero con type float
        return total_years / len(self.movies)
    
    # 14 Restituisco il titolo più lungo della collezione di film
    # creo una funzione di supporto per ottenere la lunghezza del titolo del film
    def get_title_length(self, movie):
        return len(movie["title"])
    
    # creo un metodo che mi restituisca il film con il titolo più lungo tra quelli presenti nella libreria
    def get_longest_title(self):
        # uso il metodo get_title_length come chiave per trovare il titolo più lungo
        longest_movie = max(self.movies, key=self.get_title_length)
        return longest_movie["title"]    

    # 15 restituisco la lista di film pubblicati tra due anni specifici estremi inclusi
    def get_titles_between_years(self, start_year, end_year):
        # filtro tra i titoli dei film quelli pubblicati tra gli anni specificati, estremi inclusi
        return [movie["title"] for movie in self.movies if start_year <= movie["year"] <= end_year]
    
    # 16 Restituisco l'anno che si ripete più spesso tra i film della collezione
    def get_most_common_year(self):
        years = [movie["year"] for movie in self.movies]
        # utilizzando set elimino tutti i duplicati della lista lasciando solo i valori distinti e poi con max e key trovo quale anno si ripete con una frequenza maggiore
        return max(set(years), key=years.count)

# Creazione dell'istanza della libreria dei film per poter testare i vari metodi creati
movie_library = MovieLibrary("movies.json")

#17 
"""quando ho creato la classe MovieLibrary ho già creato un metodo costruttore 
    affinchè sollevi un'eccezione nel caso in cui  il file non venisse trovato ( riga 7-17 )
    per farlo ho usato il blocco try tentando l'esecuzione di un codice che potrebbe generare errore, 
    in caso di errore ho creato l'eccezione FileNotFoundError e  
    l'ho gestita con il blocco except sollevando poi un messaggio personalizzato"""
    
#18 eseguito linea 3-55-71

#test 1
print(movie_library.get_movies())

#test 2
movie_library.add_movie("The Green Mile", "Frank Darabont", 1999, ["Drama"])
print(movie_library.get_movies())

#test 3
removed_movie = movie_library.remove_movie("The Green Mile")
print(removed_movie)

#test 4
updated_movie = movie_library.update_movie("The Matrix", year=2000, genres=["Action", "Sci-Fi", "Adventure"])
print(updated_movie)

#test 5
print(movie_library.get_movie_titles())

#test 6
print(movie_library.count_movies())

#test 7
print(movie_library.get_movie_by_title("Inception"))

#test 8
print(movie_library.get_movies_by_title_substring("dark"))

#test 9
print(movie_library.get_movies_by_year(2008))

#test 10
print(movie_library.count_movies_by_director("Christopher Nolan"))

#test 11
print(movie_library.get_movies_by_genre("Sci-Fi"))

#test 12
print(movie_library.get_oldest_movie())

#test 13
print(movie_library.get_average_year())

#test 14
print(movie_library.get_longest_title())

#test 15
print(movie_library.get_titles_between_years(2000, 2010))

#test 16
print(movie_library.get_most_common_year())

