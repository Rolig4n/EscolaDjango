from django.http import JsonResponse

def estudantes(request):
    """
    Visualização para lidar com solicitações de dados do aluno.
    Retorna uma resposta JSON com informações do aluno.
    """
    if request.method != 'GET':
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    else:
        # Example student data
        student_data = {
            "name": "John Doe",
            "age": 20,
            "course": "Computer Science"
        }
    
        return JsonResponse(student_data)