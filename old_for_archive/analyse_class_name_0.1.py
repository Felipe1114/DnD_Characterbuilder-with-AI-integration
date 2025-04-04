"""
analysiert den user promt mit embedings
wandelt den user promt und die Klasse-Key-words in vectoren um und vergleicht deise semantisch
"""
from sentence_transformers import SentenceTransformer, util
from src.handle_data.CRUD import CRUD

CLASS_KEYWORDS_URL = "../static_dnd_data/class_keywords.json"
# TODO was genau dauert so lange: das laden?
# TODO wenn es zu lange dauert, auch Mistral einfach verwenden / oder eine ghostere variante des transformers
class AnalyceClassName:
    def __init__(self, class_keywords: dict[str, list[str]]=None, model_name="all-MiniLM-L6-v2"):
        self.class_keywords = class_keywords
        self.model = SentenceTransformer(model_name)

        self.crud = CRUD(CLASS_KEYWORDS_URL)

        # Vektorisierung der Klassen-Keywords vorbereiten
        self.class_vectors = self._prepare_class_vectors()

    def _prepare_class_vectors(self):
        """wandelt klass_keywords für den vergleich vor"""
        vectors = {}
        for class_name, keywords in self.class_keywords.items():
            text = " ".join(keywords)
            embedding = self.model.encode(text, convert_to_tensor=True)
            vectors[class_name] = embedding
        return vectors

    def analyze(self, user_input, top_n=3) -> list[tuple[str, float]]:
        """gibt liste mit den 'n' passendsten Klassen zurück.
        Über die klassen_namen werden dann die Klassen-Json-files geladen"""
        user_vector = self.model.encode(user_input, convert_to_tensor=True)
        scores = []

        for class_name, class_vector in self.class_vectors.items():
            similarity = util.cos_sim(user_vector, class_vector).item()
            scores.append((class_name, similarity))

        # Sortieren und Top-N zurückgeben
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_n]

    @property
    def class_key_words(self):
        return self.class_keywords

    @class_key_words.setter
    def class_key_words(self, new_class_keywords: list[tuple[str, float]]):
        try:
            if isinstance(new_class_keywords, list) and all(
                    isinstance(t, tuple) and len(t) == 2 for t in new_class_keywords):
                self.class_keywords = new_class_keywords

            else:
                raise ValueError("new_class_keywords muss eine Liste von Tupeln (class_name, score)'list[tuple[str, float]]' sein")

        except ValueError as e:
            print(f"Error: {e}")


    def results(self):
        """gibt die die n besten klassen für den user promt zurück"""
        self.class_keywords = self.crud.data

        user_input = input("Beschreibe deinen Charakterwunsch: ")

        result = self.analyze(user_input)

        return result