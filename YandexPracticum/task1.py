input1 = [3, 4, 5, 8, 9, 4, 8]
input2 = [3, 4, 5, 7, 6]
result = set(input1) - set(input2)
print(result)
# Преобразование входных массивов в set имеет сложность O(n): просмотр всех значений n1
# в массиве input1 и всех значений n2 в массиве input2 O(n1) + O(n2)
# для вычитания множеств нужно проитерироваться по уменьшаемому, то есть сложность равно O(n1)
# Таким образом, общая сложность равна O(n1) + O(n2) + O(n1) или просто O(n)