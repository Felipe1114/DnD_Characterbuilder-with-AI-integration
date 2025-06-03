from src.handle_data.algo.binary_base import BinaryBase

class BinaryDict(BinaryBase):
	# initialisiert __init__ funktio von BinaryBase
	def __init__(self, analyse_data, prompt_alpha_version):
		self._nums = analyse_data
		self._target = prompt_alpha_version
	
	def _binary_algo(self, analyse_data, prompt_alpha_version):
		"""geht durch eine liste von geordnetne zahlen und findet den index der gesuchten zahl"""
		# falls target: f"prompt_alpha_{i}" ist
		if not isinstance(prompt_alpha_version, int):
			int_target = int(prompt_alpha_version.split("_")[-1])
		else:
			int_target = prompt_alpha_version
		
		# wenn liste leer ist:
		if len(analyse_data) == 0:
			raise ValueError("List has no data")
	
		mid_idx = len(analyse_data) // 2
		# TODO: wenn es hier einen Type oder ValueError gibt: Try-block
		if int(analyse_data[mid_idx]["prompt_generation"].split("_")[-1]) == int_target:
			return mid_idx
		elif int(analyse_data[mid_idx]["prompt_generation"].split("_")[-1]) < int_target:
			offset = mid_idx + 1
			
			return offset + self._binary_algo(analyse_data[offset:], int_target)
		else:
			return self._binary_algo(analyse_data[:mid_idx], int_target)
		
	
	


"""
liste = [
  {"prompt_generation": "prompt_alpha_1",
  "llm_answers": []},
  {
    "prompt_generation": "prompt_alpha_2",
    "llm_answers": [
      {
        "user_prompt": "dunkler Magier, der tote beschwört und feuer Zauber beherrscht",
        "answer": "```json\n{\n  \"matched_classes\": [\"warlock\", \"wizard\", \"sorcerer\"],\n  \"keywords\": [\"dunkler\", \"Magier\", \"tote\", \"beschwört\", \"feuer\", \"Zauber\"],\n  \"rewritten_prompt_template\": [\n    \"dunkler warlock, der tote beschwört und Feuerzauber beherrscht\",\n    \"dunkler wizard, der tote beschwört und Feuerzauber beherrscht\",\n    \"dunkler sorcerer, der tote beschwört und Feuerzauber beherrscht\"\n  ]\n}\n```"
      }
    ]
  },
  {
    "prompt_generation": "prompt_alpha_3",
    "llm_answers": [
      {
        "user_prompt": "dunkler Magier, der tote beschwört und feuer Zauber beherrscht",
        "answer": "{\n  \"matched_classes\": [\"warlock\", \"wizard\", \"sorcerer\"],\n  \"keywords\": [\"dunkel\", \"Magier\", \"beschwört\", \"tote\", \"feuer\", \"Zauber\"],\n  \"rewritten_prompt_template\": [\"dunkler warlock, der tote beschwört und Feuerzauber beherrscht\", \"dunkler wizard, der tote beschwört und Feuerzauber beherrscht\", \"dunkler sorcerer, der tote beschwört und Feuerzauber beherrscht\"]\n}"
      },
      {
        "user_prompt": "Ein bote des lichts. Er hat ein großes schwert und beherrscht die elemente. Er ist in eine strahlende Rüstung getaucht.",
        "answer": "{\n  \"matched_classes\": [\"paladin\", \"fighter\", \"cleric\"],\n  \"keywords\": [\"Bote des Lichts\", \"großes Schwert\", \"Elemente beherrschen\", \"strahlende Rüstung\"],\n  \"rewritten_prompt_template\": [\n    \"Ein paladin des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.\",\n    \"Ein fighter des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.\",\n    \"Ein cleric des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.\"\n  ]\n}"
      }
    ]
  }
]

print(int(liste[2]["prompt_generation"].split("_")[-1]))
"""

