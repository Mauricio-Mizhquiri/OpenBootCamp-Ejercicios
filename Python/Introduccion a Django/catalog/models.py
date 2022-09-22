from django.db import models
from django.urls import reverse
import uuid
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length= 64, help_text='pon el nombre del genero')

    def __str__(self) -> str:
        return self.name

     
class Book(models.Model):
    title = models.CharField(max_length=32)
    autor = models.ForeignKey("Author",on_delete=models.SET_NULL, null=True)
    sumary = models.TextField(max_length=100,help_text='pon aqui de que va el libro')
    isbn = models.CharField('ISBN',max_length=13,help_text='El ISBN de 13 caracteres')
    genre = models.ManyToManyField(Genre)
    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse('book-details', args=[str(self.id)])

    
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text= 'ID unico para este libro')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null = True, blank=True)

    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On loan'),
        ('a','Available'),
        ('r','Reversed')
    )
    status = models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='m',help_text='Disponibilidad del libro')

    class Meta:
        ordering = ["due_back"]
        def __str__(self) -> str:
            return '%s (%s)' %(self.id, self.book.title)
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died',null=True,blank=True)

    def get_absolute_url(self):
        return reverse("author_detail",args = [str(self.id)])
    
    def __str__(self) -> str:
        return '%s, %s' %(self.last_name, self.first_name)

