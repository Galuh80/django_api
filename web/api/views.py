from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *

#Subkategori API
class SubkategoriView():
    @api_view(['GET'])
    def list(request):
        subkategori = SubkategoriModel.objects.all()
        serializer = SubkategoriSerializer(subkategori,many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def detail(request,pk):
        try:
            subkategori = SubkategoriModel.objects.get(sub_soal_id=pk)
            serializer = SubkategoriSerializer(subkategori, many=False)
            return Response(serializer.data)
        except SubkategoriModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def create(request):
        serializer = SubkategoriSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PUT'])
    def update(request,pk):
        try:
            subkategori = SubkategoriModel.objects.get(sub_soal_id=pk)
            serializer = SubkategoriSerializer(subkategori, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except SubkategoriModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['DELETE'])
    def delete(request,pk):
        subkategori = SubkategoriModel.objects.get(sub_soal_id=pk)
        subkategori.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Kategori API
class KategoriView():
    @api_view(['GET'])
    def list(request):
        kategori = KategoriModel.objects.all()
        serializer = KategoriSerializer(kategori,many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def detail(request,pk):
        try:
            kategori = KategoriModel.objects.get(kat_soal_id=pk)
            serializer = KategoriSerializer(kategori, many=False)
            return Response(serializer.data)
        except KategoriModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def create(request):
        serializer = KategoriSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PUT'])
    def update(request,pk):
        try:
            kategori = KategoriModel.objects.get(kat_soal_id=pk)
            serializer = KategoriSerializer(kategori, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except KategoriModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['DELETE'])
    def delete(request,pk):
        kategori = KategoriModel.objects.get(kat_soal_id=pk)
        kategori.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Essay API
class EssayView():
    @api_view(['GET'])
    def list(request):
        essay = SoalEssayModel.objects.all()
        serializer = SoalEssaySerializer(essay,many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def detail(request,pk):
        try:
            essay = SoalEssayModel.objects.get(essay_id=pk)
            serializer = SoalEssaySerializer(essay, many=False)
            return Response(serializer.data)
        except SoalEssayModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def create(request):
        file_uploaded = request.FILES.get('essay_image')
        serializer = SoalEssaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PUT'])
    def update(request,pk):
        try:
            essay = SoalEssayModel.objects.get(essay_id=pk)
            file_uploaded = request.FILES.get('essay_image')
            serializer = SoalEssaySerializer(essay, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except SoalEssayModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['DELETE'])
    def delete(request,pk):
        essay = SoalEssayModel.objects.get(essay_id=pk)
        essay.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Pilgan API
class PilganView():
    @api_view(['GET'])
    def list(request):
        pilgan = SoalPilganModel.objects.all()
        serializer = SoalPilganSerializer(pilgan,many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def detail(request,pk):
        try:
            pilgan = SoalPilganModel.objects.get(pilgan_id=pk)
            serializer = SoalPilganSerializer(pilgan, many=False)
            return Response(serializer.data)
        except SoalPilganModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def create(request):
        file_uploaded = request.FILES.get('pilgan_image')
        serializer = SoalPilganSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PUT'])
    def update(request,pk):
        try:
            pilgan = SoalPilganModel.objects.get(pilgan_id=pk)
            file_uploaded = request.FILES.get('pilgan_image')
            serializer = SoalPilganSerializer(pilgan, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except SoalPilganModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['DELETE'])
    def delete(request,pk):
        pilgan = SoalPilganModel.objects.get(pilgan_id=pk)
        pilgan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)