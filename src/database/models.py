"""

"""
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class UserPrompt(Base):
    """
	Contains the character ideas (the user_prompt) for the generation of a DnD Character	
    """
    __tablename__ = 'user_prompt'
    user_prompt_id = Column(Integer, primary_key=True, autoincrement=True)
    user_prompt = Column(Text)

    character = relationship("Character", back_populates="user_prompt")
    rewritten_prompt = relationship("RewrittenPrompts", uselist=False, back_populates="user_prompt")
    best_char = relationship("BestChar", uselist=False, back_populates="user_prompt")
    class_table = relationship("Classes", uselist=False, back_populates="user_prompt")
    idea_descriptions = relationship("DescriptionToPrompt", back_populates="user_prompt")
    rewritten_user_prompts = relationship("RewrittenPrompts", back_populates="user_prompt")

class RewrittenPrompts(Base):
    """
    Contains the rewritten Prommpts from the rewrite process of the POST api endpoint
    """
    __tablename__ = 'rewritten_user_prompts'
    rewritten_prompt_id = Column(Integer, primary_key=True, autoincrement=True)
    user_prompt_id = Column(Integer, ForeignKey('user_prompt.user_prompt_id'))
    rewritten_prompt = Column(String)

    user_prompt = relationship("UserPrompt", back_populates="rewritten_user_prompts")

class Character(Base):
    """
	Contains the DnD character in form of a JSON-like dict
    """
    __tablename__ = 'character'
    character_id = Column(Integer, primary_key=True, autoincrement=True)
    user_prompt_id = Column(Integer, ForeignKey('user_prompt.user_prompt_id'))
    character = Column(JSON)

    user_prompt = relationship("UserPrompt", back_populates="character")

class KeyDescription(Base):
    """
	Key descriptions represnetate the key Values of a Character. Like 'Avatar' or 'strong'
    """
    __tablename__ = 'key_descriptions'
    description_id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)

    description_links = relationship("DescriptionToPrompt", back_populates="description")

class DescriptionToPrompt(Base):
    """
    Connection Table of a key-description to a user_prompt
    """
    __tablename__ = 'description_to_prompt'
    user_prompt_id = Column(Integer, ForeignKey('user_prompt.user_prompt_id'), primary_key=True)
    description_id = Column(Integer, ForeignKey('key_descriptions.description_id'), primary_key=True)

    user_prompt = relationship("UserPrompt", back_populates="idea_descriptions")
    description = relationship("KeyDescription", back_populates="description_links")

class Classes(Base):
    """
	contains all twelve dnd classes and shows, wich user_prompt best with wich three classes.
    """
    __tablename__ = 'classes'
    class_table_id = Column(Integer, primary_key=True)
    user_prompt_id = Column(Integer, ForeignKey('user_prompt.user_prompt_id'))

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

    user_prompt = relationship("UserPrompt", back_populates="class_table")

class BestChar(Base):
    """
    Contains a sorted 'list' of all four generated characters by a user_prompt, in order of its 'bestness'
    """
    __tablename__ = 'best_char'
    user_prompt_id = Column(Integer, ForeignKey('user_prompt.user_prompt_id'), primary_key=True)
    num_one = Column(Integer, ForeignKey('character.character_id'))
    num_two = Column(Integer, ForeignKey('character.character_id'))
    num_three = Column(Integer, ForeignKey('character.character_id'))
    num_four = Column(Integer, ForeignKey('character.character_id'))

    user_prompt = relationship("UserPrompt", back_populates="best_char")