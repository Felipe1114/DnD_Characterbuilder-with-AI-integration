"""überprüfe simple error handlings mit einfachem code
einfache funktion schreiben die mathemathische berechnungen macht und sehen,
was die DebugLog Klasse macht, wenn ein falscher Type eingefügt wird
"""
from src.debug.debug_log import DebugLog


def sum_num(num_1, num_2):
	try:
		res = sum([num_1, num_2])
		return res
	except Exception as e:
		DebugLog.log_error(e, context="Fehler in sum_num, debug_log_überpfüfung.py")
		raise

def main():
	try:
		num_1 = 1
		num_2 = 2
		list_1 = [1, 2]
		dict_1 = {num_1: 1,
				  num_2: 2}
		tuple_1 = (1, 2)
		res_list =[
			sum_num(num_1, num_2), # 3
			sum_num(num_1, list_1), # TypeError
			sum_num(num_2, dict_1) # TypeError
		]

		for res in res_list:
			print(res)
	except Exception as e:
		DebugLog.log_error(e, context="Fehler in main, debug_log_überpfüfung.py")
		raise

if __name__ == "__main__":
	main()
