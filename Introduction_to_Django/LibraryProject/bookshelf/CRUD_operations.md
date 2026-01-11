CREATE

Book.objects.create(title="1984", author="George Orwell", publication\_year=1949)



RETRIEVE

Book.objects.get(title="1984")



UPDATE

b.title = "Nineteen Eighty-Four"

b.save()



DELETE

b.delete()



