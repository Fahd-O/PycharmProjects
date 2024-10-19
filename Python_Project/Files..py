Bread = open('Orange..txt', 'r')
print(Bread.read())
Bread.close()

Bread = open('Orange..txt', 'w')
Bread.write("Oranges are Succulent\n")
Bread.write('Oranges grows on Trees\n')
Bread.close()

Bread = open('Orange..txt', 'r')
print(Bread.read())
Bread.close()