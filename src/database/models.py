"""
Dieses Modul definiert die Datenbankmodelle für das DnD Characterbuilder-Projekt
auf Basis der überarbeiteten Datenbankstruktur. Die Klassen beschreiben die
Tabellenstruktur für Charakterideen, generierte Charaktere, analysierte Prompts,
Beschreibungen, Klassen und Bewertungen.
"""
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class AnalysedPrompt(Base):
    """
    Enthält die analysierten Prompts, die für die Generierung von Charakteren verwendet werden.
    """
    __tablename__ = 'analysed_prompts'
    analysed_prompt_id = Column(Integer, primary_key=True, autoincrement=True)
    idea_id = Column(Integer, ForeignKey('char_ideas.idea_id'))
    analysed_prompt = Column(Text)

    idea = relationship("CharIdea", back_populates="analysed_prompt")

class CharIdea(Base):
    """
    Enthält die vom Benutzer eingegebenen Ideen (Prompts), auf denen Charaktere basieren.
    """
    __tablename__ = 'char_ideas'
    idea_id = Column(Integer, primary_key=True, autoincrement=True)
    user_prompt = Column(Text)

    characters = relationship("Character", back_populates="idea")
    analysed_prompt = relationship("AnalysedPrompt", uselist=False, back_populates="idea")
    best_char = relationship("BestChar", uselist=False, back_populates="idea")
    class_table = relationship("Classes", uselist=False, back_populates="idea")
    idea_descriptions = relationship("DescriptionToIdea", back_populates="idea")
    rewritten_user_prompts = relationship("RewrittenPrompts", back_populates="idea")

class RewrittenPrompts(Base):
    """
    Enthält die umgeschriebenen Prompts aus dem user_prompt für die llm anfrage.
    """
    __tablename__ = 'rewritten_user_prompts'
    rewritten_prompt_id = Column(Integer, primary_key=True, autoincrement=True)
    idea_id = Column(Integer, ForeignKey('char_ideas.idea_id'))
    rewritten_prompt = Column(String)

    idea = relationship("CharIdea", back_populates="rewritten_user_prompts")

class Character(Base):
    """
    Repräsentiert einen generierten Charakter und enthält dessen Daten als JSON.
    """
    __tablename__ = 'characters'
    character_id = Column(Integer, primary_key=True, autoincrement=True)
    idea_id = Column(Integer, ForeignKey('char_ideas.idea_id'))
    character = Column(JSON)

    idea = relationship("CharIdea", back_populates="characters")

class KeyDescription(Base):
    """
    Repräsentiert eine einzelne Eigenschaft oder Beschreibung wie 'groß', 'feurig', etc.
    """
    __tablename__ = 'key_descriptions'
    description_id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)

    description_links = relationship("DescriptionToIdea", back_populates="description")

class DescriptionToIdea(Base):
    """
    Verbindet eine Beschreibung mit einer bestimmten Idee.
    """
    __tablename__ = 'descriptions_to_idea'
    idea_id = Column(Integer, ForeignKey('char_ideas.idea_id'), primary_key=True)
    description_id = Column(Integer, ForeignKey('key_descriptions.description_id'), primary_key=True)

    idea = relationship("CharIdea", back_populates="idea_descriptions")
    description = relationship("KeyDescription", back_populates="description_links")

class Classes(Base):
    """
    Enthält alle möglichen Klassen (als Boolean-Werte) und gibt an, welche Klassen zu einer bestimmten Charakteridee passen.
    """
    __tablename__ = 'classes'
    class_table_id = Column(Integer, primary_key=True)
    idea_id = Column(Integer, ForeignKey('char_ideas.idea_id'))

    barbarian = Column(Boolean)
    bard = Column(Boolean)
    cleric = Column(Boolean)
    druid = Column(Boolean)
    fighter = Column(Boolean)
    monk = Column(Boolean)
    paladin = Column(Boolean)
    ranger = Column(Boolean)
    rogue = Column(Boolean)
    sorcerer = Column(Boolean)
    warlock = Column(Boolean)
    wizard = Column(Boolean)

    idea = relationship("CharIdea", back_populates="class_table")

class BestChar(Base):
    """
    Speichert die vier besten Charaktere für eine bestimmte Idee,
    sortiert von 'am besten' bis 'weniger gut'.
    """
    __tablename__ = 'best_char'
    idea_id = Column(Integer, ForeignKey('char_ideas.idea_id'), primary_key=True)
    num_one = Column(Integer, ForeignKey('characters.character_id'))
    num_two = Column(Integer, ForeignKey('characters.character_id'))
    num_three = Column(Integer, ForeignKey('characters.character_id'))
    num_four = Column(Integer, ForeignKey('characters.character_id'))

    idea = relationship("CharIdea", back_populates="best_char")