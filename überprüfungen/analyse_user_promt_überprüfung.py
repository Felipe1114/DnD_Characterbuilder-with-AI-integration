"""
"""

from src.LLM.analyse_user_promt import AnalyzeUserPrompt
from src.handle_data.CRUD import CRUD

def main():
    crud = CRUD("../static_dnd_data/class_keywords.json")
    class_keywords = crud.data

    analyzer = AnalyzeUserPrompt(class_keywords=class_keywords)

    user_input = input("Beschreibe deinen Charakterwunsch: ")
    results = analyzer.analyze(user_input)

    print("\nAm besten passende Klassen:")
    for class_name, score in results:
        print(f"{class_name.capitalize()}: {score:.4f}")

    print(results)

if __name__ == "__main__":
    main()