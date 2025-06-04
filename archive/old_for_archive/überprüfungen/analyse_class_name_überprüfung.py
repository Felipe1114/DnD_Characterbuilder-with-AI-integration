"""
"""

from src.LLM.analyse_user_promt import AnalyceClassName
from src.handle_data.crud_json import CrudJsonFiles

def main():
    crud = CrudJsonFiles("../class_keywords.json")
    class_keywords = crud.data

    analyzer = AnalyceClassName(class_keywords=class_keywords)

    user_input = input("Beschreibe deinen Charakterwunsch: ")
    results = analyzer.analyze(user_input)

    print("\nAm besten passende Klassen:")
    for class_name, score in results:
        print(f"{class_name.capitalize()}: {score:.4f}")

    print(results)

if __name__ == "__main__":
    main()