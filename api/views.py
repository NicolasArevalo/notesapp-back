from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import getAllNotes, createNote, getSingleNote, editNote, deleteNote


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
     
    return Response(routes)

@api_view(['GET', 'POST'])
def notes(request):
    if request.method == 'GET':
        return getAllNotes(request)
        
    if request.method == 'POST':
        return createNote(request)
        

@api_view(['GET', 'PUT', 'DELETE'])
def note(request, pk):
    
    if request.method == 'GET':
        return getSingleNote(request, pk)
    
    if request.method == 'PUT':
        return editNote(request, pk)
    
    if request.method == 'DELETE':
        return deleteNote(request, pk)
        