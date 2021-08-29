ORIGINAL_ANIMALS_OF_THE_SONG = ['fly', 'spider', 'bird', 'cat', 'dog', 'cow', 'horse']


class Song:
    first_verse_of_the_song = "There was an old lady who swallowed a {}."
    first_verse = "There was an old lady who swallowed a {};"
    first_middle_verse = "She swallowed the {} to catch the {},"
    middle_verse = "She swallowed the {} to catch the {};"
    last_verse = "I don't know why she swallowed a {} - perhaps she'll die!"
    final_verse_of_the_song = "There was an old lady who swallowed a {}...\n...She's dead, of course!"
    funny_verses = [
        'That wriggled and wiggled and tickled inside her.',
        'How absurd to swallow a {}.',
        'Fancy that to swallow a {}!',
        'What a hog, to swallow a {}!',
        "I don't know how she swallowed a {}!",
    ]
    new_line = "\n"
    new_paragraph = "\n\n"

    def __init__(self, animals_for_song):
        if not animals_for_song:
            self.animals_for_song = ORIGINAL_ANIMALS_OF_THE_SONG
        else:
            self.animals_for_song = animals_for_song
    
    def first_verse_lyrics_generator(self, animal):
        first_verse_lyrics = self.first_verse_of_the_song.format(animal)
        first_verse_lyrics += self.new_line + self.last_verse.format(animal)
        return first_verse_lyrics

    def funny_verse_position_checker(self, funny_verse_position):
        if funny_verse_position == len(self.funny_verses) - 1:
            return 0
        return funny_verse_position + 1

    def funny_verse_lyrics_generator(self, animal, funny_verse_position):
        if funny_verse_position == 0:
            return self.new_line + self.funny_verses[funny_verse_position]
        else:
            return self.new_line + self.funny_verses[funny_verse_position].format(animal)

    def middle_verse_lyrics_generator_loop(self, animals):
        first_animal_in_verse = animals[1]
        second_animal_in_verse = animals[0]
        if (len(animals) == 2):
            return self.new_line + self.first_middle_verse.format(first_animal_in_verse, second_animal_in_verse)
        else:
            return self.middle_verse_lyrics_generator_loop(animals[1:]) + self.new_line + self.first_middle_verse.format(first_animal_in_verse, second_animal_in_verse)

    def last_middle_verse_lyrics_generator(self, animals):
        first_animal_in_verse = animals[1]
        second_animal_in_verse = animals[0]
        return self.new_line + self.middle_verse.format(first_animal_in_verse, second_animal_in_verse)

    def middle_verse_lyrics_generator(self, amount_of_animals_for_use_in_middle_verse):
        middle_verse_lyrics = ""
        middle_verse_animals = self.animals_for_song[0:amount_of_animals_for_use_in_middle_verse + 2]
        if (len(middle_verse_animals) > 2):
            middle_verse_lyrics += self.middle_verse_lyrics_generator_loop(middle_verse_animals[1:])
        middle_verse_lyrics += self.last_middle_verse_lyrics_generator(middle_verse_animals)
        return middle_verse_lyrics

    def final_verse_lyrics_generator(self, animal):
        return self.final_verse_of_the_song.format(animal)

    def adapt_original_lyrics(self):
        first_animal = self.animals_for_song[0]
        amount_of_animals = len(self.animals_for_song)
        if amount_of_animals == 1:
            return self.final_verse_lyrics_generator(first_animal)
        final_song = self.first_verse_lyrics_generator(first_animal)
        funny_verse_position = 0
        for position, animal in enumerate(self.animals_for_song[1:amount_of_animals - 1]):
            final_song += self.new_paragraph + self.first_verse.format(animal)
            final_song += self.funny_verse_lyrics_generator(animal, funny_verse_position)
            final_song += self.middle_verse_lyrics_generator(position)
            final_song += self.new_line + self.last_verse.format(first_animal)
            funny_verse_position = self.funny_verse_position_checker(funny_verse_position)
        return final_song + self.new_paragraph + self.final_verse_lyrics_generator(self.animals_for_song[amount_of_animals - 1])


class Singer:
    def __init__(self):
        self.animals_for_song = []

    def choose_animals_for_song(self, animals_for_song):
        self.animals_for_song = animals_for_song

    def sing(self):
        return Song(self.animals_for_song).adapt_original_lyrics()


singer = Singer()
singer.choose_animals_for_song(['fly', 'spider', 'bird', 'cat', 'dog', 'cow', 'horse'])
# singer.choose_animals_for_song(['fly'])
# singer.choose_animals_for_song(['fly', 'spider', 'bird', 'cat', 'dog', 'cow', 'horse', 'monkey'])
#singer.choose_animals_for_song(
#    ['perezoso', 'cucharacha', 'bb8', 'doraemon', 'marvinelmarciano', 'luisitocomunicia', 'messi', 'ibai'])
print(singer.sing())
