from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from task.models import *
from .serializers import *

# GET ALL ROUTES FOR API
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/tasks/'},
        {'GET': '/api/task/id/'},
        {'POST': '/api/create-task/'},

        {'POST': '/api/user/token'},
        {'POST': '/api/user/token/refresh'},
        {'GET': '/api/users/'},
        {'GET': '/api/user/id/'},

        {'DELETE': '/api/delete-note/'},
    ]
    return Response(routes)

# GET ALL USERS WITH TASKS & NOTES
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUsers(request):
    users = Profile.objects.all()
    serializer = ProfileSerializer(users, many=True)
    return Response(serializer.data)

# GET SINGLE USER WITH TASKS & NOTES
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request, pk):
    user = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)

# GET ALL TASKS
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

# GET SINGLE TASK WITH ID
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

# CREATE NEW TASK
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# DELETE NOTE_
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteNote(request):
    task_id = request.data['task']
    note_id = request.data['note']

    task = Task.objects.get(id=task_id)
    notes = Note.objects.get(id=note_id)

    notes.delete()
    task.getNotesCount
    return Response('Note was removed successfully!')



# # CREATE NEW NOTE_
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def createNote(request, pk):
#     task = Task.objects.get(id=pk)
#     user = request.user.profile
#     data = request.data

#     note, created = Note.objects.get_or_create(
#         user = user, 
#         task = task,
#     )
#     note.new_note = data['new_note']
#     note.save()
#     task.getNotesCount
#     serializer = TaskSerializer(task, many=False)
#     return Response(serializer.data)

