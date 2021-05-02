from django.db import models

# Create your models here.
class SubkategoriModel(models.Model):

    sub_soal_id = models.BigAutoField(primary_key=True)
    kode_sub_kategori = models.CharField(max_length=20,blank=False,null=False)
    nama_sub_kategori = models.CharField(max_length=50,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sub_kategori_soal'

    def __str__(self):
        self.nama_sub_kategori

class KategoriModel(models.Model):

    kat_soal_id = models.BigAutoField(primary_key=True)
    kode_kategori = models.CharField(max_length=20, blank=False, null=False)
    nama_kategori = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'kategori_soal'

    def __str__(self):
        return str(self.nama_kategori)

class SoalEssayModel(models.Model):

    essay_id = models.BigAutoField(primary_key=True)
    kat_soal_id = models.ForeignKey(KategoriModel,on_delete=models.CASCADE)
    sub_soal_id = models.ForeignKey(SubkategoriModel, on_delete=models.CASCADE)
    nama_soal = models.TextField(blank=False,null=False)
    essay_image = models.ImageField(upload_to='resources',max_length=255,blank=True,null=True)
    jawaban = models.TextField(blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'soal_essay'

    def __str__(self):
        return str(self.nama_soal)

class SoalPilganModel(models.Model):

    pilgan_id = models.BigAutoField(primary_key=True)
    kat_soal_id = models.ForeignKey(KategoriModel,on_delete=models.CASCADE)
    sub_soal_id = models.ForeignKey(SubkategoriModel, on_delete=models.CASCADE)
    nama_soal = models.TextField(blank=False, null=False)
    pilgan_image = models.ImageField(upload_to='resources',max_length=255, blank=True, null=True)
    jawaban_a = models.TextField(blank=False, null=False)
    jawaban_b = models.TextField(blank=False, null=False)
    jawaban_c = models.TextField(blank=False, null=False)
    jawaban_d = models.TextField(blank=False, null=False)
    jawaban_e = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'soal_pilgan'

    def __str__(self):
        return str(self.nama_soal)