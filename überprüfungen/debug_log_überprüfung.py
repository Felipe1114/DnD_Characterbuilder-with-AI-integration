"""überprüfe simple error handlings mit einfachem code
einfache funktion schreiben die mathemathische berechnungen macht und sehen,
was die DebugLog Klasse macht, wenn ein falscher Type eingefügt wird
"""
from src.debug.debug_log import DebugLog


@DebugLog.debug_log
def sum_num(num_1, num_2):
	res = sum([num_1, num_2])
	return res


def main():
	num_1 = 1
	num_2 = 2
	list_1 = [1, 2]
	dict_1 = {num_1: 1,
			  num_2: 2}
	tuple_1 = (1, 2)
	
	res = sum_num(num_1, list_1)
	print(res)
	res = sum_num(2, 3)
	print(res)
		

if __name__ == "__main__":
	main()
